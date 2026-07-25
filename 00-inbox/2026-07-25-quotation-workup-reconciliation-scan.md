---
type: note
status: open
created: 2026-07-25
tags: [inbox, estimating, data-quality, audit, formosa, marathon, hf-sinclair]
related:
  - "[[2026-07-24-dsp26085-submitted-wrong-quote-number]]"
  - "[[workup-to-proposal-generator-build-spec]]"
---

# Quotation-vs-workup reconciliation — Formosa, Marathon, HF Sinclair

Follow-on to the Exxon Baytown scan. **Method changed deliberately:** the Exxon pass compared the
embedded quote number against the filename, which [[2026-07-24-dsp26085-submitted-wrong-quote-number]]
proved insufficient — DSP26071.1 was caught only because the number happened to travel with a
migrated pricing block. This pass reconciles **totals** against the workup, using the built
generator's `extract_workup.extract()` (in `usadebusk-estimating/scripts/`) against each
quotation's rendered pricing block.

## Results — 8 pairs

| Pair | Workup total | Quotation | Verdict |
|---|---|---|---|
| DSP25156 Formosa VR-401C | $128,531.50 | matches | reconciles |
| DSP26080 HF Sinclair Navajo (3 htr) | $161,678.92 | matches | reconciles |
| DSP26019 Marathon Garyville (4 trucks) | $452,826.28 | $452,826.28 | reconciles exactly |
| DSP26068.1 Formosa VR-401G | $112,642.23 | matches | reconciles |
| DSP26075 Formosa VR-401C | $69,396.75 | matches | reconciles |
| DSP25142 Sinclair Rawlins | $151,703.70 | matches | reconciles |
| **DSP26058 Marathon Garyville** | **$460,516.10** | **$470,118.10** | **open — +$9,602.00** |
| DSP26026 Marathon Detroit | — | — | not reconcilable, see below |

DSP#24021.2 (Marathon Catlettsburg) has a quotation but **no workup xlsx** in either tree, so it
cannot be reconciled at all.

## The one open item — DSP26058, +$9,602.00

Truck 1 quotes $226,794.00 and Truck 2 quotes $243,324.10, summing $9,602.00 above the workup's
$460,516.10. That gap is exactly **2 × $4,801.00** — the mob and the demob lump sum, each of which
appears on *both* truck pages while the workup counts them once.

Independently, `extract_workup` flags the workup's own internal inconsistency: its line items sum
to $465,317.10 against a stated Total of $460,516.10, a gap of exactly $4,801.00 — one more mob/demob
unit.

**This is not settleable from the files and needs Jesse.** Two trucks plausibly mob and demob
separately, in which case the quotation is right and the workup under-counts. Or the lump sum is
per-job and the quotation double-bills it. The quotation is the *higher* number, so if it is wrong
it is an over-quote to Marathon, not lost recovery.

## DSP26026 Marathon Detroit — cannot select a work tab

`extract_workup` picks the `Rate Sheet` tab (quote "81.73" — a rate value misread as a quote number)
because the workup carries **multiple scenarios and none matches the filename**: the scenarios are
labelled `TA Heaters = 26027` and `Rate Sheet`, while the file is named DSP#26026. No `Total:` row
is found. Either the workup holds 26027's scenario under a 26026 filename (the DSP26071.1 pattern
again, one number off) or the numbering is intentional. Worth one look.

## Two process findings, both bigger than any single file

**1. The old `OneDrive\Desktop\Facilities` tree is still live and not a subset of the canonical
store.** `rfq-intake-protocol` step 1 records `OneDrive\USADeBusk\Facilities\` as the canonical
store. But DSP26068.1 (Formosa VR-401G) and DSP26075 (Formosa VR-401C) exist **only** under
`Desktop\Facilities` — they are absent from the canonical tree. Both were used as back-test
evidence for the generator. So the canonical-store rule is currently false in practice, and any
audit scoped to the canonical tree silently misses two live bids.

**2. `backtest_workup.py` hard-codes the stale path.** `FAC = r"C:\Users\Jwuts\OneDrive\Desktop\Facilities"`
at the top of `usadebusk-estimating/scripts/backtest_workup.py`. It still runs only because the
Desktop tree happens to survive. When that tree is cleaned up, the generator's regression suite
breaks. Fix alongside finding 1, since the right path depends on where those two Formosa bids land.

## Minor

DSP26019's pricing header reads `Quotation #: DPS#: 26019` — `DPS` transposed from `DSP`, on all
four truck pages. Cosmetic, already submitted, not worth a reissue on its own.

## Method note for whoever runs this next

Two parsing traps cost real time here, both producing false positives that looked like serious
defects until checked:

1. Multi-truck quotations put **more than one pricing block on a single page** — DSP26019's page 10
   carries both Truck 2 and Truck 3. A one-`Total`-per-page parse reported DSP26019 as $32,563.80
   short and appeared to show a missing Truck 3 page. It reconciles exactly once every block is
   summed.
2. Comparing a single truck page against a whole-job workup total will always diverge on
   multi-truck jobs. Sum all blocks first.

Also: LibreOffice must fully exit between conversions. Firing `soffice --convert-to` back-to-back
in a shell loop silently converts only the first file or two. Drive it from Python with an explicit
wait per file.
