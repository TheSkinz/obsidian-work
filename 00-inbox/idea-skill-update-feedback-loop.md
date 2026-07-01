---
type: idea-seed
status: researched
created: 2026-06-30
related:
  - [[2026-07-01-idea-research-skill-update-feedback-loop]]
tags: [idea, vault-system, future]
---

# Skill-update feedback loop

Idea seed captured 2026-06-30 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** Close the loop between vault knowledge and the USADeBusk skills at `~/.claude/skills/`. When the system harvests a durable finding that should change a skill (a corrected spec, a new equipment fact, a refined estimating rule), it flags or proposes a skill update instead of letting skill content silently drift from vault truth.

**To explore:** What triggers a proposed skill change vs. just a vault note? Propose-only or auto-PR to the claude-config repo? How is skill/vault drift detected? Relationship to the on-demand Review Loop ([[vault-agent-loop-spec]]) and the two-tier ceremony model.
