---
type: task
status: resolved
created: 2026-07-23
tags: [pointer-dead, source-files, estate-hygiene]
---

# Three dead source-file pointers — RESOLVED

Surfaced 2026-07-23 by the new POINTER-DEAD lint rule (built this session — see [[2026-07-23-triage-vault-architecture-first-principles]]). The OneDrive estate reorg had broken four recorded bid trails; DSP26080 was re-pointed first, then these three.

**Resolved 2026-07-23.** Jesse identified the real store: the vault had recorded `Desktop\…` working-copy paths, but the reliably-present tree is `C:\Users\Jwuts\OneDrive\USADeBusk\Facilities\<Client City ST>\{Bids,Jobs,Reference,_History}\`. All three quote files were found there with exact-match names and re-pointed against verified paths; POINTER-DEAD now reads 0. The durable finding (canonical store location + structure) is recorded in [[rfq-intake-protocol]] step 1, its permanent home.

| Quote note | Re-pointed to (verified) |
|---|---|
| [[DSP25084]] | `…\USADeBusk\Facilities\ExxonMobil Baytown TX\Jobs\USA26022 PS8 F-802 2026-05\Exxon Baytown PS8 F-802\` (quote now `.docx`/`.xlsx`; the `AM4411442151.pdf` earlier flagged was a PO copy, not the quote) |
| [[DSP26039]] | `…\USADeBusk\Facilities\ExxonMobil Baytown TX\Jobs\Exxon Baytown_HU9-F301_371\ExxonMobil Baytown HU9 Unit\Quote & Workup\` (path tail identical to the old record — only the root moved off `Desktop\`) |
| [[DSP26058]] | `…\USADeBusk\Facilities\Marathon Garyville LA\_History\Marathon Garyville_1Q2027 TAR\1Q27 Pigging Docs\Submit\` |

**One caveat left for Jesse:** [[DSP26080]] still points at a `Desktop\Facilities\…` working copy — it resolves today (not dead) but was **not** found in the `USADeBusk\Facilities\` canonical tree, so it's the one pointer still on the fragile root. Move its folder into the canonical store and re-point when convenient, or it will be the next to go dead. (Its folder name also carries the U+00A0 trailing-space gotcha, already handled in-note.)
