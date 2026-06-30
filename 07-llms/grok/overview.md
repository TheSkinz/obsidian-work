---
title: Grok — Overview
created: 2026-06-29
tags: [grok, xai, vision, forensic-engineering, image-generation]
---

# Grok

xAI's Grok platform. Primary uses: forensic multi-model engineering workflows, vision analysis on degraded refinery drawings, Grok Imagine for iterative image generation, and automation integrations.

## Forensic engineering workflow

Multi-model approach combining Grok vision analysis, `code_execution` OCR preprocessing (pytesseract + Pillow), and Gemini/Claude cross-validation to extract technical data from poor-quality refinery drawings. Recreated outputs in Visio or Mermaid.

Applied to:
- Marathon Detroit 70H1 Coker Furnace
- Paulsboro P5-F2
- Shell Oil direct fired heater (F-1235)

This is treated as the operational standard for forensic mechanical engineering tasks on degraded or low-resolution drawings — not a one-off experiment.

## Custom agent / skill development

Grok Build CLI, skill-creator tooling, Zapier/Albato integrations, Gmail and Google Drive automation, email digest pipelines. Use cases are in active exploration — document specific deployed integrations as they stabilize.

## Account and credential separation

Strict work/personal account separation: personal Gmail (not work email) is used exclusively for Grok/xAI accounts, API keys, and automations. This prevents credential linkage between USADeBusk systems and personal AI activity. Do not use the work email for any xAI account or API key registration.

## Grok Imagine

Iterative character-consistent image generation — see [[ai-image-generation]] for workflow details.
