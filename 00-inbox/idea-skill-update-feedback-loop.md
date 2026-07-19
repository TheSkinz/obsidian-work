---
type: idea-seed
status: superseded
superseded_by: "[[vault-skill-drift-loop-spec]]"
created: 2026-06-30
related:
  - [[2026-07-01-idea-research-skill-update-feedback-loop]]
  - [[vault-skill-drift-loop-spec]]
tags: [idea, vault-system, future]
---

# Skill-update feedback loop

> **Superseded 2026-07-19 by the Skill-Drift Loop** ([[vault-skill-drift-loop-spec]], built 2026-07-07). This seed asked for exactly what that loop now does, and its research note's one identified gap is the loop's core mechanic — see the closing note at the bottom.

Idea seed captured 2026-06-30 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** Close the loop between vault knowledge and the USADeBusk skills at `~/.claude/skills/`. When the system harvests a durable finding that should change a skill (a corrected spec, a new equipment fact, a refined estimating rule), it flags or proposes a skill update instead of letting skill content silently drift from vault truth.

**To explore:** What triggers a proposed skill change vs. just a vault note? Propose-only or auto-PR to the claude-config repo? How is skill/vault drift detected? Relationship to the on-demand Review Loop ([[vault-agent-loop-spec]]) and the two-tier ceremony model.

---

## Closing note (2026-07-19)

Every open question above was answered by building the Skill-Drift Loop on 2026-07-07, two days after this seed's investigation was approved and blocked on environment.

The research note ([[2026-07-01-idea-research-skill-update-feedback-loop]]) concluded that off-the-shelf staleness tools would cover detection but that one thing would need original design: *"None of them span two repos and propose that a change in repo A (`obsidian-work`) should produce a proposed diff in repo B (`~/.claude/skills/`)."* That cross-repo propagation mechanic is the Skill-Drift Loop's core: drift class (a) is a vault note contradicting a skill's stated fact, and the loop packages its fixes as an unmerged `drift/YYYY-MM` branch in the config repo — propose-only, zero application authority, which also satisfies this seed's "propose-only or auto-PR?" question in favor of propose-only.

Drift class (c) — a skill referencing a file, folder, or workflow that no longer exists — covers the `2026-06-30-skill-naming-cleanup` incident (the stale OneDrive vault path) that motivated this seed in the first place.

Proven, not just designed: the loop's first run (2026-07-12) produced 13 findings, and all of them were adjudicated and applied (V1–V8 in the vault, U1–U4 in the skills). The approved bounded investigation — trialing an existing staleness-audit skill — was never run and no longer needs to be; it was a means to this end, and the end arrived by a better route.
