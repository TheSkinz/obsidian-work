---
type: idea-seed
status: researched
created: 2026-07-11
related:
  - [[2026-07-18-idea-research-job-sheet-type-formalization]]
tags: [idea, vault-system, future, job-sheet]
---

# Formalize the "job sheet" document type (template + render pipeline)

Idea seed captured 2026-07-11 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** The USA26038 session created a genuinely new artifact type — `type: job-sheet` — that the vault has no schema home for. A job sheet is static (created at bid-win from the quoted work-up), crew-facing, and printable: project details, rig/shift crew assignment, per-heater work-up billing tables (for keying service receipts), compact coil-data, and carry-forward notes from the prior decoke. It is distinct from a heater card (persistent physical facts + accumulated actuals) and a job report (post-job timeline + actuals). It currently exists as a one-off at `02-facilities/HF-Sinclair/Artesia-NM/USA26038-job-sheet.{md,html,pdf}` with no template and no tooling. Every won bid produces one of these, so it should be formalized the way heater cards were (`_canonical-heater-card.md` + `_heater-template.md`).

**To explore:**
- A `templates/_job-sheet-template.md` markdown template, and the companion HTML skeleton used to render the printable PDF (the USA26038 HTML is the working prototype — light header, gold accent, fixed-width tables, per-heater billing blocks side-by-side).
- Whether a `tools/` render script (headless-Chromium HTML→PDF, as done manually this session) is worth adding so the pipeline isn't rebuilt from session context each time.
- Where job sheets live long-term (facility folder alongside heater cards worked, but confirm) and naming convention (`<JOB#>-job-sheet`).
- How much of the billing-table math should be generated vs. hand-entered (see companion capture note on the work-up billing conventions).
