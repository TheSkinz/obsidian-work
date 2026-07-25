---
type: capture
status: resolved
created: 2026-07-24
resolved: 2026-07-25
tags: [capture, estimating, proposal, data-quality, exxon-baytown]
---

# DSP26085 carried a stale quote number in its pricing block — not submitted, fixed 2026-07-25

> [!warning] Correction 2026-07-25. The original note below asserted this was a **submitted**
> proposal in ExxonMobil's hands. Jesse: **that version was never sent to the customer.** There
> is no external exposure and no reissue. The note's title and framing were wrong; the underlying
> defect was real and is now fixed.

**What was actually wrong.** `DSP#26085_Exxon Baytown_27GF1A F-201_2027 Jan Quotation.docx`
carried `Quotation #: DSP#:26000` in its Section-7 pricing block while the live workup's
`Insert Quote` tab (cell E5) resolved correctly to `DSP#:26085`. The block is a pasted
Enhanced Metafile — a static vector paste, not a linked OLE object — so it froze whatever the
cell read at copy time and never followed the workup.

The `26000` did not come from a real bid. There is a `DSP#26000_Exxon Baytown_CLEU2-F3_2027 Jan.docx`
draft in the CLEU2-F3 Jobs folder, but per Jesse **that was not the actual workup** for 26061 —
it was a placeholder-numbered draft. The paste's lineage traces to that draft state, not to any
issued quotation.

**Fix applied 2026-07-25.** Rather than re-pasting from Excel and risking a re-render, the ten
bytes were patched inside `word/media/image6.emf`: `26000` → `26085`, same string length, and the
font's digits are tabular (all five advance width 8), so nothing reflowed. A page-by-page text
diff of the before/after PDF renders across all 17 pages returns exactly one changed line. Total
holds at $40,477.08, matching the workup. The corrected file was promoted over the original in
the Bids folder with Jesse's explicit go-ahead; OneDrive version history retains the prior copy.

**Estate scan, same session.** All 13 Exxon Baytown DSP#-era quotations were rendered and their
pricing-block quote numbers compared against their filenames. Eleven clean (26005 ×2, 26015,
26039, 26061 ×3, 26071.2 ×2, 25070, 25084 Rev 1, 25084 Rev 2).

**One further mismatch — worse than it first looked, resolved by deletion.**
`Jobs\Exxon Baytown_HU5-F501 Heater_2026 Aug\Submit\DSP#26071.1_...Rev001.docx` showed
`DSP#:26071.2` under the Rev001 filename. The first read was "wrong number, same byte-patch fix."
That was wrong. Comparing pricing blocks showed the docx carried **Rev002's entire quotation**:

| | Genuine Rev001 (native PDF) | The docx named Rev001 | Rev002 |
|---|---|---|---|
| Quote # | DSP#:26071.1 | DSP#:26071.2 | DSP#:26071.2 |
| Decoke line | $71,120.00 | $40,280.00 | $40,280.00 |
| Hours | 48 Pig / 16 Smart Pig | 24 / 8 | 24 / 8 |
| Total | **$98,134.26** | **$60,287.42** | **$60,287.42** |

Patching the number would have manufactured a document labeled Rev001 showing Rev002's total —
wrong by $37,846.84 and carrying the authority of a source file. The two docx files are not
byte-identical (5.22 MB vs 5.39 MB), so this was a working copy that received Rev002's paste
before the Save-As, not a duplicate: **no Rev001 docx source survives.** The authoritative Rev001
record is the native PDF, which is correct and is what the customer received. Jesse's call
2026-07-25: delete. Sent to the Recycle Bin (recoverable; session backup also in scratchpad).

**Durable lesson — bigger than a wrong quote number.** The pricing block is a static metafile
paste, so it silently decouples from the workup the moment either changes. DSP26071.1 shows the
severe form: an entire pricing block migrated between revisions undetected, and the only reason
it was caught is that the quote number happened to travel with it. **A paste carrying the wrong
amounts under the right number would leave no signal at all.** Number-vs-filename checking is
therefore not a sufficient audit; totals have to be reconciled against the workup. This is the
class of error the workup-to-proposal generator eliminates by reading the live workup at render
time — a concrete proof-point for the build, already noted in the spec banner.

Related: [[workup-to-proposal-generator-build-spec]].
