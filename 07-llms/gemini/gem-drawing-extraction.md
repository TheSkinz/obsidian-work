---
title: Gemini Gem — Fired Heater Tube Drawing Extraction (retired)
status: deprecated
created: 2026-06-29
tags: [gemini, vision, drawing-extraction, engineering, retired]
---

# Fired Heater Tube Drawing Extraction Gem

**Retired 2026-07-07 along with Gemini itself. There is no validated replacement — no tool has been benchmarked for fired-heater drawing extraction since.** Kept for the confabulation finding below, which is tool-independent and still governs, and as the record of what this path could do. Do not treat anything here as the current way to extract a drawing.

A custom Gemini Gem built for extracting tube and pass data from scanned fired heater engineering drawings. It was the production path for that task from 2026-06-29 until the retirement.

## Final version: v8.1

Capabilities it had reached by retirement:
- Enhanced scan mode for low-resolution or high-noise scans
- F58 calibration reference (used to normalize extracted dimensions against a known reference point in the drawing)
- Structured output format for downstream use in job estimation and heater card population

## Key finding: LLM self-diagnosis is confabulation

When the Gem returned incorrect extractions, asking it to explain its reasoning or identify its own errors produced confident but fabricated explanations. The model cannot reliably audit its own vision output. External validation against the drawing (human review or cross-check against a second pass) is required for any production-critical values.

This applies to all LLM vision tasks, not just this Gem, and it survives the retirement unchanged — it is the reason this note is kept.

## Status

**Retired 2026-07-07. No tool of record for drawing extraction.**

The retirement left the task without a benchmarked owner, and nothing has claimed it since:

- Claude vision has never been benchmarked against this Gem for engineering drawings — see [[code]].
- The Grok forensic path ([[drawing-extraction-strategy]]) is a single pilot, not benchmarked either.
- The Copilot agent architecture ([[heater-extraction-agent]]) was scoped against this Gem as its comparator and inherits the same gap.

Until something is actually benchmarked, treat every extracted value as unvalidated: cross-check it against the drawing before it reaches a proposal or a heater card. Naming a successor is a decision, not an inference — it needs a head-to-head run first.

## Usage notes (historical)

Input was a scanned PDF or image of a tube drawing. The Gem handled multi-pass heaters; pass count had to be specified where the drawing was ambiguous. The standing advice outlasts the tool: cross-check extracted tube counts and OD values against the drawing legend before using them in a proposal.
