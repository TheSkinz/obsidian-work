---
title: Local Models — Overview
created: 2026-06-29
tags: [local-models, lm-studio, vulkan, rdna4]
---

# Local Models

Local model inference via LM Studio on the desktop workstation. Primary motivation: offline capability, privacy for sensitive job data, and latency-free inference for tasks that don't need frontier-model quality.

## Environment

- **Runtime:** LM Studio
- **GPU:** AMD RX 9070 XT (RDNA 4 architecture)
- **Backend:** Vulkan (AMD's supported path; ROCm is Linux-only on RDNA 4 as of mid-2026)
- **Host:** Ryzen 7 9800X3D, 32GB DDR5-6000 — see [[desktop-hardware]] for full spec

## Model evaluations

| Tool / Model | Task | Result |
|---|---|---|
| ComfyUI (via Pinokio) | Local image generation | Failed to execute — abandoned |
| Amuse 3.1.8 | Local image-to-video generation | Active working pipeline — difficulty locating specific models (e.g., Wan 2.2) but pipeline itself functional |

See [[ai-image-generation]] for image-generation workflow details.

## Use case candidates

Tasks that make sense for local inference in this context: document classification, structured extraction from clean text, draft generation for review, chat-style Q&A on locally stored knowledge. Tasks that don't: vision on complex engineering drawings, multi-step reasoning chains requiring high accuracy, anything needing real-time web data.
