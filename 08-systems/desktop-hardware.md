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

**Wireless card antenna connectors.** The wireless card uses proprietary ASUS Q-Antenna quick-connectors, not standard screw-on RP-SMA barrels. This matters for any future antenna swap or wireless hardware troubleshooting — RP-SMA accessories won't fit without an adapter.

**RAM upgrade path.** 64GB is the first recommended upgrade if local AI workloads, large PDF/OCR batch jobs, engineering drawing processing, or heavy multitasking become priorities. No urgent compute upgrade needed for gaming alone at current config.

**AMD/CUDA tradeoff.** Vulkan-backed local AI inference works, but CUDA-first NVIDIA tooling (many AI frameworks, ComfyUI extensions, ROCm-dependent workflows) remains smoother for a wide range of AI tasks. This is a known tradeoff of the current GPU choice — worth tracking as RDNA 4 tooling matures.
