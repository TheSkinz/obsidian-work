<!-- vault-loop: operational — heater-card/facility table-schema and lint-rule decisions (02-facilities, 04-knowledge scope). Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
---
type: idea
status: unexplored
created: 2026-07-27
tags: [vault-hygiene, schema, heater-card]
---

# Over-wide tables: what's left after the Tube Geometry fix

Follow-on to `e4de4a5`, which dropped the Tube Geometry `Notes` column and moved 75
notes across 39 cards into keyed blocks. That took over-wide rows in `02-facilities`
from **82 down to 48**. Two things were deliberately left, plus one open enforcement
question.

## 1. `02-facilities/_directory.md` — an index used as a narrative store

Its Facilities table has 3 columns whose trailing cell runs to **765 and 647
characters** — full paragraphs describing a facility's history, folder tier, and which
cards live under it. This is a different problem from Tube Geometry: not a prose column
bolted onto a data table, but an index table doing a job an index shouldn't. Widening
the column won't help; the content wants to be somewhere else.

Worth deciding: does `_directory.md` stay a scannable one-line-per-facility index with
the narrative pushed down to each `_facility.md`, or is it accepted as a rich directory
and the width tolerated because nobody reads it as a table?

## 2. The 2-column key/value tables — probably leave alone

Connection Info (15 rows, ~272 ch), Site Equipment and Constraints (3), Identity (2),
Project Details (1). These wrap cleanly in Obsidian and don't scroll sideways, so they
do not look broken — they were excluded from `e4de4a5` on that basis. Recorded here so
a later session doesn't "discover" them and re-litigate. Only revisit if Jesse actually
finds them hard to read.

## 3. Open: should the 11-column header get a lint lock?

Right now the new schema is protected by a **dead string** in `usadebusk-core` (a Tube
Geometry header ending in `| Notes |`), which makes the skill-drift loop flag a
reversion rather than cause one. That catches an agent re-adding the column. It does
**not** catch a hand edit, or a new card authored from a stale copy.

`vault_lint.py` already has `DURATIONS-HEADER` doing exactly this job for the Task
Durations table — machine-checking a header tuple against the canonical schema. A
`TUBE-GEOM-HEADER` rule would be a near-copy of it. Not built, because it is a new lint
rule and was outside what was asked.

The general question underneath: **which canonical tables deserve a header lock and
which don't?** Two of them now have one or want one, which is the point where a rule
beats case-by-case judgment.
