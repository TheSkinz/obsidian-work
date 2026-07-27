<!-- vault-loop: operational — PM billable-hours pricing ruling and F1 baseline record, Lane 4 (04-knowledge, usadebusk-estimating scope). Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
---
type: note
status: closed
created: 2026-07-25
closed: 2026-07-25
tags: [inbox, estimating, regression, pricing, lane-4, awaiting-decision]
related:
  - "[[2026-07-25-skill-drift-lane4-holds]]"
  - "[[2026-07-24-fixtures-work-better-as-rule-audit]]"
---

# How many hours does a billable Project Manager bill? — F1 baseline is wrong, and the vault says so

**RULED 2026-07-25 — Jesse: "A PM is always on dayshift, so it's like any other dayshift employee. Day side."** Written into `usadebusk-estimating` (config `e396ddf`) next to the per-diem-exclusion line, with USA26038's H-20 row as the worked actual and the $1,680 over-quote named so it does not drift back. Verified by replay: the run billed `1 × 24 hrs @ $80.00 = $1,920.00` and stated the rule unprompted.

**CLOSED — F1's frozen baseline re-cut 2026-07-25** (config `8fa272c`). Promotion was held one extra round because the verifying run rounded the pigging build-up twice, which the skill then forbade. That turned out to be a fifth implicit rule rather than a run defect: **Jesse ruled the parallel-friction allowance applies *after* the coil round-up** (`13.18 → 14`, then `14 × 1.25 = 17.5 → 18`), which made the run right and the baseline wrong. The old "round once, do not re-round downstream" sentence was amended to name both rounding steps, and the worked example now carries the allowance step — omitting it is what left the order inferable. Frozen F1 now reads PM `1 × 24 = $1,920.00`, max pig OD `4.250"`, 32 pigging hours, 46 project hours, total **$61,085.00** (was $61,717.60).

Two independent fresh-context runs, one before and one after the text amendment, reached the same total to the dollar — the strongest reproducibility this fixture has shown.

*(original finding below)*

Surfaced by the F1 replay on 2026-07-25, the first run under the new replay-on-skill-edit trigger.
Not caused by any rule written that day; the replay just executed a rule nobody had written.

**The divergence.** Every figure in the F1 estimate matched the frozen baseline exactly — 45
project hours, 31 pigging, 6/6 rig, 1 rig-over, $35,750.00 equipment, $4,181.60 materials,
$3,648.00 mob and demob, 60 pigs — **except the Project Manager's hours.** Frozen bills the PM
1 × 45, the full project duration spanning both shifts, $3,600.00. The replay bills 1 × 24, the
day-side figure, identical to the Day Supervisor, $1,920.00. That single line is the entire
$1,680.00 gap between frozen's $61,717.60 and the replay's $60,037.60 — 2.8% of the quote.

**The skill is silent.** It gives the PM's rate ($80.00/hr) and says per-diem headcount excludes a
billable PM. It says nothing about the PM's hours, so both readings are available and the estimate
swings on which one the model reaches for.

**The vault settles it.** `02-facilities/HF-Sinclair/Artesia-NM/USA26038-job-sheet.md`, H-20, a
real job sheet carrying a real billable PM:

| Qty | Item | Amt | Unit |
|---|---|---|---|
| 1 | Project Manager | 44 | Hrs |
| 1 | Day Supervisor | 44 | Hrs |
| 2 | Day Operators | 88 | Hrs |
| 1 | Night Supervisor | 36 | Hrs |
| 2 | Night Operators | 72 | Hrs |

Day side 44 + night side 36 = the 80-hr project total. The PM bills **44** — the day-side figure,
matching the Day Supervisor exactly — not the 80-hr total. The replay follows that pattern; frozen
does not.

**So frozen F1 was cut in violation of a live actual.** Same defect shape as F3 on 2026-07-24,
where the old baseline carried "no overrun flag" against a rule the skill already had. That is now
three baselines found enforcing or violating something the skills never stated, which is the
pattern the fixtures-as-rule-audit note predicted.

**Decision needed (Lane 4 — pricing, so nothing was changed).** Two parts:

1. Does a billable Project Manager bill **day-side hours** (the USA26038 pattern, and the replay's
   reading), or the **full project duration**? One line in `usadebusk-estimating` next to the
   existing per-diem-exclusion rule either way. Recommend day-side: it is what the only real job
   sheet with a billable PM actually did, and the alternative over-quotes.
2. If day-side is right, **F1's frozen baseline needs re-cutting** on the PM line, the labor
   subtotal, and the project total. It was not re-cut — a known-stale baseline is readable, a
   laundered one is not.

Worth noting the direction: the unwritten rule was costing an over-quote, not an under-quote. Not
dangerous, but it is 2.8% of a bid on a question with a clean one-line answer sitting in a job
sheet.
