---
type: note
status: inbox
created: 2026-08-21
related:
  - "[[2026-08-21-idea-research-stated-justifications-unmeasured]]"
  - "[[_canonical-job-sheet]]"
tags: [generator, job-report, validation, cross-cutting, owed]
---

# The remaining because-clause sweep is owed — roughly a dozen, both renderers

Item 3 of the DQ-028 ruling (2026-08-21). Items 1, 2 and 4 were done; this one was
deliberately not started rather than half-done at the end of a long session.

**What it is.** Roughly a dozen layout-rule comments across `render_job_report.py` and the
proposal renderer state a justification about the rendered output — the shape of
`# 6.90" — full text width`. Read each, mark it measured / hedged / unmeasured, then either fix
it or date-stamp it. An afternoon, one pass, no recurrence. The specific clauses are listed in
evidence item 6 of the source note.

**Why it is worth doing rather than dropping.** The one clause that was measured turned out to be
**true** — the text column really is 6.90" and that spec sums to exactly 6.90. The defect was
never the number. It was that every *other* table in the same renderer declares 7.00"–7.70", so a
correct comment read as a house convention that does not exist. A tier-one structural check written
to enforce that phantom convention fired on 17 of 18 tables in a report that had shipped and been
accepted, and was only caught by rendering to PDF and measuring before believing it.

That is the risk sitting in the other clauses: not that they are wrong, but that a true statement
reads as a general rule, and the next person to write a check enforces the rule that was never
there.

**What already guards against a repeat.** `_canonical-job-sheet.md`'s LAYOUT-rule class now
requires a rule stating a reason about rendered output to record the date it was last checked
against a rendered artifact — verifiable is not verified. That applies to these clauses as they are
touched, so the sweep is cleanup of a known backlog rather than an open-ended hazard.

**Not urgent.** Nothing is generating more of these, and the convention catches new ones.
