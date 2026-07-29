---
type: capture
status: open
created: 2026-07-28
tags: [capture, estimating, proposal, data-quality, westlake, external-exposure]
related:
  - "[[DSP26095]]"
  - "[[2026-07-24-dsp26085-submitted-wrong-quote-number]]"
  - "[[2026-07-27-idea-research-quotation-workup-reconciliation-check]]"
---

# DSP26095 shipped to Westlake reading `DSP#:26000` — second occurrence, first one that reached a customer

**What happened.** The DSP26095 quotation sent to Westlake South on 2026-07-28 carries
`Quotation #: DSP#:26000` in its Section 7 pricing block. The correct number is DSP#:26095,
assigned 2026-07-27. Everything else on the document is right — $44,415.88, the five line items
reconcile to the workup total exactly, rates and markup are as intended, and the execution-plan
dates read 2026 correctly.

**Root cause, verified not inferred.** The pricing block in
`DSP#26095_..._Decoke_2026-7 Quotation.docx` is a pasted Enhanced Metafile at
`word/media/image7.emf`; the string `DSP#:26000` is present in it as UTF-16LE. A static vector
paste freezes whatever the source cell read at copy time and never follows it afterward. The PDF
is exported from that docx, so it inherits the frozen number.

**What makes this one different from [[2026-07-24-dsp26085-submitted-wrong-quote-number]].** Two
things, and both matter.

First, **the workup is wrong too.** On DSP26085 the workbook's `Insert Quote` tab resolved
correctly to 26085 and only the pasted image was stale, so patching the EMF was a complete fix.
Here the workbook itself never got the number: `extract_workup.py` reads `quote_no_raw: 26000`,
the header block as `DSP#:26000`, and registers the build tab as `('Build', '26000')`. Patching
the EMF alone would leave the source of truth still carrying the placeholder, and the next
document generated from that workbook would reproduce the defect.

Second, **this one reached the customer.** DSP26085 was caught before sending and had no external
exposure. This is a live quotation in Westlake's hands with the wrong number on it. Whether to
reissue is Jesse's call and is recorded as the open item on [[DSP26095]].

**Two lesser defects on the same document,** both template-stale rather than newly introduced:
the quotation date reads `1-Jul-2026` when the number was not assigned until 2026-07-27, and the
Execution Plan names **Travis Trenholm** as Project Manager — the same superseded name carried on
[[DSP26071]], where the job sheet already records that Jesse is running the job.

## Why this is evidence for a pending decision

[[2026-07-27-idea-research-quotation-workup-reconciliation-check]] is sitting undecided in
`06-insights`, proposing an event-triggered check that parses the quotation's own figures and
diffs them against the workup. Its Decision box is unchecked.

That review argued the trigger should be a script edit plus an optional pre-send gate. **This
incident is a direct argument for the pre-send gate specifically**, and it sharpens what the gate
has to compare. A totals-only diff would have passed this document cleanly — the money is
correct to the cent on both sides. What was wrong was the *identity* field, and it was wrong
identically in both artifacts, so a workup-vs-quotation diff would have found them in agreement
and said nothing.

So the check needs a third comparison the review did not name: **the quote number in the
generated document and in the workup, both against the DSP number the vault says this bid was
assigned.** That is the only one of the three sources that was right. Any gate built without an
external anchor would have shipped this.

Worth carrying into the decision rather than filing as a separate idea — it is the same build,
with one more assertion in it.

## Also worth a look

The `.docx` filename reads `..._Decoke_2026-7 Quotation.docx` while the PDF and workup both read
`2026-9`. Execution is September, so the docx filename is the outlier. Cosmetic, but it is the
kind of thing that makes the wrong file get picked up later.
