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

> ⚠ **USADeBusk SUPPLIES 4× 6" 300# × 6" 300# RFWN 90° SPOOLS** — two per pass, to adapt the
> heater connections to the launchers/receivers. Carried forward from the 2024 bid on this
> heater. This supersedes the OEM data sheet, which records flange size and rating as **NONE**
> on all three sections (all terminals bevelled and welded) — the connections were evidently
> flanged to 6" 300# RFWN at some point after 1989. See Connection Info.

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
| Convection — Liquid Preheat | Horizontal | Incoloy 800H | 5.25 | (not stated) | 0.3125 (avg) | 4.625 (derived) | 12 | 30.92 | 371.0 | 180° bend, same material as tube, 0.2" MSW, in header box | 24 tubes total, 6 rows @ 4/row, all extended-surface (solid fin, 11 Cr, 0.75" × 0.06", 4/inch). Overall tube length 30'-11". Corrosion allowance 0.063". Terminal 4" Sch 40, bevelled, external. |
| Convection — Shock/Vaporization | Horizontal | Incoloy 800H | 5.25 | (not stated) | 0.3125 (avg) | 4.625 (derived) | 12 | 30.92 | 371.0 | 180° RB, A297 Gr.HT-40, 5/16" AW, in header box | 24 tubes total, 6 rows @ 4/row — 8 bare + 16 extended-surface (solid fin, 11 Cr, 0.75" × 0.06", 4/inch). Overall tube length 30'-11". Corrosion allowance 0.063". Terminal 5.25" × 5/16", bevelled, welded, external. |
| Radiant | **Vertical** | Incoloy 800H | 6.5 | (not stated) | 0.3125 (avg) | 5.875 (derived) | 26 | 23.5 | 611.0 | Cast/wrought 180° RB, equiv. 800H, 5/16" AW, **in firebox** | 52 bare tubes, 2 rows @ 26/row. Overall straight length 23'-6"; heated length 25'-1". Tube spacing 12" in line; 8'-6" between radiant tube rows. Tube-to-wall 42" min. Corrosion allowance 0.063". Terminal 6.5" × 5/16", bevelled, welded, external. |

**ID is derived, and that is normal.** Facilities rarely state ID — they give size/OD plus
minimum wall or schedule, and ID is calculated from those (Jesse, 2026-07-27). ID here =
OD − 2 × stated average wall. Wall is stated as *average* with a 0.063" corrosion allowance,
so a 37-year-old coil may run thinner and looser than these figures; verify in the field before
committing a pig load list.

---

## Config Rollup — Estimating Reference

Lengths are **straight tube length only** — return-bend development is not included in the data
sheet and must be added at execution.

| Scale | Section | Pipe ID(s) (in) | Total Tubes | Total Length (ft) | Notes |
|---|---|---|---|---|---|
| Per circuit | Convection — Liquid Preheat | 4.625 | 12 | 371.0 | 12 × 30.92 ft |
| Per circuit | Convection — Shock/Vaporization | 4.625 | 12 | 371.0 | 12 × 30.92 ft |
| Per circuit | Radiant | 5.875 | 26 | 611.0 | 26 × 23.5 ft |
| Per circuit | **All sections** | 4.625 / 5.875 | **50** | **1,353.0** | One full pass, all three sections |
| Heater total | Convection — Liquid Preheat | 4.625 | 24 | 742.0 | 2 passes, not looped |
| Heater total | Convection — Shock/Vaporization | 4.625 | 24 | 742.0 | 2 passes, not looped |
| Heater total | Radiant | 5.875 | 52 | 1,222.0 | 2 radiant coil assemblies, 1 per pass (drawing LH936-E102: "One Radiant Coil Assembly, 2 Req'd/Furnace") |
| Heater total | **All sections** | 4.625 / 5.875 | **100** | **2,706.0** | 2 individual passes, no loop arrangement recorded |

> **The estimating base is a subset of this table — see ⚠ Pigging Scope below.** Scope is
> "the two process coils" (Jesse, 2026-07-27), which is fewer than all three sections. Do not
> multiply off the All-sections rows until scope is pinned.

---

## Connection Info (Facts)

| Field | Value |
|---|---|
| Launcher flange | 6" 300# RFWN — inferred from the 2024 bid note requiring 6" 300# × 6" 300# RFWN spools. Confirm at the job walk. |
| Receiver flange | 6" 300# RFWN — same basis. |
| USADeBusk-supplied spools | **4× 6" 300# × 6" 300# RFWN 90° spools, two per pass** (2024 bid note). Goes in the proposal's Section 8 provided-items list. |
| Water supply source | (not recorded) |
| Max pig OD (in) | Scope-dependent — **6.125"** if radiant only (5.875 + 0.250); **4.875"** if any 4.625" convection section is in the pig path (4.625 + 0.250). Both land exactly on a 1/8" size, no round-down needed. Resolve with Pigging Scope below. |

**OEM data sheet says otherwise, and is superseded.** Sheet 3 line 129 records "Flange: size and
rating — NONE" on all three sections, with all terminals bevelled and welded (radiant 6.5" ×
5/16" welded, shock/vap 5.25" × 5/16" welded, liquid preheat 4" Sch 40 bevelled). The 2024 bid's
spool requirement is evidence the connections were flanged to 6" 300# RFWN sometime after 1989.
Recorded both ways deliberately — the 1989 sheet is the source of record, the 2024 note is the
later field evidence.

**The 6"/6" symmetry is itself a scope clue.** A spool flanged 6" 300# on *both* ends fits the
radiant terminals (6.5" OD, 5.875" derived ID) at both launch and receive. It does not fit a
launch at the liquid preheat inlet, which the data sheet puts at 4" Sch 40. That points toward
the pig path running radiant-only, or at least not starting at the liquid preheat — see below.

**Crossover:** two per furnace, external, welded, Incoloy 800H, 5.25" × 5/16", no flange rating.
Data sheet Note (6): *"Radiant inlet has concentric reducer from 5.25" OD crossover to 6.5" OD
radiant inlet (new material begins w/ this reducer through radiant coil)."* This reducer is the
size transition point in the pig path and it sits in **external piping**, not in the coil.

---

## ⚠ Pigging Scope — UNRESOLVED

Jesse, 2026-07-27: **"We are only pigging the two process coils."** The restrictive *only* means
this is a subset of the three coil sections, not all of them, so the heater-total footage above
is not the estimating base. Three readings, and they differ by more than 2×:

| Reading | Sections in pig path | Circuits | Ft / circuit | Total ft |
|---|---|---|---|---|
| A — radiant only | Radiant | 2 | 611.0 | **1,222.0** |
| B — radiant + shock/vap | Shock/Vap → crossover → Radiant | 2 | 982.0 | **1,964.0** |
| C — full pass | Liq Preheat → Shock/Vap → crossover → Radiant | 2 | 1,353.0 | **2,706.0** |

Reading A is best supported: 4 spools at 2 per pass = one launch and one receive per circuit,
both flanged 6" 300#, which matches the 6.5" OD radiant terminals at both ends and does not
match the 4" Sch 40 liquid preheat inlet. Reading A also keeps a single tube ID in the pig path,
removing the size-transition sequencing at the crossover reducer.

**Not resolved here — this sets footage, pig sizing, and duration, so it is an ask, not a
derive.** The 2024 bid package will likely settle it outright; recover it before assuming.

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
| — (not awarded) | (2024 quote # unknown) | 2024 | **Bid and lost** (Jesse, 2026-07-27). Package is outside the vault. Carries at least one note of record: *"Bring 4× 6" 300# × 6" 300# RFWN 90 degree spools."* **Recover this package** — it is the best available source for pigging scope, connection detail, footage basis, duration, and the rates that lost. |
| (pending) | (quote # pending — assigned by quote-log owner) | 2026-08-31 to 2026-09-07 (flexible window) | RFQ received 2026-07-27 from Russell Brown, Planner Sr.-Maintenance, Tri-Ethane. Planned decoke, 1× TriMax, filtration elected. |

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

**Current path — known-temporary, will go dead:**
`C:\Users\Jwuts\OneDrive\Desktop\Westlake South TE2 2026 Sept\`

Target estate path is `C:\Users\Jwuts\OneDrive\USADeBusk\Facilities\Westlake South Westlake LA\Bids\`.
Jesse was blocked from moving it on 2026-07-27 and will move it later; update this pointer then.
Watch for a trailing non-breaking space (U+00A0) when the estate folder is created.

The **2024 bid package** for this heater is also somewhere in the estate and is not yet located.
It is the highest-value missing document — see Job History.

An Excel workup sheet from a previous bid also sits in the RFQ folder. Provenance unconfirmed —
Jesse flagged on 2026-07-27 that it may belong to a different heater or facility. **Not read,
not used.** Resolve provenance before it informs anything.

### ID derivation

| Section | OD (stated) | Wall (stated) | ID = OD − 2×wall |
|---|---|---|---|
| Convection — Liquid Preheat | 5.25" | 0.3125" | 4.625" |
| Convection — Shock/Vaporization | 5.25" | 0.3125" | 4.625" |
| Radiant | 6.5" | 0.3125" | 5.875" |

Governing ID and therefore max pig OD depend on which sections are in the pig path — see
Pigging Scope. Radiant-only gives 5.875" → **6.125"**; any path including a convection section
gives 4.625" → **4.875"**.

**Schema conflict to rule on (Lane 4, Jesse's call).** `usadebusk-estimating` states a heater
card carries stated values only, "even when it is trivially computable," and would put
`(not recorded)` in every ID cell. Jesse, 2026-07-27: facilities rarely state ID — they give
size/OD plus minimum wall or schedule, and ID is always calculated from those. Applied as
written, the rule blanks the one field pig sizing keys off on essentially every card. This card
carries the derived IDs marked `(derived)`. The skill text is unedited and still says otherwise.

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

**Gating — pigging scope.** Which sections are in the pig path (readings A/B/C above). Sets
footage, pig sizing, and duration. The 2024 bid package is the fastest route to an answer.

**Rates.** No active contract at this site. Jesse will construct rates and input them later
(2026-07-27) — do not populate from the generic baseline table in the meantime, and do not
carry a third-party markup tier until Jesse sets one. The 2024 losing bid's rates are useful
context for what not to repeat, once recovered.

**Remaining.** Water source; launcher/receiver elevation and access; whether Westlake's fitters
hang the launchers; fouling character from the last decoke; post-cleaning treatment instruction
for the Incoloy 800H; smart-pig election; confirmation that the connections are in fact 6" 300#
RFWN. Commercially, nothing was received — no bid instructions, submission platform, due date
and time zone, required forms, insurance or safety-qualification requirements, or pricing-sheet
mandate.

Equipment profile confirmed by Jesse 2026-07-27: **1× TriMax, filtration elected.**
