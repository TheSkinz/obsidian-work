<!-- vault-loop: operational — Syncrude 7-1-F-1 actuals question feeding the estimating-actuals-rollup (02-facilities, 04-knowledge scope). Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
<!-- vault-prestaged: 2026-08-13-prestaged-syncrude-fill-flush-question.md -->
---
type: note
status: superseded
created: 2026-07-29
closed: 2026-08-15
tags: [inbox, estimating, actuals, open-question]
---

# Open question — does the Syncrude ~6 ft/hr figure include fill/flush time?

> **Superseded 2026-08-15** by the retirement sweep — bookkeeping only, no new decision. This note carried no `status` field, which kept it invisible to the Terminal-Note Sweep (see [[2026-07-29-statusless-notes-invisible-to-the-sweep]]). Ruled as DQ-012, which **reordered the question**: the ~6 ft/hr figure **cannot be reproduced from card data at all**, because the 47 tubes / 2,311 ft are unevenly split across coils and no per-coilset footage exists to divide by the 63/48/53-hour sub-totals. Reproduce first, ask about fill/flush second. Closing as moot was explicitly rejected — that is precisely how the figure would later enter a benchmark with the question still open — so a `revisit-trigger:` was pinned to the same event that unparks the per-coilset re-grain decision. Marked superseded rather than resolved because the live question now lives in two better places: the trigger on [[2026-08-13-prestaged-syncrude-fill-flush-question]] and the record on the 7-1-F-1 card itself.

Split out of [[2026-07-28-idea-research-rollup-per-rig-coilset-grain]] when that note was parked
2026-07-29. It does not gate the schema decision and should not wait on it.

Syncrude 7-1-F-1 (CND25004) carries a per-coilset breakdown that works out to roughly 6 ft/hr —
far below every other rate in `04-knowledge/estimating-actuals-rollup.md`. Before that number is
allowed to enter any service-class benchmark, Jesse's read is needed on whether the elapsed hours
behind it include fill and flush time, or only pig travel.

Why it matters: the actuals rollup normalizes `ft/hr per pig` by dividing elapsed hours by mode,
so a figure that silently bundles fill/flush is not on the same basis as the rest of the table and
would drag a service-class average down without anyone being able to see why.

Card: `02-facilities/Syncrude/Fort-McMurray-AB/7-1-F-1.md`, Field Notes.
