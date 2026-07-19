---
type: job-sheet
job-number: <USA#####>
client: <Client name>
facility: <Client>-<City>-<ST>
  # ↑ JOIN KEY — must exactly match the facility-id in this site's _facility.md,
  #   same convention as the heater card's facility field.
source: <DSP##### — the specific quoted work-up this sheet was built from>
verified: <YYYY-MM-DD the tables were last checked against that work-up | never>
last-updated: <YYYY-MM-DD>
tags: [job-sheet, <Client>, <USA#####>]
---

<!--
CANONICAL EXEMPLAR — NOT A LIVE JOB SHEET.
This file is the schema authority for all job sheets in the vault. It is never a record of an
actual job; it exists to stay stable while live job sheets mutate. templates/_job-sheet-template.md
derives its structure FROM this file.

STATUS: DRAFT — validated against ONE instance (USA26038, HF Sinclair Navajo, July 2026).
The heater-card exemplar was validated against seven cards before it stabilized; this one has a
single example behind it, so treat section shape as provisional until a second won bid either
confirms it or forces a change. Sections marked "conditional" below are the ones most likely to
move.

WHAT A JOB SHEET IS (the fact/time wall — core principle):
  A job sheet is STATIC. It is created once, at bid-win, from the quoted work-up, and it holds
  the QUOTE's resource plan — not what actually happened. Actuals, timeline, and real crew belong
  on the job report; accumulated heater facts belong on the heater card. The quote's plan and the
  mobilized reality routinely differ (USA26038 quoted 12 people, sent 10) and that gap is a job
  report finding, never a correction to the job sheet. A job sheet edited to match reality has
  destroyed the only record of what was sold.

  See quote-lifecycle.md for the three-document model (job sheet / heater card / job report) and
  where each is created in the lifecycle.

PROVENANCE (`source` / `verified`): tools/vault_lint.py's OP-FRONTMATTER rule requires both on
every operational note, and for a job sheet they carry real meaning rather than ceremony. `source`
is the specific DSP##### work-up the billing tables were built from — a sheet built from a
superseded quote revision is a live failure mode, and the job number alone does not identify which
revision was used. `verified` is the date the tables were last checked against that work-up. Do not
fill either with a placeholder to silence the lint; an honest warning is worth more than a false
green. (USA26038's own sheet carries neither field, and its DSP# is not recorded anywhere in the
vault as of 2026-07-18 — it stays flagged in the provenance backfill backlog until someone supplies it.)

LOCATION AND NAMING (follows the USA26038 precedent):
  02-facilities/<Client>/<City-ST>/<USA#####>-job-sheet.md — alongside the heater cards for the
  same site, flat, no per-job subfolder. The printable pair (.html source, .pdf render) sits
  beside it under the same basename.
-->

# <USA#####> — <Client> <Facility Name>, <City>, <ST>

> Vault-native copy of the printable crew job sheet. The canonical printable version is
> `<USA#####>-job-sheet.pdf` (rendered from `<USA#####>-job-sheet.html`). A job sheet is static —
> created at bid-win from the quoted work-up. Actuals and timeline live on the job report, never here.

---

## Project Details

<!--
Job-level identity. Everything here is fixed at bid-win. "Scope" states the mechanical work plus
the pumper count and whether filtration is in scope — filtration is a customer election (a Job
Options decision on the heater card), so state it as elected scope here, never as a heater spec.
-->

| Field | Value |
|---|---|
| Facility | <Facility name — City, ST> |
| Job # | <USA#####> |
| Scope | <e.g. Mechanical decoke — H19 & H20, (2) TriMax pumpers with filtration> |
| Heaters | <Tag + service, separated by ·> |
| Project Type | <Emergency turnaround project / Planned TA / Routine decoke> |
| Training | <e.g. Site Specific> |

---

## Crew Assignment — By Rig & Shift

<!--
One table per shift. The structural rule confirmed on USA26038:
  - Supervisors are FIXED to a rig.
  - Operators are a SHARED POOL by shift — they may move between rigs within their shift.
  - Equipment is NOT pre-assigned to a heater. Which rig works which heater is a field decision,
    deliberately left open here.
Name the customer-facing lead explicitly, and note if that person also bills as Project Manager
on a heater's work-up (that drives a billing line — see Billing Reference).
-->

**Dayshift**

| Rig | Supervisor | Operators |
|---|---|---|
| <TriMax #> | <name> | <names> |

**Night Shift**

| Rig | Supervisor | Operators |
|---|---|---|
| <TriMax #> | <name> | <names> |

<One-paragraph note: who is customer-facing lead / final-decision authority, and any billing role
that person carries.>

---

## Billing Reference — By Heater

<!--
PURPOSE: this is how the crew keys service receipts against what was quoted. It is a reference for
the field, not an invoice, and it reflects the QUOTED work-up exactly.

One `###` block per heater. Heading carries the heater total and its task split:
    ### <TAG> <Service> — <N> Hrs Total (Rig-In <a> / Pig <b> / Rig-Out <c>)

WORK-UP BILLING MATH (authoritative — derived from the USA26038 work-up, 2026-07-11):
  - Shift basis: (day-shifts × 12h, last may be partial) + (night-shifts × 12h) = the heater's
    total pumper hours. That total is the heading figure and the equipment Amt.
  - Equipment — TriMax Pumper, Support Unit, Filter Unit, Crew Truck — bills at the heater's
    pumper total hours. Qty 1 each; Amt = heater total.
  - Labor Amt is COMBINED MAN-HOURS, not per-person hours: Amt = Qty × per-person shift hours.
    (2 Day Operators at 44 h/person = 88.) This is the single easiest line to get wrong.
  - Per Diem bills per DAY, not per hour. Headcount EXCLUDES a billable Project Manager — it
    matches the night side's Supervisor + Operators pattern.
  - Materials: DEF bills per SHIFT. Use the quoted shift count as given; do not re-derive it from
    the total shift count.
  - A billable Project Manager line appears on a heater ONLY when the quote carries one
    (USA26038: on H-20, not on H-19). It is not a default line.

Filter Unit appears only when filtration was elected. Omit the row on non-filtered jobs rather
than carrying it at zero.
-->

### <TAG> <Service> — <N> Hrs Total (Rig-In <a> / Pig <b> / Rig-Out <c>)

| Qty | Item | Amt | Unit |
|---|---|---|---|
| 1 | TriMax Pumper | <heater total> | Hrs |
| 1 | Support Unit | <heater total> | Hrs |
| 1 | Filter Unit | <heater total> | Hrs |
| 1 | Crew Truck | <heater total> | Hrs |
| 1 | Project Manager | <hrs> | Hrs |
| 1 | Day Supervisor | <hrs> | Hrs |
| <n> | Day Operators | <combined man-hours> | Hrs |
| 1 | Night Supervisor | <hrs> | Hrs |
| <n> | Night Operators | <combined man-hours> | Hrs |
| <n> | Per Diem: Dayshift | <days> | Days |
| <n> | Per Diem: Nightshift | <days> | Days |
| 1 | Materials: DEF | <shifts> | Shifts |

<!-- Repeat one ### block per heater. -->

Operator / Night Operator Amt is combined man-hours (Qty × per-person shift hours). Quoted total
across all heaters: <N> pumper hours.

---

## <TAG> — Coil Data

<!--
COMPACT reference only — the crew needs enough to work from, not the full card. The heater card
(02-facilities/.../<TAG>.md) remains the single source of truth for tube geometry; this is a
convenience copy of what matters at the launcher, and it should be copied FROM the card, never
authored here and back-filled later.

One table per heater, then a one-paragraph prose line carrying metallurgy, pass configuration,
connection points, and effluent handling. Link both heater cards at the end of the last block.
-->

| Section | Coils | Pipe OD | Pipe Wall | Pipe ID | Tube Length | Tubes/Coil | Ft/Section |
|---|---|---|---|---|---|---|---|
| Convection | | | | | | | |
| Radiant | | | | | | | |

Metallurgy: <value>. Pass config: <e.g. (2) coils looped to (1) pass, 180° at radiant outlet>.
Connections: <e.g. (2) 4" launchers at control valve station (grade)>. Effluent: <e.g. firewater,
filtered through press, stored in frac tanks>.

<!-- After the last heater's block: -->
Full tube geometry, config rollup, and pig spec history: [[<TAG>]], [[<TAG>]].

---

## Carry-Forward Notes — Prior Decoke (<USA#####>, <Month Year>)

<!--
CONDITIONAL SECTION — include only when the heater(s) have prior job history to carry forward.
On a first-time heater there is nothing to carry and the section is omitted entirely rather than
left as an empty shell (same rule as the heater card's stainless warning block).

Source is the prior job's Field Notes on the heater card. Every row is actionable: what to watch
for, and what to do about it. "Confirm still in effect" is a legitimate Action — conditions change
between turnarounds and the crew should verify rather than assume.
-->

| Heater | Watch For | Action |
|---|---|---|
| <TAG> | <what went wrong or slowed the prior job> | <what to do on arrival> |
| Both | <cross-heater or customer-procedure item> | <action> |

---

## Notes

Printable deliverable: `<USA#####>-job-sheet.pdf` (source `<USA#####>-job-sheet.html`), alongside
this file. Billing tables reflect the quoted work-up (<N>-person resource plan). Actual mobilized
crew and timeline are recorded on the job report, not here.

<!--
RENDER PIPELINE (not yet tooled): the printable PDF is currently produced by hand from the HTML
source via headless Chromium. A tools/render_job_sheet.py wrapper was scoped and explicitly
deferred on 2026-07-18 — build it if and when the manual step becomes a real friction point, not
before. See 06-insights/2026-07-18-idea-research-job-sheet-type-formalization.md.
-->
