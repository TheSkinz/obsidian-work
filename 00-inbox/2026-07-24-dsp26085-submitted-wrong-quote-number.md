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
26039, 26061 ×3, 26071.2 ×2, 25070, 25084 Rev 1, 25084 Rev 2). One further mismatch found and
**not yet fixed**: `Jobs\Exxon Baytown_HU5-F501 Heater_2026 Aug\Submit\DSP#26071.1_...Rev001.docx`
carries `DSP#:26071.2` under the Rev001 filename. The submitted PDF of that name reads `26071.1`
correctly, so the customer copy is right — the working docx no longer matches its own PDF. Same
byte-patch fix available.

**Durable lesson.** The pricing block is a static metafile paste in every proposal built this way,
so it silently decouples from the workup the moment either changes. This is the exact class of
error the workup-to-proposal generator eliminates by reading the live workup at render time — a
concrete proof-point for the build, already noted in the spec banner. No tool change needed.

Related: [[workup-to-proposal-generator-build-spec]].
