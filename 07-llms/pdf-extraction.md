---
title: PDF Extraction — Cross-Platform Best Practices
created: 2026-06-29
platforms: [claude, gemini, copilot]
tags: [pdf, extraction, cross-platform]
---

# PDF Extraction

Best practices for extracting text and structured data from PDFs across tools.

## General principles

Text-layer PDFs (digitally created, not scanned) extract cleanly through any tool's native PDF reader. Scanned PDFs — especially engineering drawings, handwritten field tickets, or photocopied documents — require vision-capable models and have meaningfully lower accuracy ceilings.

Quality varies by: scan resolution, document density, presence of tables vs. prose, and whether the target values are in structured fields or embedded in drawing callouts.

## Claude

Claude Code's `Read` tool handles text-layer PDFs natively. For image-heavy or scanned PDFs, Claude's vision processes the page as an image. Accuracy on clean scans of text documents is high; accuracy on dense engineering drawings with callouts and symbols is not yet benchmarked (see [[gem-drawing-extraction]] for current status).

Practical limit: Claude Code currently caps PDF reads at 20 pages per call for large documents. For longer documents, specify `pages: "1-20"` and paginate.

## Gemini

**Retired 2026-07-07.** The Fired Heater Tube Drawing Gem (v8.1) was the production path for drawing extraction until then; **nothing has been benchmarked to replace it**, so no tool currently holds that role — see [[gem-drawing-extraction]]. Recorded here because the section used to say the opposite, and because the finding below outlived the tool.

Standing limitation, tool-independent: a vision model cannot reliably self-diagnose extraction errors (see the confabulation finding in [[gem-drawing-extraction]]). Validate extracted values against the drawing, not against the model's own account of them.

## Copilot

Best suited to text-layer PDFs in a business-document context. Copilot via Microsoft 365 can read PDFs attached to emails or stored in SharePoint. Not evaluated for engineering drawing extraction.

## Structured extraction tips

When the goal is structured data (tube counts, dimensions, job numbers), specify the exact fields and format required upfront. Asking for free-text summaries and then trying to parse them downstream is slower and less reliable than prompting for a structured output (table or JSON) from the first call.

For repeating structured tasks (like heater card population), a dedicated system prompt or skill with field definitions outperforms ad-hoc prompting. (The principle was learned on a Gemini Gem, but it is about the field definitions, not the vehicle.)

Extraction quality is only half the problem. Deciding whether an extracted value means what it appears to mean — whether a cell is data or template boilerplate, whether two sources genuinely disagree — is tool-agnostic and lives in [[source-reconciliation]].
