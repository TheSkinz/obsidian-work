#!/usr/bin/env python3
"""notify_grok_bot.py — POST to a Grok Bot webhook so a routine fires on push.

WHY THIS EXISTS. Grok Bot's `Vault refresh` routine pulls `/workspace/vault`, the
read-only clone its Bots cite domain truth from. Without a trigger that clone goes
stale between sessions, and a Bot citing a stale clone is exactly the defect that
cost this project a day on 2026-09-06: the config repo replaced the rig-in method
on 09-05, the vault did not receive it, and a citation audit quoted the stale line
verbatim and correctly. A passing citation audit does not detect a stale source.

WHY A HOOK AND NOT A CONNECTOR. Tested 2026-09-06: Grok Bot's "Git event" trigger
is pull-request shaped and carries **no push event at all** (Opened/Updated/Merged,
review, comment, CI, issue). The PR-opened trigger that does exist did not fire —
one run in three hours, and that one was a manual Test run, with `gh api
repos/.../hooks` confirming no webhook was ever registered. The **Webhook** trigger
fires immediately and needs no GitHub connector and no personal access token, so
this route removes a third-party credential rather than adding one.

WHY pre-push. Librarian pulls from the REMOTE, so the notification has to be tied
to the push, not the commit. Git has no `post-push` hook, so `pre-push` is the only
option. It fires just before the push completes; if the push then fails, Librarian
pulls, finds nothing new, and says so. Harmless.

WHY IT IS FIRE-AND-FORGET (fixed 2026-09-07). The endpoint does not acknowledge and
return -- it **blocks until the run is queued, and gets slower as runs pile up.**
Measured back to back on 2026-09-07 against an idle endpoint and then a busy one:

    call 1 (idle)   HTTP 200 after   1.0s
    call 2          HTTP 200 after  21.7s
    call 3          HTTP 200 after  53.3s

The original `timeout=5` therefore only ever worked on a cold endpoint. Push twice
in a session -- normal on any day with real work -- and every push after the first
timed out and printed `webhook unreachable (TimeoutError)`. **That message was
misleading: the webhook was never unreachable.** DNS, TLS and the route were all
fine throughout; an unauthenticated POST returned a well-formed 401 in 0.3s. The
trigger was also almost certainly being delivered each time, since the run is
created server-side before the response comes back. Only the acknowledgement was
lost.

Raising the timeout was the wrong fix: at 53s and climbing it would hang `git push`
for the better part of a minute, which breaks rule 1 far worse than a spurious
warning does. So the hook now **spawns a detached child and returns immediately.**
The push never waits on a queue whose depth it cannot predict. The cost is that
success and failure are no longer visible in the push output -- so the child writes
a one-line outcome to `.grok-bot-last` (gitignored) instead of stderr, because by
the time it knows, the push has finished and nothing is reading.

THE SHIM. `.git/hooks/` is not tracked by git, so the logic lives here where it is
versioned and visible. Recreate `.git/hooks/pre-push` as:

    #!/bin/sh
    exec python "$(git rev-parse --show-toplevel)/tools/notify_grok_bot.py"

and make it executable (`chmod +x .git/hooks/pre-push`).

CONFIGURATION — two environment variables, and the key never touches a file:

    GROK_BOT_WEBHOOK_URL   the routine's "POST to" endpoint
    GROK_BOT_WEBHOOK_KEY   the routine's "key"

Both are read from the environment. **Unsetting either is the off switch** — the
hook goes idle with nothing to uninstall.

**The URL points at `api2.cursor.sh`, and that is correct.** Grok Bot is xAI's
product **running on Cursor's infrastructure** — the Bot's own sandbox terminal
opens at `box@cursor:/workspace$`, and the webhook trigger hands out an
`api2.cursor.sh/automations/webhook/<uuid>` endpoint. So a Cursor host here is
expected; an `x.ai` host would be the anomaly. Written down because reading that
hostname as a vendor mismatch cost a diagnostic detour on 2026-09-07, with the
answer sitting in `07-llms/grok/bot-setup/SETUP.md` the whole time.

THREE RULES THIS SCRIPT OBEYS, and the reasons matter more than the code:

1. **It never blocks a push.** Missing key, no network, webhook 500, xAI outage —
   every path exits 0, and since 2026-09-07 the request itself runs in a detached
   child so the push does not even wait for it. A knowledge-vault notification is
   not worth failing a push over, and a hook that can wedge `git push` is worse
   than no hook at all. This is the rule the 5-second timeout was protecting; the
   detach protects it better and without the false alarm.
2. **The key is never written anywhere.** Not to a file, not to a log line, not
   into an error message, and **never on a command line** — the detached child
   inherits it through the environment, because argv is visible to anything that
   can list processes.
3. **Silence on success.** A hook that prints on every push becomes noise you stop
   reading. The only thing printed to stderr now is the idle notice; outcomes go
   to `.grok-bot-last`, which you read when you care and ignore when you do not.

POWERSHELL TRAP, recorded because it cost four attempts: PowerShell aliases `curl`
to `Invoke-WebRequest`, which rejects `-H`. If firing this by hand rather than via
the hook, use `curl.exe`, or assign the URL and key to variables and call
`Invoke-RestMethod` so the header is built by PowerShell rather than parsed by a
shell.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

URL_VAR = "GROK_BOT_WEBHOOK_URL"
KEY_VAR = "GROK_BOT_WEBHOOK_KEY"

# Generous on purpose. Nothing waits on this any more -- the push has already
# gone by the time the child is still holding the socket -- so the only thing a
# short timeout would buy is throwing away a trigger that was about to succeed.
# Measured worst case on 2026-09-07 was 53s and the trend was still upward.
TIMEOUT_S = 180

# One line, overwritten each run. Gitignored: it is machine state, not content.
LOG_PATH = Path(__file__).resolve().parent.parent / ".grok-bot-last"

# Internal flag. The hook invocation re-execs itself with this to do the actual
# POST in a detached process; it is not part of the interface.
CHILD_FLAG = "--_send"


def note(msg: str) -> None:
    """One line to stderr. Never stdout — git shows stderr from hooks plainly."""
    print(f"[grok-bot] {msg}", file=sys.stderr)


def log(msg: str) -> None:
    """Record the outcome where it can be read later. Never the key, never the URL."""
    try:
        stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        LOG_PATH.write_text(f"{stamp} {msg}\n", encoding="utf-8")
    except OSError:
        pass  # An unwritable log is not a reason to make noise.


def send(url: str, key: str) -> None:
    """The actual POST. Runs in the detached child; nothing is waiting on it."""
    req = urllib.request.Request(
        url,
        data=json.dumps({"source": "obsidian-work pre-push"}).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
            log(f"ok - HTTP {resp.status}" if resp.status < 400
                else f"webhook returned HTTP {resp.status}")
    except urllib.error.HTTPError as exc:
        # Status only. The request carried the key; the message must not.
        log(f"webhook returned HTTP {exc.code}")
    except Exception as exc:  # noqa: BLE001 — nothing here may raise
        log(f"webhook did not answer ({type(exc).__name__}) after {TIMEOUT_S}s")


def spawn_detached() -> bool:
    """Re-exec ourselves to POST in the background. True if the child started.

    The key travels by inherited environment, never in argv — argv is readable
    by anything that can list processes on this machine.
    """
    kwargs: dict = {
        "stdin": subprocess.DEVNULL,
        "stdout": subprocess.DEVNULL,
        "stderr": subprocess.DEVNULL,
        "close_fds": True,
    }
    if os.name == "nt":
        # Detach from the console so git does not wait on it, and put it in its
        # own process group so Ctrl-C on the push does not kill it mid-request.
        kwargs["creationflags"] = (
            getattr(subprocess, "DETACHED_PROCESS", 0x00000008)
            | getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0x00000200)
        )
    else:
        kwargs["start_new_session"] = True
    try:
        subprocess.Popen([sys.executable, os.path.abspath(__file__), CHILD_FLAG], **kwargs)
        return True
    except Exception:  # noqa: BLE001 — a push must never fail on this
        return False


def main() -> int:
    url = os.environ.get(URL_VAR, "").strip()
    key = os.environ.get(KEY_VAR, "").strip()

    if not url or not key:
        # Idle, not broken. This is the documented off switch.
        note(f"idle - set {URL_VAR} and {KEY_VAR} to notify Grok Bot on push")
        return 0

    if CHILD_FLAG in sys.argv:
        send(url, key)
        return 0

    if not spawn_detached():
        # Could not fork. Do NOT fall back to a blocking send — that reintroduces
        # exactly the hang this design exists to prevent. Record and move on.
        log("could not spawn detached sender; trigger skipped")
    return 0


if __name__ == "__main__":
    # Belt and braces: even an unhandled error above must not fail the push.
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001
        note(f"notifier failed ({type(exc).__name__}) - push continuing")
        sys.exit(0)
