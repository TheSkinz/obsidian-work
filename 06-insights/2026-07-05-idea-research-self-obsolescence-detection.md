---
type: review
status: open
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-05
review_after: 2026-08-05
related:
  - [[idea-self-obsolescence-detection]]
  - [[vault-idea-loop-spec]]
  - [[vault-agent-loop-spec]]
  - [[knowledge-system-governance]]
tags: [review, knowledge-system, idea-research, vault-system]
---

# Idea Research — Self-Obsolescence Detection

## Trigger

On-demand run of the Vault Idea Research Loop (first manual run since the loop was set on-demand on 2026-07-05). Idea-seed [[idea-self-obsolescence-detection]] (created 2026-06-30) selected by Jesse for this test run. The seed asks whether the system should actively notice when its *own* artifacts — notes, specs, skills, prior decisions — no longer reflect reality and flag them for retirement, beyond passive `review_after` staleness.

## Evidence

**Internal — the vault already has most of the detection scaffolding, and this session produced live proof the gap is real.**

- The Review Loop already defines **Staleness Check Categories** ([[vault-agent-loop-spec]]): "stale reviews" (past `review_after`, or with an unresolved Decision) and "stale claims" (an operational claim contradicted by a newer source → contradiction note). [[knowledge-system-governance]] carries the `stale` and `deprecated` status values and the "Stale Review" mechanism (`review_after` / `last_reviewed`). So staleness *detection* is specced — but it is **manual**: the review loop is on-demand and a human or agent notices while reading.
- **Scripted coverage is partial.** `tools/vault_lint.py` already catches reference-integrity rot (DEAD-LINK) and confidence/status drift, but it does **not** yet check `review_after` overdue — even though every governance note carries the field. A cheap, unbuilt scripted check sitting right next to a field that already exists.
- **The hard case — a decision silently reversed — is unwatched, and this session produced two.** The vault recorded "keep claude-obsidian for now" (commit `17d8798`) while the `claude-config` repo had already dropped the plugin (`e343e5f`); and the loop specs asserted nightly/weekly schedules that no longer existed. Both were caught by a human doing cross-surface reconciliation, not by any check. This is exactly the "self-obsolescence" the seed names.

**External — obsolescence detection is a known discipline, but only the mechanical slice is reliably automatable.**

- The enterprise framing is **ROT** (Redundant / Obsolete / Trivial data): detection leans on metadata — document age, duplicates, "departed custodians" — plus periodic audits, with AI/ML classification recommending retention or disposal ([Komprise](https://www.komprise.com/glossary_terms/rot-data/), [RecordPoint](https://www.recordpoint.com/blog/how-metadata-driven-classification-helps-eliminate-rot)).
- The closest technical analogue is **detecting outdated code-element references in documentation** — scan docs for references to source that no longer exists, run as a GitHub Action on every commit ([Springer, Empirical Software Engineering](https://link.springer.com/article/10.1007/s10664-023-10397-6)). This is precisely the shape of a lint rule, and the vault already does the link-integrity version of it.
- **Obsidian plugins** cover only the mechanical layer: **Expiring Notes** (a "best-by" date that auto-archives — `review_after` with teeth, [GitHub](https://github.com/joerncodes/obsidian-expiring-notes)), and **find-unlinked-files** / **Janitor** (orphan / empty-note detection, [GitHub](https://github.com/Vinzent03/find-unlinked-files)). None attempt semantic "this was superseded by a later truth."
- The semantic case is studied but hard: an empirical study of **obsolete answers on Stack Overflow** ([arXiv 1903.12282](https://arxiv.org/pdf/1903.12282)) finds obsolescence detectable mainly through domain-specific signals (library versions, timestamps), not general reasoning — i.e. no turnkey semantic detector exists.

## Interpretation

**Sound, but it must be cut in two.**

- The **mechanical slice is sound, cheap, and partly already built.** Scripted `review_after`-overdue detection is a small lint rule that matches proven prior art (Expiring Notes; outdated-reference scanning) and the vault's own scripts-over-attention pillar. It fills a real, named gap.
- The **semantic slice — auto-detecting that a note, spec, or decision has been superseded by a later reality — is premature-bordering-on-a-trap at this scale.** Prior art shows general semantic-obsolescence detection is unreliable, and this session's two real cases were caught exactly where human cross-surface judgment beats a script. A contradiction/reversal detector for a single-user vault of this size is high-cost, low-yield, and would risk false "obsolete" flags on notes that are deliberately historical (the vault keeps frozen logs and closed reviews on purpose).
- A cheap **middle bridge exists:** make obsolescence *declared*, not *inferred* — a `superseded_by:` frontmatter field (pointing at the newer note) that a human sets at the moment a decision is reversed (as this session did in prose for claude-obsidian). A lint rule can then flag any `status: active` note that carries a `superseded_by` link. That converts the hard semantic problem into a cheap structural check, set by human judgment at the one moment the judgment is easy.

## Recommended Action

Bounded build of the mechanical slice only; park the semantic slice.

1. **Build now (Lane 3, small):** add a `REVIEW-OVERDUE` warning rule to `vault_lint.py` (flag notes whose `review_after` is past), shipped with a fixture. It surfaces in `health.md` and matches the Expiring-Notes / outdated-reference prior art. This is the tractable majority of the idea's value.
2. **Adopt a `superseded_by` convention** (Lane 3, additive frontmatter) + a lint rule flagging `status: active` notes that carry it. Cheap, human-declared, zero semantic inference.
3. **Park** the automated semantic reversal-detector — keep "stale claims / superseded decisions" as the on-demand Review Loop's human responsibility, where it already lives in the Staleness Check Categories. Revisit only if vault size makes manual cross-checking stop scaling.

## Decision

- [ ] Build now — bounded (`REVIEW-OVERDUE` lint rule + `superseded_by` convention)
- [ ] Bounded one-shot investigation first
- [ ] Park — leave to the on-demand Review Loop for now
- [ ] Drop

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| | | | |
