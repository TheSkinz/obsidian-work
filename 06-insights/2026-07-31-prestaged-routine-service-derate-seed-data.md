---
type: review
status: open
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-07-31
review_after: 2026-08-30
related:
  - 2026-07-22-duration-model-capture
  - estimating-actuals-rollup
  - concepts/estimating-pricing
tags: [review, estimating, duration-model, actuals]
---

# Review — Is the routine ft/hr spread worth a service-based derate yet, or is n=5 too sparse?

## Trigger

Pre-staging loop run 2026-07-31, processing the oldest genuine-open-question candidate carrying a `vault-loop:` marker: `00-inbox/2026-07-22-routine-ftphr-baseline-established.md`. The note reports that the estimating rollup now carries 5 mode-normalized routine rates (range 47–259 ft/hr, mean 99) and flags — without proposing a change — that the spread looks service-shaped rather than random, and that this is the seed data if a derating-by-service refinement to the flat 100 ft/hr benchmark is ever built.

That inbox item also lists three smaller open threads (DSP26030 outcome unrecorded, H-19 footage-verification gap, HP-0007/0003+0006 rig-billing quirks). Those are separate execution/tracking items already annotated on their own cards or quote notes (`02-facilities/P66/Ponca-City-OK/DSP26030-H28-H29-Decoke-Proposal-May2026.md` exists and is the live tracking location for the first) — they are not part of this ask and are excluded per the loop's one-question-per-note scope.

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-07-22-routine-ftphr-baseline-established.md` (read this run) | Observed | States the 5 routine rows (47/HF-0012, 51/HP-0007, 52/F-802, 85/HP-0002, 259/HP-0025), explicitly "not proposing a benchmark change (n=5, huge spread)," and characterizes the split as slow-end = big/hard coils (12k-ft coker, 14k-ft crude, four-bore vacuum) vs fast-end = short clean single-coil scopes. |
| `04-knowledge/estimating-actuals-rollup.md` (read this run) | Observed, generated | Confirms the same 5 routine rows and mean 99 ft/hr (range 47–259) under "ft/hr per pig by coil condition." The file's own "Reading this" section already states the governing rule: "With 24 actual job row(s), this is a growing dataset, not a calibrated model. Treat per-job ft/hr as anecdotes until several same-service jobs accumulate," and "Rig-In/Rig-Out actuals well off the 6/6 hr defaults, or ft/hr consistently off 100, are the signal to revisit the Duration Model — raise it with Jesse rather than editing the skill from here." No numeric service-derate exists in this file — it is descriptive only. |
| `04-knowledge/concepts/estimating-pricing.md` (read this run, lines 28-34) | Observed | The duration model already has a *qualitative* derate: "Reduce ft/hour rate (more hours required) for: harder fouling (coker / crude / vacuum), pitch presence, tube restrictions, multiple tube sizes..." No numeric coefficient exists for any of these — the model direction is established, the magnitude is not. |
| `06-insights/2026-07-22-duration-model-capture.md` (read this run) | Observed | The 2026-07-22 session that built the current qualitative derate list (dirty-service, multi-tube-size, vacuum) — confirms the direction was deliberately captured from Jesse without a numeric factor at the time. |
| Memory `feedback-automation-after-data-maturity` (session context) | Observed | Jesse, 2026-07-26, unprompted: "I think I've put too much emphasis on automation way too early... I should have built up the system and data before suggesting it." Distinguishes descriptive/validation stats (fine on sparse data) from predictive/fitted rates (need volume) — a numeric derate coefficient is the fitted-rate case. |
| Memory `feedback-condition-matched-actuals` (session context) | Observed | Heater actuals only govern when coil condition AND service match; routine baseline (5 rows, mean ≈99 ft/hr) exists since 2026-07-22 — consistent with treating this as evolving evidence rather than a settled figure. |

## The Question

The rollup's own governing text names this exact situation — "ft/hr consistently off 100" — as the signal to raise the Duration Model with Jesse, and the inbox note independently flags the same 5-row spread as service-shaped. But both the inbox note (n=5, huge spread) and the automation-after-data-maturity principle (fitted rates need volume, not just direction) argue against acting on it numerically yet. Is 5 routine rows, split roughly 2 hard-service (47, 52) vs 3 clean (51 read as an outlier here, 85, 259), enough to do anything now — and if so, what — or should this stay flagged as seed data with no action until the routine row count grows?

## Proposed Change

### A. No action — let the rollup keep tracking it

The rollup already surfaces this correctly: descriptive stats on a growing dataset, explicitly not yet a calibrated model. Leave the qualitative derate list as-is in `estimating-pricing.md`, take no numeric action, and let `estimating_rollup.py`'s existing "Reading this" guidance be the trigger for raising it again once routine rows grow (e.g., ~10-15).

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

### B. Set an explicit re-visit trigger now

Same as A, but instead of leaving the threshold implicit in the rollup's generic prose, add a specific `revisit-trigger:` note (frontmatter or inline) on the rollup or on `estimating-pricing.md` — e.g., "revisit routine ft/hr derate once ≥10 routine mode-normalized rows exist" — so a future pre-staging or agent-review run has a mechanical condition to check instead of re-judging "is this enough data" from scratch each time.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

### C. Build a coarse two-bucket derate now (hard-service vs clean-service)

Rather than a fitted coefficient, split the existing qualitative list into two named buckets (hard: coker/crude/vacuum/pitch/restrictions vs clean: everything else) and attach the current means as *illustrative, not authoritative* reference points (hard ≈ 50 ft/hr, clean ≈ 85-260 ft/hr) directly in `estimating-pricing.md`, clearly labeled as provisional pending more data. This gets the seed data into the document where an estimator would see it, without claiming it's calibrated.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

Option A risks losing the observation entirely — "the rollup will surface it" assumes someone re-reads the "Reading this" section with this specific pattern in mind, which is exactly what the inbox note's author (a prior session) was worried about when they filed it rather than trusting it to resurface on its own. Option B adds a small piece of process (a revisit-trigger field) for a one-off situation, and threshold numbers like "≥10 rows" are themselves a guess with no more backing than n=5 has — it risks looking more rigorous than it is. Option C is the one closest to what the inbox note explicitly said not to do ("not proposing a benchmark change") — even framed as illustrative and provisional, putting numbers in the canonical pricing document creates a real risk that a future estimator (or agent) reads "≈50 ft/hr" as a rate to use rather than a footnote, especially since HP-0007's 51 ft/hr is routine, not hard-service, and would sit inside the "hard" bucket's illustrative range by coincidence — the two-row hard bucket (47, 52) is too thin to name a number next to. This is Jesse's judgment call on data sufficiency, not something this loop can settle from the actuals alone.

## Decision

Open — awaiting Jesse's disposition on A/B/C above.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-07-31 | Note filed by pre-staging loop from `00-inbox/2026-07-22-routine-ftphr-baseline-established.md`; confirmed via `estimating-actuals-rollup.md` and `estimating-pricing.md` that no numeric service-derate exists yet (qualitative direction only); no vault content modified beyond the source marker | Claude (pre-staging loop) |
