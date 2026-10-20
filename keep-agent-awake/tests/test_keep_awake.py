"""Run with python -m unittest discover -s tests -v. No third-party packages."""

import argparse
import ctypes
import importlib.util
import os
import pathlib
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest import mock


SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "keep_awake.py"


class KeepAwakeTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SCRIPT.is_file(), "The portable keep-awake helper is missing")
        spec = importlib.util.spec_from_file_location("keep_awake", SCRIPT)
        self.awake = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.awake)

    @unittest.skipIf(os.name == "nt", "Linux holder readiness uses POSIX pipes")
    def test_owned_holder_is_reaped_when_scope_ends(self):
        code = "import sys; print('KEEP_AWAKE_READY', flush=True); sys.stdin.buffer.read()"
        with self.awake.managed_process([sys.executable, "-u", "-c", code], ready=True) as process:
            self.assertIsNone(process.poll())
        self.assertIsNotNone(process.poll())

    @unittest.skipIf(os.name == "nt", "Linux holder readiness uses POSIX pipes")
    def test_backend_acquisition_failure_is_not_reported_as_ready(self):
        code = "import sys; sys.stderr.write('inhibitor denied'); sys.exit(7)"
        with self.assertRaisesRegex(self.awake.KeepAwakeError, "inhibitor denied"):
            with self.awake.managed_process([sys.executable, "-c", code], ready=True):
                self.fail("A failed backend must not enter the active scope")

    @unittest.skipIf(os.name == "nt", "Linux holder readiness uses POSIX pipes")
    def test_startup_timeout_reaps_the_owned_process(self):
        processes = []
        real_popen = subprocess.Popen

        def start(*args, **kwargs):
            process = real_popen(*args, **kwargs)
            processes.append(process)
            return process

        with mock.patch.object(self.awake, "STARTUP_TIMEOUT", 0.05), mock.patch.object(
            self.awake.subprocess, "Popen", side_effect=start
        ):
            with self.assertRaisesRegex(self.awake.KeepAwakeError, "ready"):
                with self.awake.managed_process(
                    [sys.executable, "-c", "import time; time.sleep(30)"], ready=True
                ):
                    self.fail("A backend without readiness must not enter the scope")
        self.assertEqual(len(processes), 1)
        self.assertIsNotNone(processes[0].poll())

    @unittest.skipIf(os.name == "nt", "Linux holder readiness uses POSIX pipes")
    def test_backend_death_while_work_is_active_is_an_error(self):
        code = "print('KEEP_AWAKE_READY', flush=True); raise SystemExit(3)"
        with self.awake.managed_process([sys.executable, "-u", "-c", code], ready=True) as process:
            process.wait(timeout=2)
            with self.assertRaisesRegex(self.awake.KeepAwakeError, "exited"):
                self.awake.wait_for_stop(threading.Event(), process, timeout=1)

    def test_timeout_ends_a_session(self):
        start = time.monotonic()
        self.assertEqual(self.awake.wait_for_stop(threading.Event(), None, 0.03), "timeout")
        self.assertLess(time.monotonic() - start, 1)

    def test_cancellation_does_not_wait_for_the_deadline(self):
        stop = threading.Event()
        stop.set()
        self.assertEqual(self.awake.wait_for_stop(stop, None, 3600), "cancelled")

    @unittest.skipIf(os.name == "nt", "Deterministic POSIX signal delivery")
    def test_signal_during_wait_cannot_deadlock_cancellation(self):
        code = r'''
import contextlib, importlib.util, os, signal, sys, threading, time
spec = importlib.util.spec_from_file_location("awake", sys.argv[1])
awake = importlib.util.module_from_spec(spec)
spec.loader.exec_module(awake)
awake.select_inhibitor = lambda *args: contextlib.nullcontext(None)
original_sleep = time.sleep
sent = False

def interrupt_locked_wait(self, timeout=None):
    with self._cond:
        os.kill(os.getpid(), signal.SIGTERM)
    return True

def interrupt_sleep(seconds):
    global sent
    if not sent:
        sent = True
        os.kill(os.getpid(), signal.SIGTERM)
    original_sleep(min(seconds, 0.01))

threading.Event.wait = interrupt_locked_wait
time.sleep = interrupt_sleep
raise SystemExit(awake.main(["--timeout", "1"]))
'''
        try:
            result = subprocess.run(
                [sys.executable, "-c", code, str(SCRIPT)], capture_output=True, text=True, timeout=3
            )
        except subprocess.TimeoutExpired:
            self.fail("Signal-handler cancellation deadlocked before releasing the inhibitor")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Released owned sleep inhibitor (cancelled)", result.stdout)

    def test_windows_default_requests_system_sleep_protection_and_releases_it(self):
        state = mock.Mock(return_value=0x80000000)
        library = mock.Mock(SetThreadExecutionState=state)
        with mock.patch.object(ctypes, "WinDLL", return_value=library, create=True):
            with self.awake.windows_inhibitor(display=False):
                self.assertEqual(state.call_args.args, (0x80000001,))
        self.assertEqual(state.call_args_list, [mock.call(0x80000001), mock.call(0x80000000)])

    def test_windows_display_is_optional_and_cleanup_survives_task_failure(self):
        state = mock.Mock(return_value=0x80000000)
        library = mock.Mock(SetThreadExecutionState=state)
        with mock.patch.object(ctypes, "WinDLL", return_value=library, create=True):
            with self.assertRaisesRegex(ValueError, "task failed"):
                with self.awake.windows_inhibitor(display=True):
                    raise ValueError("task failed")
        self.assertEqual(state.call_args_list, [mock.call(0x80000003), mock.call(0x80000000)])

    def test_windows_failed_request_is_an_error(self):
        library = mock.Mock(SetThreadExecutionState=mock.Mock(return_value=0))
        with mock.patch.object(ctypes, "WinDLL", return_value=library, create=True):
            with self.assertRaisesRegex(self.awake.KeepAwakeError, "SetThreadExecutionState"):
                with self.awake.windows_inhibitor(display=False):
                    self.fail("Windows rejected the request")

    def test_linux_missing_inhibitor_fails_without_installing_anything(self):
        with mock.patch.object(self.awake.platform, "release", return_value="generic"), mock.patch.object(
            self.awake.shutil, "which", return_value=None
        ):
            with self.assertRaisesRegex(self.awake.KeepAwakeError, "systemd-inhibit"):
                with self.awake.linux_inhibitor(display=False):
                    self.fail("No Linux backend is available")

    @unittest.skipIf(os.name == "nt", "Linux subprocess contract requires POSIX")
    def test_linux_backend_owns_a_holder_until_scope_ends(self):
        with tempfile.TemporaryDirectory() as temp:
            executable = pathlib.Path(temp) / "systemd-inhibit"
            executable.write_text(
                '#!/bin/sh\nwhile [ "$#" -gt 0 ]; do\n'
                '  case "$1" in --*) shift ;; *) break ;; esac\n'
                'done\nexec "$@"\n'
            )
            executable.chmod(0o700)
            with mock.patch.object(self.awake.platform, "release", return_value="generic"), mock.patch.object(
                self.awake.shutil, "which", return_value=str(executable)
            ), mock.patch.dict(os.environ, {"WSL_INTEROP": ""}):
                with self.awake.linux_inhibitor(display=False) as process:
                    self.assertIsNone(process.poll())
                self.assertIsNotNone(process.poll())

    def test_linux_does_not_claim_portable_display_inhibition(self):
        with self.assertRaisesRegex(self.awake.KeepAwakeError, "display"):
            with self.awake.linux_inhibitor(display=True):
                self.fail("Linux display inhibition is not implemented")

    def test_wsl_does_not_claim_to_inhibit_the_windows_host(self):
        with mock.patch.object(self.awake.platform, "release", return_value="6.6-microsoft-standard-WSL2"):
            with self.assertRaisesRegex(self.awake.KeepAwakeError, "Windows host"):
                with self.awake.linux_inhibitor(display=False):
                    self.fail("The request must run on the native Windows host")

    def test_unsupported_os_has_a_clear_error(self):
        with self.assertRaisesRegex(self.awake.KeepAwakeError, "unsupported"):
            self.awake.select_inhibitor("FreeBSD", display=False)

    def test_duration_rejects_nonfinite_and_nonpositive_values(self):
        for value in ("0", "-1", "nan", "inf", "-inf"):
            with self.subTest(value=value):
                with self.assertRaises(argparse.ArgumentTypeError):
                    self.awake.positive_seconds(value)
        self.assertEqual(self.awake.positive_seconds("0.5"), 0.5)


if __name__ == "__main__":
    unittest.main()
