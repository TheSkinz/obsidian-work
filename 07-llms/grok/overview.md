---
title: Grok — Overview
created: 2026-06-29
tags: [grok, xai, vision, forensic-engineering, image-generation]
---

# Grok

xAI's Grok platform. Primary uses: forensic multi-model engineering workflows, vision analysis on degraded refinery drawings, Grok Imagine for iterative image generation, and automation integrations.

## Forensic engineering workflow

Multi-model approach combining Grok vision analysis, `code_execution` OCR preprocessing (pytesseract + Pillow), and Claude cross-validation to extract technical data from poor-quality refinery drawings. Recreated outputs in Visio or Mermaid — see [[diagram-creation]] for format-choice guidance.

Applied to:
- Marathon Detroit 70H1 Coker Furnace
- Paulsboro P5-F2
- Shell Oil direct fired heater (F-1235)

This is a repeatable method rather than a one-off experiment, but it is **not the standard for anything** — it has never been benchmarked. The Gemini Gem that formerly held the drawing-extraction role retired 2026-07-07 and no successor was named, so no tool is of record for this task (see [[gem-drawing-extraction]]). An earlier version of this line called the method "the operational standard"; that claim had no benchmark behind it and was corrected 2026-08-24.

See [[drawing-extraction-strategy]] for the canonical two-pass tile method distilled from the Grok repo's heater-drawing-analysis skill.

## Custom agent / skill development

Grok Build CLI, skill-creator tooling, Zapier/Albato integrations, Gmail and Google Drive automation, email digest pipelines. Use cases are in active exploration — document specific deployed integrations as they stabilize.

## Account and credential separation

Strict work/personal account separation: personal Gmail (not work email) is used exclusively for Grok/xAI accounts, API keys, and automations. This prevents credential linkage between USADebusk systems and personal AI activity. Do not use the work email for any xAI account or API key registration.

## Grok Imagine

Iterative character-consistent image generation — see [[ai-image-generation]] for workflow details.
