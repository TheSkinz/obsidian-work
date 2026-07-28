<!-- vault-loop: 2026-07-13 capture run — "Undocumented tasks/ directory" item harvested to 07-llms/claude/code.md. Remaining two items are operational/governance (vault five-loop scheduling, USADebusk skill formatting) and stay here for Jesse or the on-demand Agent-Review loop. -->
<!-- vault-prestaged: skipped — already covered: Agent-Review on-demand-only is deliberate per [[vault-agent-loop-spec]] (line 33, and line 118 blocks scheduling it); format-split item's own revisit condition ("if inconsistency is observed") has not fired — branding rules remain single-sourced in usadebusk-core, heater-card schema single-sourced to _canonical-heater-card.md -->
---
type: session-note
created: 2026-07-07
tags: [session-log, harness, claude-config]
---

# Harness audit — open items (2026-07-07)

Session log for a skill-design research audit + full harness survey. Two items surfaced that weren't resolved in-session and need Jesse's eyes rather than agent judgment.

**Agent-Review loop has no scheduled-task cron entry.** The vault's five-loop system (Capture, Agent-Review, Idea-Research, Skill-Drift, Consolidation) only has four matching entries in `mcp__scheduled-tasks`. The governance doc frames Agent-Review as intentionally on-demand-only, not cron-driven — but this wasn't explicitly re-confirmed this session. Worth a quick check that this is deliberate and not a loop that quietly never got scheduled.

**Format-enforcement skill split — deferred, not forgotten.** Format rules (Helvetica canonical, Arial DOCX fallback, gold `#FCC30A`, Heater Card `## Task Durations` schema) remain scattered across `usadebusk-core`/`usadebusk-equipment` rather than split into a dedicated format-enforcement skill. The pattern is validated by Anthropic's own docs (reference-content vs. task-content split, `frontend-design` as the canonical example) but there's no evidence of actual drift yet — revisit only if formatting inconsistency is observed across skills.
