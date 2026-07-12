---
type: review
status: open
review_type: skill-drift
source_authority: primary
confidence: high
created: 2026-07-12
review_after: 2026-08-12
related:
  - "[[vault-skill-drift-loop-spec]]"
  - "[[2026-07-11-three-document-model-and-billing-math]]"
  - "[[2026-07-11-job-sheet-type-formalization]]"
  - "[[estimating-actuals-rollup]]"
tags: [review, skill-drift, skills, knowledge-system]
---

# Skill-Drift Review — 2026-07 (First Run)

## Trigger

First run of the Vault Skill-Drift Loop (previously `pending` on the health dashboard), executed manually from a remote session per Jesse's request, against a fresh clone of `claude-config` (`main` @ `6a82ab7`). No prior `skill-drift:` heartbeat exists, so the comparison window is the whole current state of both repos rather than a date-bounded delta. Every SKILL.md and reference file was read in full, alongside `04-knowledge/`, `06-insights/`, `07-llms/`, `08-systems/`, the actuals rollup, both CLAUDE.md files, and the 2026-07-11 inbox captures.

**Proposal branches:** `drift/2026-07` (factual skill fixes, findings D1–D5) and `upgrade/2026-07` (judgment improvements, U1–U3) — both pushed to `claude-config` origin, neither merged, `main` untouched. Vault-side findings (V1–V8) have no branch: this loop never edits vault content, so their proposed diffs live in this note for Jesse to apply or delegate.

**Skipped surface:** the agent-memory directory (`~/.claude/projects/.../memory/`) is on the desktop machine and not reachable from this remote container — class (e) was not audited this run. Also noted in passing: `claude-config` carries two stale remote branches (`claude/nifty-maxwell-1at5et`, `claude/task-planning-99chnf`) worth deleting or merging at some point; branch deletion is hard-banned for agents, so that's a Jesse action.

---

## Part 1 — Skill drift (proposed on branch `drift/2026-07`)

### D1 · usadebusk-fieldpm is dormant while a job is mobilized — HIGH

- **File:** `skills/usadebusk-fieldpm/SKILL.md:3-5`
- **Current:** `status: dormant` / `disable-model-invocation: true` / `description: DORMANT between mobilizations — load only during an active job mobilization.`
- **Vault truth:** `01-context/active-jobs.md:11` — "USA26038 | HF Sinclair Navajo, Artesia NM | H19, H20 | Mobilized 2026-07-10".
- **Proposed:** flip to `status: active`, remove `disable-model-invocation`, and prepend the description with "ACTIVE for USA26038 (HF Sinclair Navajo, mobilized 2026-07-10)." The skill's own line 10 says it "reactivates when a job mobilizes" — the flip just never happened. Re-dormant it at demob.
- **Lane:** workflow config, not Lane 4.

### D2 · Syncrude missing from vault-ingest's known-clients list — MEDIUM

- **File:** `skills/usadebusk-vault-ingest/SKILL.md:71`
- **Current:** "### Known clients (32 active)" — list runs "…Sniper-Elite, Suncor, Targa, Valero, Westlake" with no Syncrude.
- **Vault truth:** `02-facilities/Syncrude/Fort-McMurray-AB/` exists with a live heater card (7-1 F-1) and a recorded job actual (CND25004 in the rollup).
- **Proposed:** add `Syncrude`, retitle "(33 active)". Without it, any Syncrude document would be flagged `client: UNKNOWN` and routed to inbox despite the client having a facility folder and job history.
- **Lane:** mechanical fact.

### D3 · Work-up billing math exists in the vault but not in usadebusk-estimating — HIGH

- **File:** `skills/usadebusk-estimating/SKILL.md:266-267`
- **Current:** "## Estimation Workup Tool — Excel workup template is a work in progress. Explain estimating logic from this skill when asked — do not attempt to replicate the workup structure until the template is documented here."
- **Vault truth:** `00-inbox/2026-07-11-three-document-model-and-billing-math.md` documents the per-heater work-up billing conventions, with `02-facilities/HF-Sinclair/Artesia-NM/USA26038-job-sheet.md` as the live worked exemplar: shift basis (day-shifts × 12h + night-shifts × 12h = heater pumper hours, last shift may be partial); labor Amt = combined man-hours (Qty × per-person hours); equipment lines billed at the heater's pumper total; per-diem headcount excludes the billable Project Manager; DEF billed at the quoted shift count as given; a billable PM line appears per-heater only when the quote carries one. The inbox note exists precisely because "most of the USA26038 job-sheet session was spent re-deriving these distinctions from scratch."
- **Proposed:** add a "Work-Up Billing Math (per-heater Qty / Item / Amt / Unit table)" subsection carrying those six rules, and soften the Workup Tool stub to defer to it for billing-table math (the Excel template itself remains undocumented).
- **Lane:** **Lane 4 (billing math)** — flagged; merge is the approval.

### D4 · usadebusk-sop restates an SOP section structure the formatting standard supersedes — MEDIUM

- **File:** `skills/usadebusk-sop/SKILL.md:88-98`
- **Current:** "## SOP Document Structure (Standard)" — a 10-item numbered list (Header block → Completion sign-off).
- **Vault truth:** `04-knowledge/sops/sop-formatting-standard.md` is the single canonical home for SOP layout (per vault `CLAUDE.md`: "anything else that mentions SOP formatting points at it"), and its structure differs — phase-based Procedure section, Definitions section, "Order adapts to job complexity," and an explicit note that the old prescriptive list "is aspirational."
- **Proposed:** replace the skill's list with a pointer: "SOP document structure, title block, section order, and layout are canonical in `04-knowledge/sops/sop-formatting-standard.md` — do not reproduce a section list from memory."
- **Lane:** pointer hygiene (formatting authority already decided).

### D5 · Naming-lock violations inside fieldpm references — LOW

- **Files:** `skills/usadebusk-fieldpm/references/extraction-format.md:26` ("Trimax unit number") and `:41` ("Trimax trailer number"); `skills/usadebusk-fieldpm/references/report-structure.md:129` ("USADebusk").
- **Vault truth / canon:** `usadebusk-core` — "USADeBusk is standard"; TriMax capitalization is part of the naming lock.
- **Proposed:** "Trimax" → "TriMax" (2×), "USADebusk" → "USADeBusk". Note: `sop-ops-lodge-001.md` also contains "Trimax" twice but its scope note says "Technical steps reproduced as authored" — left untouched deliberately.
- **Lane:** cosmetic.

---

## Part 2 — Upgrade proposals (branch `upgrade/2026-07`, separate so drift can merge alone)

### U1 · usadebusk-estimating: quoted-vs-billed rate drift caution

`04-knowledge/pricing/Rate Reference.md` (2026-07-06 QB pull) established that billed rates drift from quoted rates within the same job — "Valero PA billed TriMax pigging at $550/hr vs. $500/hr quoted; ExxonMobil billed the PM role at the Day Supervisor rate rather than the quoted PM rate" — and that no standalone company-wide rate schedule exists; contracted rates live on each facility's `_facility.md`. Proposed: a short caution block under the Baseline Rate Table pointing Section 9 population at the facility `_facility.md` first and flagging the quoted-vs-billed drift pattern for invoice review.

### U2 · usadebusk-fieldpm: three-document model boundary

The skill compiles the job report but doesn't know the job sheet exists, and the boundary was re-derived from scratch in the USA26038 session. Proposed: a compact "Document boundaries" note (job sheet = static, quote-facing, created at bid-win; heater card = persistent facts + accumulated actuals; job report = post-job timeline and actuals, where quoted-vs-actual gaps are reconciled — e.g., USA26038 quoted 12 crew, sent 10) plus a `/report` reminder to record that reconciliation. Sourced from `00-inbox/2026-07-11-three-document-model-and-billing-math.md` and `00-inbox/2026-07-11-usa26038-crew-12-vs-10.md`.

### U3 · usadebusk-vault-ingest: job-sheet misrouting guard

`references/document-routing.md` Priority 1 routes anything with `USA\d{5}` as a job report and dissolves it into heater cards. A job-sheet file (`USA26038-job-sheet.md` — a real, existing type) would be wrongly dissolved: it carries a USA# by construction but is a quote-facing document whose home is the facility folder. Proposed: a Priority-0.5 guard — frontmatter `type: job-sheet` or "job-sheet" in the filename routes to `02-facilities/[Client]/[City-State]/[JOB#]-job-sheet.md`, never dissolved. Deliberately minimal: the full template/render formalization stays with the unexplored idea seed (`00-inbox/2026-07-11-job-sheet-type-formalization.md`) — this only prevents data destruction in the meantime.

---

## Part 3 — Vault-side drift (no branch; this loop doesn't edit vault content)

The dominant pattern: corrections landed in skills over June–July, while the `04-knowledge/` prose notes that restate the same facts kept the pre-correction versions. In each case below the skill is the corrected home (evidence cited) and the vault note is stale.

### V1 · equipment-library.md describes a pre-Triple TriMax — HIGH

`04-knowledge/equipment/equipment-library.md:11-15` — "Control cab (operator station, far left) … Waterous CMU Series Two-Stage Centrifugal Pump (far right end)" — a single pump, a single operator station, no assemblies. Corrected canon (`usadebusk-equipment` SKILL.md:11): "One TriMax trailer contains 3 independent pumping assemblies … Three operator stations in the control cab"; fleet file lists every unit as "TriMax Triple Pumper." This is the exact fact-class the 2026-07-06 audit fixed in fieldpm; the vault equipment note was never swept. **Proposed:** rewrite the "Physical layout" and "Internal routing" blocks to the triple architecture (or reduce them to a pointer at the skill + keep only the engine/pump/trailer spec-sheet data the skill doesn't carry).

### V2 · equipment-library.md asserts a cross-unit direction constraint — HIGH

`equipment-library.md:64` — "Both units pig the same direction — B→R means convection-inlet-to-radiant-outlet (standard direction)." Corrected canon (`usadebusk-equipment` SKILL.md:123): "Each assembly runs its own circuit fully independently — direction, flow state, and progress are set per assembly. No cross-assembly direction constraint." **Proposed:** delete the sentence.

### V3 · equipment-library.md 2× filtration is unconditional and self-contradictory — MEDIUM

`equipment-library.md:61` — "One shared 4×3 pump and one shared filter press" (unconditional), while its own line 179 says "2× = 2 filter presses, 2 trash pumps (shared or mirrored)." Corrected canon (`usadebusk-equipment` SKILL.md:121): "Filtration scales conditionally: 2× … when customer requires it AND a 2nd press is available; otherwise 1× shared…". **Proposed:** replace both spots with the conditional rule.

### V4 · Looped-circuit transit times carry superseded ranges — LOW

`equipment-library.md:138` — "pig transit times of 15-20 minutes or more"; `04-knowledge/concepts/process-flow.md:61` — "pig transit times 10–20+ minutes depending on footage." Corrected canon (`usadebusk-sop` SKILL.md:67): "observed ~6–30 min across looped jobs, not a fixed range." **Proposed:** align both to the not-a-fixed-range phrasing.

### V5 · process-flow.md calls Rig-In/Rig-Out "12-hour fixed events" — MEDIUM

`process-flow.md:9` — "Rig-In (12-hour fixed event, simultaneous Day and Night shift)"; `:31` — "Rig-Out (12-hour fixed event)." Canon everywhere else (estimating skill:37, `01-context/estimating-approach.md`): Rig-In/Rig-Out default 6 hrs, duration varies; the "12-hour simultaneous Day and Night" framing belongs to **Mob/Demob** (estimating skill:29). Actuals agree rig-in is not fixed-12 (4, 5, 5, 27\*, 34.5\* hrs in the rollup). **Proposed:** relabel as "fixed events, default 6 hrs (see Duration Model)" and move the 12-hr framing to a Mob/Demob line.

### V6 · Stale billing facts in field-operations.md — MEDIUM

`04-knowledge/concepts/field-operations.md:50` — "Third Party | Third Party | N hrs | Cost + 10%" (canon: contract-dependent, "as low as 5%", never assume — estimating skill:94); `:51` — "Plant Down Time | Stand-by | N hrs | Stand-by rate" (canon: "no generic stand-by line — billed via the TriMax Pumper / Filter Press stand-by rates only," usadebusk-ops:86). **Proposed:** "Cost + markup (contract-specific)" and the two-rate-lines-only phrasing.

### V7 · process-flow.md treats filtration as always-connected — MEDIUM

`process-flow.md:14` — "5. Connect filtration circuit: dirty tank → 4×3 pump → filter press → clean tank" and `:25-26` unconditional concurrent filtration. Corrected canon (`usadebusk-sop` SKILL.md:17, 27, 209): filtration connects "only when filtration is Elected — read the heater card Job Options"; default effluent path is coke pit / oily water sewer. This distinction is billing-relevant (filter press is a billed line). **Proposed:** add the election gate to both spots.

### V8 · Heater-card Field Notes shape is out of sync across its three homes — MEDIUM

The schema authority (`04-knowledge/_canonical-heater-card.md:221-227`) and `templates/_heater-template.md:120-126` both template Field Notes as "**Task Durations (actuals):** / **Obstacles:** / **Facility Procedures:**" — but all three copies of the Task Durations table comment (exemplar, template, ingest skill) rule "per-rig split stays in Field Notes" and vault-ingest SKILL.md:337 adds "Never duplicate the duration numbers as prose." Vault-ingest's derived template (SKILL.md:321-325) carries the corrected shape: "**Pigs Ran:** / **Obstacles:** / **Facility Procedures:** / **Per-rig split (multi-TriMax only):**". Live cards show the cost of the mismatch: F-802's Field Notes duplicate the full duration row as prose. **Proposed:** sync exemplar + template to the ingest-skill shape (drop the prose durations slot, add Pigs Ran and Per-rig split) — the exemplar is the declared authority, so this is Jesse's schema call.

Also noted, one line each, owned by other loops: `04-knowledge/concepts/quote-lifecycle.md` still describes a standalone-DSP-note + `_pipeline.md` Dataview workflow — no `_pipeline.md` exists and DSPs dissolve into heater cards (needs a rewrite when convenient); `07-llms/claude/chat.md` still lists three "Active" Claude Projects (retired 2026-07-07) and `07-llms/claude/cowork.md` says the capture loop is "not built" and "no other scheduled tasks" exist (four loops are deployed) — consolidation-loop territory, listed here only so it isn't lost.

---

## Part 4 — Open questions (domain knowledge this loop can't settle from files; no edits proposed)

1. **Operating pressure range** differs across three homes: `usadebusk-equipment:33` "100–400 PSI typical," `usadebusk-sop:107` "100–200 PSI nominal; 150–400 PSI hard fouling," `equipment-library.md:34` "Normal operating: 150–250 PSI." All agree on 600 max. Which formulation is canonical? (Lane 4.)
2. **9 Chrome metallurgy.** Skills model metallurgy as a carbon/stainless binary (estimating intake #9 "carbon steel or stainless"; SOP Variants A/B) — but both live USA26038 heaters record "9 Chrome" per-section (H19.md:37-39). Presumably runs as Variant A with no passivation, but that's an inference; how should chrome alloys be recorded and handled? (Lane 4.)
3. **Labor: 12-hr Day Rate or hourly?** Estimating skill:78 says "Labor | 12-hr Day Rate" while its own Baseline Rate Table, the receipts, and the USA26038 work-up all carry labor in $/hr and Hrs. Both models coexist in the same skill. (Lane 4.)
4. **Passivation numeric extras.** `industry-foundation.md:56-61` carries values absent from the canonical home (circulation 1–2 ft/s, 4–6 hrs duration, chloride ≤250/≤500/<0.5 ppm, "USADeBusk can supply if required") — `usadebusk-core:103` says such values live only in sop Variant B, which omits them. Promote to the skill, or trim the vault note to a pointer? (Lane 4 — safety chemistry.)
5. **Rig-in 6-hr default calibration.** Valero actuals 27/34.5\* hrs; USA26038 H-20 quoted Rig-In 12. The rollup already flags this class; benchmark changes are yours. (Lane 4.)
6. **Filter press rate during smart pigging:** usadebusk-ops:75 counts smart pigging as "pumping"; usadebusk-estimating:85 defines pumping as "TriMax actively pigging" without mentioning smart pig. One sentence in estimating would close it — which way?
7. **Registry oddities:** vault-ingest lists both "FHR" and "Flint-Hills" as separate clients (same company?); `equipment-library.md:119` expands HR as "High-Recovery / Hard Rubber" where the skill registry says only "High-Recovery."

---

## Decision

- [ ] **D1–D5:** merge `drift/2026-07` as-is (D3 is Lane 4 — merging applies the billing-math addition)
- [ ] **D1–D5:** merge partially — note which findings to drop in Apply Log
- [ ] **U1–U3:** merge `upgrade/2026-07` as-is
- [ ] **U1–U3:** merge partially — note which proposals to drop in Apply Log
- [ ] **V1–V8:** approve vault-side fixes as proposed (apply in a follow-up session using this note's diffs)
- [ ] **V1–V8:** walk through individually first
- [ ] Discard branch(es) — reason in Apply Log
- [ ] Open questions: answers / decisions recorded in Apply Log

## Apply Log

*(empty — filled when decisions are applied)*
