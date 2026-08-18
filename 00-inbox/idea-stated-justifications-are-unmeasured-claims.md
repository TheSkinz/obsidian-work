---
type: idea-seed
status: unexplored
created: 2026-08-17
tags: [idea, generator, validation, cross-cutting, future]
related: [[2026-08-17-triage-job-report-generator-layout-gaps]]
---

# A design's stated justification is a claim, and ours go unmeasured

Idea seed captured 2026-08-17 out of the job-report generator work. The read below is tentative —
confirm intent with Jesse before designing.

**Tentative read:** the job report's Pigs Used table was split across two side-by-side sub-tables,
and both the renderer and two spec documents gave the same reason: the size rows split "to fit the
page." On 2026-08-17 that was rendered and measured for the first time, against USA25025 — the
26-size job the split was built for — and it was **false**. The section starts low on page 2, so
the 2-up broke anyway at 5 of its 13 rows. The split had never delivered the thing it existed for,
on any job, and the reason was written down in three places and repeated for months without anyone
rendering it. The fix turned out to be smaller than either the split or the row-count threshold
that was proposed to replace it: keep the table together and let it move whole.

The generalisable part is not about pig tables. A design decision that ships with a stated reason
reads as *checked* — the reason is right there — when nothing about writing a reason down makes it
true. This is the same failure the generator already produced once in a different register: a
back-test that compared only numbers reported PASS on a document that had never drawn a table
border (see [[2026-08-16-backtest-passed-on-a-visually-broken-document]]). There the gap was what
counted as the match surface; here it is that the justification itself was never a measurement.

**To explore:** which other stated justifications in the document generators have never been
measured? Candidates visible from this session — rig hours pooled at project level because
"rigging is fungible", the claim that per-heater pig/smart allocation is safe wherever a pumper
stays on one heater, the `_widths()` column figures that were sampled once from a shipped PDF, and
the equivalent reasoning in the workup-to-proposal transfer step. Is there a cheap standing form
for this — when a design carries a because-clause about the *output*, does the back-test have to
assert that clause rather than restate it? And is it worth a one-time sweep of the existing
because-clauses rather than any standing machinery, given how few of them there are?

**Gate:** None — researchable now. Cheap to do as a read-and-list pass before any of it becomes a
build.
