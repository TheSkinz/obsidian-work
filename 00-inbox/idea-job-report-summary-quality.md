---
type: idea-seed
status: unexplored
created: 2026-09-03
tags: [idea, job-report, fieldpm, writing, future]
---

# Job-report summaries are not good enough yet

Idea seed captured 2026-09-03 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Jesse's own words, 2026-09-02:** *"I'm still not fully happy with any of the job report summaries we do. At some point in the future we need to figure out how we can perfect it, but this will do for now."* Said after four rounds of revision on the CAD26001 Project Summary, so this is not about one bad paragraph — it is about the class.

**Tentative read:** every generated table in the job report is solved; the prose is the one part still hand-fought each time. The CAD26001 rounds are the evidence and are worth reading before designing anything, because each correction names a failure mode rather than a preference:

- *"You don't 'carry to completion on effluent return'"* — invented phrasing that reads like jargon and means nothing to a reader.
- *"Sounds like you're describing the SOP"* — narrating **how the work is done** instead of reporting **what happened**. "Each circuit was pigged until the return water ran clear" became "each circuit was pigged until clean."
- *"No reason to reassert the technical data of the furnace. They know their own furnace"* — restating what the data table already carries, to an audience that owns the asset.
- *"Why even mention that flow tests are recorded before and after? Remove it."* — describing the report's own contents inside the report.
- *"Stop putting specific types of pig names"* and *"no reason to go into that much detail"* — operator-level granularity in a document for engineers and metallurgists.

**The through-line worth testing:** the failures are all the same shape — writing for a reader who does not know the plant, when the actual reader owns it. The summary's job may be much smaller than it has been written as: what was done, what was found, what it means for the next run.

**To explore:**
- Is there a house structure a summary should always follow, or is per-job judgement the point? A three-move shape (scope executed → condition found → what it means next) would be testable against the delivered USA26038, USA26041 and CAD26001 reports.
- Should any of this become skill content in `usadebusk-fieldpm`, or is a worked exemplar enough? The generator spec already owns tables and layout; prose is deliberately the PM's.
- **Back-test before building** (standing rule): reconcile any proposed shape against at least two structurally different delivered reports before it governs anything.
- Who is the reader of record? CAD26001 went to Syncrude reps — metallurgists and engineers. Confirm that generalises before designing for it.

**Gate:** none. Researchable now — the delivered reports and this session's revision trail are the corpus.

**Partly explored 2026-09-03.** The terminology half of this is now worked up in [[2026-09-03-fouling-terminology-vocabulary]] — a decision packet awaiting Jesse's term-by-term rulings. It covers the vocabulary and the register question ("who is the reader of record"), and answers it with a three-register split rather than a single audience. It does **not** cover the *structure* question above — the three-move shape (scope executed → condition found → what it means next) is still open and still needs the back-test. Close this seed when both halves are settled.

Related: [[CAD26001-job-sheet]], the delivered CAD26001 report, and `usadebusk-fieldpm/references/report-structure.md`.
