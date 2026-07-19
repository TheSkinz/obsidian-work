---
type: job-sheet
job-number: <USA#####>
client: <Client name>
facility: <Client>-<City>-<ST>
source: <DSP##### — the quoted work-up this sheet was built from>
verified: <YYYY-MM-DD | never>
last-updated: <YYYY-MM-DD>
tags: [job-sheet, <Client>, <USA#####>]
---

<!-- Derived from 04-knowledge/_canonical-job-sheet.md — the schema authority.
     On any structural question, that exemplar governs; keep this template in sync with it.
     `facility` is the JOIN KEY — must exactly match the facility-id in the site's _facility.md.

     Save as 02-facilities/<Client>/<City-ST>/<USA#####>-job-sheet.md, alongside the heater cards.

     A job sheet is STATIC: created at bid-win from the quoted work-up, never updated to match what
     actually happened. Actuals and timeline go on the job report. -->

# <USA#####> — <Client> <Facility Name>, <City>, <ST>

> Vault-native copy of the printable crew job sheet. The canonical printable version is
> `<USA#####>-job-sheet.pdf` (rendered from `<USA#####>-job-sheet.html`). A job sheet is static —
> created at bid-win from the quoted work-up. Actuals and timeline live on the job report, never here.

---

## Project Details

| Field | Value |
|---|---|
| Facility | |
| Job # | |
| Scope | |
| Heaters | |
| Project Type | |
| Training | |

---

## Crew Assignment — By Rig & Shift

<!-- Supervisors are fixed to a rig; operators are a shared pool by shift. Equipment is NOT
     pre-assigned to a heater — which rig works which heater is a field decision. -->

**Dayshift**

| Rig | Supervisor | Operators |
|---|---|---|
| | | |

**Night Shift**

| Rig | Supervisor | Operators |
|---|---|---|
| | | |

<Note who is customer-facing lead / final-decision authority, and any billing role they carry.>

---

## Billing Reference — By Heater

<!-- One ### block per heater. Billing math (see exemplar for the full rules):
       - Equipment (Pumper, Support Unit, Filter Unit, Crew Truck) = heater total pumper hours.
       - Labor Amt = COMBINED MAN-HOURS = Qty × per-person shift hours. Easiest line to get wrong.
       - Per Diem bills per day; headcount EXCLUDES a billable Project Manager.
       - DEF bills per shift — use the quoted shift count as given.
       - Project Manager line only when the quote carries one. Not a default.
       - Filter Unit row only when filtration was elected. -->

### <TAG> <Service> — <N> Hrs Total (Rig-In <a> / Pig <b> / Rig-Out <c>)

| Qty | Item | Amt | Unit |
|---|---|---|---|
| 1 | TriMax Pumper | | Hrs |
| 1 | Support Unit | | Hrs |
| 1 | Filter Unit | | Hrs |
| 1 | Crew Truck | | Hrs |
| 1 | Day Supervisor | | Hrs |
| | Day Operators | | Hrs |
| 1 | Night Supervisor | | Hrs |
| | Night Operators | | Hrs |
| | Per Diem: Dayshift | | Days |
| | Per Diem: Nightshift | | Days |
| 1 | Materials: DEF | | Shifts |

Operator / Night Operator Amt is combined man-hours (Qty × per-person shift hours). Quoted total
across all heaters: <N> pumper hours.

---

## <TAG> — Coil Data

<!-- Compact reference copied FROM the heater card — the card stays the source of truth.
     One table per heater. -->

| Section | Coils | Pipe OD | Pipe Wall | Pipe ID | Tube Length | Tubes/Coil | Ft/Section |
|---|---|---|---|---|---|---|---|
| Convection | | | | | | | |
| Radiant | | | | | | | |

Metallurgy: . Pass config: . Connections: . Effluent: .

Full tube geometry, config rollup, and pig spec history: [[<TAG>]].

---

## Carry-Forward Notes — Prior Decoke (<USA#####>, <Month Year>)

<!-- CONDITIONAL — omit this whole section on a first-time heater with no prior job history.
     Source is the prior job's Field Notes on the heater card. -->

| Heater | Watch For | Action |
|---|---|---|
| | | |

---

## Notes

Printable deliverable: `<USA#####>-job-sheet.pdf` (source `<USA#####>-job-sheet.html`), alongside
this file. Billing tables reflect the quoted work-up (<N>-person resource plan). Actual mobilized
crew and timeline are recorded on the job report, not here.
