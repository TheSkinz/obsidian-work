<!-- vault-loop: no home yet, candidate for [markdown-ranking-retest] -->
---
type: review
status: resolved
review_type: eval
source_authority: session
confidence: high
created: 2026-08-10
resolved: 2026-08-11
related:
  - "[[overview]]"
  - "[[2026-08-10-sharepoint-pilot-cleanup-owed]]"
tags: [copilot, sharepoint, eval, markdown]
---

# Markdown ranking retest — owed on the Furnace Decoking library

> **CLOSED 2026-08-11 — PASSED.** Both questions ran against the 21-file `Knowledge` library with `Decoking Knowledge` tagged in the M365 desktop app, and both passed all three citation criteria with no fabrication. Q1 cited `MANUAL-11` alone, beating `MANUAL-14` §14.6 — titled *"Approval gate before rig-out"*, a stronger surface match than §11.1 — which is body-content ranking over a title match. Q2 cited `MANUAL-04` §4.3 and `MANUAL-18` §18.1, reaching both halves without dropping either. Full result and the two supporting discriminators are in [[overview]]. The `.md` ruling stands, the converter contingency is closed, and tranche B plus the agent relocation are unblocked.
>
> One correction to the design below, recorded because it nearly misgraded the run: the rule and the rig-out gate are each stated in **four** chapters, so "governing chapter vs plausible neighbour" was under-specified. Q2's rule half landed on chapter 4, not the predicted chapter 9 — §4.3 is titled *Pig sizing derivation*, which is the better answer to a question asking how the figure is *determined*. Scored as a pass on the merits.
>
> Four earlier runs were voided because the agent was not tagged and the questions reached tenant-wide Copilot, which answered from a job SOP on OneDrive. That is filed as its own finding in [[overview]].

The last open risk in the SharePoint knowledge-base build. Everything else in tranche A is done and verified.

## What is actually unproven

Markdown is proven **reachable and citable** in this tenant: `TEST-A.md` and `TEST-B.docx` held byte-identical content apart from a calibration token, both indexed, and the M365 app cited the `.md` on a content query naming no file. That was n=2 with *identical* content, which proves retrieval works and proves nothing about ranking.

What is unproven is whether markdown **ranks** — whether, against a corpus of nineteen differing documents that all discuss one process, the right chapter surfaces rather than an arbitrary one. Tranche A is the sharpest available test of this precisely because the manual is homogeneous: nineteen chapters about mechanical decoking, competing directly with each other. This is why tranche B was held back — adding eight unrelated concept and context notes first would dilute the test.

## Timing — do not run it early

New documents on a site accessible to two or more users **index daily**; updates to already-indexed documents are immediate. Tranche A landed 2026-08-10. Run this **2026-08-11 or later**, from the **M365 desktop app** tagging `Decoking Knowledge` — the in-site SharePoint Copilot panel is unreliable for custom agents and will waste the run.

## The question to ask

Ask something several chapters could plausibly answer, where one is clearly correct:

> What has to be true before rig-out can start?

The gate before rig-out is chapter 11 (`11.1 Gate before rig-out`). Chapters 6, 8 and 10 are all plausible neighbours — safety and permit interface, rig-in, and completion criteria — so a model that is pattern-matching rather than ranking has somewhere to go wrong.

A second question worth running if the first is ambiguous:

> How is maximum pig OD determined, and where are the tube dimensions?

This should reach chapter 9 for the rule and chapter 18 for the reference table, and it tests whether the agent can pull two chapters that answer different halves.

## How to score it

Not pass/fail on the answer's correctness — the answer will probably be right either way. Score the **citations**:

1. Does it cite the *governing* chapter, or a plausible neighbour?
2. Are citations specific — one or two chapters — or scattered across many, which indicates weak ranking?
3. Does it silently drop a chapter it should have reached (the two-chapter question tests this)?

**Pass** → load tranche B (eight files, staged and ready in `_OUTPUTS/sharepoint/`), then author the Outlook routing document. **Fail** → convert tranche A to `.docx` before loading anything else, and reopen the converter ruling in [[overview]], which was reversed on the strength of the n=2 test.

Either way the result goes into [[overview]]. It closes the open risk this build has carried from the start.

## Two things gated behind this

- Moving `Decoking Knowledge.agent` out of the `Knowledge` library — deferred because that agent is the instrument this retest measures with. See [[2026-08-10-sharepoint-pilot-cleanup-owed]].
- Tranche B, including the decision on whether `01-context/workflow-map.md` belongs on the site at all. It describes itself as retired-system history with nothing live, so Copilot would answer from it as though it were current.
