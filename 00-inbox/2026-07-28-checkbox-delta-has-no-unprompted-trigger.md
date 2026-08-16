<!-- vault-loop: operational — lint-rule trigger design decision for tools/vault_lint.py and ~/.claude hooks (04-knowledge, tooling scope). Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
<!-- vault-prestaged: 2026-08-06-prestaged-checkbox-delta-trigger.md -->
---
type: finding
status: resolved
created: 2026-07-28
closed: 2026-08-15
tags: [knowledge-system, tooling, lint, data-integrity]
---

# CHECKBOX-DELTA has no unprompted trigger

> **Closed 2026-08-15** by the retirement sweep — bookkeeping only, no new decision. Ruled as DQ-007 on 2026-08-15: A approved with edits, B/C/D rejected. This note's own closing instinct was right — the fire rate was measured rather than argued, and 43 daily-loop commits replayed gave WORD-DELTA 43/43 against CHECKBOX-DELTA 0/43, so the diff rules now skip generated paths and both loop specs move to `--worktree`. B was rejected as an ungated hook on an unmeasured fire rate.

Rule `CHECKBOX-DELTA` shipped 2026-07-28 (`b4092d7`) and works, but nothing runs it on its own. It fires only when someone types `vault_lint.py --staged` or `--worktree`.

## Why the existing hook does not cover it

`~/.claude/hooks/usadebusk-word-delta-guard.mjs` filters parsed findings on the literal string `WORD-DELTA`, so CHECKBOX-DELTA findings are dropped even when the hook runs.

More fundamentally, **the hook's trigger is the wrong shape for this rule.** It gates on the commit message claiming a presentation-only scope (format / reflow / whitespace / cleanup), which was measured as the right gate for WORD-DELTA — it holds the fire rate at 7% instead of 70%. But a stray checkbox click has nothing to do with formatting commits. The originating incident arrived via an Obsidian click during unrelated work, and would never have been committed under a "reformat" message.

## The question

What should trigger CHECKBOX-DELTA unprompted? Candidates, none evaluated:

- Session-start check (pairs naturally with `--worktree`, which is already the recommended session-start habit).
- A separate PreToolUse hook on *every* vault commit, ungated — viable only because the rule is already narrow (closed notes only), so its fire rate should be near zero in normal use.
- Fold it into the capture or pre-staging loop's existing daily run.
- Leave it manual and accept that.

The fire rate has not been measured over real history, which is the thing that settled the WORD-DELTA gate design and should probably settle this one. Replaying it over the last N commits would answer it cheaply.

## Provenance

Found while verifying proposal B on [[2026-07-28-prestaged-stale-editor-buffer-guard]]. Deliberately left open at the time rather than bolted on, because choosing a trigger is a real decision and the wrong one produces either noise or false confidence.
