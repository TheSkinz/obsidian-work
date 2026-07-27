---
title: Claude Chat (claude.ai)
created: 2026-06-29
tags: [claude, chat, strategy]
---

# Claude Chat

claude.ai is the browser-based chat interface. It handles open-ended reasoning, strategy, architecture design, and long-form drafting — tasks where iteration and dialogue matter more than file access.

## Role vs Claude Code

The split is deliberate: **chat = decisions, Code = execution**. Claude chat is where architectural choices get made, approaches get evaluated, and ambiguous problems get framed. Once the decision is clear, Claude Code implements it against the actual files.

Running a design pass in chat first is faster than giving Claude Code an underspecified task and watching it make assumptions. The cost is that chat has no vault or filesystem access — context has to be pasted in manually.

## How I use it

Architecture and planning passes for vault structure, skill design, and document standards. Long-form drafting that benefits from back-and-forth editing. Exploratory research on concepts that don't need real data.

Claude Projects are the structured variant — each project has a system prompt and pre-loaded context. Active projects:

| Project | Version | Use |
|---|---|---|
| Technical Docs | v2.1 | SOP and pre-execution package writing |
| Operations & Admin | v2.0 | Receipt analysis, crew packages, ops handoff |
| Field Execution | Current | Per-job field PM, receipt extraction, shift emails |

Sales & Proposals project was retired 2026-06-15; that content dissolved into the `usadebusk-estimating` skill.

## Memory system

Claude.ai has a native memory layer (separate from the vault memory system). It stores preferences, recurring context, and facts that carry across conversations. The vault's `~/.claude/projects/.../memory/` directory is a parallel file-based memory system for Claude Code sessions.

## Past-chat search

claude.ai does not have robust search across conversation history. Anything worth keeping from a chat session should be saved to the vault explicitly — either via the `/save` skill or manually.

## The claude.ai skill library is a disconnected second copy

Skills uploaded to the claude.ai skill library (Settings > Capabilities, or Customize > Skills) are a separate upload, not a view onto `~/.claude/skills/` — there is no sync mechanism in either direction. `usadebusk-core` is confirmed active there as of 2026-07-20. This means skill content lives in two disconnected places: the config repo (`~/.claude/skills/usadebusk-*`, maintained, version-controlled, the target of the monthly Skill-Drift Loop) and the claude.ai library (a frozen copy of whatever was uploaded, whenever). A Skill-Drift Loop correction lands in the config repo copy only — if the claude.ai upload predates it, chat/Cowork keeps answering from the stale value, and the loop reports success regardless. The exposure is worse in cloud Cowork specifically: desktop sessions run locally and can cross-check the skill against the vault, cloud sessions have no vault access at all, so a stale skill there just sounds fluent with no vault to catch it.

Nobody has verified how stale the current upload is — that's the first thing to check before designing a fix, since if the upload postdates the most recent drift run this is theoretical. Three unevaluated shapes if it turns out to matter: (1) add a re-upload step to the Skill-Drift Loop's follow-through, (2) treat claude.ai as deliberately thin — upload only `usadebusk-core` as a vocabulary layer, never a source of numbers (the profile instructions already carry a guard along these lines), (3) don't upload skills to claude.ai at all and run chat/Cowork on profile instructions alone. Option 2 is closest to what's live now and needs no new machinery.

Source: Claude Code session, 2026-07-20.
