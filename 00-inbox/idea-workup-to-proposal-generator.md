---
type: idea-seed
status: spec-complete
created: 2026-07-19
related:
  - [[2026-07-23-idea-research-workup-to-proposal-generator]]
  - [[workup-to-proposal-generator-build-spec]]
tags: [idea, estimating, automation, cross-cutting]
---

# Workup-to-proposal generator

Idea seed captured 2026-07-19 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** Jesse builds every estimate in an Excel work-up tool, then hand-types the numbers into a Word doc and converts it to PDF for the customer-facing proposal — on every bid, regardless of facility. That manual transcription step is the actual recurring friction (surfaced when a "duration model" recommendation was checked against how estimates are really produced), and it's also where a transposition error could enter a six-figure quote. A generator that takes the finished Excel work-up and produces the Word proposal directly — using the existing 14-section structure and branding already defined in `usadebusk-estimating` — would remove that step from every future bid, not just one facility's.

**Convergence note (added 2026-07-21, from the job-report-generator exploration):** these two
ideas share an inheritance pattern, not one engine. Jesse's document-lineage model — heater
drawings → heater card → quote → job sheet → job report — makes each generator a *transfer step*
between adjacent documents. Recommended shape: a shared "structured-source → branded-docx" render
core + shared brand/layout library, with **separate mapping front-ends** (this one = quote /
heater-card → proposal; the other = job sheet + actuals → job report). Prove each transfer step
against its own back-test before merging the render cores. See [[job-report-generator-build-spec]]
and [[idea-job-report-generator]].

**To explore:** Whether the work-up Excel has a stable structure across bids (clean 1-session mapping-spec build) or gets reshaped per job (harder, family-by-family problem) — this is the fork that decides feasibility and should be asked directly rather than guessed. What the actual cell-to-proposal-line mapping is, including the transforms Jesse currently does mentally (lump-sum vs T&M lines, third-party markup handling, multi-heater quotes). Whether a small back-test set exists: 2-3 recent work-ups paired with their actually-submitted Word/PDF proposals (DSP26080's pair is one candidate) to prove the generator reproduces the real document before it touches a live bid. Whether this is a Fable-authored mapping spec once, then Sonnet/Codex-operated forever, or needs recurring frontier involvement.
