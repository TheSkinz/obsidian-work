---
type: review
status: open
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-08-20
related:
  - "[[F-501]]"
  - "[[idea-smart-pig-report-as-cleaning-verification]]"
  - "[[2026-08-19-idea-research-smart-pig-report-verification-gated]]"
  - "[[2026-08-16-steady-flux-f501-report-audit-findings]]"
tags: [review, smart-pig, inspection, UT, ExxonMobil, F-501, pre-staged, lane4]
---

# Review — Where does "air and fouling are the standing causes of UT data loss" land, and does F-501's B_8_C reading get a data-quality caveat?

## Trigger

Pre-staging loop run 2026-08-20, processing `00-inbox/2026-08-16-ut-data-loss-air-and-fouling.md`. Six candidates carried the defer marker without a pre-staged marker; three tied at the oldest filename date (2026-08-16) and again at `created:`, so git first-commit time broke the tie — this note committed at 15:34:40 −05:00, ahead of the frozen-fixture note (16:21:53) and the agnix-trial note (17:42:13). Nothing was skipped this run.

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-08-16-ut-data-loss-air-and-fouling.md` (read this run) | Observed | The item under review. Captured from Jesse in session 2026-08-16 and explicitly held: "Lane 4 domain truth — recorded here only, not written into [[F-501]], the ingest skill, or any other authoritative surface pending his ruling on where it belongs." The facts as stated: air in the coil is a common occurrence on smart-pig runs; many coils have no high-point bleeders; USADebusk has a method of bleeding that does not always work; air and fouling are the two common factors behind data loss in a UT inspection. The note itself names the candidate homes it wants ruled on — "a note under `04-knowledge/`, the smart-pig handling in the ingest skill, or both." |
| Same note, the consequence paragraph (read this run) | Observed | The part that carries more weight than the missing-extent question. Air causes dropout you can *see* — the pixels go white. Residual fouling can add an interface the tool may gate on, "producing a reading that looks valid and reads thin." B_8_C's minimum sits at 7:00 in a horizontal tube, which is both where deposit settles and where bottom-of-line corrosion lives, and the note states those two are not distinguishable from the C-scan alone. Its conclusion: "If there was residual fouling in that segment, the 0.224 in figure itself is in question, not just the missing extent." |
| Same note, the asymmetry paragraph (read this run) | Observed | The generalisable finding. It qualifies the load-bearing inference in [[idea-smart-pig-report-as-cleaning-verification]] — that a clean low-noise C-scan across a full coil is itself evidence the pigging reached bare metal. That direction holds; the converse does not, because trapped air produces the same noisy signature and is a coil-venting limitation rather than a cleaning failure. The note's warning: "the first unflattering report will be read against USADebusk for something that was never in scope." |
| Same note, the counter-evidence paragraph (read this run) | Observed | Offered by the note as evidence and explicitly not as a verdict. Against air for this specific segment: Figure 3 puts convection tube 1 at the top of the stack with flow running down to 9, so a gas pocket collects in B_1_C rather than B_8_C, and B_1_C images clean at 0.435. The note itself flags that this assumes drawn order matches physical elevation and says nothing about entrained air moving through during the run. Against uniform deposit: the zoom is heterogeneous. The note closes the paragraph by discounting its own evidence — "Inferring surface condition from a rendered image is weak evidence and should be held loosely." |
| `04-knowledge/manual/14-ancillary-smart-pig-support.md:27` (§14.3, read this run) | Observed | The nearest existing coverage, and it is only half. "Ultrasonic wall measurement requires acoustic coupling to the tube wall, and a coke deposit between the transducer and the steel degrades or invalidates the reading." This is framed entirely as a **prerequisite** — clean the coil before the tool goes in — not as a caveat on how a returned report is read. **Air is not mentioned anywhere in the section**, and neither is the possibility that a fouled reading looks valid rather than failing visibly. |
| `04-knowledge/manual/14-ancillary-smart-pig-support.md:53, :55–61` (§14.5 step 6 and §14.6, read this run) | Observed | §14.5 step 6 puts the valid-dataset call entirely with the vendor: "The vendor confirms whether the run produced a valid dataset. Where it did not, the run is repeated before the circuit is broken." §14.6 states the preliminary report "answers two questions at once: whether the vendor captured the data it needs, and whether any fouling remains." So the manual already ties data capture and fouling together at the gate — but as a pass/fail on the run, not as an interpretation limit on a number that did come back. |
| `04-knowledge/manual/14-ancillary-smart-pig-support.md:15–23` (§14.2, read this run) | Observed | The role boundary that bounds any option here: USADebusk "does not configure the tool, operate it, acquire data, interpret data, or make any representation about wall thickness results." This cuts both ways for the proposal — it is the reason a USADebusk-authored caveat on a vendor's number has to be phrased as a limit on what the data can support, never as a competing interpretation. |
| `02-facilities/ExxonMobil/Baytown-TX/F-501.md:277–283` (read this run) | Observed | The card's B_8_C entry, currently carrying **no data-quality caveat at all**: "0.224" remaining against 0.400" nominal, 43.9% loss, internal, minimum at 195.7" from the upstream weld at 210° from TDC (7:00 clock position), with loss extending nearly the full 226" segment. Ovality a normal 2.2%, so not mechanical." It records that ExxonMobil supplied no minimum allowable wall threshold and that fitness-for-service sits with ExxonMobil, but it does not record that the reading's validity is itself an open question with the vendor. |
| `02-facilities/ExxonMobil/Baytown-TX/F-501.md:271–275` (read this run) | Observed | The inspection-outcome paragraph, which is where the cleaning-verification claim already lives on a real card: coil "generally clean with only minor fouling remaining," no improperly-cleaned coke identified, and the card's own editorial — "That is third-party verification that the pigging met scope, and it is the most reusable artifact this job produced." This is the sentence the asymmetry bears on directly; it is already written, in the affirmative direction, with no statement of what a noisy scan would and would not mean. |
| `02-facilities/ExxonMobil/Baytown-TX/F-501.md:296` (shift record, receipt 10782, read this run) | Observed | Independent corroboration that venting is a live operational item on this specific job, not a general remark: the 2026-08-12 night shift records "a shutdown for bleeder-valve closure on the cross-overs" inside its 6 stand-by hours. The card carries **no** mention of high-point bleeders or their absence, which is the specific gap the inbox note's venting fact would fill. |
| `grep -rn -iE "trapped air\|air pocket\|venting\|dropout\|drop-out\|couplant"` over `04-knowledge/`, `06-insights/`, `01-context/` (run this run) | Observed | **Zero substantive hits** — the only returns are unrelated matches on "inventing" and one `quote-lifecycle.md` line about contract types. A companion grep for "high-point"/"high point bleeder" across `04-knowledge/` and `02-facilities/` returns **nothing**. The vault holds no statement anywhere that air causes UT data loss, that many coils lack high-point bleeders, or that a noisy C-scan is ambiguous between fouling and venting. |
| `~/.claude/skills/usadebusk-vault-ingest/SKILL.md` and `usadebusk-sop/SKILL.md` grepped for air/dropout/coupling/C-scan (run this run) | Observed | Two hits, both false positives — a customer-name list containing "Chev**ron**"-adjacent tokens in the ingest skill and a pass/circuit line in the SOP skill. Neither skill carries any smart-pig data-quality content. The ingest skill's smart-pig handling, which the inbox note names as a candidate home, does not currently exist as a distinct section. |
| `tools/*.py` grepped for smart-pig/inspection; `~/.claude/hooks/` listed (run this run) | Observed | Ten hook files, all guards on git, exec, fixture replay, staged counts and word-delta — nothing touching inspection data. In `tools/`, the only hits are the `Smart Pig` **column name** in the Task Durations schema (`estimating_rollup.py:38`, `vault_lint.py:182`) and the SharePoint export mapping. No implementation exists that any option here would duplicate. |
| `tools/sharepoint_export.py:100–101` (read this run) | Observed | **Load-bearing for Option A2.** `manual/14` is one of the notes projected to the SharePoint `Knowledge` library, so amending it is not a private edit — it propagates to a shared internal surface on the next export run. The script's own docstring bounds the exposure: "Every member of the Furnace Decoking site is trusted with all of its data (Jesse, 2026-08-10)," so this is internal, not customer-facing. Still means an edit here reaches readers who will not see the review note behind it. |
| `06-insights/2026-08-19-idea-research-smart-pig-report-verification-gated.md` (read this run) | Observed | The adjacent smart-pig thread, closed as **gated** on 2026-08-19 pending a second vendor report, with the correction that Quest does not release project reports so the gate now waits on a future job. It concerns *report access* and whether a report is a durable commercial asset. It does **not** state the asymmetry this note is about — its own reasoning still runs one-directional ("a clean low-noise C-scan across a full coil is itself evidence the pigging reached bare metal") with no note of what a noisy scan does not prove. So it neither covers this question nor blocks it, and its being parked is the argument for Option D: the guardrail should be attached now, while the claim is still unbuilt. |
| `06-insights/2026-08-19-prestaged-treat-gas-loss-nominal-basis.md` and DQ-024 (read this run) | Observed | The sibling pre-staged note from the same source cluster, drafted from the audit-findings note. Read specifically to confirm no overlap: DQ-024 asks what **baseline** a reported loss percentage is computed against (nominal vs minimum wall) on the Treat Gas section. This note asks whether a reading is **valid at all** on a convection segment, and where a general data-quality fact lives. Different sections, different failure modes, no overlap. That note's own Source Material row on this file reached the same conclusion independently: "Read to confirm the two do not overlap — they do not." |
| `00-inbox/2026-08-16-steady-flux-bore-profile-request-owed.md` (read this run) | Observed | Checked because both concern open Steady Flux questions and might be the same outreach. They are not — that one requests internal-radius/bore-profile data for A_1_X and B_1_X to convert the 4.75 in pig assumption into a measured number, and it retired itself the same day (`status: closed-unactioned`, handled by text). The B_8_C dropout question is separate and, per the item under review, still **awaiting response**. |
| `50-dashboards/decision-queue.md` (checked this run) | Observed | Seven open rows, DQ-016 through DQ-021 plus DQ-024; highest id ever issued is DQ-024. Under the cap of 10, so this run may append. No open or closed row concerns UT data quality, coil venting, or the validity of an inspection reading. Nearest neighbours are DQ-021 (rig-out acceptance gate) and DQ-024 (loss baseline) — adjacent, not overlapping. |
| `git log --oneline --since=2026-08-14` (run this run) | Observed | Nothing since the note was captured touches UT data quality or coil venting. The smart-pig-adjacent commits are `c12168e` (seed instance count corrected, DQ-021 opened on the §14.6 gate), `87deb89` (Lane 4 launcher/receiver role-boundary correction) and `00fd105` (the Quest-does-not-release-reports finding). Confirms this is genuinely unaddressed rather than merely un-found in prose. |

## The Question

Jesse's field knowledge — air and fouling are the two standing causes of UT data loss, many coils have no high-point bleeders, and the USADebusk bleeding method does not always work — is Lane 4 domain truth sitting in an inbox note with no durable home. It carries two consequences the vault does not currently state anywhere: that a noisy C-scan is **not** evidence of poor cleaning even though a clean one is evidence of good cleaning, and that residual fouling can produce a reading that looks valid and reads thin rather than failing visibly. Where does the general fact land, and does F-501's B_8_C entry get a validity caveat while the question sits open with Steady Flux?

## Proposed Change

**Options A1, A2, B and C are mutually exclusive — pick one. Options D and E are additive and can ride with any of them.**

**A1 (exclusive). A short note under `04-knowledge/`, outside the manual.** Record the fact where domain knowledge lives without touching a procedural document: air and fouling as the two standing causes of UT data loss, the venting limitation (many coils have no high-point bleeders, the bleeding method does not always work), the visible-vs-invisible failure distinction, and the asymmetry. The case for this home is that the content is *interpretive* rather than procedural — it tells a reader how to read a report, which is not what the manual's numbered sections do — and `04-knowledge/concepts/` already holds exactly this kind of orienting material. It also keeps the edit out of the SharePoint projection until Jesse decides it should go there.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**A2 (exclusive). Amend `manual/14` — extend §14.3 or add a §14.8 on data-quality limits.** The manual already carries the fouling half at §14.3, framed as a prerequisite, and already ties data capture to fouling at the §14.6 gate. Adding air alongside coke, and stating that a returned reading can be degraded without failing visibly, completes a statement the manual already half-makes rather than starting a second document that says something adjacent. The cost is that `manual/14` is projected to the SharePoint `Knowledge` library (`sharepoint_export.py:100`), so this reaches a shared internal surface on the next export — and it is SOP content, which is Lane 4 and squarely outside what this loop may write.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**B (exclusive). Record it on [[F-501]] only, and generalise later.** Treat it as a job observation rather than a standing rule until the Steady Flux answer lands. The card is where B_8_C, the bleeder-valve shutdown on the cross-overs and the inspection outcome all already live, so the fact would sit beside the evidence that prompted it. The argument for waiting: the vendor's raw A-scan waveforms may show the dropout was coupling, surface condition or something else entirely, and a general rule written now off one segment would be a rule written from the weakest available evidence — which the source note itself concedes when it discounts its own image-based reasoning.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**C (exclusive). Leave it in `00-inbox/` as captured.** Nothing downstream depends on it today: the cleaning-verification idea is parked and gated on a future job, no proposal or close-out language has been built on it, and F-501's next scope is years out. On this reading the note is already doing its job — it is written down, it is findable, and it is honestly labelled as unruled. Giving it a permanent home now spends a Lane 4 ruling on a fact with no current consumer.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**D (additive). Attach the asymmetry to the cleaning-verification claim wherever it is written.** Independent of where the general fact goes, the specific guardrail — *a clean C-scan supports the cleaning claim; a noisy one does not refute it, because trapped air produces the same signature* — needs to travel with any close-out or proposal language built on a vendor report. The seed is parked and its research note reasons one-directionally today, so the guardrail can be attached before anything is built on it rather than retrofitted after the first unflattering report. This is the highest-leverage half of the whole item: it is the piece that protects USADebusk commercially, and it costs one sentence.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**E (additive). Add a validity caveat to F-501's B_8_C entry while the vendor question is open.** The card presents 0.224 in / 43.9% loss as a measured fact with no note that its validity is itself under question with Steady Flux, and that B_8_C is the one segment the report quantifies with only a clock position and a distance. The exposure is the same asymmetric shape the card already guards against one screen earlier for the 45.7% radiant figure ("Do not let the 45.7% figure travel without this context") — an unqualified 43.9% on the one segment flagged for ExxonMobil's attention is exactly the number that travels. The caveat states a limit on what the data supports, not a competing interpretation, which keeps it inside the §14.2 role boundary.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

**The strongest argument against acting now is that the whole item is one open vendor question away from being answered.** Jesse put the B_8_C question to Steady Flux on 2026-08-16 and it is still outstanding; their raw A-scan waveforms settle whether the dropout is coupling, residual fouling or surface condition, and nothing on the USADebusk side can. Every option except C writes something that a single vendor reply could make wrong or redundant. That argues for B or C on evidence grounds — with the important exception of Option D, whose content does not depend on the answer at all. The asymmetry is a physics fact about what a noisy scan can and cannot prove; it is true whichever way B_8_C resolves.

**The general fact and the specific segment rest on very different evidence, and merging them would be an error.** The general fact — air is common, many coils lack high-point bleeders, the bleeding method does not always work — comes from Jesse's own field experience and is as authoritative as vault content gets. The application to B_8_C is inference from a rendered figure, and the source note discounts it twice in its own text. The memory rule applies directly: a field base rate from Jesse outranks a mechanism guess off a rendered image. Any option that writes the general fact should write it as Jesse's stated field knowledge and must not import B_8_C as its evidence, or a strong fact acquires a weak citation.

**A2's real cost is scope, not content.** `manual/14` is SOP content and it projects to SharePoint, so amending it is a Lane 4 write on a shared surface — the one thing this loop is barred from doing, and correctly so. Nothing in this note should be read as recommending the edit itself; the option exists so the *home* question can be decided in one pass rather than two.

**Option E's counter-argument is that the card is already honest about the limits it knows.** It records that ExxonMobil supplied no minimum allowable wall threshold and that fitness-for-service sits with ExxonMobil. A reader who takes that seriously already knows the card is not making a condition call. The counter-counter is that "no threshold supplied" and "the reading may not be valid" are different limitations, and only the first is written down.

**Everything in this review traces to two sources.** The inbox note and the F-501 card — and the card's inspection content itself traces to the same Steady Flux report the inbox note is questioning. The corroborating grep results establish *absence* of coverage, which is a different and weaker claim than independent confirmation of any fact asserted here. The Steady Flux PDF was not opened this run, and no figure in the source note was re-verified against it.

## Decision

- [ ] A1 — durable note under `04-knowledge/`
- [ ] A2 — amend `manual/14`
- [ ] B — record on [[F-501]] only for now
- [ ] C — leave in `00-inbox/` as captured
- [ ] D (additive) — attach the asymmetry guardrail to the cleaning-verification claim
- [ ] E (additive) — add a validity caveat to F-501's B_8_C entry

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
|  |  |  |  |
