---
type: review
status: resolved
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-07-31
review_after: 2026-08-30
revisit-trigger: "10 routine mode-normalized rows in the actuals rollup -> revisit the ft/hr service derate (n=5 at ruling, 2026-08-01) [machine: routine-rows>=10]"
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

- [ ] ~~Approved~~
- [ ] ~~Approved with edits~~
- [x] **Rejected** — superseded by B, which keeps A's no-numeric-action stance and only replaces the implicit trigger with a checked one
- [ ] Needs more research

### B. Set an explicit re-visit trigger now

Same as A, but instead of leaving the threshold implicit in the rollup's generic prose, add a specific `revisit-trigger:` note (frontmatter or inline) on the rollup or on `estimating-pricing.md` — e.g., "revisit routine ft/hr derate once ≥10 routine mode-normalized rows exist" — so a future pre-staging or agent-review run has a mechanical condition to check instead of re-judging "is this enough data" from scratch each time.

- [x] **Approved 2026-08-01 (Jesse)** — threshold set at 10 routine mode-normalized rows, made machine-checkable
- [ ] ~~Approved with edits~~
- [ ] ~~Rejected~~
- [ ] ~~Needs more research~~

**Placement note.** The trigger went on this review note, not on the rollup or `estimating-pricing.md`. The rollup carries the GENERATED marker and is rewritten by `estimating_rollup.py` on every run, so frontmatter added there would not survive; and `estimating-pricing.md` is the canonical pricing document, where a revisit field would sit next to the content it governs and invite exactly the "is this a rate?" misreading option C was rejected for. A resolved review note carrying a live trigger is the pattern the dormant-triggers table already expects — the field's presence puts it on the dashboard regardless of the note's status (`vault_health.py:87-91`).

### C. Build a coarse two-bucket derate now (hard-service vs clean-service)

Rather than a fitted coefficient, split the existing qualitative list into two named buckets (hard: coker/crude/vacuum/pitch/restrictions vs clean: everything else) and attach the current means as *illustrative, not authoritative* reference points (hard ≈ 50 ft/hr, clean ≈ 85-260 ft/hr) directly in `estimating-pricing.md`, clearly labeled as provisional pending more data. This gets the seed data into the document where an estimator would see it, without claiming it's calibrated.

- [ ] ~~Approved~~
- [ ] ~~Approved with edits~~
- [x] **Rejected** — no numeric figure enters the pricing document at n=5. The note's own counter-argument decides it: HP-0007's 51 ft/hr is routine service, not hard, and would land inside an illustrative "hard ≈ 50" range by coincidence, off a two-row bucket.
- [ ] ~~Needs more research~~

## Risks and Counter-Arguments

Option A risks losing the observation entirely — "the rollup will surface it" assumes someone re-reads the "Reading this" section with this specific pattern in mind, which is exactly what the inbox note's author (a prior session) was worried about when they filed it rather than trusting it to resurface on its own. Option B adds a small piece of process (a revisit-trigger field) for a one-off situation, and threshold numbers like "≥10 rows" are themselves a guess with no more backing than n=5 has — it risks looking more rigorous than it is. Option C is the one closest to what the inbox note explicitly said not to do ("not proposing a benchmark change") — even framed as illustrative and provisional, putting numbers in the canonical pricing document creates a real risk that a future estimator (or agent) reads "≈50 ft/hr" as a rate to use rather than a footnote, especially since HP-0007's 51 ft/hr is routine, not hard-service, and would sit inside the "hard" bucket's illustrative range by coincidence — the two-row hard bucket (47, 52) is too thin to name a number next to. This is Jesse's judgment call on data sufficiency, not something this loop can settle from the actuals alone.

## Decision

**B approved 2026-08-01 (Jesse). A and C rejected.** No numeric service derate at n=5 — the qualitative derate list in `estimating-pricing.md` stands unchanged, and no figure enters any pricing document. What changes is only the trigger: the "is this enough data yet" judgment is replaced by a counted threshold of 10 routine mode-normalized rows, evaluated on every health run, so no future session has to re-litigate data sufficiency from scratch.

This is a Lane 4 topic, but the ruling makes no Lane 4 change — the derate model and every rate are untouched.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-07-31 | Note filed by pre-staging loop from `00-inbox/2026-07-22-routine-ftphr-baseline-established.md`; confirmed via `estimating-actuals-rollup.md` and `estimating-pricing.md` that no numeric service-derate exists yet (qualitative direction only); no vault content modified beyond the source marker | Claude (pre-staging loop) |
| 2026-08-01 | **B applied.** `revisit-trigger:` added to this note's frontmatter with a `[machine: routine-rows>=10]` token; `status` → `resolved`. No edit to `estimating-pricing.md`, the rollup, or any rate. | Claude |
| 2026-08-01 | **`routine-rows` token implemented in `tools/vault_health.py`.** Jesse approved a *machine-checkable* trigger, and an unrecognized `[machine: …]` token silently degrades to the event-shaped wording (`trigger_rows`, else branch) — the token would have looked checked without being checked. Added `TRIGGER_RR_RE` + `count_routine_rows()`, which parses the `routine` row of the rollup's condition table by cell (the rollup is GENERATED, so `collect_notes` skips it and it is read from disk). Returns `None` rather than 0 on an unreadable source, since 0 would read as "no routine actuals" and never fire. | Claude |
| 2026-08-01 | DQ-005 moved to the decision-queue Closed table | Claude |
