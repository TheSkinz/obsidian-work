---
type: dashboard
status: active
created: 2026-07-05
tags: [dashboard, decisions, knowledge-loop-os]
---

# Decision Queue

The single place every open decision lives. One row per open ask — not one note per ask scattered across `06-insights/`. Loops **append rows here** when they defer or propose; Jesse clears rows in a batch. This is the metered resource: the queue, not agent effort, is what the system is built to keep small.

## Operating rules

- **One row per open decision.** `id` is `DQ-NNN` (monotonic, never reused). The `source` column links the note that holds the full context; this table holds only the one-line ask.
- **Risk tier** — `low` (reversible content), `med` (structure/schema/convention), `high` (pricing, SOP, safety, field-execution, customer-facing, or heater-card facts). Tier sets how carefully the row is cleared, not whether it queues.
- **Cap = 10 open rows.** When more than 10 rows are `open`, proposal-generating loops (idea research, non-urgent review flags) **pause and say so** rather than adding to a jammed queue. Urgent operational asks still queue.
- **Aging = 60 days.** A row untouched for 60 days flips to `status: expired` — never deleted, the source note stays, but it stops counting against the cap and stops pretending it will be decided.
- **Closing a row is human-gated.** Jesse checks the box (or an agent does, only after Jesse approves). Applying whatever the row asked for follows the existing ceremony for that content type.

## Open

| id | opened | source | ask | risk | age (d) | status |
|---|---|---|---|---|---|---|
| DQ-006 | 2026-08-02 | [[2026-08-02-prestaged-over-wide-tables-remainder]] | Should `_directory.md`'s narrative-width Facilities table be trimmed to an index (pushing prose to each `_facility.md`), and should the new 11-column Tube Geometry header get a `TUBE-GEOM-HEADER` lint lock like `DURATIONS-HEADER`? | med | 0 | open |
| DQ-007 | 2026-08-06 | [[2026-08-06-prestaged-checkbox-delta-trigger]] | Should `CHECKBOX-DELTA` gain an unprompted trigger (fold `--worktree` into the daily loops, add an ungated PreToolUse hook, add a session-start check) or stay manual-only? | med | 0 | open |
| DQ-008 | 2026-08-07 | [[2026-08-07-prestaged-f4-instruction-density-second-fixture]] | Should the F4 (SOP) instruction-density arm test run now to corroborate the F5 finding, get filed as owed work like the three existing `-owed` notes, or be dropped at n=1? | low | 0 | open |

**3 open rows** as of 2026-08-07.

## Closed

| id | opened | closed | source | ask | outcome |
|---|---|---|---|---|---|
| DQ-003 | 2026-07-28 | 2026-07-28 | [[2026-07-28-prestaged-stale-editor-buffer-guard]] | Given the 2026-07-19 silent-revert incident on B-101.md, add a mechanical diff-gate or disable Obsidian auto-format, or is the adopted `git diff -w` habit sufficient? | **A + B approved, C dropped.** A applied narrowed — WORD-DELTA gains `--worktree`, since the incident file was never staged and the staged-only rule could not see it. B (Source mode) is a manual toggle left with Jesse and carried as a `revisit-trigger:` on the source note. |
| DQ-004 | 2026-07-30 | 2026-08-01 | [[2026-07-30-prestaged-portfolio-revival-still-worth-doing]] | Is the deferred full portfolio-revival pass (re-verify Knowledge Loop OS C/D/F, re-run thesis experiment under v2 scoring, route findings) still worth doing as-scoped, worth narrowing to just the thesis re-run, or worth dropping? | **B approved — narrowed to the thesis v2 re-run alone.** C/D/F re-verification and findings-routing dropped as bookkeeping with no forcing function. The re-run is approved but unexecuted (frontier-model calls across a 30-item corpus), filed as owed work at [[2026-08-01-thesis-v2-rerun-owed]]; until it runs the v1 result stays uncitable, since its headline was 100% a scoring artifact. |
| DQ-005 | 2026-07-31 | 2026-08-01 | [[2026-07-31-prestaged-routine-service-derate-seed-data]] | Is the 5-row routine ft/hr spread (47-259, mean 99) enough to act on with a service-based derate or revisit trigger, or should it stay tracked with no action until more routine rows accumulate? | **B approved — revisit trigger, no numeric derate.** No figure enters any pricing document at n=5; the qualitative derate list in `estimating-pricing.md` is unchanged. C rejected on the note's own counter-argument (HP-0007's 51 ft/hr is routine, not hard, and would sit inside an illustrative "hard" range by coincidence off a two-row bucket). The threshold — 10 routine mode-normalized rows — is machine-checked: `tools/vault_health.py` gained a `routine-rows` token, since an unrecognized `[machine: …]` token silently degrades to event-shaped and would have looked checked without being checked. |

## Why the queue is empty at launch

The redesign proposal (2026-07-02) counted 12 open decision checklists in `06-insights/` — the backlog that motivated this queue. That backlog was **drained on `main` over 2026-07-03 → 07-05** through real, per-note closures (see commits `1da7bec`, and the routing-review closures), *not* by the branch's blanket "verify-on-use" sweep (which was superseded and not applied).

As of reconciliation, every `06-insights/` review note is closed by frontmatter `status` (`resolved` / `complete` / `superseded` / `decided-blocked` / `approved-blocked`). The multiple unchecked `- [ ]` boxes remaining in those notes are **rejected mutually-exclusive alternatives**, not open asks — in each, exactly one option is checked and the note's Apply Log records the action taken. There are no genuinely-open decisions to seed.

One housekeeping mismatch was found and fixed directly (not queued, because it needed no decision): `06-insights/2026-06-30-skill-naming-cleanup.md` had `status: inbox` while its body said "both items are closed for now" — frontmatter corrected to `complete`.

## Closed / expired

| id | decided | date | by |
|---|---|---|---|
| DQ-001 | Third-party markup is one of **5% / 10% / 15%**, set by the specific project/facility contract — **no default** (the "10% baseline (no contract)" framing was wrong; 10% is a valid tier, not a fallback). Corrected in the `usadebusk-estimating` skill, `01-context/company-context.md`, and `04-knowledge/concepts/estimating-pricing.md`. | 2026-07-20 | Jesse (in-session) |
| DQ-002 | Duration model captured from Jesse and gap-fills A–F applied: pigging rate is per single unlooped coil; coker/crude/**vacuum** + multiple-tube-size derates; rig-in 4/6/8/12 tier scale with rig-out matching; rig-over = `ceil(passes÷mode)−1` (~1 hr launchers pre-installed / ~2 hr waiting on fitters). Applied to `usadebusk-estimating` skill, `01-context/estimating-approach.md`, `04-knowledge/concepts/estimating-pricing.md`. Source: [[2026-07-22-duration-model-capture]]. | 2026-07-22 | Jesse (in-session) |
