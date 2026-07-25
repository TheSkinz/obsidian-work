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
| DSP26058 Marathon Garyville | $460,516.10 | $470,118.10 | not a defect — see below |
| DSP26026 Marathon Detroit | — | — | not reconcilable, see below |

DSP#24021.2 (Marathon Catlettsburg) has a quotation but **no workup xlsx** in either tree, so it
cannot be reconciled at all.

## DSP26058's +$9,602.00 — CLOSED, not a defect (Jesse 2026-07-25)

Truck 1 quotes $226,794.00 and Truck 2 quotes $243,324.10, summing $9,602.00 above the workup's
$460,516.10 — exactly 2 × the $4,801.00 mob/demob. `extract_workup` separately flagged the workup's
own lines summing $4,801.00 above its stated Total.

**Jesse's ruling: a mob/demob mismatch between workup and quotation is expected and does not need
to reconcile.** Mob and demob are billed as a **lump sum — a flat fee regardless of what actually
happens during the mobilization.** Where the two figures diverge, it is because *the contract caps
what can be billed*. The workup is a template used across all facilities, and its mobilization
build-up is still performed — but for **internal cost/profit visibility**, not to derive the
quoted number. The contract governs what is quoted.

**Consequence for this audit method:** mob and demob lines must be **excluded** from
quotation-vs-workup reconciliation. A gap that equals a whole number of mob/demob units is the
expected signature of a contract-capped lump sum, not a finding. Reconcile the execution lines
(decoke, labor & per diem, materials) and treat mob/demob as contract-governed.

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

## Two generator defects this ruling exposes — NOT applied, Lane 4, awaiting Jesse

Both are in `usadebusk-estimating/scripts/`, which produces client-facing proposal drafts.

**1. `extract_workup.py:431` treats the workup's mob amount as the quotable figure.** It sets
`"amount": roles["mob"]` (and `roles["demob"]` at :459) directly onto the quotation line, so the
generator emits the internal cost/profit build-up as the customer-facing lump sum. Per the ruling
above that number is *not* authoritative — the contract's capped flat fee is. The generator carries
no flag telling the reviewer to confirm those two lines against the contract, unlike the `(J field)`
CONFIRM prompts it already emits for prepared-by, valid-until, and third-party markup. Proposed fix:
add mob and demob to the CONFIRM set rather than presenting them as derived.

**2. The `LINE ITEMS DO NOT RECONCILE … Do not send until resolved` flag will fire on normal jobs.**
It triggers whenever lines fail to sum to the financials Total, which is precisely what a
contract-capped mob/demob produces. DSP26058 tripped it legitimately-looking and was a false
positive. A hard "do not send" that fires on healthy jobs trains the reviewer to ignore it — the
worst failure mode for a safety flag. Proposed fix: exclude mob/demob from that sum and, if the
residual gap is a whole multiple of the mob/demob unit, report it as expected rather than blocking.

Neither is applied. Both touch pricing behavior in a deliverable-producing tool.

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
