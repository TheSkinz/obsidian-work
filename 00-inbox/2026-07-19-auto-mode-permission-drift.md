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

## The re-check — RESOLVED 2026-07-29, seven weeks early

The 2026-09-19 date assumed drift was slow enough that two months was the right sampling interval. That assumption was wrong. A targeted read on **2026-07-29** found the list back at **59 rules** — ten days after the prune to 36, a rate of roughly two rules per day, saturating in under three weeks rather than two months.

The first branch of the test fired: hazardous wildcards were among them. `Bash(python -c ' *)` and `Bash(python -)` had returned verbatim, both pruned by this very note's session, plus a new `Bash(gh repo *)` covering `delete`, `create`, and `edit --visibility public`. The drift is not cosmetic.

Two further live demonstrations during the 2026-07-29 session: three rules were auto-added while investigating (including a `WebFetch` domain for a fetch that returned 403), and three more during a single verification command — one of them `Bash(node -e "…")`, another arbitrary-execution shape.

**Resolution: neither branch.** Turning auto mode off pays a large prompt tax to fix a narrow problem, and a scheduled prune is a recurring chore that never converges. Instead the hazard class was moved to enforcement that does not depend on the allow list staying clean — `~/.claude/hooks/usadebusk-exec-guard.mjs`, registered as a PreToolUse Bash hook (config repo `529ba04`). A hook exiting 2 stops the call *before* permission rules are evaluated, so it overrides any allow rule auto mode restores. Auto mode stays on; its drift is now cosmetic rather than load-bearing.

Deny rules were considered and rejected: they are glob matches on the command string and are documented-leaky, with `python -c` as the canonical bypass ([Steve Adams, "Your Claude Code Deny List Is Leaky"](https://steve-adams.me/claude-code-deny-list-is-leaky.html)). Sandboxing — the stronger OS-level layer — is unavailable, since native Windows is not supported.

No new re-check date. The list will keep growing and that is now expected; what mattered was the hazard class, and that is gated independently.

## Note on the pruned rules

None were deleted destructively. The failure mode of an over-pruned allow list is a permission prompt, not data loss: if a removed rule was actually load-bearing, it re-prompts and gets re-approved. Backups were taken and then deleted once both repos were clean, since every removed rule is enumerated above.
