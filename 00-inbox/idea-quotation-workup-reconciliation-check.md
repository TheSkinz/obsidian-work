---
type: idea-seed
status: gated
created: 2026-07-25
tags: [idea, estimating, data-quality, audit, future]
related:
  - "[[2026-07-27-idea-research-quotation-workup-reconciliation-check]]"
---

# Standing quotation-vs-workup reconciliation check

> **Queued as a build 2026-08-15** (Jesse, retirement sweep) — DQ-015. **This came into the sweep as a retirement candidate and came out load-bearing.**
>
> The seed reads like something to close: its own text records that the one-off scan found no customer-facing defect, and argues against a calendar-driven sweep. But since it was written, **two other decisions quietly deferred work to the gate it describes, and the gate does not exist.** DQ-010 (2026-08-15) rejected value reconciliation in lint and in the health dashboard's `Bid folder` column, deferring it to "the pre-send gate, which reads the workup's reconciled total instead of guessing from filenames." `50-dashboards/health.md` now states the same on its face: "Value reconciliation is out of scope here and belongs to the quotation-vs-workup pre-send gate." Retiring this seed would have left both pointing at nothing, and neither would have said so.
>
> **The trigger question the seed left open is answered by that dependency.** Not a calendar sweep, and not a run after every script edit — a **pre-send gate on the single quotation/workup pair being submitted**. That is the cheapest shape, it catches the error where it matters, and it is the shape DQ-010 already assumed. The seed's own analysis reached the same place ("at bid submission as a pre-send gate on a single pair, which is cheaper and catches the error where it matters"); what it lacked was a reason to prefer it, and DQ-010 supplied one.
>
> Build constraints carried forward from the seed, unchanged: exclude mob/demob per the contract-cap rule, sum **all** pricing blocks on multi-truck jobs (one page can hold two), and allow legitimate scope narrowing — DSP26026's workup is scoped wider than its quotation and that is not an error.

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
