---
type: eval-result
status: complete
source_authority: primary
confidence: high
created: 2026-07-23
related:
  - knowledge-system-evaluation-questions
  - 2026-07-23-triage-vault-architecture-first-principles
  - idea-llm-navigable-vault-map
tags: [knowledge-system, evaluation, retrieval]
---

# Retrieval Eval Run — 2026-07-23

First execution of the retrieval-eval defined in [[knowledge-system-evaluation-questions]] (created 2026-06-26, never run until now). Test 3 from [[2026-07-23-triage-vault-architecture-first-principles]]. A fresh session answered all ten KS/USA questions cold, retrieving from the vault rather than from memory, and graded each against the note's own pass criteria.

## Result

**10 / 10 pass, 0 hard failures.**

| ID | Verdict | Primary source retrieved |
|---|---|---|
| KS-001 | pass | [[knowledge-system-governance]] Source Hierarchy + contradiction-note rule |
| KS-002 | pass | [[_canonical-heater-card]] + CLAUDE.md schema authority |
| KS-003 | pass | [[sop-formatting-standard]] |
| KS-004 | pass (scan) | `00-inbox/` frontmatter (no single by-status surface) |
| KS-005 | pass | [[health]] + `review_after`/`status` fields |
| USA-001 | pass | usadebusk-core terminology lock (dual-pumper banned) |
| USA-002 | pass | canonical-card stainless passivation block |
| USA-003 | pass | canonical-card quarantined Job Options section |
| USA-004 | pass | SOP standard + card schema (required-not-assumed inputs) |
| USA-005 | pass (deep) | governance Retrieval-Feedback + 2026-07-06 Lane-1 facility delegation |

## Decision

Per the test criterion (≥2 failures → fold a quarterly eval pass into the consolidation loop; ≤1 → retrieval isn't the constraint, record and stop): **stop.** No sixth loop, no quarterly pass. Retrieval is not the binding constraint at this vault size (~100 notes). [[idea-llm-navigable-vault-map]] (INDEX description hooks) was gated on this run producing failures; it did not, so the idea stays parked, not killed.

## Latent risks (passed, but worth recording)

Two questions cleared their criteria only because retrieval read the *whole* relevant note, not because the note surfaces the current answer cleanly. These are the failure modes to watch if the vault grows or if a weaker/faster session runs the same query:

- **USA-005 — stale lead paragraph.** [[knowledge-system-governance]] opens with "The vault improves through reviewable proposals, not silent rewrites," which is the pre-2026-07-06 rule. The Lane-1 carve-out that inverts this for heater-card/facility facts lives further down in the Delegated Autonomy Policy. A retrieval that stops at the Operating Principle gives a confidently stale answer. Not fixed here; noted as the one governance passage whose top line no longer matches its own body.
- **KS-004 — scan, not lookup.** No note is an inbox-by-status index; the answer is reconstructed by scanning 26 files' frontmatter. Fine at this size. If inbox volume grows, a generated inbox-by-status view (health.py already scans the folder) would convert this from a scan to a lookup — a cheap future move, not warranted now.

Neither rose to a `type: question` note (that's reserved for failures). They are recorded here as the substantive output of a clean run.
