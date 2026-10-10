# Handoff — Claude Code → Grok Bot

Task files from Claude Code to a Grok Bot. Claude Code runs on Linda2 and cannot see the Bots' `/workspace`; the Bots cannot see Linda2. This folder and OneDrive are the two halves of the channel between them (set up 2026-10-10).

```
Claude commits handoff/<file>.md and pushes
  → Bots pull it into /workspace/vault/handoff/
  → the named Bot does the task
  → the Bot uploads <file>.reply.md to OneDrive GrokBot-Backup/handoff/
  → Claude reads it on Linda2 at C:\Users\Jwuts\OneDrive\GrokBot-Backup\handoff\
```

**Wake-up.** Nothing watches this folder on its own. After pushing, Claude fires the "Claude inbox" routine with `python tools/notify_grok_bot.py --target inbox` (idle until `GROK_INBOX_WEBHOOK_URL` and `GROK_INBOX_WEBHOOK_KEY` are set). Without the routine, Jesse relays one line: "ask <Bot> to read handoff/<file>".

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

A handoff file is never edited after it is pushed — a correction is a new file. Bots read this folder and do not write to it; replies go to OneDrive only. Files here are messages, not notes, so `tools/vault_lint.py` skips the folder. Delete a handoff once its reply has been read and acted on; git keeps the history.
