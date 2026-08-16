---
type: idea-seed
status: complete
created: 2026-07-20
closed: 2026-08-15
related:
  - [[2026-07-24-idea-research-lint-lock-heater-schema]]
tags: [idea, vault-system, future]
---

# vault_lint rule: assert heater Task-Durations header matches the exemplar

> **Built — closed 2026-08-15** by the retirement sweep. `DURATIONS-HEADER` is live at `tools/vault_lint.py:496` with fixture `tools/fixtures/02-facilities/TestClient/Test-City-TX/T-200.md`, and its docstring cites the same `Condition`-column drift this seed was written about. It resolved the seed's open questions as built: the canonical header is read from `DURATIONS_HEADER` rather than hard-coded, severity is warning ("a header fix is a to-do, not a stop-the-line"), and the rule anchors on the `## Task Durations` heading so it cannot false-positive on the many other tables mentioning Rig-In. The general question underneath it — which canonical tables deserve a header lock — was answered again in the same shape by `TUBE-GEOM-HEADER` (DQ-006), which was built on this rule's anchor-and-compare structure.
>
> This sat at `status: researched` for three weeks *after* being built. Because the Terminal-Note Sweep is forbidden from touching `researched` — that status means "Jesse has not decided" — a completed build was indistinguishable from a pending decision, and nothing could move it.

Idea seed captured 2026-07-20 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** The heater-card `## Task Durations` column set is the schema authority's job (the exemplar `_canonical-heater-card.md`), but it's currently only prose-enforced — which is exactly how the stale 10-column copy in vault CLAUDE.md drifted (missing `Condition`) before it was caught this session. A `vault_lint.py` rule that reads the exemplar's header row and fails any heater card (or any file) whose `## Task Durations` header doesn't match would turn the schema from a drift-prone reminder into a machine-checked lock — the "hard rules need hard checks" principle from the harness-map work ([[2026-07-20-harness-map]], rule 5).

**To explore:** Should the check target only live cards under `02-facilities/`, or also flag any other file that inlines the columns (which would have caught the CLAUDE.md drift directly)? What's the failure severity — warning or error? How does it read the canonical header without hard-coding it (parse the exemplar at runtime, so the lock and the authority never diverge)? Ships with a failing-then-passing fixture per the Lane 3 lint-rule convention. Cheap to build; deferred only because the prose fix already removed the one known drifted copy.
