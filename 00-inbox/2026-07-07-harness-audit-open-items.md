---
type: session-note
created: 2026-07-07
tags: [session-log, harness, claude-config]
---

# Harness audit — open items (2026-07-07)

Session log for a skill-design research audit + full harness survey. Two items surfaced that weren't resolved in-session and need Jesse's eyes rather than agent judgment.

**Agent-Review loop has no scheduled-task cron entry.** The vault's five-loop system (Capture, Agent-Review, Idea-Research, Skill-Drift, Consolidation) only has four matching entries in `mcp__scheduled-tasks`. The governance doc frames Agent-Review as intentionally on-demand-only, not cron-driven — but this wasn't explicitly re-confirmed this session. Worth a quick check that this is deliberate and not a loop that quietly never got scheduled.

**Undocumented `tasks/` directory.** `C:\Users\Jwuts\.claude\tasks\` contains four UUID-named folders with numbered `.json` files and `.lock` files — looks like internal session/agent task-queue plumbing, not anything user-authored, and isn't referenced anywhere in either CLAUDE.md or the governance doc. Not flagged as broken, just unexplained; low priority to understand what it is before assuming it's safe to ignore long-term.

**Format-enforcement skill split — deferred, not forgotten.** Format rules (Helvetica canonical, Arial DOCX fallback, gold `#FCC30A`, Heater Card `## Task Durations` schema) remain scattered across `usadebusk-core`/`usadebusk-equipment` rather than split into a dedicated format-enforcement skill. The pattern is validated by Anthropic's own docs (reference-content vs. task-content split, `frontend-design` as the canonical example) but there's no evidence of actual drift yet — revisit only if formatting inconsistency is observed across skills.
