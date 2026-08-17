---
type: review
status: complete
review_type: idea-research
source_authority: primary
confidence: high
created: 2026-08-03
review_after: 2026-09-03
related:
  - "[[idea-rig-layout-diagram]]"
  - "[[2026-08-01-coil-visualization-build-owed]]"
  - "[[vault-idea-loop-spec]]"
tags: [review, idea-research, gated, field-ops, visualization]
---

# Idea Research — Generated Rig / Hose Layout Diagram (Gate Check)

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. Only one `idea-seed` was `unexplored` in `00-inbox/`: [[idea-rig-layout-diagram]] (`created: 2026-07-30`). Per [[vault-idea-loop-spec]] step 3, the seed's own gate is checked from files before any web research starts.

## Evidence

The seed's `**Gate:**` line: "Do not spend a research cycle until the coil-visualization decision is made — if that build is approved, this one should reuse whatever rendering and job-sheet-embedding path it establishes rather than inventing a second one." Its `revisit-trigger:` frontmatter sharpens this to a build-landing event, not an approval event: "Coil-visualization Tier 2+3 build lands... — event: check when the coil-viz SVG generator exists."

Checked [[2026-08-01-coil-visualization-build-owed]] directly: frontmatter `status: inbox`, and the note body states "Approved by Jesse 2026-08-01... Scope approved, build not started." The gate text itself anticipates this distinction — approval alone doesn't open it, landing does.

Checked `tools/` for the SVG generator the trigger names: current contents are `audit_commit.py`, `audit_worktree.py`, `estimating_rollup.py`, `pig_usage_rollup.py`, `vault_health.py`, `vault_index.py`, `vault_lint.py`. No coil-elevation SVG generator exists — the Tier 2 extraction of `buildGeometry()` from `apps/pig-tracker/pig-tracker.html:393` described in the owed note has not been started.

## Interpretation

**Gate verifiably unmet.** The trigger condition is landed code (an SVG generator that exists), not approval. Approval happened 2026-08-01; the build itself is still an unstarted item sitting in `00-inbox/` with `status: inbox`. Nothing in the vault contradicts this — no new file under `tools/` or `apps/pig-tracker/` reflects Tier 2 or Tier 3 work. Per spec, no web research was performed this run.

## Recommended Action

**Stay gated — no research yet.** Re-check when [[2026-08-01-coil-visualization-build-owed]] shows Tier 2 (SVG coil elevation) landed — evidence would be a new generator module under `tools/` or `apps/pig-tracker/` and/or the owed note's status moving off `inbox`. At that point this seed should research the rig/hose layout diagram against whatever render and job-sheet-embedding path that build establishes, per its own gate.

## Decision

**Mutually exclusive — one only.**

- [ ] ~~Confirm continued gated status~~
- [x] **Re-open now** (Jesse, 2026-08-16) — gate judged *obsolete* rather than satisfied; see below
- [ ] ~~Drop entirely~~

**Why "obsolete" and not "satisfied."** The trigger condition was never met — `tools/` still has no
coil-viz SVG generator on 2026-08-16 (three new tools since this note; none of them a renderer). The
gate was released because its *stated reason* does not hold. It exists to prevent inventing a second
rendering and job-sheet-embedding path, and on re-check the rendering path already exists in
production on both sides: the rig diagrams are HTML with hand-authored inline SVG printed to PDF
(`…\Active Work\Schematic\DeBuskFiltrationSchematic.html`), and job sheets use the same headless-Chrome
`--print-to-pdf` invocation recorded at `_canonical-job-sheet.md:353`. The coil-viz build would consume
that path, not establish it. What it *does* newly establish — a stdlib generator parsing heater-card
markdown tables — a rig layout structurally cannot use, having no heater-card source. The embedding
half is genuinely shared, but `2026-08-01-coil-visualization-build-owed.md:53` defers it explicitly
("decide standalone file vs job-sheet page 2 only after it works"), so the trigger firing would not
have resolved it either.

This note's 2026-08-03 reasoning was correct on the evidence available. It read the trigger literally
and checked it honestly; what it did not do — and was not scoped to do — was test whether the
condition was worth waiting on.

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-08-16 | **Re-opened; gate retired** | Claude (Opus 5), Jesse sign-off | Gate reason re-checked and found half-obsolete. `revisit-trigger:` removed from [[idea-rig-layout-diagram]], `status: gated` → `active`. Seed's two factual errors corrected: five hand-made diagrams exist, not one, and the cited `HU5A-F501-job-sheet.md` path does not exist (real: `USA26041-job-sheet.md`). Corpus captured at [[rig-diagram-corpus]]. Next step is a bounded back-test on F-901, not a build. |
