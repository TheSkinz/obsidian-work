---
type: finding
status: open
created: 2026-08-16
related:
  - "[[DSP26085]]"
  - "[[idea-quotation-workup-reconciliation-check]]"
  - "[[2026-07-24-dsp26085-submitted-wrong-quote-number]]"
tags: [finding, estimating, data-quality, quotes, exxon-baytown, awaiting-decision]
---

# Three bids have two workups on file that disagree on price

Found 2026-08-16 while building the pre-send gate (DQ-015). **Nothing was changed in any file** —
which copy is authoritative is Jesse's call in every case below.

## The live one — DSP26085, still pending

Two files named `DSP#26085_Exxon Baytown_27GF1A F-201_2027 Jan Workup.xlsx` exist under the
canonical store with **different contents**:

| Copy | Saved | Total | Mechanical Decoke |
|---|---|---|---|
| `ExxonMobil\ExxonMobil Baytown TX\Bids\Exxon Baytown_F-201\` | 2026-07-07 | **$40,477.08** | $23,580.00 |
| `ExxonMobil\ExxonMobil Baytown TX\Jobs\` | 2026-07-25 | **$46,657.08** | $29,760.00 |

Task hours are **identical** on both (6 rig-in / 18 pig / 6 smart / 6 rig-out). The entire
**$6,180.00** sits on the Mechanical Decoke line, so this is not a scope difference.

The `Bids` copy is the one that matches the submitted quotation, the regression suite's frozen
expectation, and this vault's recorded `value: 40477.08` on [[DSP26085]]. The `Jobs` copy is
later, higher, has no quotation beside it, and sits in a folder that normally means awarded — for
a quote that is **still `pending`, valid through 2026-09-29, execution 2027-01.**

**Why the date matters.** 2026-07-25 is the same day the DSP26085 pricing-block quote-number
defect was fixed ([[2026-07-24-dsp26085-submitted-wrong-quote-number]]). But that fix was a
ten-byte patch inside `word/media/image6.emf` and explicitly avoided re-pasting from Excel — it
had no reason to touch a money line, and the note records the total holding at $40,477.08. So the
coincidence of dates does not explain the $6,180. It is worth checking whether the two events
share a cause rather than assuming they do.

This is the **second** document defect on this one bid.

## Two more, both historical rather than live

The same check across the estate found six DSP#-era workup filenames with two copies each. Three
disagree on total, three do not:

| Bid | Copies | Verdict |
|---|---|---|
| **DSP25138** Valero McKee | `Bids\DSP25138 2025-11\` **$166,484.46** vs facility root **$262,828.10** | **disagree by $96,343.64** |
| **DSP25070** Exxon PS3 | `Jobs\USA26007 PS3 2026-02\` **$162,576.42** vs `_History\` **$169,947.76** | **disagree by $7,371.34** |
| **DSP26085** Exxon F-201 | see above | **disagree by $6,180.00** |
| DSP26061 Exxon CLEU2-F3 | both $57,205.12 | agree — benign duplicate |
| DSP26075 Formosa VR-401C | both $69,396.75 | agree — benign duplicate |
| DSP24144 Hunt Tuscaloosa | neither readable by `extract_workup` (older template) | not compared |

**Neither DSP25138 nor DSP25070 has a vault quote note** — both predate the practice — and both
are historical: DSP25138 executed July 2026, DSP25070 became USA26007. So they are a
data-integrity question, not live commercial exposure. Only DSP26085 is pending.

**A differing total is not automatically a defect.** DSP25070's second copy sits under `_History\`,
which is plausibly a deliberate archive of a superseded revision — exactly what an archive is for.
DSP25138's odd copy is the one loose at the facility root, in neither a `Bids` nor a `Jobs` folder.
The question in each case is not "why do these differ" but **"is the copy someone would open the
authoritative one."**

## Why this is a known class, not a surprise

The 2026-07-25 estate scan already found this shape one layer over, in quotations rather than
workups: `DSP#26071.1_...Rev001.docx` in a `Jobs\...\Submit\` folder carried **Rev002's entire
pricing block** — $60,287.42 under a filename promising $98,134.26. The two files were not
byte-identical, so it was a working copy that received a paste before a Save-As. Jesse's call was
to delete it, keeping the native PDF as the authoritative Rev001 record.

**That scan covered quotations only. Workups were never scanned** — which is why these sat
undetected for a year. This note is that missing half.

## What is actually needed

Per bid, one ruling: which copy is authoritative, and does the stray get deleted (the DSP26071.1
precedent) or kept as a labelled revision. **DSP26085 first** — it is the only pending one, and a
$6,180 ambiguity on a live bid is the one with a clock on it.

Worth considering as a follow-on, not decided here: the `Bids/ → Jobs/` move on award is what
creates most of these pairs, and nothing checks that the two copies match at the moment of the
move. The pre-send gate (`presend_gate.py`) reconciles a quotation against *a* workup — it cannot
know it was handed the wrong one, which is precisely why `backtest_workup.py` now needs a `prefer`
field to disambiguate DSP26085.
