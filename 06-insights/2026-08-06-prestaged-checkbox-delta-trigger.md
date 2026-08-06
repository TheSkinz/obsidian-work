---
type: review
status: open
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-08-06
related:
  - "[[2026-07-28-prestaged-stale-editor-buffer-guard]]"
tags: [review, knowledge-system, tooling, lint, data-integrity]
---

# Review — What should trigger CHECKBOX-DELTA unprompted?

## Trigger

Pre-staging loop run 2026-08-06, processing `00-inbox/2026-07-28-checkbox-delta-has-no-unprompted-trigger.md` after the next-oldest candidate (`2026-07-28-b-151-max-pig-od-unconfirmed.md`) triaged as an execution correction and was skipped without a review note. This item asks what should trigger the `CHECKBOX-DELTA` lint rule on its own, since today nothing does.

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-07-28-checkbox-delta-has-no-unprompted-trigger.md` (read this run) | Observed | States `CHECKBOX-DELTA` shipped 2026-07-28 (`b4092d7`) and works, but fires only when someone manually runs `vault_lint.py --staged` or `--worktree`. Lists four candidate unprompted triggers, none evaluated: a session-start check, an ungated PreToolUse hook on every vault commit, folding it into the capture or pre-staging loop's daily run, or leaving it manual. |
| `tools/vault_lint.py:885-903` (read this run) | Observed | Confirms the mechanism: `WORD-DELTA` and `CHECKBOX-DELTA` are diff rules gated behind `--staged`/`--worktree` and "never appear in a normal lint pass" — a bare `python tools/vault_lint.py` invocation runs neither rule. |
| `04-knowledge/vault-capture-loop-spec.md:62` and `04-knowledge/vault-prestaging-loop-spec.md:87` (read this run) | Observed | Both daily loops' own pre-commit step runs the bare `python tools/vault_lint.py` command with no `--staged`/`--worktree` flag. Neither of the vault's two daily-cadence loops would catch a `CHECKBOX-DELTA` finding even on the files they themselves touch — candidate "fold it into the capture or pre-staging loop's existing daily run" is not yet true of either loop as specified. |
| `~/.claude/hooks/usadebusk-word-delta-guard.mjs:66-71` (read this run) | Observed | `parseFindings()` filters hook stdout on the literal substring `'WORD-DELTA'` — confirms the inbox note's own claim that the existing PreToolUse hook drops `CHECKBOX-DELTA` findings even when it does run `vault_lint.py --staged` as part of the git-guard chain. |
| `~/.claude/hooks/` directory listing and config-repo `git log --oneline -- hooks/` (checked this run) | Observed | No hook file dated after `b4092d7` (2026-07-28) touches trigger logic for `CHECKBOX-DELTA` or the word-delta guard. No session-start check, no new PreToolUse hook, and no loop-spec change has shipped since the inbox note was filed nine days ago — the question is genuinely unaddressed, not partially covered. |
| `04-knowledge/knowledge-system-governance.md` (grepped this run) | Observed | No mention of `CHECKBOX-DELTA`, checkbox-trigger design, or an unprompted-trigger policy. |

## The Question

Should `CHECKBOX-DELTA` gain an unprompted trigger, and if so which of the four candidates the source note lists — and if not, is "manual only, run before committing" an acceptable permanent state for a rule whose whole point is to catch a decision recorded without anyone noticing?

## Proposed Change

**A. Fold `--worktree` into both daily loops' existing lint step.** Change `vault-capture-loop-spec.md` step and `vault-prestaging-loop-spec.md` step 8 from bare `python tools/vault_lint.py` to `python tools/vault_lint.py --worktree`, surfacing any stray checkbox tick (or word loss) on the vault's own daily cadence without a new hook or session-start habit. Lowest-effort option — it's a two-line spec edit, both loops already run the script and already commit vault paths daily.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**B. Add a second, ungated PreToolUse hook on every vault `git commit`.** Sibling to `usadebusk-word-delta-guard.mjs` but unconditional — no commit-message scope gate, since the note argues `CHECKBOX-DELTA`'s fire rate should already be near zero (closed-notes only) and the WORD-DELTA-style formatting-vocabulary gate is the wrong shape for a stray click that has nothing to do with reformatting. Catches interactive-session commits the daily loops never touch, which is the gap Option A leaves open — the incident that motivated this rule (a stray Obsidian click during unrelated work) happened in an interactive session, not a loop run.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**C. Session-start check, paired with the already-recommended `--worktree` habit.** Adds a reminder (CLAUDE.md line or similar) to run `vault_lint.py --worktree` at the start of a session, catching drift accumulated since the last commit before it gets buried under new work. Cheapest to implement (a doc line, no code) but relies on the operator remembering, which is the exact failure mode `CHECKBOX-DELTA` exists to catch in the first place — a human forgetting a manual step.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**D. Leave it manual, accept the gap.** No new mechanism. `CHECKBOX-DELTA` remains available on demand for anyone who thinks to run it, same as today. Matches the note's own unresolved framing of "leave it manual and accept that" as one of its four listed candidates, and is consistent with the vault's general bias toward warning-not-blocking coverage — but it means the rule's entire value depends on someone remembering to invoke it, the same gap that let the original stray-checkbox incident go unnoticed.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

Option A's risk: `--worktree` also re-enables `WORD-DELTA` on both loops' daily runs, which is a *second* rule turning on as a side effect — worth confirming that's intended and not scope creep past this one question. Its coverage is also bounded to whatever the loops themselves touch; an interactive Jesse-driven edit to an already-closed note between loop runs would still go unseen until the next day's loop fires. Option B's risk is the one WORD-DELTA's own design note already measured: an ungated hook can over-fire. The source note's counter is that `CHECKBOX-DELTA` is structurally narrower (closed-notes only, a rare state to touch), so the same over-fire risk that forced WORD-DELTA's commit-message gate may not apply — but that claim has not been measured against real commit history the way WORD-DELTA's 70%-vs-7% numbers were, and building an ungated hook on an unmeasured assumption repeats the mistake WORD-DELTA was built to avoid. Option C's risk is named above: it re-introduces the manual-step dependency the rule exists to remove. Option D's risk is simply that the gap stays open — acceptable only if Jesse judges the rule's value as "available when I think to check" rather than "always watching."

## Decision

*(Jesse: check one box per lettered option above.)*

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-06 | Note filed by pre-staging loop from `00-inbox/2026-07-28-checkbox-delta-has-no-unprompted-trigger.md`; confirmed via `vault_lint.py`, both daily loop specs, the word-delta hook, and `~/.claude/hooks/` git history that no unprompted trigger has shipped since the inbox note was filed. No vault content modified beyond the source marker. | Claude (pre-staging loop) |
