---
title: Grok — Heater Drawing Extraction Strategy
created: 2026-07-09
tags: [grok, xai, vision, drawing-extraction, engineering]
---

# Drawing extraction strategy

Canonical method decisions from the Grok repo (`.grok/skills/heater-drawing-analysis/SKILL.md`). Package geometry stays in that repo (`packages/*/analysis/`, `proposal-tech-data.md`); this note is the distilled cross-platform record for the vault. See [[overview]] for Grok's broader role.

## Problem class

Customer heater packages are often **image / uncontrolled VIEW prints**, not clean vector text PDFs. Sparse PDF text layers, vertical CAD OCR, MarkItDown, and default full-page multimodal vision all fail or under-read dense BOMs, title blocks, and mid-page tables. That is the right diagnosis for the pilot (Valero Jean-Gaulin TA2027) and the default assumption until a package proves a real text layer.

## Primary method (adopted)

**Two-pass high-DPI local tiles + domain-aware vision + evidence worksheets.**

1. **Pass A — overview:** render full pages cheaply (`--preset overview`, ~120 dpi); classify page type; mark high vs low yield.
2. **Pass B — dense:** only high-value pages (`--preset dense`: 288 dpi, 3×3, max-edge 3500, skip-full, capped PNGs). Prefer one primary crop set (3×3 **or** title-block/corners), not all at once.
3. Agent reads **winning tiles** with vision; writes `analysis/<Tag>.md` with evidence + confidence; drafts cards when solid.
4. Snippets under `packages/*/snippets/` are **regenerable and gitignored** — delete freely; re-render via `tools/render_drawing_snippets.py`.

This matches how field engineers read drawings (overview, then zoom) and the architecture engineering-drawing research rediscovers: **region → high-res read → structure**. Generic agents often skip the zoom step and stall on full-page vision.

### Pilot lesson (do not repeat)

Kitchen-sink dense crops on every page (3×3 + title-block + br/bl, dual full-res + `_vis`) produced ~400 PNGs / ~180 MB. Purged 2026-07-09. Accuracy of the zoom idea was good; breadth before triage was waste.

Title-block alone misses mid-page / upper-right tables (H405 radiant Liste). Keep 3×3 available when layout is unknown.

## Hybrid layers (optional assists — not replacements)

| Layer | Role | When |
|-------|------|------|
| Native PDF text extract | Fast path | Real text layer present and numbers check out |
| Two-pass tiles + VLM | **Primary SoT for image prints** | Default |
| OCR engine on the same tiles (e.g. PaddleOCR-class) | Speed BOM row copy; agent still verifies | Optional A/B; never sole SoT |
| Acrobat / Bluebeam | Human spot-check one sticky field | Exception only |
| P&ID symbol / graph CV (Azure/AWS samples, commercial) | Plant topology digitization | Skip unless client program needs full connectivity |
| Fine-tuned detectors / drawing-specific VLMs | Scale automation | Only if package volume justifies training |

### What not to chase (current bid volume)

- Making Adobe OCR or AI Assistant the package pipeline (prose/OCR soup; no heater-card semantics).
- Full P&ID graph ML as the first step for estimating geometry.
- Always denser than 3×3 or always dual full-res + vis copies.
- Committing snippet PNGs or vault-promoting crops.

## Efficiency definition

Not "fewest tokens on one lucky page." Reliable geometry with evidence in a few hours per package, without a labeled training set, across multi-format client VIEW prints. For that bar, selective high-DPI tiles + domain skill + worksheets beat both pure full-page LLM and pure desktop OCR.

## Status

Experimental, single pilot (Valero Jean-Gaulin TA2027) as of 2026-07-09. Not yet benchmarked against Claude's drawing extraction path (Gemini Gem retired, extraction moved to Claude — see [[gem-drawing-extraction]]). Promote this method into a shared USADeBusk skill only after it validates across a second package.
