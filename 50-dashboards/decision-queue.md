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
| DQ-001 | 2026-07-20 | [[company-context]] | Third-party markup disagrees across homes: the `usadebusk-estimating` skill (and the now-thinned `estimating-approach.md`) say **15% typical** — Jesse-confirmed 2026-07-19, 5 of 6 recent DSP workups at 15%; but `company-context.md` and `04-knowledge/concepts/estimating-pricing.md` still say **10% baseline (no contract)**. Decide: is 10% a real no-contract default, or is 15% now typical with no default (confirm-per-contract only)? Then update the two stale homes to match. | high | 0 | open |

**1 open row** as of 2026-07-20.

## Why the queue is empty at launch

The redesign proposal (2026-07-02) counted 12 open decision checklists in `06-insights/` — the backlog that motivated this queue. That backlog was **drained on `main` over 2026-07-03 → 07-05** through real, per-note closures (see commits `1da7bec`, and the routing-review closures), *not* by the branch's blanket "verify-on-use" sweep (which was superseded and not applied).

As of reconciliation, every `06-insights/` review note is closed by frontmatter `status` (`resolved` / `complete` / `superseded` / `decided-blocked` / `approved-blocked`). The multiple unchecked `- [ ]` boxes remaining in those notes are **rejected mutually-exclusive alternatives**, not open asks — in each, exactly one option is checked and the note's Apply Log records the action taken. There are no genuinely-open decisions to seed.

One housekeeping mismatch was found and fixed directly (not queued, because it needed no decision): `06-insights/2026-06-30-skill-naming-cleanup.md` had `status: inbox` while its body said "both items are closed for now" — frontmatter corrected to `complete`.

## Closed / expired

_(none yet — this section is the append-only audit trail of cleared rows: id, what was decided, date, by whom.)_
