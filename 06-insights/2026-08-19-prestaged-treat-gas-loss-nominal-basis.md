---
type: review
status: open
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-08-19
related:
  - "[[F-501]]"
  - "[[USA26041-job-report]]"
  - "[[2026-08-16-steady-flux-f501-report-audit-findings]]"
tags: [review, smart-pig, inspection, ExxonMobil, F-501, pre-staged, lane4]
---

# Review — Is F-501's Treat Gas "9–14.5% loss, general thinning" measured against the right baseline, and does the card change?

## Trigger

Pre-staging loop run 2026-08-19, processing `00-inbox/2026-08-16-steady-flux-f501-report-audit-findings.md`. Five candidates tie at the oldest filename date (2026-08-16) and at `created:`; three tie again at the same git first-commit timestamp (15:34:40 −05:00), so the tie was broken alphabetically. The first of those, `2026-08-16-steady-flux-bore-profile-request-owed.md`, was skipped this run as already covered — it retired itself the same day and is already cited by name in DQ-018.

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-08-16-steady-flux-f501-report-audit-findings.md` (read this run) | Observed | Full-document audit of Steady Flux `26-0663-002 Rev. A`, captured at USA26041 close-out. Its findings sort into three tiers by the note's own labels. The **airtight** tier (Appendix D vs body contradictions on C_10_R, the duplicated "Distance to Upstream Circumferential Weld" header meaning two different things, four Table-12-vs-figure distance splits, A_15_R's blank-vs-1.5% ovality and its 516.0 in outlier, the undocumented crossover section, two overreaching executive-summary statements, three unmarked C-scan colour scales, and a typo list) was **already sent informally to the Steady Flux CEO on 2026-08-16** — those need transcribing, not deciding. The **needs-an-argument** tier is the water speed-of-sound figure. The note then isolates one item explicitly under "Questions, not findings — deliberately not asserted," and states of it: "This is Lane 4 and unresolved; the card has not been changed." That item is the subject of this review. |
| Same note, the Lane 4 paragraph (read this run) | Observed | The report's Table 4 describes the Treat Gas pipe as "5-inch schedule 80 (5.563 in x 0.375 MWT)" while the results header calls that same 0.375 figure "Nominal Wall Thickness." The note's argument: those are different things, A53/A106 permit −12.5%, so 0.328 in is an acceptable **as-new** wall, and it reports that 28 of the 31 Treat Gas readings sit above 0.328. If the pipe was bought to schedule rather than to a minimum wall, much of the reported "9–14.5% loss" may be original mill under-tolerance rather than corrosion. The same terminology slip runs the **other** way on the 9Cr sections: if 0.400 and 0.464 are genuinely minimum wall as Table 4 says, real loss there is understated. |
| `02-facilities/ExxonMobil/Baytown-TX/F-501.md:286` (read this run) | Observed | The card's Field Notes currently state, without qualification: "Treat Gas a uniform 9–14.5%, min 0.321" at A_7_TG. The Treat Gas pattern is general thinning with no localised anomaly, consistent with it being the one **carbon steel** section against 9Cr elsewhere." This is the sentence the question bears on — it reads the percentages as a corrosion characterisation. |
| `02-facilities/ExxonMobil/Baytown-TX/F-501.md:40` (Tube Geometry, read this run) | Observed | Treat Gas row: `Horizontal · Carbon steel · OD 5.563 · Sched 80 · Wall 0.375 · ID 4.813 · 16 tubes · 19.08 ft avg · 325 ft`. **Metallurgy is recorded only as "Carbon steel" — no grade.** The −12.5% argument is an A53/A106 mill-tolerance rule, so the card as it stands cannot confirm the spec the tolerance would come from. The geometry note beneath adds that the whole row is measured from the Steady Flux report, and that "The report identifies it as 5-inch schedule 80." |
| `02-facilities/ExxonMobil/Baytown-TX/F-501.md:400–414` (Rev B section, read this run) | Observed | The card already carries a "**Errors in Steady Flux report 26-0663-002 Rev. A — send back for Rev B**" section holding the two errors found on the 2026-08-15 pass, with the framing "Both are display-only; the arithmetic underneath each is correct, so no result changes." The Treat Gas basis question is a different class — it does not change any printed number, it changes what the printed number *means* — and the section as written has no place for that. None of the audit note's new findings appear in this section or anywhere else on the card. |
| `02-facilities/ExxonMobil/Baytown-TX/USA26041-job-report.md` (grepped this run for Treat Gas / thinning / 9–14) | Observed | The vault-native index of the customer-facing job report mentions Treat Gas three times — scope, "Treat Gas had no fouling," and the pig-count line — and carries **no wall-loss or condition claim at all**. The report is marked "operational only." So the disputed characterisation lives on the internal heater card, not in a document already delivered to ExxonMobil. |
| Arithmetic checked this run against the figures above | Derived | 0.375 × 0.875 = **0.328125** in, confirming the note's 0.328 as-new floor. The card's own worst reading, 0.321 in at A_7_TG, is 14.4% below 0.375 — matching the "9–14.5%" range — but only **2.1%** below 0.328125. The two readings of the same measurement differ by roughly a factor of seven at the worst point. The note's "28 of 31 readings above 0.328" claim was **not** verified this run; the Steady Flux PDF was not opened. |
| `50-dashboards/decision-queue.md` (checked this run) | Observed | Six open rows, DQ-016 through DQ-021, highest id ever issued DQ-023. None concerns Treat Gas, wall-loss baselines, or vendor-report terminology. DQ-021 is the closest neighbour and is about the rig-out acceptance gate, not inspection data interpretation. Not already queued. |
| `grep -rn -iE "minimum wall\|MWT\|mill tolerance\|under-tolerance\|12.5%"` over `04-knowledge/`, `06-insights/`, `01-context/` (run this run) | Observed | **Zero hits.** The vault holds no convention anywhere for how a smart-pig report's percentage-loss baseline should be read. Related grep for `A106\|A53\|0.328\|as-new` returns only heater-card metallurgy cells on other heaters and the inbox note itself. |
| `tools/*.py` grepped for `nominal` / `schedule 80` (run this run); `~/.claude/hooks/` listed (run this run) | Observed | Only two unrelated hits (`estimating_rollup.py:171` nominal *fouling*, `pig_usage_rollup.py:64` nominal *pig size*). Ten hook files, all guards on git/exec/fixture/word-delta — nothing touching inspection data. No implementation exists that this proposal would duplicate. |
| `git log --oneline -25` (run this run) | Observed | Nothing since 2026-08-15 touches Treat Gas, wall-loss baselines, or the F-501 inspection interpretation. The recent F-501-adjacent commits are the Lane 4 launcher/receiver role-boundary correction (`87deb89`) and DSP26085 workup work. Confirms the question is genuinely unaddressed rather than merely un-found in prose. |
| `06-insights/2026-08-19-idea-research-smart-pig-report-verification-gated.md` (read this run) | Observed | The adjacent smart-pig thread — whether a clean inspection report is a durable commercial asset — was closed as gated on 2026-08-19, pending a second vendor report. It does not touch how loss percentages are baselined, so it neither covers nor blocks this question. |
| `00-inbox/2026-08-16-ut-data-loss-air-and-fouling.md` (read this run) | Observed | The sibling note the audit points to for its open item. It carries a separate Lane 4 question (air and fouling as standing causes of UT data loss, and whether B_8_C's 0.224 in reading is itself in question). Read to confirm the two do not overlap — they do not. It remains an unprocessed candidate for a future run of this loop. |

## The Question

The card characterises Treat Gas as "a uniform 9–14.5%" loss showing "general thinning," a percentage computed against 0.375 in — a figure the vendor's report labels **minimum wall** in one table and **nominal wall** in another. If it is nominal schedule wall, an A53/A106 as-new floor of 0.328 in puts nearly every reading inside mill tolerance and the thinning characterisation is wrong; if it is genuinely minimum wall, the characterisation stands and the 9Cr sections are understated instead. Does the card get qualified now, does it wait on confirmation of the basis, or does it stay as written?

## Proposed Change

**Options A, B and C are mutually exclusive — pick one. Option D is additive and can ride with any of them.**

**A (exclusive). Qualify the card now; change no number.** Add one sentence to the Field Notes Treat Gas line recording that the percentages are computed against 0.375 in, that the report labels that figure both MWT and nominal, and that if the pipe was bought to schedule the −12.5% as-new floor of 0.328 in puts nearly every reading inside mill tolerance. The 0.321 in minimum and the 9–14.5% range stay exactly as they are; only their reading is bounded. The case for acting now is that the caveat costs nothing and the exposure is asymmetric — an unqualified "general thinning" line on a carbon-steel section is the kind of sentence that travels into a future proposal or scope conversation as though it were a condition finding, which is the exact failure the card already guards against one screen earlier with "Do not let the 45.7% figure travel without this context."

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**B (exclusive). Ask first, write after.** Hold the card unchanged and confirm the basis — either from Steady Flux (which table is right, and against what the software computed) or from ExxonMobil's material records for that pipe. Write whatever comes back, as measured fact rather than as a caveat. The channel already exists and is warm: Jesse sent the audit list to the Steady Flux CEO on 2026-08-16 and has an open question with them on B_8_C, so this rides along at near-zero cost. The case for waiting is that a caveat written now would itself have to be rewritten once the answer lands, and a vault sentence that says "possibly one thing, possibly another" is weaker than either resolved version.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**C (exclusive). Leave the card as written.** The percentages are the vendor's own, reproduced faithfully; ExxonMobil supplied no minimum allowable wall and owns fitness-for-service, as the card already records for B_8_C; and no USADebusk decision depends on the Treat Gas number — it did not affect pig sizing (the radiant governs at 4.635 in ID), it did not affect scope, and the section pigged clean in under two hours. On this reading the ambiguity is real but inert, and adding a hedge to a section nothing depends on is ceremony.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**D (additive). Settle the convention once, for every section and every future report.** The same nominal-vs-minimum-wall slip runs in both directions in this one document — overstating loss on the carbon-steel Treat Gas if 0.375 is nominal, understating it on the 9Cr sections if 0.400 and 0.464 are genuinely minimum wall. The vault currently holds no rule for reading a percentage-loss baseline anywhere (zero grep hits across `04-knowledge/`, `06-insights/`, `01-context/`), so the next vendor report gets read the same unexamined way. This would be a short convention — record which baseline a reported percentage is computed against, and treat an unstated or self-contradictory baseline as a documented unknown rather than resolving it silently — with a home in `04-knowledge/` and/or the `usadebusk-vault-ingest` smart-pig handling.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

The load-bearing weakness in A and D alike is that **the −12.5% argument is not established for this pipe.** It is a mill tolerance on A53 and A106 seamless and welded pipe; the card records the Treat Gas metallurgy only as "Carbon steel," with no grade, and records the schedule from the vendor's own sentence rather than from an ExxonMobil material record. If the pipe is a grade with a different tolerance rule, or was procured to a minimum wall, the whole reframing collapses and a caveat written now would be a wrong caveat rather than a cautious one. Option A's phrasing has to carry that conditional honestly, and if it does, it starts to read like Option B written in the card instead of in a question to the vendor.

A second and sharper counter-argument to A: this note is itself the product of one unverified reading. The "28 of 31 readings above 0.328" figure comes from the inbox note and was **not** checked against the PDF this run, and the memory of the DSP26085 workup applies directly — several artifacts agreeing prove nothing when they all derive from the one artifact in question. Every number in this review traces to either the audit note or the card, and the card's Treat Gas row traces to the same Steady Flux report the audit is auditing. Nothing here has been corroborated against an independent source. That argues for B over A on evidence grounds, not just on tidiness.

The counter-argument to B is decay, and it is the same one that made the bore-profile request urgent: vendor goodwill and technician recall are freshest now, and the F-501 next scope is years out. If the question is not asked in the same conversation as the audit findings, it likely never gets asked, and the card sits unqualified anyway — which is Option C by default rather than by decision.

The counter-argument to C is narrower than it looks. C is defensible on the merits — nothing operational turns on the number — but it leaves an unqualified characterisation of a customer's asset on a card that feeds proposals, and the card's own precedent one section earlier is to qualify exactly this kind of figure rather than let it travel. C is a decision to accept that, not an absence of one.

D's risk is scope creep from a single instance: one document with an ambiguous baseline does not establish that vendor reports generally have this problem, and n=1 conventions written into a skill are how the vault has previously acquired rules it later had to unpick. It is included because the two directions of the same slip inside one report is more than a single data point about that report, but it should be read as the weakest-evidenced of the four.

**Falls out regardless of which option wins, and is not part of this decision:** the audit note's airtight tier — the Appendix D contradictions, the two-meanings header, the four distance splits, A_15_R's ovality and length outlier, the undocumented crossover, the two executive-summary overreaches, the three unmarked colour scales and the typo list — is already sent to Steady Flux and belongs in the card's existing "send back for Rev B" section. That is transcription, not a decision, and this loop cannot write it.

## Decision

*(Pending — Jesse to review.)*

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-19 | Note filed by pre-staging loop from `00-inbox/2026-08-16-steady-flux-f501-report-audit-findings.md`. Coverage checked in all four required places before drafting: prose (`04-knowledge/`, `06-insights/`, `01-context/` grepped for minimum-wall/MWT/mill-tolerance — zero hits), `tools/` (two unrelated "nominal" hits), `~/.claude/hooks/` (ten guards, none inspection-related), and `git log --oneline -25` (nothing on the topic). F-501 read directly at the Tube Geometry row, the Field Notes Treat Gas line and the existing Rev B section; the job report grepped to confirm the disputed characterisation is internal-only. The 0.328125 as-new floor and the 14.4%-vs-2.1% split were computed this run; the audit note's "28 of 31" claim was **not** verified — the Steady Flux PDF was not opened. `decision-queue.md` checked, not already queued. One sibling candidate skipped this run as already covered (DQ-018). No vault content modified beyond this note, the queue row, and the two inbox markers. | Claude (pre-staging loop) |
