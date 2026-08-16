---
type: idea-seed
status: closed-unactioned
created: 2026-07-07
closed: 2026-08-15
related:
  - [[2026-07-09-idea-research-context-packet-builder-skill]]
tags: [idea, skills, claude-config, future]
---

> **Disposition (2026-07-18):** **Parked** — revisit only if a real mobilization/bid shows manual context-gathering actually causing friction. Adaptation path (domain-scoped `/prime`-style command, propose-and-confirm) recorded in [[2026-07-09-idea-research-context-packet-builder-skill]].

# Context-packet-builder skill

> **RETIRED 2026-08-15** (Jesse, retirement sweep). **The trigger fired against a real event and the answer was no.** USA26041 (ExxonMobil Baytown, HU5A F-501) mobilized on 2026-08-11 — job sheet, crew pool, equipment, vehicles, badging and loadout — which is exactly the condition this seed was parked against. It showed no manual context-gathering friction worth a build.
>
> The failure worth naming is not the answer but the delay: the trigger had already fired and nobody checked it. It sat on the dashboard reading as dormant while the event it named had come and gone four days earlier. Retiring on a fired-and-answered trigger is the honest close; re-parking it would have preserved the same blind spot.
>
> **What killed it is not that the idea was bad.** `usadebusk-core` and the domain skills already auto-load on task type, which was the seed's own leading doubt ("is this meaningfully different from just loading the right skills manually?"). A live mobilization answered that empirically rather than by argument.
>
> **If this ever returns**, the trigger wording is the thing to fix first. "Shows manual context-gathering friction" has no observer and no moment of check — which is how a fired trigger went unnoticed. A revived version needs a condition someone actually encounters at a step in the workflow.

Idea seed captured 2026-07-07 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** During a skill-design research audit, no existing skill or vault loop assembles a *pre-task* context packet (schemas, naming rules, prior-art pointers, relevant heater cards, etc.) before starting a job — the closest thing, the Skill-Drift loop, works retrospectively/monthly, not on-demand before a task starts. Anthropic's own skill-authoring docs describe the adjacent-but-different pattern of turning post-task reusable context into a skill, which isn't the same as a pre-task packet builder. No strong external prior art was found either — this may be a genuine gap in the skill ecosystem, or it's being done informally elsewhere rather than packaged as a Skill.

**To explore:** What would trigger it (a new bid, a new job mobilization, an explicit `/context-packet` command)? What would it actually assemble — heater-card lookups, relevant SOPs, past-job actuals, format rules? Is this meaningfully different from just loading the right skills/context files manually (usadebusk-core already auto-loads on task type), or would it add real value on top of that? Worth designing custom since no reusable prior art exists — deferred from the 2026-07-07 skill-design audit as not urgent.
