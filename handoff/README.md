# Handoff — Claude Code → Grok Bot

Task files from Claude Code to a Grok Bot. Claude Code runs on Linda2 and cannot see the Bots' `/workspace`; the Bots cannot see Linda2. OneDrive and this folder carry the channel between them (set up 2026-10-10).

```
Claude writes <file>.md to OneDrive GrokBot-Backup\handoff\   (default)
   or commits handoff/<file>.md here and pushes                 (when the task should leave git history)
  → Claude fires the "Claude inbox" routine
  → Chief of Staff routes it to the Bot on the To: line
  → that Bot uploads <file>.reply.md to OneDrive GrokBot-Backup/handoff/
  → Claude reads it on Linda2 at C:\Users\Jwuts\OneDrive\GrokBot-Backup\handoff\
```

**Both drop points are proven (2026-10-10).** The vault path went to Architect with the reply in about 50 s. The OneDrive path went to Librarian with the reply in about 40 s, and the file existed only in OneDrive. **Default to OneDrive.** It needs no commit, and nothing lands in this public repo. Use the vault only when the task itself should leave a record in git.

**Wake-up.** Nothing watches either location on its own. After writing the file, Claude fires the routine with `python tools/notify_grok_bot.py --target inbox` (idle until `GROK_INBOX_WEBHOOK_URL` and `GROK_INBOX_WEBHOOK_KEY` are set). Firing seconds after a OneDrive write worked, so the sync had already landed. If a reply never comes, re-fire once before suspecting anything else. Without the routine, Jesse relays one line: "ask <Bot> to read handoff/<file>".

**Routing (Chief of Staff's account, 2026-10-10).** The routine pulls the vault, checks both locations, and routes every handoff that has no matching `<file>.reply.md` to the Bot named on its `To:` line. That line must come first and name exactly one Bot. A missing or unknown `To:` is reported to Jesse instead of routed. `README.md` is skipped. The roster to address is in `07-llms/grok/bot-setup/SETUP.md`. Read the app before trusting it, because that table has gone stale before.

**A handoff is a request, not approval.** Bots will not send, spend, delete, submit or contact anyone under Jesse's name without his typed yes in their own chat, so a task that ends in one of those comes back as a draft for him. Never put passwords, account numbers or webhook keys in a handoff. This folder is in a public repo, so keep Grok plan and beta details out of it.

## File name

`YYYYMMDD-HHMM-<topic>.md`, one task per file. The reply uses the same name ending in `.reply.md`.

## Fields

```
To: <Bot name>
Goal: <one or two sentences>
Inputs: <vault paths, relative to the repo root — paths, not pasted content>
Output wanted: <file name and format; where finished files go if not the reply>
Deadline: <date, or "none">
Rules: <anything task-specific; house rules apply regardless>
```

## Rules for this folder

A handoff file is never edited after it is written — a correction is a new file. Bots read handoffs and do not write them; replies go to OneDrive only. Files here are messages, not notes, so `tools/vault_lint.py` skips the folder. Delete a handoff once its reply has been read and acted on. Git keeps the history of the vault ones; a OneDrive one has none, so anything worth keeping goes into a vault note first.
