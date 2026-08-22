---
type: review
status: resolved
review_type: session-finding
source_authority: observed
confidence: high
created: 2026-08-20
related:
  - "[[7-1-F-1]]"
  - "[[2026-08-13-prestaged-syncrude-fill-flush-question]]"
  - "[[2026-07-28-idea-research-rollup-per-rig-coilset-grain]]"
tags: [review, estimating, actuals, syncrude, heater-card]
---

# Review — Syncrude 7-1F-1 geometry was one pass read as the whole heater

## Trigger

Jesse opened a session on 2026-08-20 for the CAD26001 Syncrude mobilization (mob 08-25, rig-in 08-26) [**job number corrected 2026-08-21 to `CND26001`** — `CAD` is not a real prefix (Jesse); the wrong number is left in this sentence as the record of what was believed that day] and, in the course of it, corrected two of my readings and then supplied drawings he had not seen before. The drawings overturned the heater card's geometry. The chain matters more than the endpoint, so it is recorded in order.

## What happened, in sequence

**1. I proposed a field task that was physically impossible.** I suggested Jesse count radiant tubes per coil while standing at the launchers, to recover the per-coil footage DQ-017 needs. The radiant tubes are vertical, inside the firebox; the launchers are at the convection inlets and the receivers at the radiant outlets. From either you are looking at flanges. Jesse caught it. The lesson is narrow and worth keeping: **before proposing a field observation, check that the thing is visible from where the person will be standing.**

**2. Jesse corrected `crash`.** A crash/emergency decoke is an *unscheduled mobilization* — the facility hits operational trouble and needs a crew cleaning on a moment's notice. It usually means a dirty coil. It does not mean one by definition. The vault had these welded together.

**3. Jesse corrected outlier handling.** Coils on one heater clean within a few hours of each other. You never have one process coil out of four that legitimately runs 12–24 hours longer than the other three. When one does, it means a problem specific to that coil on that decoke, or corrupt data — and the estimate comes off the average of the coils that cluster, never the outlier.

**4. Applying (3) moved the ~6 ft/hr figure onto the outlier.** CND25004's three coil sets ran 48 / 35 / 36 pig hours. The 35 and 36 agree within 3% on the same rig configuration and mode; the 48 sits 13 hours off. The ~6 ft/hr figure that has circulated since 2026-07-28, and that DQ-012 then DQ-017 held out of every benchmark pending reproduction, was computed from the 48.

**5. The drawings then showed the footage was also wrong.** Jesse supplied three PDFs. One — `Syncrude WO 20667490 2024TA 37-1F-1 Furnace Binder -IFR.pdf`, 361 pages — is a **different unit**: Plant 37-1, a VDU vacuum furnace, twin cell, telescopic design with 6"/8"/10"/12" tubes. I began building on it before Jesse stopped me; he confirmed and removed it from the folder. Nothing from it reached the card. The other two are the right furnace and settle the geometry.

## The finding

The Quest Integrity isometric's title block reads `Tube Count: Conv. 16, Rad. 31` and `Tube Lengths: Conv. 65.0 ft, Rad. 38.6 ft`. On 2026-07-23 those were recorded as **heater totals across 8 coils** — 47 tubes / 2,311 ft — and per-circuit figures were derived by dividing by 8. It is the exact inverse. The same drawing traces **eight** passes and numbers each pass's radiant tubes **1 → 31 individually**; a heater-wide count of 31 cannot give one pass 31 numbered tubes. The card's own corroborating quote from the CND24002 drawing, "(16) 6" Sch 40 tubes, 63'-6" effective", is likewise per-pass.

Corrected: **2,237 ft per pass, 17,893 ft and 376 tubes for the heater** — 8× the recorded value.

Recomputed per-coilset rates for CND25004: 47 ft/hr (48-hr set), 64 (35-hr set), 62 (36-hr set), against a recorded `routine` band of 47–259 and a mean of ≈99. **The 100 ft/hr benchmark was never broken on this heater.** It looked broken because the footage was wrong by a factor of eight, and the one figure anybody had tried to derive from it was additionally drawn from the outlier coil set.

The ~6 ft/hr figure is struck rather than qualified. It reproduces exactly — `2,311 ÷ 8 ÷ 48 = 6.0` — and reproducing it is what kills it. The downstream fill/flush question is moot: it was a qualifier on a number built from bad footage and the wrong coil set.

The per-coil "3-vs-4 radiant tube split" that DQ-017 was waiting on does not exist. It was an artifact of dividing one pass's 31 radiant tubes across 8 coils. Every coil carries 31 radiant and 16 convection tubes.

## What this says about the vault, not just this heater

The 2026-07-23 pass **asked exactly the right question** — "confirm whether reported lengths are per circuit or all coils total" was an explicit Open Flag — took the wrong branch, wrote **RESOLVED**, and marked the card `verified`. Thirteen months of derived figures inherited it. Three separate later passes (the 2026-07-28 idea research, the 2026-08-13 pre-staging review, the 2026-08-15 ruling) all reasoned *downstream* of that resolution and none re-opened it, because a flag marked resolved reads as settled.

The 2026-08-13 review deserves credit for getting closest: it concluded the figure could not be reproduced from card data and that reproduction had to come first. That instinct was right. What it could not do was reach outside the card — the answer was in a drawing nobody had opened.

Method note for reuse: the geometry was recovered by rendering **zoomed `pdftoppm` crops** and reading those, never full-page renders. Every figure on the card cites which crop of which page it came from. A full-page render of a D-size scan is not legible enough to transcribe a title block from, and transcribing one anyway is how a wrong number gets a confident citation.

## Open asks

Two, both queued. Neither is settled here. — **Both closed 2026-08-21; see the Apply Log below and the DQ rows for the rulings.**

**A. What happens to the rollup's `crash` class** — see DQ-026. **Ruled: re-label, keep the class.** `crash` is now defined vault-wide as a job class / callout label (unscheduled mobilization), the causal fouling claim is struck from every live-guidance surface, and the 6-row mean stays published as the emergency-quote basis — but may no longer be cited as evidence about coil condition. No schema change; the callout-vs-condition column split folds into DQ-017.

**B. Whether the outlier rule enters the duration model** — see DQ-027. **Ruled: yes, now.** The spread check is written into `01-context/estimating-approach.md` and the `usadebusk-estimating` skill, with this note's CND25004 case (48 / 35 / 36) as the worked example. The recording convention folds into DQ-017, which owns the per-coilset grain.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-20 | Rebuilt `7-1-F-1.md` geometry, identity, configuration, metallurgy and Open Flags from the drawings; struck ~6 ft/hr; quarantined the CND25004 48-hr coil set; regenerated `estimating-actuals-rollup.md` (Syncrude footage 2,311 → 17,893 ft; both rows still excluded from the condition means on blank `Mode`, unchanged). No Task Durations hours altered. Heater-card content is Lane 1 in full per the governance facility-data note. Queued DQ-026 and DQ-027 for the Lane 4 consequences. | Claude |
| 2026-08-21 | **Both open asks ruled and applied; note closed.** DQ-026 — `crash` re-defined as job class / callout label across `_canonical-heater-card.md`, `_heater-template.md`, `estimating_rollup.py` (prose, `by coil condition` → `by job class`, new confound callout), the regenerated rollup, `estimating-approach.md`, and `usadebusk-estimating` SKILL.md; the mean and every figure in the rollup are unchanged (verified byte-identical), only the stated cause moved. DQ-027 — per-coilset outlier check added to `estimating-approach.md` and the skill as a new Outlier check bullet, citing this note's CND25004 48/35/36 case, plus a pointer in the rollup's "Reading this" noting the spread is not visible from that table. Column split (DQ-026) and outlier-recording convention (DQ-027) both folded into DQ-017. Status `open` → `resolved`. | Claude |
