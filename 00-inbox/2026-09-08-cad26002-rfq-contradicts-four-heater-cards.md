<!-- vault-loop: Lane 4 — domain truth. Four contradictions between Suncor's governing documents and the heater cards. Needs Jesse's ruling; do not self-route or apply. -->
---
type: note
status: inbox
created: 2026-09-08
tags: [inbox, suncor, CAD26002, heater-cards, data-quality, lane-4, owed]
source: "DI-GE-5-007 Rev.5 (Directive de chantier, 2020-01-10) and GM-07-000-00-001 Rev.7 (Raclage des tubes de fournaise), both read in full 2026-09-08 — the first is now in the vault at 02-facilities/Suncor/Montreal-QC/, the second is not"
verified: 2026-09-08
---

# Suncor's governing documents contradict four of the five Montreal heater cards

The RFQ text was never mined. Every card's `source:` field cites the *tube and pipe BOM* — appendix material — and the 2026-07-07 ingest commit (`7798d54`) says the same: "Heater cards built from RFQ drawings/BOMs." Nothing in the vault cites a clause of the directive itself. Reading it end to end on 2026-09-08, the night before mobilization, surfaced four direct contradictions and one resolution.

**Nothing here has been applied.** These are Lane 4 and they belong to Jesse. The crew brief drafted the same evening was written to the customer's documents, not to the cards, so the field is not exposed while these sit open.

---

## 1. Soda ash scope — RULED AND APPLIED 2026-09-08

**Closed. Jesse: "The facility document is correct about the soda ash. I think we over generalized."** The directive governs — soda ash on **B-102 radiant only**. Applied across `_facility.md`, `_walkdown-summary.md`, B-101, B-102, B-103 and B-1001; B-151's card never claimed it and its *"carbon steel (no passivation concern)"* line is now consistent rather than contradicted. The root cause is recorded on every card that carries UD1: **it is a spool material rating, not a process instruction.** Original analysis kept below.



**The directive scopes it to B-102 radiant only.** Particular conditions on furnace B-102: *"DECOKING WITH SODA ASH AND TUBE DRYING WITH NITROGEN for radiant only"*. The §.6 technical data table prints `21000 GAL` against B-102 and `N/A — NO SS IN TUBES` against B-101, B-1001, B-103 and B-151. Suncor supplies it (§.7): a baker tank of fresh 2 wt% solution, a second for used, and a vacuum truck.

**`_facility.md` says the opposite** — soda ash across all five including carbon-steel B-151, regardless of metallurgy, recorded as Jesse's call 2026-07-23 and sourced to *"the Suncor rep's decoke spec (UD1 'water/soda ash' temp-spool spec)"*.

Those are two different documents. UD1 is a temporary-spool design spec (700 psig / 370 °F design, 1050 psig hydrotest); the directive is the process instruction. The likely failure is that a spool spec calling for water/soda-ash service was read as a process requirement for every heater. **But that was Jesse's ruling and it may have come from the rep verbally, in which case the directive's table is the stale artifact.** Ask him; do not overwrite either way.

If the directive governs, four heaters lose a process step and the note in all five cards' metallurgy blocks needs rewriting.

## 2. Circuit splits differ on three heaters

| Heater | Directive | Card |
|---|---|---|
| B-102 | Circuit 1 = *"Upper two rows of convection piped together"*; Circuit 2 = *"Lower 8 rows of convection coils and complete radiant coils piped together"* | Convection is one circuit (16 tubes, 8/pass), radiant is another, crossover removed |
| B-1001 | Circuit 1 = convection + radiant **bottom** section; Circuit 2 = convection + radiant **top** section (§.1: central convection + upper radiant / outer convection + lower radiant) | Circuit 1 = passes A+D, Circuit 2 = passes B+C |
| B-101 | Two circuits, *"radiant and convection combined (north side)"* and *"(south side)"* | 10 convection coils each its own circuit, feeding 2 radiant passes |

The launcher hardware agrees in every case; only the circuit membership differs.

**B-102 carries an operational consequence.** If the lower 8 convection rows really are piped with the radiant, circuit 2 contains 4" convection tube behind an `8"-300#` launcher, so the 4" bore governs the pig on that circuit — not the 6.065" radiant the card names as governing. The card reaches the right heater-level max pig OD by a route that would be wrong per circuit.

**B-1001 gains a rig-in fact the card lacks:** *"The launchers and receivers are 5 feet from the ground next to the FVs"*, 4"-300# qty 4.

## 3. B-1001 metallurgy is mixed, not uniform

§.6 lists convection `SA213 T5 (5CR-1/2MO)` and radiant `SA213 T9 (9CR-1MO)`. The card states *"SA213 9Cr-1Mo throughout — no mixing."* Direct contradiction, and it puts B-1001 in the same mixed-metallurgy class as B-101, B-102 and B-103 rather than standing apart from them.

## 4. Footage runs high against the BOM-derived figures

| Heater | Directive (customer-stated) | Card (BOM-derived) | Delta |
|---|---|---|---|
| B-102 | ≈6,000 ft (1,000 conv + 5,000 rad) | 4,653 ft | −22% |
| B-1001 | ≈6,650 ft (2,050 + 4,600) | 5,813 ft | −13% |
| B-151 | ≈3,400 ft | ≈3,405 ft | match |
| B-101 | ≈4,600 ft | not totalled on card | — |
| B-103 | ≈1,600 ft | not totalled on card | — |

These drive duration. B-151 matching almost exactly is the useful signal: the method is sound, so the two large deltas are worth resolving rather than dismissing as customer rounding. This raises the value of [[2026-08-24-suncor-ingest-batch-audit-owed]], which is still open on the four cards never re-checked after B-102 was found carrying heater totals in per-circuit columns.

## Resolved, not contradicted

**B-101 radiant flange rating is 150#.** Stated twice — in the B-101 special conditions (`10" - 150# (qty. 2)`) and again in the §.6 table. The card has carried an unresolved *"10"-150# vs 10"-300# both appear on page 13 GA drawing"* flag since July. The directive settles it, and this one can be applied without a ruling.

## Requirements the vault records nowhere

Not contradictions — simply absent. All from the two documents, and all now in the crew brief:

- **Tungsten-carbide-tipped pigs are prohibited**, in both documents, the directive in caps. Urethane-coated foam only; square-head 600 BHN hardened steel tips or stainless hex head bolts; 3/16" square heads only on 600 BHN, 1/16" heads prohibited. Reason given: carbide studs *"severely damage 180 degree elbows."*
- **Maximum decoking pressure 740 PSIG** on all five; ambient 100 °F.
- **Cleanliness is a stop rule**: 6–8 seconds of black effluent after the pig reaches the receiver, then gray or rust water. *"Pigging must be stopped when this criterion is met to avoid creating furrows in the tubes."* Seconds recorded in the pigging log.
- **Initial and final hydraulic tests at three different flow rates.**
- New filter bag or element at the start of each pigging, dry weight recorded first.
- Last pig per bundle visually inspected by the **Suncor execution group**; cleanliness checklist and pigging log signed by the **Suncor operating group**; visible tube ends inspected when launchers come off.
- Soda-ash chemistry where used: 2 wt% Na₂CO₃, water Cl <50 ppm, fresh solution Cl <65 ppm and pH >9, inject below 130 °F, circulate 1 hr each direction (2 hr minimum), analysed at 30 min then every 2 hr max, running limits pH >9 and Cl <250 ppm. Raw diesel as anti-foam, ~1 gal at a time.
- **Nitrogen drying safety protocol**: two single-frequency radios, truck cab windows closed and HVAC off, safety perimeter, gas detector on every worker inside it, and *"The presence of an operator at the nitrogen valve is therefore mandatory at all times."*
- Vertical tubes (B-103 is vertical; B-1001 has a 12 ft vertical section): sponge pig run three times with nitrogen, hot N₂ at ≈130 °F never exceeding 140 °F, dry ≥30 min, dew point 40 °F below tube wall validated by Draeger as a GO/NO-GO.
- **Suncor supplies fuel for our decoking truck pumps and the 3" portable pumps**, plus labour and tools for handling and installing hoses and launchers/receivers, a min 375 scfm compressor, water, lighting, containment, scaffolding, zero energy, spool installation and the anti-foam diesel.
- **Suncor has decoked these units before** — the nitrogen line reads *"(was used in 2018 and 2021)"*. Prior pigging logs and hydraulic-test results may exist on their side; worth asking the rep for.

## Open questions that are not card questions

- ~~**Which tender option were we awarded?**~~ **Closed 2026-09-08 (Jesse): "It's only a one pumper job."** One Trimax, one filter press — no second truck to chase before mob. Worth recording *why* the plan looked like a mismatch, because the same shape will recur on Suncor work: §.3 frames the choice as Option 1 (one furnace after another, 1 decoke truck + 1 filter press) versus Option 2 (two furnaces in parallel, the 5th after, **2 decoke trucks + 2 filter presses**), and Travis's plan runs two heaters per run — Option 2's *sequence* — on Option 1's *equipment*. That is not a contradiction. **Suncor's options were written assuming one circuit at a time per truck; a Trimax in triple mode runs three concurrently**, which collapses their parallel option onto a single pumper. Run 1 pairs B-1001's two circuits with B-103's one, Run 2 pairs B-102's two with B-151's one, and Run 3 takes B-101's two in double mode. Do not read a future Suncor tender's option split as an equipment requirement without checking it against mode capability first. Still open and unrelated: there is **no quote note for this job anywhere in the vault** — no DSP number, no submitted price, no `type: quote` frontmatter for Suncor. The only Montreal quote in the estate is `DSP# 25011CAD Suncor Montreal April 2025.pdf`, which predates this package.
- **Were the five required sketches issued?** §.5 requires *"A sketch for each furnace showing the launchers / receivers and the various equipment including the lengths of the hoses required VS truck locations and the required connections to the launchers and receivers and to the truck."* Nothing in the vault records that we submitted them. Note the standing do-not-use ruling on the rig-diagram tool ([[2026-08-16-backtest-rig-diagram-layout-engine]]).
- The directive's own premise is **April 2026 on two 10-hour shifts**; the job is executing September on day/night. The document is DI-GE-5-007 Rev.5 dated 2020-01-10, a standing site directive reused for this turnaround, so parts of it may predate the current scope.

## What was done with this on 2026-09-08

Crew brief drafted from the two documents and handed to Jesse to send — see [[CAD26002-crew-brief]]. It quotes Suncor verbatim throughout and asserts none of the contested card content, so sending it does not commit us to either side of the four contradictions above.

**Appendix A (the GM-07 extract) is not in the vault.** It was scoped out of the 2026-09-08 copy as not field-useful, which was wrong — the directive requires that everyone directly involved in the decoke has read it, and it is where the carbide prohibition, the cleanliness stop rule, the soda-ash chemistry and the entire nitrogen protocol live. 320 KB, offered to Jesse and not yet answered.
