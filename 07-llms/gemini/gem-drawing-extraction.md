---
title: Gemini Gem — Fired Heater Tube Drawing Extraction
created: 2026-06-29
tags: [gemini, vision, drawing-extraction, engineering]
---

# Fired Heater Tube Drawing Extraction Gem

A custom Gemini Gem built for extracting tube and pass data from scanned fired heater engineering drawings. Currently the production tool for this task.

## Current version: v8.1

Key capabilities added through iteration:
- Enhanced scan mode for low-resolution or high-noise scans
- F58 calibration reference (used to normalize extracted dimensions against a known reference point in the drawing)
- Structured output format for downstream use in job estimation and heater card population

## Key finding: LLM self-diagnosis is confabulation

When the Gem returns incorrect extractions, asking it to explain its reasoning or identify its own errors produces confident but fabricated explanations. The model cannot reliably audit its own vision output. External validation against the drawing (human review or cross-check against a second pass) is required for any production-critical values.

This applies to all LLM vision tasks, not just this Gem.

## Status

Gemini Gem is **validated production tool** for fired heater tube drawing extraction. Claude vision has not been benchmarked against it yet — see [[code]] for the current Claude vision status note. Until a head-to-head benchmark is run, Gemini is the standard for this task.

## Usage notes

Input: scanned PDF or image of a tube drawing. The Gem handles multi-pass heaters; specify pass count if the drawing is ambiguous. Cross-check extracted tube counts and OD values against the drawing legend before using in a proposal.
