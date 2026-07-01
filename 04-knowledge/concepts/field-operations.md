# Field Operations & Admin
**Layer:** 04-knowledge/concepts
**Source:** Master Reference Module 9

---

## Service Receipt

Handwritten daily document completed by Project Manager for each 12-hour shift.

**Key fields:**
- Date, shift (Day/Night), job number (USA#)
- Equipment mobilized and hours (TriMax, filter press, 4×3 pump, crew trucks, support units)
- Labor headcount and hours (Supervisor, Operators)
- Per diem count
- Materials used (pigs by type and size, DEF)
- Third-party services (description, hours, cost)
- Plant Down Time (hours, cause)
- Shift summary (narrative of activities) — **includes which pump/side/circuit(s) were operated/cleaned this shift.** The L/C/R marking preprinted on the form is a legacy circling convention no longer used; which assembly (left/center/right = pump 1/2/3) ran is captured in this narrative, not by circling L/C/R.
- Clean ID — largest pig size that passed through the full circuit without obstruction. Required for progress tracking. Maximum pig size = tube ID + 0.250". Example: 5.000" ID tube → 5.25" max; 6.065" ID tube → 6.25" standard final / 6.5" max in heavy fouling.
- Customer signature and supervisor signature

**Unsigned receipts = dispute risk. Flag immediately.**

## Ticket Breakdown File

Most important per-job operational document.

Naming: `USA[YYNNN] [Facility Name] [Scope] TriMax Ticket Breakdown`

Contents: all billable resources mobilized, durations on project, billing rates, running totals.

Purpose: source for invoice generation. All service receipt data feeds here.

## Receipt extraction — import-ready table format

| Line Item | Category | Hours/Qty | Rate Basis |
|---|---|---|---|
| TriMax Pumper | Equipment | N hrs | Hourly task-based |
| Filter Press | Equipment | N hrs | Pumping / non-pumping |
| 4×3 Pump | Equipment | N hrs | Hourly |
| Support Unit | Equipment | N hrs | Hourly |
| Crew Truck | Equipment | N hrs | Hourly |
| DS Supervisor | Labor | N hrs | Day Rate |
| NS Supervisor | Labor | N hrs | Day Rate |
| Operator | Labor | N hrs | Day Rate |
| Per Diem | Labor | N count | Daily |
| DEF | Materials | N shifts | Per shift |
| Pigs | Materials | qty/type | Unit rate |
| Third Party | Third Party | N hrs | Cost + 10% |
| Plant Down Time | Stand-by | N hrs | Stand-by rate |

## Plant Down Time (PDT)

Facility-caused downtime (not USADeBusk-caused). Always flag on receipt as potentially billable at stand-by rate. Distinguish clearly from USADeBusk-caused delays in shift summary.

## Invoice readiness check

Before generating invoice:
1. All service receipts collected (no gaps in shift sequence)
2. All receipts have customer signature
3. Third-party items have sufficient description for invoicing
4. Total hours reconciled against proposal — flag significant overruns or underruns for review
5. PDT hours confirmed billable with customer

## Job number filing

All documents under USA# in Pigging Jobs folder on SharePoint. Ticket Breakdown is the anchor document. Attach service receipts (scanned) to job folder.
