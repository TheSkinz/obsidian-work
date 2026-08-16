<!-- vault-loop: 2026-07-13 capture run — "Undocumented tasks/ directory" item harvested to 07-llms/claude/code.md. Remaining two items are operational/governance (vault five-loop scheduling, USADebusk skill formatting) and stay here for Jesse or the on-demand Agent-Review loop. -->
<!-- vault-prestaged: skipped — already covered: Agent-Review on-demand-only is deliberate per [[vault-agent-loop-spec]] (line 33, and line 118 blocks scheduling it); format-split item's own revisit condition ("if inconsistency is observed") has not fired — branding rules remain single-sourced in usadebusk-core, heater-card schema single-sourced to _canonical-heater-card.md -->
---
type: session-note
status: resolved
created: 2026-07-07
closed: 2026-08-15
tags: [session-log, harness, claude-config]
---

# Harness audit — open items (2026-07-07)

> **Closed 2026-08-15** by the retirement sweep. This note carried no `status` field, which kept it invisible to the Terminal-Note Sweep for five weeks (see [[2026-07-29-statusless-notes-invisible-to-the-sweep]]) — it is one of the two notes that note identified as "done and stuck."
>
> **Item 1 — Agent-Review cron: deliberate, confirmed.** On-demand-only is stated in [[vault-agent-loop-spec]] (line 33) and actively enforced at line 118, which blocks scheduling it. `50-dashboards/health.md` now says so on the face of the loop table: "The review/agent loop is on-demand by design and not listed." The quick check this item asked for has been run, and the answer is that nothing quietly went unscheduled. The system has since grown to six loops.
>
> **Item 2 — format-enforcement skill split: closed, and its wake condition is now monitored.** The revisit condition ("only if formatting inconsistency is observed across skills") never had anywhere to be observed *from* when this was written. It does now: the Skill-Drift Loop was built 2026-07-07 and scheduled monthly, and its drift classes 2 (two skills contradicting each other) and 4 (a correction applied to one home while a restatement elsewhere carries the old version) are exactly this condition. Three runs have fired — 2026-07-12, 2026-07-25, 2026-08-01 — and none reported format drift. Branding rules remain single-sourced in `usadebusk-core` and the heater-card schema in `_canonical-heater-card.md`. No separate trigger is registered because a standing monthly audit is a better instrument than a dormant-trigger row.

Session log for a skill-design research audit + full harness survey. Two items surfaced that weren't resolved in-session and need Jesse's eyes rather than agent judgment.

**Agent-Review loop has no scheduled-task cron entry.** The vault's five-loop system (Capture, Agent-Review, Idea-Research, Skill-Drift, Consolidation) only has four matching entries in `mcp__scheduled-tasks`. The governance doc frames Agent-Review as intentionally on-demand-only, not cron-driven — but this wasn't explicitly re-confirmed this session. Worth a quick check that this is deliberate and not a loop that quietly never got scheduled.

**Format-enforcement skill split — deferred, not forgotten.** Format rules (Helvetica canonical, Arial DOCX fallback, gold `#FCC30A`, Heater Card `## Task Durations` schema) remain scattered across `usadebusk-core`/`usadebusk-equipment` rather than split into a dedicated format-enforcement skill. The pattern is validated by Anthropic's own docs (reference-content vs. task-content split, `frontend-design` as the canonical example) but there's no evidence of actual drift yet — revisit only if formatting inconsistency is observed across skills.
