---
title: Desktop Hardware
created: 2026-06-29
tags: [hardware, workstation, amd]
---

# Desktop Hardware

| Component | Spec |
|---|---|
| CPU | AMD Ryzen 7 9800X3D |
| GPU | AMD RX 9070 XT (RDNA 4) |
| RAM | 32GB DDR5-6000 |
| Monitor | Acer Nitro, 4K / 144Hz |
| OS | Windows 11 Home |

## Known issues

**VRR disabled.** Variable refresh rate causes flickering on this monitor; left disabled. Static 4K/144Hz is the stable config.

**RDNA 4 / AI inference.** ROCm (AMD's GPU compute stack for AI) is Linux-only on RDNA 4 as of mid-2026. On Windows, local model inference runs via Vulkan backend in LM Studio. See [[overview]] in local-models for inference setup.

## Notes

The 9800X3D's 3D V-Cache is designed for gaming workloads with large working sets; not especially relevant for development or LLM inference (which is GPU-bound). The RX 9070 XT is the bottleneck for local inference quality — VRAM determines the maximum quantized model size that fits in a single pass.
