<!-- PARTLY EXECUTED — triaged 2026-08-17 ([[2026-08-17-triage-job-report-generator-layout-gaps]], tally 2 execute / 1 test / 1 park / 1 merged / 10 kill). Two of the three layout gaps are closed in the generator: the narrative lead-in and the pig table, both verified. **The third gap is open** — inline image placement was never tested and is untouched; the renderer still emits a dedicated Images section on its own page, and USA26041's config still lists the `launchers.png` row the delivered report dropped. Status corrected researched -> open 2026-09-08 so the remaining third stays visible. -->
---
type: idea-seed
status: open
created: 2026-08-16
tags: [idea, fieldpm, job-report, generator, future]
related: [[2026-08-17-triage-job-report-generator-layout-gaps]]
---

# Job-report generator: three layout gaps that force hand-editing

Idea seed captured 2026-08-16 for a future exploration session. The read below is tentative —
confirm intent with Jesse before designing.

**Tentative read:** the USA26041 report needed hand-editing in Word for three layout changes the
generator cannot express, which broke the load-bearing rule that the generator owns all layout and
the PM edits only prose. The three, all from Jesse's delivered document: **images placed inline**
in the flow of the document (one after the heater callout, one after the flow tests) with no
separate Images section, rather than the generator's dedicated section; **Pigs Used as one merged
six-column table** with the legend note beneath it and the last column headed `SWAB`, rather than
two side-by-side sub-tables with the note above and `SWAB/HC`; and a **configurable narrative
lead-in** — he wants "Decoking Analysis:" where the renderer hard-codes "Result:". All three look
small. Until they exist, every report forks from its config the moment it is finished, which is
exactly how a round of his edits got destroyed by a re-render on 2026-08-16.

**To explore:** is inline placement the preferred default for every report or specific to a
single-heater job where a whole Images section is disproportionate? Is the merged pig table always
better, or only when the size count is small enough to fit one table (USA25025 had 26 sizes across
9 heaters and may genuinely need the 2-up split)? Should the lead-in be free-text per heater, or a
small enumerated set so reports stay consistent across jobs? And the wider question the incident
raises: should the generator ever write over a delivered file at all, or should it always emit to
a new path and leave merging to the PM?

**Gate:** None — researchable now, and worth doing before the next Baytown report so the same
fork does not repeat.
