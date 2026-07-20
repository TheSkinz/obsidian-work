---
type: review
status: open
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-20
review_after: 2026-08-20
related:
  - [[idea-hardened-extraction-corpus-vision-arm]]
  - [[vault-idea-loop-spec]]
tags: [review, knowledge-system, idea-research, evaluation, leverage-repo]
---

# Idea Research — Hardened Extraction Corpus + Vision Arm

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. Four idea-seeds were `unexplored` in `00-inbox/`; this one and `idea-portfolio-revival-pass` share the earliest `created` frontmatter date and the same originating commit (`557fbd3`, 2026-07-19 19:30:24). Picked this one as the tiebreak (alphabetically first, no other ordering signal in the commit).

## Evidence

**Internal — the seed's core factual claim checks out exactly.** `07-llms/self-improving-systems.md` confirms the 2026-07-06 thesis-experiment run: all three conditions (frontier 1-shot, cheap 1-shot, cheap+gate+retry) hit 100% pass rate — genuinely inconclusive, not a scoring artifact (that was a separate, already-resolved issue: a matcher blind spot on numeric-with-unit values, fixed in `DESIGN.md` amendment v2). The design doc's own next step is stated plainly: "a harder corpus is needed to actually test the claim; more items at the current difficulty won't help."

**Internal — the corpus is not purely text-only or trap-free already; the seed's framing is slightly behind.** `leverage/experiments/thesis/DESIGN.md` and `manifest.yaml` show the existing 30-item corpus already has an `h` (hard) category with `h07–h10` as designed absent-field traps, scored separately for hallucination-resistance. So one of the seed's "To explore" questions — "what makes an item genuinely hard" — is partially answered by the repo's own prior design (conflicts, distractor numbers, mixed formats, absent-field traps are already the stated hard-category recipe). What's missing is headroom, not a hardness *taxonomy*: the existing hard items still saturated. Confirmed via `grep` on `backends.py`/`run.py`: zero image/vision handling exists anywhere in the harness — the vision-arm half of the seed is correctly scoped as new work, not an extension of existing code.

**Internal — the seed's own forcing premise (metered/expiring frontier access) is now stale.** `feedback-fable-cost-after-july12` (memory, updated 2026-07-20T02:14:45Z — after this seed was written) records that Jesse upgraded to Claude Max on 2026-07-19, making Fable 5 access ongoing rather than expiring. The seed's "To explore" section asks "whether the frontier condition can still be run economically at post-window API pricing, or whether any frontier baseline has to come from captures frozen during the access window" — that question is now moot; there is no window closing. This removes the time-pressure argument for reviving the experiment now rather than later.

**Internal — this idea was one of three explicitly deferred, not prioritized, in the same-night allocation decision.** `change-log.md` (2026-07-19 entry) records the Fable-window allocation: fallback-regression fixtures first (built same night, see `idea-fallback-regression-battery.md` status `executed`), then H-2421 ground-truth drawing extraction (live money, DSP26080), then a Fable-as-adversary run on the estimating skill. This seed was captured as one of "three un-homed ideas... for the nightly idea loop" — i.e., explicitly not selected for the window, but also not rejected outright the way five other proposed meta-systems were that same session.

**Internal — the `leverage` repo's own prune rule doesn't yet apply.** `idea-portfolio-revival-pass.md` cites the repo's promotion rules: no runs in 90 days is a prune candidate. The repo has been dormant since 2026-07-02 (git log confirms last commit `d9bf723`) — 18 days as of this run, well short of 90. (Note: `project-leverage-repo` and `feedback-fable-cost-after-july12`, cited above, are agent-memory records outside this vault, not vault notes — referenced here by name only, no wikilink, since the linter correctly treats them as unresolvable.)

**External — established practice for hardening a saturated extraction eval exists and points at specific, checkable levers.** Benchmark saturation above ~85% pass rate is a documented, named failure mode (ceiling effect) that makes a benchmark statistically uninformative ([Brenndoerfer](https://mbrenndoerfer.com/writing/benchmark-saturation-ai-evaluation-metrics); [arXiv:2602.16763](https://arxiv.org/html/2602.16763v1)). Concrete hardening techniques found in the literature, several directly applicable to this corpus: raising distractor density (one study went from 4 to 26 distractor options and saw sharp score drops, [arXiv:2502.06738](https://arxiv.org/html/2502.06738v1)); widening schema breadth and field-type heterogeneity, with mixed correctness criteria per field type and forced omission-vs-hallucination distinction ([ExtractBench, arXiv:2602.12247](https://arxiv.org/html/2602.12247v2)); and per-item difficulty calibration via a pilot/human-adjudication pass using Item Response Theory before the corpus is trusted ([arXiv:2505.15055](https://arxiv.org/pdf/2505.15055)). None of these require a vision arm to apply — they're purely about the text corpus's difficulty design, and could raise headroom on the existing thesis experiment without touching the harness's image support at all.

**External — public vision-extraction benchmarks exist that are closer to this vault's actual pain point than building from scratch, though none are engineering-drawing-specific enough to reuse directly.** General document-KIE benchmarks (DocVQA, FUNSD, SROIE/CORD, Kleister) are the standard baseline. Closer analogues: **RealKIE** (SEC filings, contracts, complex tables, poor text serialization — [arXiv:2403.20101](https://arxiv.org/abs/2403.20101)) and **VRDU** (nested entities, multi-column/table templates — [Semantic Scholar](https://www.semanticscholar.org/paper/VRDU:-A-Benchmark-for-Visually-rich-Document-Wang-Zhou/53828280509cd9c90468e79e01a2ae61dfb9dc11)) model messy structured-table extraction well but aren't engineering drawings. **AECV-Bench** (120 floor plans, object counting, OCR/spatial/comparative reasoning, [arXiv:2601.04819](https://arxiv.org/abs/2601.04819)) and **MechVQA** ([arXiv:2605.30794](https://arxiv.org/html/2605.30794)) are architecture/mechanical-drawing benchmarks — the closest public analogues to heater GA drawings and BOM tables, but still a different domain and won't cover heater-specific tube-count/BOM extraction without adaptation. Documented finding relevant to design: current VLMs handle text-in-drawing extraction reasonably but struggle with symbolic/spatial reasoning — useful signal that a BOM-table vision arm (text-in-image extraction) is a more tractable first slice than symbol interpretation.

**External — adding a vision arm to an existing text harness is a known, bounded extension pattern, not a rebuild.** `lm-evaluation-harness` added multimodal support (`hf-multimodal`, `vllm-vlm`) as an explicit extension of its existing text harness — same item schema plus an image field ([GitHub](https://github.com/EleutherAI/lm-evaluation-harness)). Documented pitfall worth carrying into any design: models can score well while barely attending to the image, so an image-ablation check (wrong image, or image stripped) should be part of the validity test, not just raw accuracy ([Galileo AI](https://galileo.ai/blog/multimodal-llm-guide-evaluation)).

## Interpretation

**Sound in substance, premature in timing.** The seed's technical read holds up against both the repo's own design doc and the vault's own record of the 2026-07-06 result — this isn't a case of a misremembered or overstated problem. But two of the three things that would make reviving this urgent *now* have changed since the seed was written: the forcing deadline (metered frontier access) is gone as of the Max upgrade, and the same-night allocation decision already chose three other, higher-priority uses for available capacity (one already executed, two involving live commercial money). The 90-day dormancy prune rule the sibling seed cites also hasn't triggered yet. Nothing here argues the idea is wrong — only that "revive this specific idle project" competes weakly against live-money work with no clock forcing a decision either way.

The external research changes the *shape* of a future revival, not the recommendation to wait: hardening the text corpus (distractor density, schema breadth, difficulty calibration) is well-trodden and could be done without the vision arm at all, as a smaller, separable step from the vision-arm question — the two halves of this seed don't have to be revived together. And the vision-arm half, if pursued, should start from adapting an existing document-extraction benchmark's design principles (RealKIE/VRDU for messy tables, AECV-Bench/MechVQA for drawing-domain precedent) rather than designing item format and harness support from a blank page — though none of those datasets can be reused wholesale given the customer-confidentiality constraint the seed itself already flagged.

## Recommended Action

Park, not drop — the technical case is sound and the corpus/harness groundwork (traps, gate scoring, DESIGN.md amendment discipline) is real prior investment worth returning to. Revisit when one of two things happens: (1) a live bid or extraction task creates actual pain around cheap-vs-frontier routing on vision extraction specifically (the same trigger pattern that justified building the fallback-regression battery), or (2) the `leverage` repo crosses its own 90-day dormancy mark (~2026-09-30) and comes up for a portfolio-wide revive/kill call alongside the other parked leverage-repo work — at that point, treat this as two separable sub-decisions rather than one: hardening the text corpus (bounded, no new harness work, techniques above) vs. adding the vision arm (real harness + pre-registration-amendment work, should start from RealKIE/VRDU/AECV-Bench design patterns rather than from scratch).

## Decision

- [ ] Build now — harden corpus + add vision arm together
- [ ] Bounded one-shot investigation first
- [ ] Park — revisit on live extraction-routing pain or the 90-day leverage-repo dormancy checkpoint
- [ ] Drop

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
