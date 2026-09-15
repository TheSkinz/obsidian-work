---
title: ChatGPT — Overview
created: 2026-06-29
tags: [chatgpt, openai, codex, agent-architecture]
---

# ChatGPT

OpenAI's ChatGPT platform. Primary role: architecture and research hub for AI workflow design, agent evaluation, and M365/Copilot strategy. Distinct from Copilot's in-tenant execution — ChatGPT is where designs are evaluated, not where they run.

> ⚠ **The M365/Copilot half of that role is dead for a session as of 2026-09-07.** Company policy
> blocks third-party tools from company systems, so **Claude Code cannot reach the M365 tenant by any
> route** ([[m365-access-boundary]]). A design evaluated here can no longer be executed, tested or
> verified in the tenant by anything but Jesse himself. The ChatGPT-side content below — Projects,
> Skills, Codex — is his personal account and is unaffected.

## Canonical project: AI Workflow & Agent Architecture Lab

The primary ChatGPT project. Covers ChatGPT Projects, OpenAI agents, automation patterns, M365 Copilot, Copilot Studio, Agent Builder, connectors/actions, governance, and workflow design. This is the research layer; Copilot is the execution layer.

Full operating-manual depth on this project setup — recommended chats, instructions, decision-log structure, file strategy — lives in [[chatgpt-copilot-workflow-architecture]] (ingested 2026-06-30, not yet tenant-verified). That source also recommends the name "AI Workflow Architecture Command Center" for this same project — reconcile before next rename.

## Skills — beta caveat

ChatGPT Skills are still beta, plan-limited, and do not currently sync across products. Treat them as a secondary optimization for a workflow that's already proven, not a default home for new automation. (Source: [[chatgpt-copilot-workflow-architecture]].)

## Codex workbench

Repo: `TheSkinz/codex-workbench`
Local path: `C:\Users\Jwuts\Documents\Codex`

Operating constraints enforced via `AGENTS.md` at repo root:

- Inspect before editing — read the target file before any change
- Small diffs — minimal, targeted edits; no wholesale rewrites without explicit direction
- No secrets committed
- No destructive commands
- No push or publish without explicit approval
- Approval policy: on-request
- Sandbox mode: workspace-write, network off

Codex use case: repo/file/tool-building tasks — edits, scripts, audits, durable tooling artifacts. Not for casual Q&A or exploratory reasoning where chat is more efficient.

## Codex as heater-extraction tooling layer

Codex supports heater extraction workflows as a preprocessing and validation layer: repeatable crop management, OCR preprocessing pipelines, extraction logs, validation checks. It supports judgment; it doesn't replace it. Extraction decisions and confidence ratings remain human-reviewed.
