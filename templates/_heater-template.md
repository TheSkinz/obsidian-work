---
type: heater
heater-id: <UNIT>-<TAG>-<ShortName>
heater-tag: <e.g. F-802, 210-1401A>
unit: <e.g. PS8, Unit 210, HU9 — omit if not applicable>
facility: <Client>-<City>-<ST>
client: <Client name>
heater-type: <crude | vacuum | reboiler | other>
service: <e.g. Crude Heater, Splitter Reboiler — optional if heater-type covers it>
configuration: <e.g. Looped-at-Radiant-outlet-flanges, Individual-Passes>
last-updated: <YYYY-MM-DD>
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
     state explicitly or "(not recorded)". -->

| Section | Arrangement | Metallurgy | OD (in) | Sched | Wall (in) | ID (in) | Tubes/Circuit | Avg Length (ft) | Length/Circuit (ft) | Return Bend Type | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Convection | Horizontal | | | | | | | | | | |
| Radiant | | | | | | | | | | | |

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
     Condition = routine | crash | first | unknown (a job's hours are evidence only for the
     next decoke of the SAME condition; "emergency" in the job details means crash).
     Append `, hours-blended` if task hours weren't cleanly separated in the source, and
     `, combined-heaters` if the hours are a multi-heater job total. Full spec in
     04-knowledge/_canonical-heater-card.md. -->
| Date | Job # | Rigs | Rig-In | Pig | Smart Pig | Rig-Over | Rig-Out | Stand-By | Total | Condition |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

---

## SOPs

---

## Field Notes

### <Job # — Month Year>

**Pigs Ran:**

**Obstacles:**

**Facility Procedures:**

**Per-rig split (multi-TriMax only):**

---

## Notes
