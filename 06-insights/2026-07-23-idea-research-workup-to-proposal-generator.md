---
type: review
status: resolved
review_type: idea-research
source_authority: confirmed
confidence: high
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

## Recommended Action (superseded — see Follow-Up below)

~~Do not build or spec yet. Resolve the fork with Jesse directly, in under five minutes, next time he's answering vault questions: (1) Is the work-up Excel one template across recent bids, or does it get reshaped per job/facility? (2) Can 2-3 recent work-ups be pulled from SharePoint and paired with their submitted Word/PDF proposals to form a back-test set (DSP26080 is not usable as-is — no `.xlsx` is present in its vault record, so a real pair would need to come from SharePoint directly)?~~

## Follow-Up — 2026-07-23, same day, Jesse answered directly

Jesse: "The work ups are stable, but the data may be considered unorganized. but yes, we can back test them and even improve the structure of the current template if it warrants it."

This resolved the fork immediately, and a direct filesystem check of `C:\Users\Jwuts\OneDrive\Desktop\Facilities\` (the local OneDrive working-copy tree the 2026-07-22 audit already identified) confirmed it with real data — the original research above was correct that no back-test corpus was *vault*-visible, but one exists in full in the local file estate, just outside what the vault ingests:

- **Structure is stable across facilities, confirmed by direct inspection of 4 real workups** (HF Sinclair DSP26080, Exxon Baytown DSP26071.2 and DSP26085, Formosa Point Comfort DSP26068.1): all four share the same tab set and roles — `Insert Quote`, a heater tab (consistently `...GC197` in dimension), `Pricing Table`, `Execution`, `Heater Data`. Same shape, three different clients, three different heaters/scopes.
- **"Unorganized" matches a real, already-diagnosed problem**, not a vague impression: `Workup-Template-v1-design.md` (dated 2026-07-19, present in the same OneDrive tree, unknown to the vault) reverse-engineered the old exemplar (`DSP#26071.2`) cell-by-cell and documented exactly the mess Jesse is describing — cost rates hardcoded inside each heater block instead of a master table, duplicate rate tables (`D` vs `I` columns), implicit equipment-hour rules, a cramped mob-resource area. A **v1 redesign already exists** (`Workup-Template-v1.xlsx`, same date) addressing these, validated against one sample job, currently scoped to 1 heater / 1 mobilization only (multi-heater and quote tabs deferred). Neither file is referenced anywhere in the vault or in `usadebusk-estimating/SKILL.md` — real progress on this exact problem happened outside the system of record.
- **A full back-test pair exists on disk and was exercised end-to-end, not just inspected.** `DSP#26071.2`'s workup (`Full Conv+TG+ Rad` tab, Project Financials block `H1:K8`) and its submitted quotation (PDF, page 6) sit side by side in the same `Submit` folder. Read both: workup `Total: $60,287.42` / cost `$27,455.76` (54.46% margin) against the submitted Quotation page's printed total **$60,287.42** — exact match, and every line item matches 1:1 (Mob $3,558.72 → lump-sum mobilize line; Equip $40,280.00 → the mechanical-decoke line; Labor $8,502.48 + Per Diem $1,800 combined to $10,302.48 → the "Labor & Per Diem" line; Materials $2,587.50 → DEF & pigs line; Demob $3,558.72 → lump-sum demobilize line). The header block (`B2:C8`: date, quote #, type, facility, address, bid/scope) also maps directly onto the proposal's cover page and Requested-Service section. This is a complete, exact reproduction of one real proposal's commercial content from its workup — the same standard of proof the job-report generator's USA26038 back-test met.
- Two more matched pairs sit ready in the same tree for a second and third back-test if needed: `DSP26085` (Baytown F-201) and `DSP26068.1` (Formosa VR-401G), each with workup + submitted Quotation docx/pdf in the same folder.

**Revised Interpretation: feasible, not premature — back-tested and proven on one real pair, corpus for more exists.** The only remaining open question is which source to build the mapping spec against: the messy-but-proven old-style workup (4 confirmed live instances, exact back-test match) vs. the cleaner but unfinished, single-heater-only `Workup-Template-v1`. Recommend building the mapping spec against the **old-style workup as it exists today** (proven, multi-heater, in active use) and treating `Workup-Template-v1` as a parallel track Jesse can finish or fold in later if he wants the input side cleaned up too — don't block the generator on a template rewrite that isn't finished.

## Recommended Action

Ready for a build-spec session, mirroring `job-report-generator-build-spec.md`'s shape: shared structured-source → branded-docx render core (reuse the `docx` skill / python-docx approach already proven), separate mapping front-end for `workup xlsx → proposal docx`. Suggested next step: a dedicated session to (1) write the full cell-region mapping spec (using the already-documented region map in `Workup-Template-v1-design.md` as the starting reference for cell locations), (2) back-test against the two additional pairs (`DSP26085`, `DSP26068.1`) to confirm the mapping generalizes past one instance, (3) decide the `Workup-Template-v1` question above. Not started yet — this note stops at proof-of-concept, per the idea-research loop's boundary against building or scaffolding the idea itself.

## Decision

- [x] **Approved — back-tested and proven 2026-07-23 (Jesse); proceed to a build-spec session** — Jesse confirmed workups are stable (unorganized internally, not structurally unstable) and greenlit back-testing plus template improvement if warranted.
- [ ] Approved with edits
- [ ] Park — revisit at a later checkpoint
- [ ] Drop

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-07-23 | Follow-up back-test run same day | Claude | Found `Workup-Template-v1.xlsx` + design note (2026-07-19, local OneDrive, not in vault) documenting the exact "unorganized" problem Jesse named. Confirmed structural stability across 4 real workups (HF Sinclair, Baytown ×2, Formosa). Exact-match back-test: DSP#26071.2 workup Total $60,287.42 reproduces the submitted Quotation's printed total and every line item 1:1. Two more matched pairs identified (DSP26085, DSP26068.1) for a second back-test. No build started; recommends a dedicated build-spec session next. |
