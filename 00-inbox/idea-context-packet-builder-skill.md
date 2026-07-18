---
type: idea-seed
status: researched
created: 2026-07-07
related:
  - [[2026-07-09-idea-research-context-packet-builder-skill]]
tags: [idea, skills, claude-config, future]
---

> **Disposition (2026-07-18):** **Parked** — revisit only if a real mobilization/bid shows manual context-gathering actually causing friction. Adaptation path (domain-scoped `/prime`-style command, propose-and-confirm) recorded in [[2026-07-09-idea-research-context-packet-builder-skill]].

# Context-packet-builder skill

Idea seed captured 2026-07-07 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** During a skill-design research audit, no existing skill or vault loop assembles a *pre-task* context packet (schemas, naming rules, prior-art pointers, relevant heater cards, etc.) before starting a job — the closest thing, the Skill-Drift loop, works retrospectively/monthly, not on-demand before a task starts. Anthropic's own skill-authoring docs describe the adjacent-but-different pattern of turning post-task reusable context into a skill, which isn't the same as a pre-task packet builder. No strong external prior art was found either — this may be a genuine gap in the skill ecosystem, or it's being done informally elsewhere rather than packaged as a Skill.

**To explore:** What would trigger it (a new bid, a new job mobilization, an explicit `/context-packet` command)? What would it actually assemble — heater-card lookups, relevant SOPs, past-job actuals, format rules? Is this meaningfully different from just loading the right skills/context files manually (usadebusk-core already auto-loads on task type), or would it add real value on top of that? Worth designing custom since no reusable prior art exists — deferred from the 2026-07-07 skill-design audit as not urgent.
