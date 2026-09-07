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

THREE RULES THIS SCRIPT OBEYS, and the reasons matter more than the code:

1. **It never blocks a push.** Missing key, no network, webhook 500, xAI outage —
   every path exits 0. A knowledge-vault notification is not worth failing a push
   over, and a hook that can wedge `git push` is worse than no hook at all.
2. **The key is never written anywhere.** Not to a file, not to a log line, not
   into an error message. Failures report the HTTP status, never the request.
3. **Silence on success.** A hook that prints on every push becomes noise you stop
   reading. One line on skip or failure; nothing when it works.

POWERSHELL TRAP, recorded because it cost four attempts: PowerShell aliases `curl`
to `Invoke-WebRequest`, which rejects `-H`. If firing this by hand rather than via
the hook, use `curl.exe`, or assign the URL and key to variables and call
`Invoke-RestMethod` so the header is built by PowerShell rather than parsed by a
shell.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

URL_VAR = "GROK_BOT_WEBHOOK_URL"
KEY_VAR = "GROK_BOT_WEBHOOK_KEY"
TIMEOUT_S = 5


def note(msg: str) -> None:
    """One line to stderr. Never stdout — git shows stderr from hooks plainly."""
    print(f"[grok-bot] {msg}", file=sys.stderr)


def main() -> int:
    url = os.environ.get(URL_VAR, "").strip()
    key = os.environ.get(KEY_VAR, "").strip()

    if not url or not key:
        # Idle, not broken. This is the documented off switch.
        note(f"idle - set {URL_VAR} and {KEY_VAR} to notify Grok Bot on push")
        return 0

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
            if resp.status >= 400:
                note(f"webhook returned HTTP {resp.status} - push continuing")
    except urllib.error.HTTPError as exc:
        # Status only. The request carried the key; the message must not.
        note(f"webhook returned HTTP {exc.code} - push continuing")
    except Exception as exc:  # noqa: BLE001 — a push must never fail on this
        note(f"webhook unreachable ({type(exc).__name__}) - push continuing")

    return 0


if __name__ == "__main__":
    # Belt and braces: even an unhandled error above must not fail the push.
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001
        note(f"notifier failed ({type(exc).__name__}) - push continuing")
        sys.exit(0)
