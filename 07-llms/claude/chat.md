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
