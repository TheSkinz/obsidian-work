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
| _(none)_ | | | | | | |

**0 open rows** as of 2026-07-22.

## Why the queue is empty at launch

The redesign proposal (2026-07-02) counted 12 open decision checklists in `06-insights/` — the backlog that motivated this queue. That backlog was **drained on `main` over 2026-07-03 → 07-05** through real, per-note closures (see commits `1da7bec`, and the routing-review closures), *not* by the branch's blanket "verify-on-use" sweep (which was superseded and not applied).

As of reconciliation, every `06-insights/` review note is closed by frontmatter `status` (`resolved` / `complete` / `superseded` / `decided-blocked` / `approved-blocked`). The multiple unchecked `- [ ]` boxes remaining in those notes are **rejected mutually-exclusive alternatives**, not open asks — in each, exactly one option is checked and the note's Apply Log records the action taken. There are no genuinely-open decisions to seed.

One housekeeping mismatch was found and fixed directly (not queued, because it needed no decision): `06-insights/2026-06-30-skill-naming-cleanup.md` had `status: inbox` while its body said "both items are closed for now" — frontmatter corrected to `complete`.

## Closed / expired

| id | decided | date | by |
|---|---|---|---|
| DQ-001 | Third-party markup is one of **5% / 10% / 15%**, set by the specific project/facility contract — **no default** (the "10% baseline (no contract)" framing was wrong; 10% is a valid tier, not a fallback). Corrected in the `usadebusk-estimating` skill, `01-context/company-context.md`, and `04-knowledge/concepts/estimating-pricing.md`. | 2026-07-20 | Jesse (in-session) |
| DQ-002 | Duration model captured from Jesse and gap-fills A–F applied: pigging rate is per single unlooped coil; coker/crude/**vacuum** + multiple-tube-size derates; rig-in 4/6/8/12 tier scale with rig-out matching; rig-over = `ceil(passes÷mode)−1` (~1 hr launchers pre-installed / ~2 hr waiting on fitters). Applied to `usadebusk-estimating` skill, `01-context/estimating-approach.md`, `04-knowledge/concepts/estimating-pricing.md`. Source: [[2026-07-22-duration-model-capture]]. | 2026-07-22 | Jesse (in-session) |
