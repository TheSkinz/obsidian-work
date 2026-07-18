---
type: note
created: 2026-07-12
tags: [llm, vault-system, decision]
---

# Evaluated: automated GitHub skill-discovery pipeline

Read a post describing an 8-agent pipeline (Scout → Filter → Reader → Workflow Extractor → Skill Score → Skill Generator → Reviewer → Publisher) that scans GitHub for reusable AI workflows and auto-generates Agent Skills, gated by human PR review.

**Decision: not adopting.** The vault already covers the useful parts of this pattern at a scale that fits a single-operator system:

- Doc-before-code reading order — already the norm (README/docs before source)
- Deterministic checks before LLM judgment — already implemented via `tools/vault_lint.py` (7 rules) and `tools/vault_health.py`
- Human-approves-the-output — already how skill/SOP changes get made

Standing up a multi-agent GitHub-scanning pipeline would add discovery/triage overhead without solving a real bottleneck here (skills aren't scarce; time to use them is). No further action.
