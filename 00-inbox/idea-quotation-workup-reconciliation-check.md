---
type: idea-seed
status: researched
created: 2026-07-25
tags: [idea, estimating, data-quality, audit, future]
related:
  - "[[2026-07-27-idea-research-quotation-workup-reconciliation-check]]"
---

# Standing quotation-vs-workup reconciliation check

Idea seed captured 2026-07-25 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** The 2026-07-25 scan reconciled every DSP#-era quotation against its workup by hand
(see [[2026-07-25-quotation-workup-reconciliation-scan]]). It found no new customer-facing defect across
Formosa, Marathon and HF Sinclair — but it did surface a broken regression suite, a canonical-store rule
that was false in practice, and a latent crash in the generator. The check may be worth having as a
standing one rather than a one-off, since `extract_workup.extract()` already does the hard half and the
remaining work is parsing a rendered pricing block and diffing totals.

**To explore:** Is a recurring check actually warranted, given the one-off found nothing customer-facing?
The honest read is that its value was in auditing the *system*, not the artifacts — which argues for
running it after a change to the generator or the store, not on a calendar. What is the right trigger?
Candidates: after any `usadebusk-estimating` script edit (mirroring the fixture-replay argument in
[[2026-07-24-fixtures-work-better-as-rule-audit]]), or at bid submission as a pre-send gate on a single
pair, which is cheaper and catches the error where it matters. Also unresolved: the check must exclude
mob/demob per the contract-cap rule, must sum *all* pricing blocks on multi-truck jobs (one page can hold
two), and needs a rule for legitimate scope narrowing — DSP26026's workup is scoped wider than its
quotation and that is not an error. Rendering docx→PDF via LibreOffice is the slow step and needs a
per-file wait; a text-extractable path would be better if one exists.

**Gate:** Do not build a scheduled sweep before deciding the trigger question above — a calendar-driven
version was already the wrong shape once for the regression battery.
