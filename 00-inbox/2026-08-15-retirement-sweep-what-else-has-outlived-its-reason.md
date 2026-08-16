<!-- vault-loop: operational — commissions a sweep; needs a session, not a loop run. -->
---
type: note
status: inbox
created: 2026-08-15
tags: [inbox, knowledge-system, housekeeping, retirement, cross-cutting]
related:
  - "[[2026-08-01-thesis-v2-rerun-owed]]"
---

# Sweep the vault for commitments that have outlived their reason

**For the next session** (Jesse, 2026-08-15, immediately after retiring the thesis v2 re-run unrun).

## Why

The v2 re-run had been carried as owed work since 2026-08-01, and when it was finally examined it turned out to be **undecidable from data already in hand** — B pass@1 at 0.962 meant the frozen thresholds could only ever return "inconclusive," whatever the run produced. Nobody had checked. It was inherited forward on the strength of having once been approved.

That is not a one-off. The same session found three more of the same shape: F6's frozen baseline stale against a corrected rule for a day; F1's baseline over-billing a second crew truck through four promotions; a `~6 ft/hr` Syncrude figure circulating since July that **cannot be reproduced from card data at all**. Each survived because approval and filing are recorded, and re-examination is not.

The failure mode: *an approved commitment is never re-tested against whether it still makes sense.* Cheap to fix by sweep, and it compounds if left.

## What to sweep

Concrete surfaces, roughly in order of likely yield:

1. **`00-inbox/` owed and `approved-unexecuted` items.** At least two remain (`2026-08-01-baseline-staleness-detector-owed`, `2026-08-01-coil-visualization-build-owed`). For each, the test is not "is this still nice to have" but **"could its result change anything, and is it still answerable as specified?"** That is the question that killed the v2 re-run.
2. **Dormant triggers on `50-dashboards/health.md`.** Ten-ish rows, some parked since July. Some name conditions that can no longer fire, or fire into work nobody would now do. A trigger retires by removing the `revisit-trigger:` field from its note.
3. **Idea seeds at `status: researched`.** Researched means the loop finished and Jesse never ruled. Several are months old. Some are presumably dead on arrival now.
4. **`04-knowledge/` parked schema decisions.** The per-coilset re-grain and the Pig Specifications `Condition` column have been bundled and re-bundled across several notes without ever being opened.
5. **Frozen regression baselines and their diff keys.** Separate seed filed at [[2026-08-15-idea-frozen-baselines-may-carry-unexercised-convention-defects]] — a baseline is only tested where runs disagree, so some frozen readings are arbitrary rather than ruled.

## How to run it

Do not batch-retire. Each candidate gets the same two questions, answered from evidence rather than recall:

- **Is it still answerable as specified?** The v2 re-run was not, and that was checkable in minutes against numbers already recorded.
- **Would the answer change anything?** If nothing downstream moves either way, retiring is the honest close, not a dodge.

Retire by ruling with the reasoning written down, the way the v2 re-run was — not by silent deletion, and not by letting items age out. A retired commitment with a stated reason is a record; a deleted one is a gap that gets rediscovered and re-approved.

Expect a real hit rate. The thesis run had been carried for two weeks and died to one arithmetic check.
