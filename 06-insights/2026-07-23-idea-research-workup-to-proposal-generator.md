---
type: review
status: open
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-23
review_after: 2026-08-23
related:
  - [[idea-workup-to-proposal-generator]]
  - [[job-report-generator-build-spec]]
  - [[idea-job-report-generator]]
tags: [review, knowledge-system, idea-research, estimating, automation]
---

# Idea Research — Workup-to-Proposal Generator

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. Two idea-seeds were `unexplored` in `00-inbox/`: this one (`created: 2026-07-19`) and `idea-lint-lock-heater-schema` (`created: 2026-07-20`). This seed is oldest by frontmatter date and is picked per the loop's oldest-first rule.

## Evidence

**Internal — the seed's own load-bearing fork is still unresolved, by the vault's own authoritative source.** The seed's "To explore" section names one fork that "decides feasibility": whether the work-up Excel has a stable structure across bids. `~/.claude/skills/usadebusk-estimating/SKILL.md` (the single source of truth for estimating workflow) answers this directly, as of today: *"Excel workup template is a work in progress. Explain estimating logic from this skill... do not attempt to replicate the Excel workup structure until the template is documented here."* That line has not changed since the seed was captured four days ago (`change-log.md` 2026-07-19 entry records the same open question at the seed's origin: "its feasibility hinges on an unconfirmed fact"). The fork is exactly as open today as it was at capture — no vault activity in the intervening four days has touched it.

**Internal — this is the mirror-image finding of the job-report-generator's green light.** `job-report-generator-build-spec.md` (built and shipped 2026-07-21) explicitly called out that its own feasibility rested on "ticket-breakdown xlsx is the same template every job... one mapping-spec covers all jobs — the high-feasibility branch. This is the green light." That spec also names this idea directly as the convergent sibling ("Convergence note," `idea-workup-to-proposal-generator.md`), proposing a shared structured-source-to-branded-docx render core with separate mapping front-ends, but is explicit that **each transfer step must be proven against its own back-test before merging render cores** — it does not assume the workup side is equally ready.

**Internal — no back-test corpus is visible from inside the vault.** The seed names "DSP26080's pair" as one candidate back-test (a work-up paired with its submitted proposal). Checking `02-facilities/HF-Sinclair/Artesia-NM/DSP26080.md`: its `source:` field points to a single `.docx` quote file — no Excel work-up is referenced or present alongside it. Checked P66's `DSP26030-H28-H29-Decoke-Proposal-May2026.md` as well: same pattern, sourced from a `.pdf`/`.docx`, no paired `.xlsx`. The 2026-07-22 config audit (`change-log.md` entry, that date) recorded that **"SharePoint is canonical for all job docs and proposal workups; OneDrive per-facility folders are working copies"** — meaning the actual work-up Excel files live outside anything the vault currently ingests or indexes. Neither the structure question nor the back-test-pair question can be resolved by reading vault content; both require Jesse to open SharePoint/OneDrive and look, or answer directly, exactly as the seed's own "To explore" already anticipated ("this is the fork... and should be asked directly rather than guessed").

**External — the automation mechanics are a solved, low-risk problem once a mapping exists.** Excel-to-Word document generation from a fixed template is mature, well-trodden practice: `docxtpl` (Jinja2-style placeholders in a `.docx` template, populated from pandas/openpyxl-read Excel data) and `docx-mailmerge` are the two most common Python approaches, both used specifically for proposal/report generation ("populate a Word template with data pulled from Excel via Python" — pbpython.com, selfboot.cn). This matches the render core already proven in this vault's own job-report generator (python-docx / the `docx` skill). The rendering half of this idea is not the risk; **the risk is entirely on the input side** — whether there is one stable Excel structure to map from, or a family of ad hoc work-ups that reshape per job (the seed's own "harder, family-by-family problem" branch).

## Interpretation

**Premature, not infeasible — and the seed already knew this.** Every question this research could answer from inside the vault comes back to the same unresolved fork the seed itself flagged at capture: is the work-up Excel one stable template (like the ticket-breakdown xlsx that made the job-report generator a green light) or does it reshape per job? Four days after capture, the authoritative skill file still marks the workup template "a work in progress" and explicitly warns against assuming its structure. No vault-visible evidence moves this needle either way — the deciding artifacts (the actual work-up `.xlsx` files) live in SharePoint/OneDrive, outside what this loop or the vault currently ingests. This is not a case where research can substitute for asking; it is the specific case the loop spec (and the seed itself) anticipated by naming the question to "ask directly rather than guess." Proceeding to a build spec now would repeat the mistake the job-report spec was careful to avoid — assuming stability on the input side without checking it project-by-project first.

## Recommended Action

**Do not build or spec yet. Resolve the fork with Jesse directly, in under five minutes, next time he's answering vault questions:** (1) Is the work-up Excel one template across recent bids, or does it get reshaped per job/facility? (2) Can 2-3 recent work-ups be pulled from SharePoint and paired with their submitted Word/PDF proposals to form a back-test set (DSP26080 is not usable as-is — no `.xlsx` is present in its vault record, so a real pair would need to come from SharePoint directly)? If the answer is "one stable template," this converges immediately with `job-report-generator-build-spec.md`'s architecture (shared render core, separate mapping front-end) and is ready for a build-spec session. If it reshapes per job, this is a materially bigger, lower-ROI problem than the seed assumed and should be re-scoped or parked. Leave the idea-seed `unexplored → researched` with this note attached; do not mark it ready-to-build until the fork is answered.

## Decision

- [ ] Approved — ask Jesse the two fork questions next session, proceed to build-spec if template is stable
- [ ] Approved with edits
- [ ] Park — revisit at a later checkpoint
- [ ] Drop

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| | | | |
