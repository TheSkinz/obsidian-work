---
type: review
status: open
review_type: capture
source_authority: primary
confidence: high
created: 2026-07-22
review_after: 2026-08-22
related:
  - "[[2026-07-19-fable5-closeout-handoff]]"
  - "[[estimating-actuals-rollup]]"
  - "[[estimating-approach]]"
  - "[[DSP26080]]"
tags: [review, estimating, duration-model, pricing]
---

# Review — Duration model captured from Jesse; propose gap-fills to the three sources

## Trigger

Work order (c) in `00-inbox/2026-07-19-fable5-closeout-handoff.md` asked for a Lane-4
*adjudication* of what the 100 ft/hr pigging benchmark applies to — total coil footage (the
skill's worked example) or per pass (the benchmark's phrasing). It flagged an apparent paradox:
the H-2421 quote implies 82 ft/hr (980 ft looped, 12 h) while the H-2501 quote implies 128 ft/hr
(6,167 ft, 6 passes, 48 h).

In session 2026-07-22, picking this up, Jesse stated the duration model directly. That **dissolves
the adjudication** — there is no total-vs-per-pass fork to settle. So this note does the other
thing: it records his model as authoritative and proposes the specific places the three written
sources are incomplete against it. No source is *wrong* on a value; each is *missing detail*.

## Source Material

| Source | Authority | Notes |
|---|---|---|
| Jesse, in session 2026-07-22 | Primary | Stated the pigging rate basis, the dirty-service and multi-tube-size derates, the vacuum-heater case, the rig-in tier scale, and the mode/rig-over rule. |
| `04-knowledge/estimating-actuals-rollup.md` | Observed | Elapsed-hour actuals; every ft/hr-bearing row is a crash job (38–48 ft/elapsed-hr). |
| `02-facilities/HF-Sinclair/Artesia-NM/DSP26080.md` | Observed | Quote whose per-heater line items (rig-in 6 / decoke / rig-out 6) are the model worked out. |
| `H-2421.md`, `H-2501.md`, `H19.md`, `H-102A.md` | Observed | Footage, looping, mode, and quote-vs-actual figures used in the illustration below. |

## The duration model (as stated by Jesse — authoritative)

**Pigging rate.** ~100 ft/hr per **single unlooped coil**, nominal fouling. Reduce the rate (more
hours) for dirty service — **coker, crude, vacuum** — and for pitch, tube restrictions, first-time
cleans with no prior data, and **multiple tube sizes**: each size is pigged to completion in
sequence (pig one size out, then the next), so more sizes means more hours on a single coil.

**Vacuum heaters** are the compound-hard case — they almost always run long, because they combine
multiple tube sizes, hard coke, and having to pig the bigger tube sizes from the larger outlet
launcher.

**Estimating method (build-up).** Work out what one *unlooped* coil takes to clean first. Then take
the total coil count into account and decide whether coils can/should be looped together. Total
pigging hours build up from the per-coil figure across all coils; looping and equipment mode drive
the rig-over count and the elapsed schedule, not the footage total.

**Rig-in / rig-out.** A four-step tier scale, and **rig-out matches rig-in**:

| Tier | Hours |
|---|---|
| Small | 4 |
| Moderate | 6 |
| Large | 8 |
| Very large | 12 |

Tier is driven by heater size and height and how much hard pipe must be hung to reach the launchers
(e.g. a tall heater with launchers elevated ~60'). Usually read at the job walk, sometimes
inferable from the heater's size and design.

**Mode and rig-overs.** Mode = how many passes are cleaned per set (double mode = 2 passes/set,
triple = 3/set). A rig-over is moving the pumps / hoses / launchers to the next set of passes after
the current set is pigged to completion. Rig-over count = `ceil(passes ÷ mode) − 1`; the last set
ends in rig-out, not rig-over. Rig-over duration is **job-dependent**: ~**1 hr** when launchers /
receivers are already installed on the additional passes, ~**2 hr** when the set has to wait on the
fitters to install launchers / receivers first (Jesse, 2026-07-22).

Worked: 6 passes in double mode → pig 1&2, rig-over, 3&4, rig-over, 5&6, rig-out = **2 rig-overs**.
6 passes in triple mode → pig 1,2,3, rig-over, 4,5,6, rig-out = **1 rig-over**. 3 passes in triple
mode → one set → **0 rig-overs**.

## Illustration — the "paradox" dissolves, and what the actuals actually show

**The handoff's 82-vs-128 is not two rates.** Both are per-heater *aggregates* (total footage ÷
quoted decoke hours), and they differ because of looping, service, and bore — not because the
benchmark is ambiguous:

| Heater | Config | Footage | Quoted decoke | Aggregate ft/hr | Why it lands there |
|---|---|---|---|---|---|
| H-2421 (DSP26080) | 2 circuits looped to 1 pig path | ~980 ft | 12 h | ~82 | Single 6" bore, mild crude-charge service → a bit under the 100 nominal |
| H-2501 (DSP26080) | 6 passes, **not** looped, all launchers set | 6,167 ft | 48 h (~8 h/pass) | ~128 | Clean hot-oil service, large 6" bore → at/above the 100 nominal |

Under the model, each is one per-coil rate near 100 adjusted by condition; you never compute or
compare the aggregate as if it were the benchmark. DSP26080's per-heater line items (rig-in 6 h,
decoke, rig-out 6 h) are the model on paper.

**The actuals are elapsed and mode-blended — diagnostic, not benchmark.** Task-Duration hours are
elapsed wall-clock, so in double/triple mode a set's passes overlap and the recorded ft/elapsed-hr
compresses below any per-coil rate. Every ft/hr-bearing row is also a *crash* job (runs dirtier
than routine). So the low figures are expected, not evidence the 100 nominal is wrong:

| Heater / job | Condition | Footage | Pig h (elapsed) | ft/elapsed-hr | Note |
|---|---|---|---|---|---|
| H-19 · USA25051 | crash | 4,934 | 103 | 48 | Looped single path (no mode compression) |
| H-20 · USA25051 | crash | 2,868 | 69 | 42 | |
| H-102A · USA26025 | crash | 9,248 | 232 | 40 | Vacuum, triple mode — footage ÷ elapsed understates per-coil rate |
| H-102B · USA26025 | crash | 9,248 | 242.5 | 38 | Vacuum, triple mode |
| P66 H-28+H-29 · 24012 | crash, combined | 4,238 | 143 | ~30 | Combined-heaters; rollup shows `-`, this is the manual combined figure |
| P66 H-28+H-29 · USA25041 | routine, combined | 4,238 | 117 | ~36 | Combined-heaters |

**Quote-vs-actual overruns** (all crash/emergency work): USA26025 (Valero) billed $879k vs $554k
quoted, +59%; USA25041 (P66) ran 117 pig-h vs 80 quoted, +46%; USA26038 (H-19) ran 89 productive h
(74 pigging) vs 48 quoted. These reinforce that a crash actual is not a benchmark input for a
planned clean — consistent with the existing "actuals govern only on matched condition" rule.

## Proposed gap-fills

No value contradictions were found — all three sources reconcile numerically. Each is missing the
following detail. Wording is drafted so approval is of text, not concept. **Application routing:**
`usadebusk-estimating` is a config-repo edit (route via a `drift/2026-07` branch — write authority
is not pre-granted, so this is proposed, not applied); the two vault files can be edited directly
once approved, since Jesse is the source.

**A — Rate basis wording.** `SKILL.md:31`, `estimating-pricing.md:28`, `estimating-approach.md:9`:
change "~100 ft/hour **per pass**" → "~100 ft/hr **per single unlooped coil**." Numerically
identical; removes the ambiguity that appears once coils are looped (H-19 is literally "2 coils
looped to 1 pass").

**B — Vacuum as dirty service.** `SKILL.md:34`, `estimating-pricing.md:30`, `estimating-approach.md:10`:
add vacuum to the coker/crude derate list, with its reason — "vacuum heaters almost always run long:
multiple tube sizes, hard coke, and pigging the larger tube sizes from the larger outlet launcher."

**C — Multiple-tube-size duration driver.** All three: add as a distinct derate (separate from
pig-sizing / tube restriction) — "multiple tube sizes on one coil add pigging hours: each size is
pigged to completion in sequence."

**D — Rig-in/out tier scale.** `SKILL.md:37`, `estimating-pricing.md:33`, `estimating-approach.md:15`:
replace "6 hrs default, adjust per access" with the tier scale — "Rig-in tiers: Small 4 / Moderate
6 / Large 8 / Very large 12 hr, set by heater size/height and hard-pipe run to reach the launchers;
**rig-out matches rig-in**."

**E — Rig-over rule.** `SKILL.md:28/144`, `estimating-pricing.md:26/99`: the formula and task
sequence already carry `Rig-Over`; add the rule — "rig-over count = `ceil(passes ÷ mode) − 1`
(mode = passes cleaned per set: double 2, triple 3); last set ends in rig-out. Duration ~1 hr if
launchers/receivers are already on the added passes, ~2 hr if waiting on fitters to install them."

**F — Build-up method.** All three: state the procedure explicitly — "cost one unlooped coil →
decide looping → lay out sets by mode → add rig-overs → sum with rig-in/out." Currently only
gestured at as "loop configuration."

## Recommend-only follow-on (not this pass)

Add a `mode` (passes-per-set) signal to the card Task-Durations schema so
`tools/estimating_rollup.py` can report an elapsed figure *and* a mode-normalized one, instead of a
single blended ft/elapsed-hr the reader has to mentally de-blend. Schema change = Jesse-gated; log
only, do not build now.

## Decision

Adopt the captured duration model above and apply gap-fills A–F (skill via drift branch, vault
files direct). Both sub-confirmations resolved 2026-07-22: moderate rig-in = **6 hr**; rig-over is
**job-dependent** (~1 hr with launchers/receivers pre-installed, ~2 hr waiting on fitters) — folded
into D and E. What remains is Jesse's approval to apply.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more source material

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-07-22 | Note filed from session; model captured from Jesse, gap-fills proposed; no skill or canonical content modified | Claude (Opus 4.8) |
| 2026-07-22 | Sub-confirmations answered by Jesse: moderate rig-in = 6 hr; rig-over job-dependent (1 hr pre-installed / 2 hr waiting on fitters). Folded into D and E. Main decision still open. | Claude (Opus 4.8) |
