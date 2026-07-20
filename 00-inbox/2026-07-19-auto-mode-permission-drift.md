<!-- ROUTED 2026-07-20 — content landed in 07-llms/claude/code.md. Retained as the original capture record. -->
---
type: capture
status: inbox
created: 2026-07-19
related:
  - [[knowledge-system-governance]]
tags: [capture, vault-system, claude-code, permissions, security]
---

# Auto mode and allow-list pruning pull in opposite directions

Caught during the 2026-07-19 `/doctor` pass. Two changes landed the same session that work against each other, and the tension needs a re-check date rather than a fix.

`obsidian-work/.claude/settings.local.json` had grown to **61 allow rules**, pruned to 36. Seven were live hazards, not clutter: `Bash(git checkout *)` (matches `git checkout -- .`, which discards all uncommitted work — the same loss class as the already-banned `reset --hard`), `Bash(python -c ' *)` and `Bash(python -)` (unrestricted code execution), `Bash(pip install *)` (installs and runs arbitrary PyPI packages), `Bash(cat "...settings.json" 2>/dev/null *)` (trailing wildcard *after* a redirect, so `; <anything>` appends cleanly), and `Read(//c/Users/Jwuts/**)` (whole user profile — SSH keys, browser data, any `.env` on the machine). Eighteen more were dead one-offs: job-specific commit messages that can never match again, `ls -R` probes into the leverage repo, and three git verbs already covered by the checked-in project settings.

`~/.claude/settings.json` also lost `Bash(git fetch:*)`. It reads as read-only but is arbitrary code execution via `--upload-pack='<cmd>'` and `ext::` remote URLs, which is why Claude Code's own vetted read-only git set excludes it.

## Why this matters

The same session set `permissions.defaultMode: "auto"`. Auto mode saves approvals as you work — which is the mechanism that grew the list to 61 in the first place. It demonstrated this live: `Bash(npm view *)` was auto-added mid-session by the doctor pass's own version lookup, and had to be pruned along with the rest.

So the pruning is not a fix, it is a reset of a counter that will climb again. The open question is the rate.

## The re-check

Read the allow list around **2026-09-19** (two months). The rules are in `obsidian-work/.claude/settings.local.json` under `permissions.allow`; `/doctor` also reports the count.

- Back near 60, with hazardous wildcards among them → auto mode costs more in permission drift than it saves in prompts. Turn it off, or pair it with a scheduled prune.
- Grown modestly, all entries scoped and exact → auto mode is paying for itself; leave it.

The honest version of this is that nobody knows the rate yet — one data point (61 rules accumulated over an unknown period) is not a trend.

## Note on the pruned rules

None were deleted destructively. The failure mode of an over-pruned allow list is a permission prompt, not data loss: if a removed rule was actually load-bearing, it re-prompts and gets re-approved. Backups were taken and then deleted once both repos were clean, since every removed rule is enumerated above.
