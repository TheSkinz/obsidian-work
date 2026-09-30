---
type: reference
status: active
source_authority: vendor-docs-cached
confidence: medium
created: 2026-09-30
review_after: 2026-12-30
related:
  - [[opus-5]]
tags: [reference, claude, models, opus-5-5, routing]
---

# Claude Opus 5.5 — Release Capture

> **Provenance & freshness.** Read 2026-09-30 from the `claude-api` skill bundled with Claude Code 2.1.284, whose model table is marked *cached 2026-09-25*. Not checked against an anthropic.com release page — do that before citing a price or a date to anyone.

Claude Code switched this vault's sessions from Opus 5 to Opus 5.5 on 2026-09-30, mid-session (commit attribution changed; the model reported `claude-opus-5-5`).

| | Opus 5.5 | Opus 5 |
|---|---|---|
| Model ID | `claude-opus-5-5` | `claude-opus-5` |
| Price in / out per MTok | $4 / $20 | $5 / $25 |
| Context / max output | 1M / 128K | 1M / 128K |
| Default effort | `medium` | `high` |
| Thinking | cannot be disabled | can be disabled at `high` or below |

The skill names Opus 5.5 the default model and Opus 5's direct successor, with the same tokenizer and feature set. The API breaking changes (forced `tool_choice` 400s, thinking bound to the model, a new computer-use toolset) matter only to code calling the API; nothing in this vault or the config repo does.

## What this means here

- **The regression battery is stale.** All six frozen outputs were cut on `claude-opus-5`, and the battery README makes a model change trigger #1 — replay the whole battery. Not yet done as of 2026-09-30.
- **The default effort dropped a level.** If output quality shifts on hard estimating or extraction work, check the session effort before blaming the model.
- **No skill hardcodes a model id**, so nothing needs editing for the switch itself.
