---
type: idea-seed
status: gated
created: 2026-07-23
revisit-trigger: "Vault reaches 450 live notes (292 at the time of writing, 2026-08-15) -> re-run the retrieval eval in [[knowledge-system-evaluation-questions]]; if it shows failures, this idea unparks, and if it does not, re-park at the next threshold [machine: note-count>=450]"
related:
  - [[2026-07-25-idea-research-llm-navigable-vault-map]]
tags: [idea, vault-system, future]
---

# LLM-Navigable Vault Map (INDEX description hooks)

> **Given a wake condition 2026-08-15** (Jesse, retirement sweep). This was ruled "parked, not killed" on 2026-07-23 after the retrieval eval returned 10/10 with zero hard failures — but no `revisit-trigger:` was recorded, so nothing would ever have raised it again. A park with no wake condition is a retirement that will not admit it, and this one was additionally hidden behind `status: researched`, which the Terminal-Note Sweep may not touch.
>
> **The trigger is on the eval, not on this idea.** The seed's own gating condition was "if the eval shows retrieval failures," and the eval is what answers that. If the re-run also comes back clean, re-park at a higher threshold rather than treating a second pass as approval to build.
>
> **The eval's own "~100 notes" figure is not reproducible, and the threshold is deliberately not anchored to it.** [[2026-07-23-retrieval-eval-run]] concludes "retrieval is not the binding constraint at this vault size (~100 notes)." Counted this session against the commit as of that date, the scanned population was **169** — the same basis `vault_health.py` uses, excluding `archive/`, `templates/`, `tools/` and `_OUTPUTS/`. The stated figure was already low by about 70% when written. It is the same defect class as the Syncrude ~6 ft/hr number: a round figure that circulates because nobody divides it out. So the trigger is anchored to the count the script actually computes, with today's value (292) written into the condition text, and it fires at 450 — roughly 2.7× the size at which the eval last passed clean.
>
> This required a small tooling change to be real: `[machine: note-count>=N]` did not exist, and `tools/vault_health.py` degrades an unrecognized `[machine: …]` token to event-shaped wording rather than failing loudly — so writing the token without adding it would have produced a trigger that *looked* checked and never was. That is the DQ-005 failure mode exactly. Token added the same session.

Idea seed captured 2026-07-23 from the vault-architecture first-principles triage ([[2026-07-23-triage-vault-architecture-first-principles]], idea 4). The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** `INDEX.md` is a titles-only map, so a session deciding what to load gets no relevance signal beyond the filename. The harness already proves that one-line description hooks drive relevance decisions at two other layers — `MEMORY.md` entries and skill descriptions. A `description:` frontmatter field rendered into INDEX by `vault_index.py` could make the map a genuine recall surface rather than a table of contents.

**To explore:** What shape do Obsidian/PKM power users actually converge on for LLM-navigable vault maps — per-note descriptions, MOC (map-of-content) notes, generated summaries, or embeddings — and what does that prior art say about maintenance cost? What is the backfill cost across ~100 notes, and can the consolidation loop carry it incrementally instead of a one-shot pass? Gating condition: the retrieval-eval run (triage idea 3) — if the eval shows zero retrieval failures, this solves a problem that doesn't exist yet and should stay parked.

<!-- Do not add a Research Findings section by hand — the Vault Idea Research Loop appends that itself as a linked review note in 06-reviews/ and updates this file's status to `researched` with a `related:` link. Leave status as `unexplored` when creating a new seed. -->
