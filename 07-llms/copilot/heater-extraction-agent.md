---
title: Copilot Heater Extraction Agent
created: 2026-06-29
tags: [copilot, agent, heater-extraction, sharepoint]
---

# Copilot Heater Extraction Agent

A custom Copilot agent architecture for extracting fired heater coil data from degraded engineering drawings. This is a Copilot-side implementation — distinct from the Claude-side Gemini Gem (v8.1) and the `usadebusk-core` evidence-class system (Anchor/Estimate/Blank). They address the same problem with different tools; cross-reference but don't merge.

## Architecture overview

The system uses modular SharePoint-hosted knowledge files as its grounding layer:

- **Extraction instructions** — core prompt defining what to extract and how
- **Extraction rules** — validated rules with maturity status (see Rule maturity system below)
- **Learning log** — durable lessons written back to SharePoint after each session
- **Failure case library** — known extraction failures captured as reusable training material
- **Audit prompts** — structured prompts used by the Auditor agent

## Auditor agent pattern

A separate Auditor agent reviews extraction outputs, rule maturity, learning logs, and failure cases after extraction is complete. The Auditor does not perform the original drawing review itself — it operates on completed outputs and flags discrepancies, rule violations, or pattern matches against known failure cases. Keeping the roles separate prevents the extractor from rationalizing its own errors.

## Learning log workflow

Durable lessons from each extraction session get written back to the SharePoint learning log, not left in chat history. Copilot Chat has no durable memory across sessions — anything worth keeping must be explicitly committed to SharePoint before the session ends.

## Rule maturity system

Extraction rules are tracked by validation status. Proven rules (validated against multiple real drawings without failure) are separated from experimental or failure-prone rules. New rules start as experimental and graduate to proven only after real-data validation. This prevents over-reliance on rules that haven't been stress-tested.

## Failure case library

Known extraction failures are captured as structured entries: what was extracted, what was correct, why the model failed, which rule (if any) should have caught it. These entries are reusable training material for rule iteration and auditor grounding.

## MVP build order

Core extraction instructions → audit loop → learning log → rule maturity tracking → failure case library. Do not add heavier automation before this foundation is validated on real drawings.

## Agent boundary

This agent reads and extracts from drawings. It does not edit source files, update SharePoint records, or write to job-execution systems without explicit per-task permission. Extraction outputs are always for human review before downstream use.

## Relationship to Claude-side tools

| Dimension | Copilot Agent | Claude / Gemini |
|---|---|---|
| Primary tool | Copilot Studio / Agent Builder | Gemini Gem v8.1 + usadebusk-core |
| Knowledge substrate | SharePoint (modular .md files) | Skills in ~/.claude/skills/ |
| Evidence tracking | Rule maturity + failure library | Anchor/Estimate/Blank evidence classes |
| Audit mechanism | Separate Auditor agent | Human review + vault cross-check |
| Memory | SharePoint learning log | Vault heater cards |

These are parallel implementations of similar ideas, not duplicates. If one produces a better extraction for a specific drawing type, document that in the learning log and the failure case library respectively.
