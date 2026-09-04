---
type: heater
heater-id: <UNIT>-<TAG>-<ShortName>
heater-tag: <e.g. F-802, 210-1401A>
unit: <e.g. PS8, Unit 210, HU9 — omit if not applicable>
facility: <Client>-<City>-<ST>
client: <Client name>
heater-type: <crude | vacuum | coker | reboiler | other>
service: <e.g. Crude Heater, Splitter Reboiler — optional if heater-type covers it>
configuration: <e.g. Looped-at-Radiant-outlet-flanges, Individual-Passes>
last-updated: <YYYY-MM-DD>
source: <document(s), job number(s) or person this card was built from>
verified: <YYYY-MM-DD | never>
  # ↑ strictly a date or `never` (lint: VERIFIED-FORMAT). It records WHEN the card was last
  #   checked against a primary source — nothing else. What was checked, and what was not,
  #   goes in `## Notes` as a `**Verification:**` paragraph.
tags: [heater-card, <Client>, <heater-type>]
---

<!-- Derived from 04-knowledge/_canonical-heater-card.md — the schema authority.
     On any structural question, that exemplar governs; keep this template in sync with it.
     `facility` is the JOIN KEY — must exactly match the facility-id in the site's _facility.md. -->

# <Unit/Tag> <ShortName> — <Client> <City>, <ST>

<!-- If any section's metallurgy is stainless/passivation-requiring, include the stainless
     warning block per the exemplar. Omit entirely on carbon-steel-only heaters. -->

---

## Identity

<!-- Card-level facts only. Per-section facts (metallurgy, return bend type) go in Tube Geometry. -->

| Field | Value |
|---|---|
| Client | |
| Facility | |
| Unit ID | |
| Heater type | |
| Configuration | |

---

## Tube Geometry

<!-- One row per physical segment in flow order; per-circuit values, never totals.
     Metallurgy and Return Bend Type are PER-SECTION. Radiant arrangement has no default —
     state explicitly or "(not recorded)".
     NO Notes column (2026-07-27) — atomic values only. Explanatory text goes in the keyed
     block below, one paragraph per row, led by the Section name from column 1. Delete the
     block if no row needs one. Not Field Notes: that is the per-job record. -->

| Section | Arrangement | Metallurgy | OD (in) | Sched | Wall (in) | ID (in) | Tubes/Circuit | Avg Length (ft) | Length/Circuit (ft) | Return Bend Type |
|---|---|---|---|---|---|---|---|---|---|---|
| Convection | Horizontal | | | | | | | | | |
| Radiant | | | | | | | | | | |

**Tube geometry notes.**

**<Section>.** <provenance / confirmation reasoning / dimensional caveat>

---

## Config Rollup — Estimating Reference

<!-- Two scales, both always present: Per circuit (estimating multiplication base) and
     Heater total (actual loop arrangement — state it in Notes). -->

| Scale | Section | Pipe ID(s) (in) | Total Tubes | Total Length (ft) | Notes |
|---|---|---|---|---|---|
| Per circuit | Convection | | | | |
| Per circuit | Radiant | | | | |
| Heater total | Convection | | | | |
| Heater total | Radiant | | | | |

---

## Connection Info (Facts)

| Field | Value |
|---|---|
| Launcher flange | |
| Receiver flange | |
| Water supply source | |
| Max pig OD (in) | <governing tube ID + 0.250" — smallest ID across all sections> |

---

## ⚠ Job Options — Customer Decisions (Quarantined)

> Status only — never facts.

| Option | Status (Optional / Elected / Declined / TBD) | Vendor / Notes |
|---|---|---|
| Filtration | | |
| Smart pigging / inspection | | |

---

## Pig Specifications

| Size | Type | Qty | Unit Cost | Billed As | Source |
|---|---|---|---|---|---|
| | | | | | |

---

## Job History

| Job # | Quote | Date | Notes |
|---|---|---|---|
| | | | |

---

## Task Durations
<!-- ACTUALS ONLY — elapsed hours per decoke, one row per job. Estimates never appear here.
     Stand-By tracked but excluded from Total. "–" = confirmed did not occur; "?" = unrecorded.
     Condition = JOB CLASS, not coil condition: routine | crash | first | unknown (a job's
     hours are evidence only for the next decoke of the SAME class). `crash` = unscheduled
     mobilization, a callout label and not a fouling grade (Jesse, 2026-08-20); "emergency"
     in the job details means crash. Column name kept for schema stability — see the exemplar.
     Append `, hours-blended` if task hours weren't cleanly separated in the source, and
     `, combined-heaters` if the hours are a multi-heater job total. Mode = passes pigged
     simultaneously (single 1 / double 2 / triple 3; looped path = 1; blank = unrecorded). Full
     spec in 04-knowledge/_canonical-heater-card.md. -->
| Date | Job # | Rigs | Rig-In | Pig | Smart Pig | Rig-Over | Rig-Out | Stand-By | Total | Condition | Mode |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |

---

## Coilset Durations
<!-- OPTIONAL — delete this section on cards with no per-coilset data; its absence is not a gap.
     One row per COILSET as run. Rows SUM to the parent Task Durations row of the same Job #;
     where they don't, the parent carries `hours-blended`. Task Durations is unchanged by this.
     Coils = the set as run (`2/3/4`, `1&8 (looped)`). Rig = which Trimax.
     Mode = SIMULTANEOUS CIRCUITS, which can differ from the ticket's word — a looped pair
     written "double mode" ran as ONE circuit, so Mode 1.
     Circuit ft = FOOTAGE ONE PIG TRAVELS, never the set total. Triple-mode 2/3/4 = one coil's
     footage (three pigs at once); a looped pair = both coils. Then ft/hr per pig = Circuit ft
     ÷ Pig, a measurement rather than the parent table's ÷Mode approximation.
     No Stand-By column — stand-by is per-rig, not per-set; it stays on the parent row.
     Coil condition = how dirty the coil WAS: light | moderate | heavy | unknown. This is NOT
     Task Durations' `Condition`, which is job class. Blank on most historical rows.
     Graded against observables, in order: final pig size vs. the section's Clean ID (the
     field-measured bore — NOT the same quantity, corrected 2026-09-03), progression steps in
     pig runs and any stalled size, return duration after pig arrival, measured thickness only
     where actually measured, recovered fragments. `heavy` means HARD TO CLEAN — an effort grade, not a claim about the deposit,
     since slow hours also follow from restrictions, pig fit, flow or tube deformation. A
     fragment you actually handled CAN be described in Field Notes (hard/brittle/powdery,
     chunks/chips/fines, wet/oily/tarry, layered) — describe from the piece, never from the
     clock. Never infer a grade to fill a blank; write unknown.
     (Mirror — authority is 04-knowledge/manual/17-glossary.md § Fouling; change both in the
     same commit.)
     Localized hard spot: record in Field Notes only when the crew reported one; never record
     its absence. Not the same as the `outlier` Flag — an outlier coil is a fluke, a hard spot
     within a coil is normal.
     Flag = clean | outlier | blended | unknown. `outlier` = this set ran 12–24 hrs off its
     siblings on the same heater/rig/mode — estimate off the sets that CLUSTER, never the
     outlier, and state which set you excluded. Full spec in 04-knowledge/_canonical-heater-card.md. -->
| Job # | Coils | Rig | Mode | Circuit ft | Rig-In | Pig | Smart Pig | Rig-Over | Rig-Out | Total | Coil condition | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

---

## SOPs

---

## Field Notes

### <Job # — Month Year>

**Pigs Ran:**

**Obstacles:**

**Facility Procedures:**

**Per-rig split (multi-Trimax only):**

---

## Notes
