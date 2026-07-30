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
     actually happened. Actuals and timeline go on the job report.

     INTERNAL DOCUMENT. Goes to the crew, never the customer: no rates, no markup, no dollar
     totals, no customer-proposal boilerplate.

     OMISSION RULES — don't state what is always true (every job is a mechanical decoke), don't
     restate what another field already says, don't state mutually exclusive options as if both
     apply, don't attribute tasks to shifts, don't print computed values that look orderable.

     TARGET: ONE PAGE in the printable. Six blocks fit. If you add a seventh, take one away. -->

# <USA#####> — <Client> <Facility Name>, <City>, <ST>

> Vault-native copy of the printable crew job sheet. The canonical printable version is
> `<USA#####>-job-sheet.pdf` (rendered from `<USA#####>-job-sheet.html`). A job sheet is static —
> created at bid-win from the quoted work-up. Actuals and timeline live on the job report, never here.
>
> **Internal crew document.** No rates, markup, or quoted totals — those live on the quote and the
> ticket breakdown.

---

## Project Details

<!-- Scope = heater tag + service + customer elections (filtration / smart pigging) ONLY. Never
     write "mechanical decoke" — always true. No separate Heaters row; Scope names them.
     The field is `Mode`, not `Pigging Mode`. -->

| Field | Value | Field | Value |
|---|---|---|---|
| Scope | <TAG + service — w/ Filtration + Smart Pigging> | Job # | <USA#####> |
| Facility | <Facility name — City, ST> | Quote | <DSP#####> |
| Mode | <e.g. Double mode, 2-pass (A→C→jumper→D→B)> | PO # | <PO or TBD> |
| Project Type | <Planned outage — Month Year / Emergency turnaround> | PM | <name> |
| Lodging | <hotel> | Training | <e.g. Site specific> |

---

## Schedule

<!-- No per-phase clock times — that implies assigning phases to shifts. -->

| Mobilization | Rig-In / Start | Projected Complete |
|---|---|---|
| | | |

| Rig-In | Pig | Smart Pig | Rig-Out | Total |
|---|---|---|---|---|
| | | | | **<N> hrs** |

<N> days / <N> shifts.

---

## Crew & Labor

<!-- Qty = QUOTED plan (billing basis, never changed to match who showed up).
     Mob = ACTUAL headcount (never used in a billing figure).
     Ea. Hrs = per-person shift hours.  Man-Hrs = Qty × Ea. Hrs, combined.
     5-man crews at 3 day / 2 night are normal, not a variance.
     PM bills as PM or Day Supervisor per the quote's allocation block — read it per job.
     Operator names commonly left blank for the field; name the pool in the note. -->

| Shift | Role | Assigned | Qty | Mob | Ea. Hrs | Man-Hrs |
|---|---|---|---|---|---|---|
| Day | Supervisor | <name> | 1 | | | |
| Day | Operator | | <n> | | | |
| Night | Supervisor | <name> | 1 | | | |
| Night | Operator | | <n> | | | |
| **Per Diem — <n> day × <n> days + <n> night × <n> days = <N> days** | | | **<total>** | **<total>** | | **<total>** |

**Qty** = quoted resource plan (billing basis). **Mob** = actual headcount, <n> dayshift / <n> nightshift. Operator pool: <names> — split assigned in the field. PM runs dayshift.

---

## Equipment

<!-- Billable rows only. Non-billable movements go in the note, not the table.
     Filter Unit row only when filtration was elected. -->

| Qty | Billable As | Asset | Hrs | Status |
|---|---|---|---|---|
| 1 | Trimax Pumper | <Trimax #> | | <Staged / mobilizing from …> |
| 1 | Support Unit | <Support #> | | |
| 1 | Filter Unit | <Press #> | | |
| <n> | Crew Truck | <vehicles> | | |

DEF <n> shifts. <Gate passes and other pre-mob action items.>

---

## <TAG> — Coil Data & Connections

<!-- Copied FROM the heater card; the card stays source of truth. Metallurgy is a column.
     INLETS and OUTLETS — never "nozzles".
     Final Pigs = orderable sizes only. Never the card's "Max pig OD" rule cap, never "final foam".
     Elevation goes inside the Launchers value, never on its own line. One group = one elevation,
     but groups can differ on the same heater (USA26038 H-20: convection 10' from grade, radiant at
     grade).
     Scaffolding is a SEPARATE test: required only when the location is elevated AND lacks a sturdy
     deck with room to change pigs. Elevated on a good deck needs none. When required, say it inside
     the Launchers value ("4 × 6" · 15' elevated, scaffold req'd"); otherwise stay silent. Customer
     provides scaffolding and spools on nearly all jobs — a quote line item, never a flag. -->

| Section | Coils | Pipe OD | Wall | Pipe ID | Tube Lgth | Tubes/Coil | Ft/Section | Metallurgy |
|---|---|---|---|---|---|---|---|---|
| Convection | | | | | | | | |
| Radiant | | | | | | | | |

> **Inlets <A / B>** <size rating face> · **Outlets <C / D>** <size rating face> · **Launchers** <n × size> · <at grade> · **Final Pigs** <orderable sizes>
>
> **Adapters** — <required or not; termination vs. connection rating; who fabricates; bolt-up and wrench>
> **Water** — <source>
> **Coil** — <heater total effective footage; crossover ID and whether a reducer exists>

Full tube geometry, config rollup, and pig spec history: [[<TAG>]].

---

## Carry-Forward Notes — Prior Decoke (<USA#####>, <Month Year>)

<!-- CONDITIONAL — omit entirely on a first-time heater with no prior job history.
     Source is the prior job's Field Notes on the heater card. -->

| Heater | Watch For | Action |
|---|---|---|
| | | |

---

## Notes

Printable deliverable: `<USA#####>-job-sheet.pdf` (source `<USA#####>-job-sheet.html`), alongside
this file. Billing tables reflect the quoted work-up. Actual mobilized crew and timeline are
recorded on the job report, not here.
