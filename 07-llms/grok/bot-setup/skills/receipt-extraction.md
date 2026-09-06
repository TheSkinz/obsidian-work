# Skill — Receipt Extraction

**Owner Bot:** Ledger
**Source:** ported from usadebusk-ops, sections "Service Receipt", "Receipt Extraction Process",
"Plant Down Time". Re-read that skill in the vault if anything here looks stale.

## What this does

Turns handwritten daily service receipts into a structured, import-ready ticket-breakdown table.
One receipt per 12-hour shift, completed by the PM.

## Field map — what is on the receipt

**Header:** customer name and contact; date and shift (Day/Night); location; job number and PO;
unit number and pass number; Clean ID; final pig size; total length pigged this shift.

**Clean ID is the field-measured inner diameter of the tube being pigged**, as against the design
ID on the drawing. It is a sizing input, not a cleaning result. Where field and design disagree,
the field measurement governs. Do not read it as "the largest pig that passed" — that is the
**final pig size**, a different quantity on a different line. Max pig size = Clean ID + 0.250".

**Equipment hours:** Pumper hours (the L/C/R marking preprinted on the form is a legacy convention
and is no longer used — which pump, side or circuit was worked is in the Shift Summary narrative,
not in that marking); support unit hours; crew truck IDs and hours; materials and equipment
freeform; filtration and filter hours; pigs by type and quantity.

**Labor hours:** DS supervisor name and hours; NS supervisor name and hours; up to six operator
slots with names and hours.

**Task hours:** rig in, rig out, rig over, pigging, plant down time, third-party services with
description and hours.

**Third-party is a trap.** Smart-pig time is also recorded on that line, vendor name plus hours,
to save space on the form. A vendor name there is not by itself a third-party charge. Read the
shift summary before treating it as billable third party.

**Consumables:** per diem count (people times shifts); DEF count (shifts).

**Shift Summary:** freeform chronological narrative, including which pump, side or circuits were
worked. Example: "7am-9am: Pig (2 hrs) Polish 30 passes. 9am-12pm: Smart Pig (3 hrs). 12pm-2pm:
Stand-by (2 hrs) wait for approval. 2pm-7pm: Rig-out (5 hrs)."

**Sign-off:** customer name and signature, supervisor name and signature, date.

## Step 1 — extract every billable field

| Line item | Category | Qty | Rate basis |
|---|---|---|---|
| Trimax Pumper | Equipment | hrs | Hourly, task-based |
| Filter Press | Equipment | hrs | Pumping vs non-pumping. Pumping = pigging only. Non-pumping = rig-in, rig-out, smart pigging, stand-by |
| 4x3 Pump | Equipment | hrs | Hourly |
| Support Unit | Equipment | hrs | Hourly |
| Crew Truck | Equipment | hrs | Hourly |
| DS Supervisor | Labor | hrs | Hourly |
| NS Supervisor | Labor | hrs | Hourly |
| Operator | Labor | hrs | Hourly |
| Per Diem | Labor | count | Daily |
| DEF | Materials | shifts | Per shift |
| Pigs | Materials | qty by type | Unit rate |
| Third Party | Third Party | hrs | Cost plus markup |
| Plant Down Time | Stand-by | hrs | Billed through the Trimax Pumper and Filter Press stand-by rates only. There is no generic stand-by line |

## Step 2 — cross-check against the proposal

Are the resources on the receipt consistent with the proposal scope? Do the task hours line up
with the execution plan? Is anything being billed that was not in the original proposal? Is PDT
present? Is the third-party detail sufficient to invoice from?

## Step 3 — variance flags, stated explicitly

Hours past the proposal estimate for any task category. Resources billed that were not in scope.
Missing customer or supervisor signature. Missing Clean ID. Incomplete or missing shift summary.
Per diem count not matching headcount.

**Unsigned receipts are a dispute risk. Flag immediately, at the top, not in a list at the end.**

## Step 4 — output

A clean structured table formatted for entry into the Ticket Breakdown spreadsheet. Use the
built-in Spreadsheets skill. File naming for the breakdown itself:
`USA[YYNNN] [Facility Name] [Scope] Trimax Ticket Breakdown`.

## Plant Down Time

Facility-caused downtime, not USADebusk-caused. Always flag as potentially billable at the
stand-by rate, and keep it clearly distinct from USADebusk-caused delays in the narrative.

## Safety boundaries

Never guess an illegible field — flag it and ask. Never adjust a number to make a total
reconcile; a discrepancy is a finding. Preserve the crew's own words in the shift summary rather
than rewriting them. Do not pull data from another job's records without being asked to.
