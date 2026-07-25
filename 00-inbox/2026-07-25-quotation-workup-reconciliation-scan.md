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

## DSP26026 Marathon Detroit — quote number fixed; a scope gap remains open

**Resolved 2026-07-25.** Jesse: the `26027` was a mistake. Confirmed safe to change — **no DSP26027
exists anywhere**: no quotation, no workup, no vault reference. The number was never issued.

Fixed in the workup at `Marathon Detroit MI\DSP# 26026 RFQ - 3Q26 Coker Heater Pigging Sept 2026 T&M.xlsx`:
`TA Heaters !C3` held the literal `DSP#: 26027`, and `Insert Quote !G6` is `='TA Heaters '!$C$3`, so
both read wrong. Patched the XML inside the workbook rather than re-saving through openpyxl, which
warns it would strip the file's conditional-formatting extensions. Verified: 36 zip entries before
and after, only `sharedStrings.xml` and `worksheets/sheet2.xml` differ, the G6 formula is intact,
and both cells now read `DSP#: 26026`. Pre-fix backup in the session scratchpad.

**Still open — the workup is scoped wider than what was submitted.** With the number fixed the
extractor reaches the tab for the first time and reads **$153,715.40**, against the submitted
quotation's **$114,167.24** — a gap of $39,548.16 that is *not* a multiple of the $24,900 mob/demob
unit, so it is not the lump-sum signature. The submitted quotation covers the **70H1 Coker only**
(6 Hrs. Rig-in / 24 Pig / 6 Rig-out, decoke $58,287.24); the workup's `TA Heaters` row carries
**12 / 36 / 12** and $75,240.00 of equipment. The likely reading is an ordinary narrowing — the
workup was built for a wider turnaround scope and the bid went out for the single coker — but that
is inference, not verified. Worth one look to confirm nothing was quoted short.

*(original finding below)*

## DSP26026 Marathon Detroit — cannot select a work tab

`extract_workup` picks the `Rate Sheet` tab (quote "81.73" — a rate value misread as a quote number)
because the workup carries **multiple scenarios and none matches the filename**: the scenarios are
labelled `TA Heaters = 26027` and `Rate Sheet`, while the file is named DSP#26026. No `Total:` row
is found. Either the workup holds 26027's scenario under a 26026 filename (the DSP26071.1 pattern
again, one number off) or the numbering is intentional. Worth one look.

## Two process findings, both bigger than any single file

**1. The old `Desktop\Facilities` tree held bids the canonical store did not — RESOLVED 2026-07-25.**
`rfq-intake-protocol` step 1 records `OneDrive\USADeBusk\Facilities\` as the canonical store, but
DSP26068.1 (Formosa VR-401G) and DSP26075 (Formosa VR-401C) existed **only** under
`Desktop\Facilities`, so the rule was false in practice and any audit scoped to the canonical tree
silently missed two live bids — both of which had been used as back-test evidence for the generator.
Jesse's call: move them. Both bid folders (16 files, drawings and bid packages included) were moved
whole into `Formosa Point Comfort TX\Bids\`. The Desktop Formosa folder is now empty and the
canonical-store rule is true again.

**2. `backtest_workup.py` was not fragile — it was already broken. RESOLVED 2026-07-25.** It
hard-coded `FAC = …\Desktop\Facilities`, and its two Exxon paths had *already* gone dead when those
files moved to the canonical store, so the suite had been silently unrunnable and the generator's
"proven" back-test was not actually being run. Repointed to the canonical store; with the Formosa
move above, the legacy root is gone entirely and all three pairs reproduce exactly again. A comment
now warns against reintroducing a second root: an unreachable case is a storage bug to fix, not a
path to special-case.

**3. A latent crash, surfaced by fixing the DSP26026 number.** With the right tab finally reachable,
`read_duration` hit that workup's row 24 — a **header** row reading
`Furnace | Labor | Equipment | Materials | Perdiem | Mob | Demob` — and fed those labels into the
hour fields, where `hour_breakdown`'s numeric format raised `ValueError` and took the whole
extraction down. Non-numeric duration rows are now skipped. Worth noting the shape: the crash was
latent behind a *different* defect, and fixing one defect is what exposed it.

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
