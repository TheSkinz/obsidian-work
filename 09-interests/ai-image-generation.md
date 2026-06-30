---
title: AI Image Generation
created: 2026-06-29
tags: [image-generation, grok, local-models, amuse]
---

# AI Image Generation

## Iterative character-consistent generation (Grok Imagine)

Workflow for generating character-consistent images across multiple variations using Grok Imagine. The process: refined prompting combined with reference-editing (uploading a reference image and requesting targeted edits — background removal, colorization, costume changes) rather than prompting from scratch each iteration.

Primary subject: elderly gunslinger/western scenes — portraits, costume variations, cinematic shots. Character consistency across iterations is maintained through the reference-edit approach rather than through LoRA or fine-tuning, which aren't available in Grok Imagine's current interface.

Key constraint: the reference-edit model preserves face and expression more reliably than text prompts alone, but outfit and background changes require careful prompt specificity to avoid bleeding into facial features.

## Local pipeline: Amuse 3.1.8

Active working pipeline for local image-to-video generation. ComfyUI (via Pinokio install) was attempted and abandoned due to execution failures. Amuse 3.1.8 is the current functional alternative.

Known gap: locating specific models (e.g., Wan 2.2) within Amuse has been difficult — the pipeline works but model availability within the tool's ecosystem isn't fully mapped.

See [[overview]] in local-models for hardware specs and Vulkan/ROCm context.
