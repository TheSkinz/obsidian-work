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

**Closed 2026-07-23 (same day):** Jesse moved [[DSP26080]]'s folder into the canonical store himself — `…\USADeBusk\Facilities\HF Sinclair-Navajo Artesia NM\Jobs\DSP#26080 HFSinclair Navajo Refinery — 3 Heaters (H-2421, H-30, H-2501)\` — and the note was re-pointed and verified. All four pointers from this incident are now on the canonical tree.

**Follow-up same day:** the estate was still moving live during the first pass — DSP25084's originally-recorded subfolder got archived to a `.zip` mid-session, so my first re-point died again within minutes. Re-verified against the job root directly (files live loose in `USA26022 PS8 F-802 2026-05\`, not a subfolder) — fixed. DSP26039 and DSP26058's recorded paths held up under a second check (no edit needed). [[H-2501]] carried the same stale-`Desktop\` pattern as DSP26080 in its body prose (not a quote note, so it wasn't in the original POINTER-DEAD scope, but same root cause) — re-pointed to the canonical Sinclair tree. `vault_lint.py` now reads 0 POINTER-DEAD across the vault.
