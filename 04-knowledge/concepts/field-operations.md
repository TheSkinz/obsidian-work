# Field Operations & Admin
**Layer:** 04-knowledge/concepts
**Source:** Master Reference Module 9

---

## Service Receipt

Handwritten daily document completed by Project Manager for each 12-hour shift.

**Key fields:**
- Date, shift (Day/Night), job number (USA#)
- Equipment mobilized and hours (Trimax, filter press, 4×3 pump, crew trucks, support units)
- Labor headcount and hours (Supervisor, Operators)
- Per diem count
- Materials used (pigs by type and size, DEF)
- Third-party services (description, hours, cost)
- Plant Down Time (hours, cause)
- Shift summary (narrative of activities)
- Clean ID — largest pig size that passed through the full circuit without obstruction. Required for progress tracking. Maximum pig size = tube ID + 0.250". Example: 5.000" ID tube → 5.25" max; 6.065" ID tube → 6.25" standard final / 6.5" max in heavy fouling.
- Customer signature and supervisor signature

**Unsigned receipts = dispute risk. Flag immediately.**

## Ticket Breakdown File

Most important per-job operational document.

Naming: `USA[YYNNN] [Facility Name] [Scope] Trimax Ticket Breakdown`

Contents: all billable resources mobilized, durations on project, billing rates, running totals.

Purpose: source for invoice generation. All service receipt data feeds here.

## Receipt extraction — import-ready table format

| Line Item | Category | Hours/Qty | Rate Basis |
|---|---|---|---|
| Trimax Pumper | Equipment | N hrs | Hourly task-based |
| Filter Press | Equipment | N hrs | Pumping / non-pumping |
| 4×3 Pump | Equipment | N hrs | Hourly |
| Support Unit | Equipment | N hrs | Hourly |
| Crew Truck | Equipment | N hrs | Hourly |
| DS Supervisor | Labor | N hrs | Hourly |
| NS Supervisor | Labor | N hrs | Hourly |
| Operator | Labor | N hrs | Hourly |
| Per Diem | Labor | N count | Daily |
| DEF | Materials | N shifts | Per shift |
| Pigs | Materials | qty/type | Unit rate |
| Third Party | Third Party | N hrs | Cost + markup (contract-specific, confirm each job — some facilities as low as 5%) |
| Plant Down Time | Stand-by | N hrs | Billed via the Trimax Pumper / Filter Press stand-by rates only — no generic stand-by line |

## Demob — which one the vault records

There are two distinct demobs, and they are routinely conflated:

1. **Facility demob** — equipment comes off the unit and leaves the customer's facility. This coincides with crew demob, and it is where the job ends: **there are no additional charges after this point.**
2. **Fleet return** — equipment travels from wherever it staged back to Deer Park, TX (fleet HQ).

**The vault records concept 1 only, and "demob" with no qualifier always means concept 1.** A job's demob date is its crew-demob date.

Never record, infer, or ask about concept 2. Equipment is frequently staged near a facility for weeks because a separate upcoming project will execute there, so fleet return has no fixed relationship to job end and is not USADebusk-controlled in any way the vault could track. Assume the project leaves with the crew. If a source document gives a later equipment-return date, that is concept 2 — do not promote it to the job's demob date. This is the same rule as filter-press availability: logistics is Jesse's, not the vault's.

Caught 2026-07-25: the `usadebusk-fieldpm` dormancy banner had recorded USA26038 as "demobbed 2026-07-20", which was the fleet-return date, against a job that completed 2026-07-17.

## Plant Down Time (PDT)

Facility-caused downtime (not USADebusk-caused). Always flag on receipt as potentially billable at stand-by rate. Distinguish clearly from USADebusk-caused delays in shift summary.

## Invoice readiness check

Before generating invoice:
1. All service receipts collected (no gaps in shift sequence)
2. All receipts have customer signature
3. Third-party items have sufficient description for invoicing
4. Total hours reconciled against proposal — flag significant overruns or underruns for review
5. PDT hours confirmed billable with customer

## Job number filing

All documents under USA# in Pigging Jobs folder on SharePoint. Ticket Breakdown is the anchor document. Attach service receipts (scanned) to job folder.
