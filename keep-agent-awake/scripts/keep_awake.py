#!/usr/bin/env python3
"""Hold a task-scoped sleep inhibitor using native OS facilities."""

import argparse
from contextlib import contextmanager
import ctypes
import math
import os
import platform
import select
import shutil
import signal
import subprocess
import sys
import tempfile
import time


STARTUP_TIMEOUT = 5
READY_MARKER = b"KEEP_AWAKE_READY"


class KeepAwakeError(RuntimeError):
    pass


class StopFlag:
    """Main-thread cancellation state; signal handlers must not acquire locks."""

    def __init__(self):
        self.requested = False

    def is_set(self):
        return self.requested

    def set(self):
        self.requested = True


def positive_seconds(value):
    try:
        seconds = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("timeout must be a positive number") from exc
    if not math.isfinite(seconds) or seconds <= 0:
        raise argparse.ArgumentTypeError("timeout must be finite and greater than zero")
    return seconds


def backend_error(process, stderr):
    stderr.seek(0)
    detail = stderr.read().decode("utf-8", errors="replace").strip()
    return detail or f"inhibitor exited with status {process.poll()}"


def wait_for_ready(process, stderr):
    deadline = time.monotonic() + STARTUP_TIMEOUT
    received = b""
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise KeepAwakeError("Linux inhibitor did not become ready in time")
        readable, _, _ = select.select([process.stdout], [], [], remaining)
        if not readable:
            raise KeepAwakeError("Linux inhibitor did not become ready in time")
        chunk = os.read(process.stdout.fileno(), 4096)
        if not chunk:
            raise KeepAwakeError(backend_error(process, stderr))
        received += chunk
        if READY_MARKER in received.splitlines():
            return


@contextmanager
def managed_process(command, ready=False):
    """Own and reap one backend; Linux's holder also exits on stdin EOF."""
    with tempfile.TemporaryFile() as stderr:
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE if ready else subprocess.DEVNULL,
            stdout=subprocess.PIPE if ready else subprocess.DEVNULL,
            stderr=stderr,
        )
        try:
            if ready:
                wait_for_ready(process, stderr)
            else:
                try:
                    process.wait(timeout=0.1)
                except subprocess.TimeoutExpired:
                    pass
                else:
                    raise KeepAwakeError(backend_error(process, stderr))
            yield process
        finally:
            if process.stdin:
                process.stdin.close()
            if process.poll() is None:
                if ready:
                    try:
                        process.wait(timeout=1)
                    except subprocess.TimeoutExpired:
                        process.terminate()
                else:
                    process.terminate()
                try:
                    process.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=3)
            else:
                process.wait()
            if process.stdout:
                process.stdout.close()


@contextmanager
def macos_inhibitor(display):
    command = ["/usr/bin/caffeinate", "-i", "-w", str(os.getpid())]
    if display:
        command.append("-d")
    # Watching this helper's PID releases the assertion even if it is killed.
    with managed_process(command) as process:
        yield process


@contextmanager
def windows_inhibitor(display):
    from ctypes import wintypes

    library = ctypes.WinDLL("kernel32", use_last_error=True)
    set_state = library.SetThreadExecutionState
    set_state.argtypes = [wintypes.UINT]
    set_state.restype = wintypes.UINT
    continuous = 0x80000000
    flags = continuous | 0x00000001
    if display:
        flags |= 0x00000002
    if not set_state(flags):
        raise KeepAwakeError("SetThreadExecutionState rejected the sleep-inhibition request")
    try:
        yield None
    finally:
        # The request belongs to this dedicated process's current thread.
        if not set_state(continuous):
            raise KeepAwakeError("SetThreadExecutionState could not clear the request")


@contextmanager
def linux_inhibitor(display):
    if display:
        raise KeepAwakeError("Linux display wakefulness varies by desktop; omit --display")
    if "microsoft" in platform.release().lower() or os.environ.get("WSL_INTEROP"):
        raise KeepAwakeError("Run the Windows helper on the Windows host; WSL cannot protect host sleep")
    executable = shutil.which("systemd-inhibit")
    if not executable:
        raise KeepAwakeError("Linux requires systemd-inhibit and an accessible systemd-logind service")
    # systemd-inhibit acquires the lock before starting this holder. EOF releases
    # it if this helper exits, including abrupt termination, without a PID file.
    holder = "import sys; print('KEEP_AWAKE_READY', flush=True); sys.stdin.buffer.read()"
    command = [
        executable,
        "--what=idle:sleep",
        "--mode=block",
        "--who=Agent",
        "--why=Active agent task",
        "--no-ask-password",
        sys.executable,
        "-u",
        "-c",
        holder,
    ]
    with managed_process(command, ready=True) as process:
        yield process


def select_inhibitor(system, display):
    backends = {"Darwin": macos_inhibitor, "Windows": windows_inhibitor, "Linux": linux_inhibitor}
    if system not in backends:
        raise KeepAwakeError(f"Keep-awake is unsupported on {system}")
    return backends[system](display)


def wait_for_stop(stop, process, timeout):
    deadline = time.monotonic() + timeout if timeout is not None else None
    while not stop.is_set():
        if process is not None and process.poll() is not None:
            raise KeepAwakeError(f"Sleep inhibitor exited unexpectedly (status {process.returncode})")
        remaining = deadline - time.monotonic() if deadline is not None else 0.2
        if remaining <= 0:
            return "timeout"
        time.sleep(min(remaining, 0.2))
    return "cancelled"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout", type=positive_seconds, help="release after this many seconds")
    parser.add_argument("--display", action="store_true", help="also keep the display awake on macOS/Windows")
    args = parser.parse_args(argv)
    stop = StopFlag()
    previous = {}

    def request_stop(signum, frame):
        stop.set()

    for name in ("SIGINT", "SIGTERM", "SIGBREAK"):
        value = getattr(signal, name, None)
        if value is not None:
            previous[value] = signal.signal(value, request_stop)
    try:
        system = platform.system()
        with select_inhibitor(system, args.display) as process:
            if not stop.is_set():
                backend = f", backend PID {process.pid}" if process is not None else ""
                print(f"Ready: {system} sleep inhibition active (helper PID {os.getpid()}{backend}).", flush=True)
            reason = wait_for_stop(stop, process, args.timeout)
        print(f"Released owned sleep inhibitor ({reason}).", flush=True)
        return 0
    except (KeepAwakeError, OSError) as exc:
        print(f"Keep-awake unavailable: {exc}", file=sys.stderr, flush=True)
        return 1
    finally:
        for value, handler in previous.items():
            signal.signal(value, handler)


if __name__ == "__main__":
    raise SystemExit(main())
