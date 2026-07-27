---
type: heater
heater-id: TriEthane-TE-II-EDC-Pyrolysis
heater-tag: TE-II
unit: Tri-Ethane
facility: Westlake-South-Westlake-LA
client: Westlake South
heater-type: other
service: EDC Pyrolysis Furnace (ethylene dichloride cracking)
configuration: Individual-Passes
last-updated: 2026-07-27
tags: [heater-card, Westlake-South, other]
source: Selas Fluid Processing fired heater data sheet SFPC Job 89S-7016-0936 Rev. 2 (1989-04-12) + drawings LH936-E101 (convection coil) & LH936-E102 (radiant coil); coil confirmed still as-built by Jesse 2026-07-27
verified: partial — coil confirmed as-built by Jesse 2026-07-27; tube ID not stated in source (derived figures held in Notes, unverified in field); connection method unresolved
---

# TE-II EDC Pyrolysis Furnace — Westlake South, Westlake, LA

> ⚠ **SPECIAL METALLURGY — Incoloy 800H (Ni-Fe-Cr), all three coil sections.** Not carbon
> steel. Post-cleaning treatment method is **TBD pending Westlake's written instruction** — the
> customer rep's bid instructions govern the method, not the metallurgy alone, and no bid
> instructions accompanied the 2026-07-27 RFQ. Do not assume soda ash passivation, and do not
> assume it is out of scope either. Ask.

> ⚠ **NO FLANGED CONNECTIONS AS DESIGNED.** The data sheet records flange size and rating as
> **NONE** on all three sections; every terminal is bevelled and welded. See Connection Info.
> This is the gating open item for the whole bid.

---

## Identity

| Field | Value |
|---|---|
| Client | Westlake South (site formerly PPG Industries Inc.) |
| Facility | Westlake, LA |
| Unit ID | Tri-Ethane — TE-II (plant equipment no. 71-1686) |
| Heater type | EDC pyrolysis furnace — vertical tube, single row, double fired, two pass |
| Configuration | Individual Passes — 2 passes, no looping recorded |

---

## Tube Geometry

Rows in process flow order: Liquid Preheat → Shock/Vaporization → crossover → Radiant.

| Section | Arrangement | Metallurgy | OD (in) | Sched | Wall (in) | ID (in) | Tubes/Circuit | Avg Length (ft) | Length/Circuit (ft) | Return Bend Type | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Convection — Liquid Preheat | Horizontal | Incoloy 800H | 5.25 | (not stated) | 0.3125 (avg) | (not recorded) | 12 | 30.92 | 371.0 | 180° bend, same material as tube, 0.2" MSW, in header box | 24 tubes total, 6 rows @ 4/row, all extended-surface (solid fin, 11 Cr, 0.75" × 0.06", 4/inch). Overall tube length 30'-11". Corrosion allowance 0.063". Terminal 4" Sch 40, bevelled, external. |
| Convection — Shock/Vaporization | Horizontal | Incoloy 800H | 5.25 | (not stated) | 0.3125 (avg) | (not recorded) | 12 | 30.92 | 371.0 | 180° RB, A297 Gr.HT-40, 5/16" AW, in header box | 24 tubes total, 6 rows @ 4/row — 8 bare + 16 extended-surface (solid fin, 11 Cr, 0.75" × 0.06", 4/inch). Overall tube length 30'-11". Corrosion allowance 0.063". Terminal 5.25" × 5/16", bevelled, welded, external. |
| Radiant | **Vertical** | Incoloy 800H | 6.5 | (not stated) | 0.3125 (avg) | (not recorded) | 26 | 23.5 | 611.0 | Cast/wrought 180° RB, equiv. 800H, 5/16" AW, **in firebox** | 52 bare tubes, 2 rows @ 26/row. Overall straight length 23'-6"; heated length 25'-1". Tube spacing 12" in line; 8'-6" between radiant tube rows. Tube-to-wall 42" min. Corrosion allowance 0.063". Terminal 6.5" × 5/16", bevelled, welded, external. |

**Data-sheet gap:** ID is not stated anywhere in the source. OD and average wall are stated, so
ID is computable, but per the stated-values-only rule for heater cards the computed figures are
carried in **## Notes** below rather than in this table. Do not promote them here without
field verification.

---

## Config Rollup — Estimating Reference

Lengths are **straight tube length only** — return-bend development is not included in the data
sheet and must be added at execution.

| Scale | Section | Pipe ID(s) (in) | Total Tubes | Total Length (ft) | Notes |
|---|---|---|---|---|---|
| Per circuit | Convection — Liquid Preheat | (not recorded) | 12 | 371.0 | 12 × 30.92 ft |
| Per circuit | Convection — Shock/Vaporization | (not recorded) | 12 | 371.0 | 12 × 30.92 ft |
| Per circuit | Radiant | (not recorded) | 26 | 611.0 | 26 × 23.5 ft |
| Per circuit | **All sections** | (not recorded) | **50** | **1,353.0** | Estimating multiplication base — one full pass |
| Heater total | Convection — Liquid Preheat | (not recorded) | 24 | 742.0 | 2 passes, not looped |
| Heater total | Convection — Shock/Vaporization | (not recorded) | 24 | 742.0 | 2 passes, not looped |
| Heater total | Radiant | (not recorded) | 52 | 1,222.0 | 2 radiant coil assemblies, 1 per pass (drawing LH936-E102: "One Radiant Coil Assembly, 2 Req'd/Furnace") |
| Heater total | **All sections** | (not recorded) | **100** | **2,706.0** | 2 individual passes, no loop arrangement recorded |

---

## Connection Info (Facts)

| Field | Value |
|---|---|
| Launcher flange | **NONE as designed** — data sheet sheet 3 line 129, "Flange: size and rating — NONE" on all three sections. Terminals are bevelled and welded, external: radiant 6.5" × 5/16" (welded), shock/vap 5.25" × 5/16" (welded), liquid preheat 4" Sch 40 (bevelled). |
| Receiver flange | **NONE as designed** — same source, same finding. |
| Water supply source | (not recorded) |
| Max pig OD (in) | (not recorded) — cannot be stated as a fact while ID is unrecorded. Working figure in ## Notes. |

**Crossover:** two per furnace, external, welded, Incoloy 800H, 5.25" × 5/16", no flange rating.
Data sheet Note (6): *"Radiant inlet has concentric reducer from 5.25" OD crossover to 6.5" OD
radiant inlet (new material begins w/ this reducer through radiant coil)."* This reducer is the
size transition point in the pig path and it sits in **external piping**, not in the coil.

---

## ⚠ Job Options — Customer Decisions (Quarantined)

| Option | Status | Vendor / Notes |
|---|---|---|
| Filtration | **Elected** | Jesse, 2026-07-27. 1× TriMax against 1 filter press — within normal profile. |
| Smart pigging / inspection | TBD | Not addressed in the RFQ. |

---

## Pig Specifications

| Size | Type | Qty | Unit Cost | Billed As | Source |
|---|---|---|---|---|---|
| — | — | — | — | — | No history — first recorded USADeBusk decoke of this heater in the vault |

---

## Job History

| Job # | Quote | Date | Notes |
|---|---|---|---|
| (pending) | (quote # pending — assigned by quote-log owner) | 2026-08-31 to 2026-09-07 (flexible window) | RFQ received 2026-07-27 from Russell Brown, Planner Sr.-Maintenance, Tri-Ethane. Planned decoke. Prior Westlake work exists outside this vault — check the estate before treating this as a first-ever job. |

---

## Task Durations

| Date | Job # | Rigs | Rig-In | Pig | Smart Pig | Rig-Over | Rig-Out | Stand-By | Total | Condition | Mode |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |

---

## SOPs

None yet. EDC pyrolysis is a chlorinated-hydrocarbon cracking service with no precedent in this
vault — no existing SOP variant is known to cover it. Confirm effluent handling and any
chloride-related water-source restriction with Jesse before writing one.

---

## Field Notes

No USADeBusk job on this heater recorded in the vault.

---

## Notes

### Source documents

1989 OEM package, confirmed by Jesse on 2026-07-27 to still reflect the as-built coil:

- **Selas Fluid Processing Corporation, Fired Heater Data Sheet** — SFPC Job 89S-7016-0936
  (LH 936A), Customer Item TE-II, Customer Ref. PO # 524485, Issue Date 1989-02-24, Rev. 1
  1989-03-10, Rev. 2 1989-04-12. 5 sheets. Purchaser of record: PPG Industries Inc.
- **Drawing LH936-E101** — convection coil arrangement, one EDC pyrolysis furnace.
- **Drawing LH936-E102** — radiant coil assembly, "2 Req'd/Furnace."

Estate path: `C:\Users\Jwuts\OneDrive\USADeBusk\Facilities\Westlake South Westlake LA\` —
**path to be confirmed once the RFQ folder is filed into the estate tree.** Currently held at
`C:\Users\Jwuts\OneDrive\Desktop\Westlake South TE2 2026 Sept\`, which is a working copy and
will go dead when cleaned up.

An Excel workup sheet from a previous bid also sits in the RFQ folder. Provenance unconfirmed —
Jesse flagged on 2026-07-27 that it may belong to a different heater or facility. **Not read,
not used.** Resolve provenance before it informs anything.

### Derived values — estimating working figures, NOT card facts

Computed from stated OD and stated average wall (ID = OD − 2 × wall). Held here rather than in
Tube Geometry because the data sheet does not state ID. **Verify in the field before pig sizing.**

| Section | OD (stated) | Wall (stated) | ID (derived) |
|---|---|---|---|
| Convection — Liquid Preheat | 5.25" | 0.3125" | 4.625" |
| Convection — Shock/Vaporization | 5.25" | 0.3125" | 4.625" |
| Radiant | 6.5" | 0.3125" | 5.875" |

Governing (smallest) derived ID is the convection at 4.625", giving a working **max pig OD of
4.875"** (4.625 + 0.250; lands exactly on a 1/8" size, no round-down needed). Radiant taken
alone gives **6.125"**. Wall is stated as *average* wall with a 0.063" corrosion allowance, so
a 37-year-old coil may run thinner and looser than these figures.

### Process data (design, 1989)

Ethylene dichloride, 85,290 lb/hr, 43.1 MM BTU/hr absorbed (radiant 27.75, shock/vap 9.8,
liquid preheat 5.55). Inlet 220°F / 223 psia at the liquid preheat; radiant outlet 950°F /
195 psia at 55% conversion. Radiant flow is downflow; both convection sections counterflow.
24 John Zink SMZ-Q-20V burners, radiant floor, 4 rows of 6, natural gas. Radiant design fluid
temp 975°F, max calculated tube wall 1137°F. No plug headers anywhere on this heater.

### Access and structure (bears on rig-in/rig-out tier)

Stack is self-supporting on top of the convection section, ~120 ft above grade, ~75 ft stack
length. Platforms at one level above the radiant arch plus one at the stack damper, 2'-6"
minimum clearance, open grating. **Ladders at each end of the furnace, no stairs.** Access
doors one in each radiant endwall. Rig-in tier is set by launcher/receiver elevation and by
run distance from the TriMax to those points — both settle at the job walk, and no job walk
has occurred. Do not infer a tier from heater size.

### Open items

Gating: how launchers and receivers land, given no flanges as designed — modified since 1989,
or does Westlake supply cut-and-weld flanged pigging spools, and at what size and rating.
Then: governing contract and rate basis (recover from prior Westlake work outside the vault),
third-party markup tier, water source, launcher/receiver elevation and access, whether
Westlake's fitters hang the launchers, fouling character from the last decoke, post-cleaning
treatment instruction for the Incoloy 800H, smart-pig election, and the entire commercial
package — no bid instructions, submission platform, due date, forms, or pricing-sheet mandate
were received.

Equipment profile confirmed by Jesse 2026-07-27: **1× TriMax, filtration elected.**
