---
type: idea-seed
status: unexplored
created: 2026-07-23
tags: [idea, vault-system, future]
---

# LLM-Navigable Vault Map (INDEX description hooks)

Idea seed captured 2026-07-23 from the vault-architecture first-principles triage ([[2026-07-23-triage-vault-architecture-first-principles]], idea 4). The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** `INDEX.md` is a titles-only map, so a session deciding what to load gets no relevance signal beyond the filename. The harness already proves that one-line description hooks drive relevance decisions at two other layers — `MEMORY.md` entries and skill descriptions. A `description:` frontmatter field rendered into INDEX by `vault_index.py` could make the map a genuine recall surface rather than a table of contents.

**To explore:** What shape do Obsidian/PKM power users actually converge on for LLM-navigable vault maps — per-note descriptions, MOC (map-of-content) notes, generated summaries, or embeddings — and what does that prior art say about maintenance cost? What is the backfill cost across ~100 notes, and can the consolidation loop carry it incrementally instead of a one-shot pass? Gating condition: the retrieval-eval run (triage idea 3) — if the eval shows zero retrieval failures, this solves a problem that doesn't exist yet and should stay parked.

<!-- Do not add a Research Findings section by hand — the Vault Idea Research Loop appends that itself as a linked review note in 06-insights/ and updates this file's status to `researched` with a `related:` link. Leave status as `unexplored` when creating a new seed. -->
