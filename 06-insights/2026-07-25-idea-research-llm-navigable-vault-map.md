---
type: review
status: open
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-25
review_after: 2026-08-25
related:
  - [[idea-llm-navigable-vault-map]]
  - [[2026-07-23-triage-vault-architecture-first-principles]]
  - [[2026-07-23-retrieval-eval-run]]
  - [[vault-idea-loop-spec]]
tags: [review, knowledge-system, idea-research, retrieval, already-covered]
---

# Idea Research — LLM-Navigable Vault Map (INDEX Description Hooks)

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. Two idea-seeds were `unexplored` in `00-inbox/`: this one (`created: 2026-07-23`) and `idea-orphaned-equipment-rules-proposal-path` (`created: 2026-07-24`). This one is older by frontmatter `created` date, so it was processed this run per the one-item selection rule.

## Evidence

**Internal — the seed's own gating condition already resolved, before this loop even picked the seed up.** The seed text is explicit: "Gating condition: the retrieval-eval run (triage idea 3) — if the eval shows zero retrieval failures, this solves a problem that doesn't exist yet and should stay parked." That test already ran, same day the seed was filed. [[2026-07-23-triage-vault-architecture-first-principles]] §3 defined the criterion (2+ failures → fold a retrieval-eval pass into the consolidation loop; 0-1 → retrieval isn't the constraint, stop) and its Apply Log records the result: "ran cold in a fresh session: all 10 KS/USA questions answered against pass criteria, 10/10 pass, 0 hard failures... Criterion (≤1 failure) → stop." [[2026-07-23-retrieval-eval-run]] is the underlying result note. The triage note's own §4 disposition for this exact idea reads "Idea 4 stays parked (gate not met)." Nothing has changed since — no new eval run, no reported retrieval friction in the interim three idea-research runs (07-24 lint-lock, and this one).

**Internal — vault scale check.** As of 2026-07-25, `01-context/02-facilities/04-knowledge/06-insights/07-llms/08-systems/09-interests` together hold 129 markdown notes, close to the seed's own "~100 notes" backfill-cost estimate. `tools/vault_index.py` confirms the seed's premise about current state: `INDEX.md` entries are title-plus-subfolder only (a wikilink to the note's filename, an em-dash, its title, and its subfolder in parens), no description or summary field, so there is genuinely no relevance signal beyond filename/title today.

**External — Obsidian/PKM power-user prior art converges on MOC (Map of Content), not per-note description frontmatter, as the standard pattern for LLM-navigable vaults.** Multiple 2026 guides (Obsidian Copilot plugin docs, general PKM/AI-vault writeups) describe generating MOC notes that cluster 3-5 related notes per topic as the dominant technique for giving an LLM agent a navigable entry point into a large vault — closer to this vault's own `01-context/` + section-heading structure than to a MEMORY.md-style one-line-per-item description field. None of the sources found describe per-note `description:` frontmatter rendered into an index as an established convention; it would be a novel-to-this-vault design, not an import of proven prior art. Sources: [Map of Content (MOC) — NateCue](https://www.natecue.com/en/learn/productivity/map-of-content/), [Obsidian MCP Guide: AI Search & Retrieval (2026) — Blake Crosley](https://blakecrosley.com/guides/obsidian), [Complete Guide to Obsidian 2026 — Oflight](https://www.oflight.co.jp/en/columns/obsidian-knowledge-management-guide-2026).

**External — a directly relevant scale finding.** General guidance on LLM knowledge-base architecture notes that "at smaller scales (around 100 articles and roughly 400,000 words), index files and LLM context windows are enough to navigate without embedding infrastructure," and that the approach starts to strain only "beyond that scale with multiple large repos and years of decision history." This vault's 129 notes sit right at that threshold on the sub-100k-word end, not past it — which is independent, external corroboration of the same conclusion the internal retrieval-eval already reached: title-based navigation plus full-load of `01-context/` is still adequate at this vault's current size, not a near-miss about to break.

## Interpretation

**Already covered — the seed's own gate closed it.** This isn't a case of the idea being wrong or infeasible; it's a case where the seed shipped with an explicit, well-designed test-before-build condition, and that condition already ran and returned the "don't build" answer on the same day the seed was filed. Re-researching "what's the right shape" (MOC vs. description hooks vs. embeddings) would be answering a question the seed itself said not to bother answering yet. For the record, though: if the gate is ever re-tripped, external prior art leans toward MOC-style topic clusters over a MEMORY.md-style per-note description field — a genuinely different design than the one sketched in the seed's "Tentative read," worth knowing before any future build starts from the description-hook framing by default.

## Recommended Action

**Stay parked — no action.** Do not re-open until a future retrieval-eval run (per [[knowledge-system-evaluation-questions]]) actually logs 2 or more failures, matching idea 3's own re-trigger criterion. No standing task or reminder needed beyond that criterion already living in the triage note; this review note exists mainly to close the loop's queue and leave a record that the "what prior art fits" question was checked once, with a preliminary lean toward MOC over description-frontmatter if the seed ever gets revived.

## Decision

- [ ] Build now
- [ ] Approved with edits
- [ ] Park (confirm continued parked status)
- [ ] Drop entirely

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
|  |  |  |  |
