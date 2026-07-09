---
type: review
status: open
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-09
review_after: 2026-08-09
related:
  - [[idea-context-packet-builder-skill]]
  - [[vault-idea-loop-spec]]
  - [[2026-07-07-harness-audit-open-items]]
tags: [review, knowledge-system, idea-research, skills]
---

# Idea Research — Context-Packet-Builder Skill

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. `idea-context-packet-builder-skill` (created 2026-07-07) was the only `unexplored` idea-seed in `00-inbox/` — the other two queued seeds (`idea-self-obsolescence-detection`, `idea-skill-update-feedback-loop`) are already `researched`/`approved-blocked`. The seed was itself deferred out of a 2026-07-07 skill-design research audit as "not urgent," which had already found no strong internal or external prior art at the time — this run re-checks that finding with a dedicated search pass.

## Evidence

**Internal — confirms the seed's own claim: no pre-task packet builder exists, and existing skills lean the opposite direction (guardrails against auto-population, not toward it).** Grepped all seven deployed skills (`~/.claude/skills/`) for context-assembly patterns. Found no packet-builder anywhere. What exists instead are explicit guardrails against the failure mode a packet builder would introduce: `usadebusk-fieldpm/SKILL.md` — "Cross-thread references: Do not pull operational data from other job threads without explicit user request"; `usadebusk-estimating/SKILL.md` — "Never use default rates from a prior job. Confirm before populating." Both skills actively resist silent auto-pull of prior-job context into a new task, which is close to the opposite instinct from what a packet builder would do by default. `CLAUDE.md` already auto-loads `usadebusk-core` plus task-type skills, which is the seed's own named alternative to a dedicated builder.

**External — the general pattern is a mature, well-tooled convention (`/prime`), but it's shaped for generic software repos, not this vault's domain content.** The Claude Code community has converged on a `/prime` slash-command genre that does close to what the seed describes: `qdhenry/Claude-Command-Suite`'s [`dev/prime.md`](https://github.com/qdhenry/Claude-Command-Suite/blob/main/.claude/commands/dev/prime.md) runs `git ls-files` and a directory-tree scan, reads `README.md` and docs, and produces a 2-3 sentence project summary plus key codebase areas — explicitly for "starting work, returning after a break, onboarding teammates, or preparing for deep technical work." `avibebuilder/claude-prime` and `danielrosehill/Claude-Slash-Commands` are further examples of the same genre packaged as one-command setup. All of them assume a generic code repo shape (git history, README, source tree) — none assemble domain-specific artifacts like heater-card lookups, SOP cross-references, or past-job actuals, which is the part of this idea-seed with no off-the-shelf analogue. Anthropic's own [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) frames the right shape for this: "just-in-time" retrieval via lightweight references (file paths, stored queries) loaded at runtime by the agent itself, rather than a pre-assembled dump — relevant design constraint if this is ever built, since a bad packet builder would just re-create the "silent auto-pull" problem the field skills already guard against.

## Interpretation

**Sound, partially covered — by pattern, not by content.** The general mechanism (a slash command that gathers and summarizes context before work starts) is not a gap in the ecosystem; `/prime` is a known, working convention with multiple independent implementations. But every implementation found is generic-repo-shaped (files, README, git log), and this vault's actual need is domain-shaped (heater cards, SOPs, format rules, prior-job actuals) — nothing found assembles that. So the seed's "no strong external prior art" read was correct for the domain-specific half, and slightly overstated for the mechanism half; a `/prime`-style command is the right chassis to adapt, not something to design from scratch. Two things argue for parking rather than building now, independent of the prior-art question: (1) unlike the skill-update-feedback-loop idea (proven necessary by a live drift incident found the same night), no incident here shows the informal path — `usadebusk-core` auto-load plus manual skill selection — actually failing; the seed itself frames this as unconfirmed intent, not an observed pain point. (2) The two field skills' explicit guardrails against auto-pulling prior-job data are a real design tension a packet builder would need to resolve (propose-and-confirm, never silent-populate) before it's safe to build, which raises the design cost above a simple `/prime` port.

## Recommended Action

Park, with a concrete adaptation path recorded for whenever it's picked up. Not urgent enough to build speculatively — no incident has shown the manual path failing, matching the audit's original call. If a future job mobilization or bid does surface real friction (spending time manually finding the right heater card / SOP / past-actuals before starting), the fix is a domain-adapted `/prime`-style command (candidate trigger: `/context` or `/brief`, scoped per job or per bid) that assembles job-specific pointers (heater card links, applicable SOPs, past-job actuals, format rules) rather than a generic file/README summary — and it must propose-and-confirm rather than auto-populate, per the pattern `usadebusk-fieldpm` and `usadebusk-estimating` already establish for cross-job data.

## Decision

- [ ] Build now — domain-adapted `/prime`-style command
- [ ] Bounded one-shot investigation first
- [ ] Park — revisit only if a real mobilization/bid shows manual context-gathering friction
- [ ] Drop

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| | | | |
