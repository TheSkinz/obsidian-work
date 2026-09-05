---
type: idea-seed
status: unexplored
created: 2026-09-05
tags: [idea, vault-system, future, lint]
related:
  - "[[2026-09-05-execok-sentinel-backtest]]"
---

# Widen PATH-DEAD beyond 02-facilities, now that its backlog is zero

Idea seed captured 2026-09-05 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** `PATH-DEAD` was scoped to `POINTER_DIRS` (`02-facilities/`) on 2026-09-05 for a measured
reason — run vault-wide it found 100 dead paths in 931 references, but 70 sat in `06-reviews/` and 13 more in
`change-log.md`, records accurately citing files that have since moved. Two things have changed since that
decision. First, the **backtick convention** was settled the same day: backticks mean "this is a live path",
and a path named in order to say it is gone is written without them. That convention is exactly what makes
the record layers safe to scan — a review note quoting a since-moved filename would simply not backtick it.
Second, the scope gap is **proven real, not theoretical**: `07-llms/grok/drawing-extraction-strategy.md` told
readers to delete snippets freely and re-render via `tools/render_drawing_snippets.py`, a script git has never
held. That was found by hand, and nothing would have caught it. A live instruction pointing at a nonexistent
tool is the same defect class as the seven dead `06-insights/` paths in the scheduled prompts.

**To explore:** Re-run the vault-wide measurement *after* the backtick convention — the original 100 predates
it, so the real false-positive rate is unknown and may now be small. If it is, does the rule widen to all
layers, or to a named set (`04-knowledge/`, `07-llms/`, `08-systems/`, `apps/`, `tools/`) leaving the record
layers (`06-reviews/`, `change-log.md`, `00-inbox/`) out? Whether widening requires a backfill pass first, and
whether that backfill is mechanical (drop backticks on dead paths) or needs judgment per hit. Whether the
`_OUTPUTS/` generated projection should be exempt as it is for DEAD-STRING. And whether widening plus a zero
backlog is enough to promote the rule to `ERROR_CODES` on the DQ-006 precedent — deliberately not taken on
2026-09-05, on the grounds that it should sit at warning until a hit occurs in the wild.

Worth noting against the standing "cross-cutting work over project detail" preference: this is cross-cutting,
not a per-heater correction — it protects every future rename the way the 2026-08-24 `06-insights` →
`06-reviews` rename was not protected.
