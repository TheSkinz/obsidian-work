---
title: ChatGPT — Overview
created: 2026-06-29
tags: [chatgpt, openai, codex, agent-architecture]
---

# ChatGPT

OpenAI's ChatGPT platform. Primary role: architecture and research hub for AI workflow design, agent evaluation, and M365/Copilot strategy. Distinct from Copilot's in-tenant execution — ChatGPT is where designs are evaluated, not where they run.

## Canonical project: AI Workflow & Agent Architecture Lab

The primary ChatGPT project. Covers ChatGPT Projects, OpenAI agents, automation patterns, M365 Copilot, Copilot Studio, Agent Builder, connectors/actions, governance, and workflow design. This is the research layer; Copilot is the execution layer.

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
