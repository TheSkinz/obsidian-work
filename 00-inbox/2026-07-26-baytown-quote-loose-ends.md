<!-- vault-loop: operational — Baytown quote-note field backfill and rate-basis reconciliation (02-facilities scope). Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
<!-- vault-prestaged: skipped — execution correction, needs doing not deciding. Confirmed DSP24005.md, DSP26058.md and DSP26030_H28_H29.md still carry no contract-type field (checked 2026-08-02). Both items are read-the-source-doc-and-fill-the-field / check-the-contract tasks with no open question for Jesse to weigh, not decisions. -->
---
type: note
status: open
created: 2026-07-26
tags: [loose-end, estimating, ExxonMobil, quotes]
---

# Loose ends from the F-901 session — Baytown quotes

Two items left open on 2026-07-26. Neither blocks anything; both are cheap to close the next
time the relevant file is open, and both go stale if nobody writes them down.

**1. `contract-type` still blank on three quote notes.** The `contract-type` / `rate-basis` /
`billing-basis` fields were adopted 2026-07-19 ([[2026-07-19-rate-model-grain-review]]
proposal D) and backfilled this session only where a source document actually states the
answer — [[DSP25084]] (`short-form scope contract`), [[DSP25123]] (`spot PO`, taken verbatim
from the ExxonMobil PO's own `Lump Sum, T&M, or Spot:` field), and [[DSP26039]]
(`contract-type` deliberately left blank, bid instructions not at hand).

Still empty: **DSP24005** (CHS), **DSP26030** (P66), **DSP26058** (Marathon). Each needs its
bid instructions read — per the spec, a blank beats a guess, so do not infer them from the
quote body. These fields are what any future rate-history rollup would segment on; without
them it can compare rates but not explain them.

**2. 4×3 pump billing basis is unreconciled at Baytown.** [[DSP25084]] and [[DSP25123]] bill
it at **$1,016/shift**; [[DSP26039]], submitted one day after DSP25123, bills it at
**$85/hr**. That is a change of *basis*, not just of rate, so it is not the same class of
thing as a competitive rate cut. Check which basis the governing contract uses before pricing
a 4×3 on the next Baytown bid. Recorded in the Rate History table on
`02-facilities/ExxonMobil/Baytown-TX/_facility.md`.
