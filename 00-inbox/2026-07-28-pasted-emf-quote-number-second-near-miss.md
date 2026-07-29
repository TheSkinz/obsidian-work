---
type: capture
status: resolved
created: 2026-07-28
resolved: 2026-07-28
tags: [capture, estimating, proposal, data-quality, westlake]
related:
  - "[[DSP26095]]"
  - "[[2026-07-24-dsp26085-submitted-wrong-quote-number]]"
  - "[[2026-07-27-idea-research-quotation-workup-reconciliation-check]]"
---

# The pasted-EMF quote number went wrong a second time — caught pre-send, but a totals diff would not have caught it

**Resolved same day.** [[DSP26095]] briefly carried the placeholder `DSP#:26000` in its Section 7
header, in both the quotation and the workup. Jesse corrected both on 2026-07-28 before the quote
went to Westlake. No external exposure. Nothing here needs action — the note is kept for the one
durable point below.

**The recurrence itself.** This is the second instance of the same mechanism as
[[2026-07-24-dsp26085-submitted-wrong-quote-number]]: the Section 7 pricing block is a pasted
Enhanced Metafile, a static vector paste that freezes whatever the source cell read at copy time
and never follows it afterward. Both instances were caught before sending. Two near-misses is
worth recording as a pattern even though neither cost anything, because the mechanism is silent
by construction — nothing about the document signals that the block has stopped tracking its
source.

DSP26095 differed from DSP26085 in one way worth remembering: **the workup was wrong too.** On
DSP26085 the workbook resolved correctly and only the paste was stale, so patching the EMF was a
complete fix. Here the placeholder was in the workbook as well — the raw cell, the header block,
and the build-tab registration — so the source of truth needed the same correction as the paste.
When this recurs, check both.

## The point worth carrying into a pending decision

[[2026-07-27-idea-research-quotation-workup-reconciliation-check]] is awaiting Jesse's decision in
`06-insights`, proposing a check that parses a quotation's figures and diffs them against the
workup.

**A totals-only diff would have passed this document silently.** The money was correct to the cent
on both sides — the five line items reconciled to the workup total exactly. What was wrong was an
*identity* field, and it was wrong **identically in both artifacts**, so a workup-vs-quotation
diff would have found them in perfect agreement and said nothing.

So the check needs an assertion the review did not name: **compare the quote number in the
generated document and in the workup against the DSP number the vault records for that bid.** The
vault was the only one of the three sources that was right. Any gate built purely as a two-way
diff between the two documents inherits their shared error.

Worth folding into that decision as one more assertion in the same build, not filed as a separate
idea.
