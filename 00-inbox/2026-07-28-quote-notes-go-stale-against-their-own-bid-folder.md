<!-- vault-loop: operational — quote-note-vs-bid-folder staleness check design, overlapping Lane 4 reconciliation work (02-facilities, 04-knowledge, health-dashboard scope). Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
<!-- vault-prestaged: 2026-08-10-prestaged-quote-note-bid-folder-staleness.md -->
---
type: capture
status: resolved
created: 2026-07-28
closed: 2026-08-15
tags: [capture, vault-system, data-quality, estimating, quotes]
related:
  - "[[DSP26095]]"
  - "[[rfq-intake-protocol]]"
  - "[[quote-lifecycle]]"
  - "[[2026-07-27-idea-research-quotation-workup-reconciliation-check]]"
---

# A quote note can go stale against its own bid folder and nothing in the vault notices

> **Closed 2026-08-15** by the retirement sweep — bookkeeping only, no new decision. Ruled as DQ-010: the lint-rule option was rejected, because lint is a binary 0-errors gate and cannot distinguish an unsynced folder, an offline machine and a genuinely stale note. Built instead as a `Bid folder` column on the Commercial pipeline table — existence and recency only, base-gated exactly like POINTER-DEAD — which is the mechanism this note correctly identified as missing. It found two real gaps on first run, neither of them the motivating DSP26095 case: DSP26080 records no bid-folder path and DSP26039 no `verified:` date. Value reconciliation was deferred to the pre-send gate rather than guessed from filenames.

**What happened.** On 2026-07-28, asked what the most important task in the vault was, the answer
was built on [[DSP26095]], which read `status: pending`, "Not yet priced — no rates on file", and
carried three items listed as *blocking the quotation*. The bid folder at the path that same note
records already held a finished quotation `.docx`, an exported `.pdf`, and a priced workup
`.xlsx`. The note was roughly a day behind, and the conclusion drawn from it — that the bid was
unpriced, unsent, and against an unknown deadline — was wrong in every part.

**Why nothing caught it.** `50-dashboards/health.md` was all-green at the time, and correctly so
by its own rules. Every check it runs is *internal* to the vault: lint errors, decision-queue
depth, loop heartbeats, inbox age, and a Commercial pipeline table that reads `status`,
`valid-through` and `date-execution` straight out of the frontmatter. **Nothing compares a quote
note against the artifacts in the folder the note itself points at.** A quote note asserting it is
unpriced while a priced workup sits at its own recorded `## Source Files` path is not a state any
current check can see, because both halves are individually well-formed.

The pointer already exists and is already load-bearing — [[rfq-intake-protocol]] step 1 makes the
full OneDrive path mandatory in `## Source Files` precisely so the trail does not go cold, and
POINTER-DEAD already lints that the path still resolves. So the vault knows where the bid folder
is. It just never looks inside it for anything other than existence.

**Why this matters more than a one-off correction.** A stale quote note does not read as stale.
It reads as a confident, well-formed record, and the more complete the note is, the more
authoritative it looks. This one was detailed and internally consistent — which is exactly why it
was believed. The failure mode is not a gap in the vault, it is a *false positive*: the vault
answered a commercial question with high confidence and got it backwards. That is worse than an
acknowledged blank, and it is the thing the whole indexing model is supposed to prevent.

Note also that the staleness window is short. The quote was priced the same day the note was
last verified. Any check whose cadence is weekly would have been just as wrong.

## What a check might look like

Rough, not designed — the point is the shape, and the trigger question is the real one.

For each `type: quote` note whose `status` is not terminal, resolve the `## Source Files` path and
compare what is in the folder against what the note claims:

- A quotation `.docx`/`.pdf` or a workup `.xlsx` bearing this DSP number exists, but the note
  carries no `value` or says it is unpriced.
- The newest artifact in the bid folder is more recent than the note's `verified:` date.
- The note's `value` disagrees with the workup total that `usadebusk-estimating/scripts/extract_workup.py`
  already knows how to read — it reconciles line items to the total and returns `total` directly,
  so this comparison costs nothing new to build.

## Open questions

**Where it lives.** `tools/vault_lint.py` runs over the vault and would be the natural home, but
this check has to reach outside the vault into OneDrive, which no current rule does. That is the
same vault-side/config-side split that [[idea-baseline-staleness-detector]] is stuck on, and the
two may want the same answer.

**Whether it can be a lint rule at all.** A missing OneDrive path, an unsynced folder, or a laptop
offline would all fire it spuriously. It may belong on the health dashboard as a soft signal
rather than in lint as a rule — which fits the existing pattern, since the Commercial pipeline
table is already the place quote-state anomalies surface.

**Whether it overlaps the pending reconciliation check.**
[[2026-07-27-idea-research-quotation-workup-reconciliation-check]] is awaiting decision and
already proposes reading the quotation and the workup together. This is a third comparison in the
same neighbourhood — quotation vs. workup vs. **the vault's own note** — and the
[[2026-07-28-pasted-emf-quote-number-second-near-miss|EMF near-miss]] filed the same day argues
for a fourth (the assigned DSP number as an external anchor). Four assertions over the same three
artifacts is one build, not four ideas. Worth deciding them together rather than separately.
