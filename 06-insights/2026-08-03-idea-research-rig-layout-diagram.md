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

- [ ] Confirm continued gated status
- [ ] Re-open now (gate judged satisfied)
- [ ] Drop entirely

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| | | | |
