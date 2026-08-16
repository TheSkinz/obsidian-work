<!-- ROUTED 2026-07-20 — content landed in 07-llms/self-improving-systems.md. Retained as the original capture record. -->
---
type: note
status: complete
created: 2026-07-12
closed: 2026-08-15
tags: [llm, vault-system, decision]
---

# Evaluated: automated GitHub skill-discovery pipeline

> **Closed 2026-08-15** by the retirement sweep — bookkeeping only. The decision was made and the content routed on 2026-07-20 (marker above); the note simply carried no `status:` field, so the Terminal-Note Sweep could never move it. It is one of the two notes [[2026-07-29-statusless-notes-invisible-to-the-sweep]] identified as "done and stuck." Note that the rule count below ("7 rules") is stale as a description of the linter — it is now 16 — but it is left as written, since it records what was true when the decision was made and the decision does not turn on it.

Read a post describing an 8-agent pipeline (Scout → Filter → Reader → Workflow Extractor → Skill Score → Skill Generator → Reviewer → Publisher) that scans GitHub for reusable AI workflows and auto-generates Agent Skills, gated by human PR review.

**Decision: not adopting.** The vault already covers the useful parts of this pattern at a scale that fits a single-operator system:

- Doc-before-code reading order — already the norm (README/docs before source)
- Deterministic checks before LLM judgment — already implemented via `tools/vault_lint.py` (7 rules) and `tools/vault_health.py`
- Human-approves-the-output — already how skill/SOP changes get made

Standing up a multi-agent GitHub-scanning pipeline would add discovery/triage overhead without solving a real bottleneck here (skills aren't scarce; time to use them is). No further action.
