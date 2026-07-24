---
type: capture
status: inbox
created: 2026-07-24
tags: [capture, estimating, proposal, data-quality, exxon-baytown]
---

# Submitted DSP26085 quotation shows the wrong quote number ("DSP#:26000") in its pricing image

Found while back-testing the workup-to-proposal generator against the submitted proposals. The
submitted **DSP26085** proposal (Exxon Baytown, 27GF1A F-201, Jan 2027) carries its Section-7
pricing as a **pasted Excel image** in the Word doc. That image shows `Quotation #: DSP#:26000` —
a stale placeholder value frozen into the screenshot — while the live workup's `Insert Quote` tab
resolves the same cell to the correct `DSP#:26085`.

Source read: rendered the submitted `DSP#26085_...2027 Jan Quotation.docx` → PDF via `soffice.exe`
and read the pricing page; the header block clearly reads `DSP#:26000`. Everything else on the page
(totals, line items, Pricing Summary box) is correct — only the quotation number is wrong.

Two things worth deciding:
1. **Does the already-submitted DSP26085 need a correction to ExxonMobil?** It went out with the
   wrong quote number on the pricing page. May cause PO/matching confusion on their side. Jesse's
   call whether to reissue or let it ride.
2. This is the **exact class of stale-paste error the new generator eliminates** — reading from the
   live workup emits `26085`. Good concrete proof-point; already noted in the build-spec banner. No
   tool change needed.

Related: [[workup-to-proposal-generator-build-spec]].
