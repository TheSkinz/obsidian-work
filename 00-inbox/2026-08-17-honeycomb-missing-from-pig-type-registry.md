<!-- vault-loop: operational — Lane 4 domain truth (canonical pig-type registry, heater-card units). Capture loop cannot write this content. -->
---
type: finding
status: resolved
closed: 2026-09-07
closed-by: "Both halves ruled and applied 2026-09-07 (consolidated decision pass). (a) Honeycomb added to the canonical pig-type registry (config f7440c0): polyurethane body with tapered conical ends, appendages threaded into the body, different manufacturer, limited supply — roughly 1 project in 5 (Jesse). (b) The three cells were NOT lengths — honeycomb sizes are recorded in MILLIMETRES (Jesse): 104 mm = 4.094 in on H-19's 4.026 in ID, 76 mm = 2.992 in and 84 mm = 3.307 in on H-20's 3.068 in ID. Cards corrected and pig_usage_rollup.py now converts on the unit (5b4ac3b), so 22 real pigs rejoin the size breakdown."
created: 2026-08-17
related:
  - "[[2026-08-17-triage-job-report-generator-layout-gaps]]"
tags: [finding, equipment, pig-types, heater-cards, lane-4]
---

# Honeycomb is tracked in three places and defined in none of them

Surfaced 2026-08-17 while making the job-report generator's last pig-table column header follow the
data. HC is a real tool USADebusk runs — the shipped USA26038 report's own legend reads "Swab —
dewatering swab. HC — honeycomb gauge," and that job ran 35 of them — but it is absent from the
canonical registry that everything downstream is supposed to defer to.

**The registry gap.** `usadebusk-equipment` §Pig Types lists Foam, TC, HR and Swab, plus the field
shorthand codes BLT, Wire Brush, Bald and Gauge. Honeycomb appears in neither list. The extraction
reference is written to defer to that registry on any definition conflict, so on honeycomb it defers
to nothing.

**Why it leaks.** The extractor's `pig_bucket()` routes anything matching "honey" into a shared
`SWAB/HC` bucket, which is why dewatering swabs and honeycomb gauges share one column on the customer
report, and why the column header now has to be derived per job rather than fixed.

**The unit problem.** The H-19 and H-20 heater cards record honeycomb "sizes" as `76"`, `84"` and
`104"`. Those are lengths sitting in a diameter column. `pig-usage-rollup.md` already flags them and
excludes them from the size breakdown, so the rollup is not wrong today — but the cards are, and any
future consumer that does not know to exclude them will read a 104-inch pig.

## What is owed, and why the capture loop stopped here

Adding the registry row needs Jesse: the body description and use case are domain truth he holds, and
`usadebusk-equipment` §Pig Types is Lane 4. Correcting the H-19/H-20 dimension fields is a heater-card
edit, also outside this loop's write scope. Both belong to the on-demand operational loop or an
interactive session.

Source: Claude Code session `8e7a4b72`, 2026-08-17, closing exchange after the pig-table work.
