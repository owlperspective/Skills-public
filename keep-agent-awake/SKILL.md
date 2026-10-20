---
name: keep-agent-awake
description: Use when a user asks to keep a computer awake during local agent work, or for a long-running local task that would be interrupted by idle sleep. Supports macOS, native Windows, and Linux with systemd-logind. Does not extend model usage limits or keep a remote client's computer awake.
---

# Keep Agent Awake

Hold a sleep-inhibition request for the active task, then release only the request this task owns. Use the included Python helper without changing system power settings or installing a service.

## Requirements and scope

The helper requires Python 3.9 or newer and only its standard library. Resolve `scripts/keep_awake.py` relative to the folder containing this loaded `SKILL.md`, including when the skill is installed through a symlink. Do not assume the current project contains the script.

| Host OS | Native mechanism | Display behavior |
|---|---|---|
| macOS | Built-in `caffeinate`, watching the helper's PID | Display may sleep by default; `--display` also keeps it awake. |
| Native Windows | `SetThreadExecutionState` on the helper's main thread | Display may sleep by default; `--display` also keeps it awake. |
| Linux | `systemd-inhibit` and an accessible, permitted systemd-logind service | System sleep/idle inhibition only. `--display` is unsupported because desktop display control varies. |

Run on the computer that needs protection. A command inside SSH, a container, or a remote executor does not establish protection for the user's laptop. WSL is rejected because Linux-side inhibition does not protect the Windows host; run the helper with native Windows Python instead.

## Start and retain ownership

1. Locate the available Python interpreter on the intended host. If Python or the native backend is unavailable, report that limitation and continue the requested work. Do not install dependencies or alter power policy automatically.
2. Start one helper in a persistent foreground terminal with a short initial yield. Retain its terminal/session identifier. Do not detach it, use `nohup`, or launch an unmanaged background process.
3. Require the `Ready:` message and a still-running session before claiming protection. A startup failure or unexpected exit means protection is unavailable.

For macOS or Linux, substitute the installed skill's absolute path:

```sh
python3 "<skill-dir>/scripts/keep_awake.py" --timeout 3600
```

For native Windows with the Python launcher:

```powershell
py -3 "<skill-dir>\scripts\keep_awake.py" --timeout 3600
```

Choose a timeout long enough for the task. Omit `--timeout` only when the persistent session can be retained and reliably stopped. An expired timeout releases protection even if the work is unfinished. Add `--display` only when display wakefulness is needed on macOS or Windows.

## Release and verify

Complete the authorized work, verification, and any other owned process cleanup first. Then send Ctrl-C to this helper's retained terminal, verify that it exits and reports `Released owned sleep inhibitor`, and return the final response. If it already expired, confirm the exit rather than starting another assertion merely for cleanup.

On cancellation or interruption, make a best-effort attempt to stop the retained session before yielding. Never terminate unrelated keep-awake processes with a blanket command. If the session is lost, inspect the helper PID recorded in its `Ready:` message and verify ownership before stopping it.

The helper clears the Windows thread request on exit, ties macOS's request to its own PID, and closes Linux's holder pipe to release its lock. A backend failure is reported as an error rather than a successful keep-awake session. Do not promise protection against forced sleep, lid closure, administrator overrides, or every desktop policy. This does not extend agent, API, network, or usage-limit timeouts.

## Checks and platform references

Run the helper's portable contract tests from this skill folder with `python -m unittest discover -s tests -v`. Tests using substitute APIs or processes do not establish a native OS pass; report those limits when validating a release.

- [Apple caffeinate implementation](https://github.com/apple-oss-distributions/PowerManagement/blob/main/caffeinate/caffeinate.c)
- [Microsoft SetThreadExecutionState](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate)
- [systemd-inhibit documentation](https://www.freedesktop.org/software/systemd/man/latest/systemd-inhibit.html)
