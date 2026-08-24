---
type: review
status: resolved
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-18
review_after: 2026-08-18
related:
  - [[2026-07-11-job-sheet-type-formalization]]
  - [[vault-idea-loop-spec]]
  - [[_canonical-heater-card]]
tags: [review, knowledge-system, idea-research, job-sheet, estimating]
---

# Idea Research — Job-Sheet Type Formalization

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. `2026-07-11-job-sheet-type-formalization` was the only `unexplored` idea-seed in `00-inbox/` — the other three inbox idea-seeds are already `researched`, `complete`, or `approved-blocked`. The seed proposes formalizing the `job-sheet` document type (currently a one-off at `02-facilities/HF-Sinclair/Artesia-NM/USA26038-job-sheet.{md,html,pdf}`) the same way heater cards were formalized: a canonical exemplar plus a derived template, and possibly a render script for the markdown-to-PDF pipeline.

## Evidence

**Internal — confirmed no existing coverage; confirmed the proven in-vault pattern to extend.** Searched `04-knowledge/`, `templates/`, `06-insights/`, and all seven deployed skills (`~/.claude/skills/`) for "job sheet," "job-sheet," "billing table," and "work-up" — zero hits outside the USA26038 files themselves. The vault's schema-authority pattern (`04-knowledge/_canonical-heater-card.md` as exemplar → `templates/_heater-template.md` derived from it, per root `CLAUDE.md`) is the only precedent, and it's a good fit: `USA26038-job-sheet.md` already has a clean, stable section shape (Project Details, Crew Assignment, Billing Reference by heater, Coil Data, Carry-Forward Notes) that reads as ready to lift into a template with minimal rework. The companion capture note `2026-07-11-three-document-model-and-billing-math.md` (still sitting in `00-inbox/` as an unrouted `type: capture`, destination `04-knowledge/`) already contains the billing-math rules a template's field-generation logic would need — worth routing together if this idea is picked up, since building the template without it would re-derive rules that are already written down.

**External — the render-pipeline half of the idea is a solved, low-effort problem; the document-content half is a mature but heavier-weight category that doesn't fit this use case.** For markdown→HTML→PDF rendering (the seed's "worth adding a tools/ render script" question), headless-Chromium pipelines are a standard, well-documented pattern: [md-to-pdf](https://github.com/simonhaenisch/md-to-pdf) is a small Node CLI that renders markdown to HTML via markdown-it, applies CSS, and prints via Puppeteer/headless Chrome — functionally identical to what was done manually for USA26038 this session, just scripted. [Gotenberg](https://gotenberg.dev/docs/convert-with-chromium/convert-markdown-to-pdf) does the same via an HTTP API against an HTML template. A pure-Rust alternative, [ironpress](https://rexai.top/en/languages/rust/2026-04-25-pure-rust-html-to-pdf-engine/), skips the browser process entirely for faster cold starts, though it's newer and less battle-tested. Any of these would replace the manual "render HTML, screenshot/print to PDF" step with a one-line `tools/render_job_sheet.py`-style script, consistent with the vault's existing `tools/` scripts pattern (`vault_lint.py`, `vault_health.py`, `vault_index.py`). For the document-content half, the closest external category is field-service work-order/job-ticket tooling — [BuildOps' work order templates](https://buildops.com/resources/service-work-order-template/), [Zentive's work order generator](https://zentive.io/tools/work-order-template/), and open-source field-service platforms (OCA Field Service, ERPNext, LibreWO) all converge on the same core fields the seed already identified independently: crew/technician assignment, per-job billing line items, scope/materials. That convergence is a validation signal, not a build option — these are multi-technician dispatch SaaS/ERP systems sized for businesses managing many concurrent field crews across many customers, which is a different problem shape than one operator maintaining a handful of markdown job sheets per bid-won job in a personal vault. No open-source tool found does "markdown template + lightweight PDF render" at USADeBusk's scale; adopting one would mean absorbing a platform, not a template.

## Interpretation

**Sound — this is a genuine formalization gap, not a trap or premature idea.** Three things point away from "trap": (1) the artifact already exists and works (USA26038's job sheet was used for a real job this month), so this isn't speculative infrastructure ahead of need; (2) the pattern to follow (canonical exemplar → derived template) is already proven in-vault for heater cards, so there's no novel design risk; (3) every "every won bid produces one of these" claim in the seed is verifiable and true given the vault's own workflow docs. The one open design question — how much of the billing-table math should be generated vs. hand-entered — is already partially answered by the sibling capture note's billing-math rules, so a build session wouldn't be starting from zero. The render-pipeline sub-question has a clear, low-effort external answer (headless-Chromium scripting is a solved pattern); the heavier field-service-SaaS category is a false lead and should be explicitly ruled out rather than explored further.

## Recommended Action

Bounded one-shot investigation/build, not urgent enough to jump the queue but low-risk when picked up: (1) promote `USA26038-job-sheet.md` into `04-knowledge/_canonical-job-sheet.md` (schema authority, mirroring `_canonical-heater-card.md`) and derive `templates/_job-sheet-template.md` from it; (2) route the `2026-07-11-three-document-model-and-billing-math.md` capture note's billing rules into the same session so the template's generation logic isn't re-derived; (3) skip evaluating field-service SaaS/ERP tooling — ruled out by scale mismatch; (4) if the manual HTML→PDF step is still a friction point by the time this is picked up, a small `tools/render_job_sheet.py` wrapping a headless-Chromium markdown-to-PDF library (Puppeteer-based, matching `md-to-pdf`'s approach) is a low-effort addition, not a separate project. This is `04-knowledge/`-canonical content, so per the Idea Research Loop's own boundaries it stays out of this loop's write scope regardless of disposition — the actual build is a session for the on-demand Agent-Review/build workflow, gated on Jesse's decision below.

## Decision

- [x] Build now — canonical + template, routed with the billing-math capture note
- [ ] Bounded one-shot investigation first (confirm template shape with Jesse before writing canonical)
- [ ] Park — revisit at the next won bid
- [ ] Drop

Jesse, 2026-07-18: "Build now."

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-07-18 | Created `04-knowledge/_canonical-job-sheet.md` | Claude (Opus 4.8) | Schema authority, derived from USA26038. Carries the work-up billing math as authoritative field-generation rules. Marked DRAFT — validated against one instance only. |
| 2026-07-18 | Created `templates/_job-sheet-template.md` | Claude (Opus 4.8) | Derived from the exemplar; annotations reduced to the failure-prone rules (combined man-hours, per-diem PM exclusion, conditional Filter Unit / Carry-Forward sections). |
| 2026-07-18 | Routed `00-inbox/2026-07-11-three-document-model-and-billing-math.md` | Claude (Opus 4.8) | Three-document model → `concepts/quote-lifecycle.md` (+ job-sheet creation step at award); billing math → the canonical. Capture note set `status: complete`, retained as origin record. |
| 2026-07-18 | Render script NOT built | Claude (Opus 4.8) | Out of the approved scope and gated on real friction per this note's recommendation. Deferral documented in the canonical's closing comment. |
