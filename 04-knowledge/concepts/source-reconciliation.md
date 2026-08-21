---
type: concept
status: active
source_authority: secondary
confidence: medium
created: 2026-08-21
last_reviewed: 2026-08-21
related:
  - "[[h-2421]]"
  - "[[pdf-extraction]]"
  - "[[knowledge-system-governance]]"
tags: [extraction, ground-truth, heater-cards, method]
---

# Source Reconciliation

Two reusable patterns for the step *after* extraction: deciding whether two
sources actually disagree, and whether a cell you extracted is data at all. Both
were proven on the H-2421 ground-truth workup (2026-07-19) and generalize to any
BOM-versus-datasheet dispute, not just heater tubes.

## A cell is only data if it varies across instances

Engineering workbooks are built from templates, and a template's unfilled cells
survive into every instance that uses it. A cell reading `Ubend to Plug-Head /
Unknown. Validate` looks like a finding — a recorded uncertainty about this
heater. It is not. The same string appeared in two different heaters' workbooks
at the same cell, which makes it a template artifact rather than an observation
about either heater.

The test is cheap and it is the whole pattern: **before treating a cell as a fact
about this instance, check whether it differs across instances.** Identical text
in the same position across two unrelated units is boilerplate. This is the
spreadsheet form of the rule that drawings carry generic notation which is not
project truth.

The reconciliation chain that surfaced it, in order:

1. Piece-count the BOM rather than trusting a summary row.
2. Apply the serpentine identity — returns = tubes − 1 per circuit — as an
   independent check on the count.
3. Roll per-circuit totals up and compare against the heater-total rows.
4. Back-compute from the weight column to separate finned from bare tube and to
   verify wall thickness independently of any stated schedule.
5. Only then compare cells across files, and treat matches as suspect.

Steps 1–4 are each an independent path to the same number. Agreement between two
of them is worth more than any single stated value, because a stated value can be
inherited from a template while a computed one cannot.

## Test the reconciliation before declaring a conflict

When two sources give different tube lengths, the usual reflex is to pick one and
flag the other. Run one check first: **cut length + return development ≈ effective
length**, where return development is approximately π × NPS / 2 per short-radius
return.

On H-2421 this resolved what looked like a hard conflict — the BOM's cut lengths
and the datasheet's effective lengths were *both correct simultaneously*,
differing by 0.25% on the radiant section and 1.6% on the convection section
(192.9 ft against 210 ft convection). Neither source was wrong; they were
measuring different things and no one had said so.

Declaring a conflict destroys information. It sends someone to re-verify a figure
that was already right, and it can push a correct value out of a card in favour of
an equally correct one that answers a different question. Reconcile first, and
flag only when *neither* interpretation closes the gap.

## Why this sits here and not in the extraction notes

Extraction quality is tool-specific and lives in [[pdf-extraction]]. These two
patterns are tool-agnostic — they apply the same way to a Claude read, a Gemini
Gem output, or a value typed in by hand. What they govern is whether an extracted
number means what it appears to mean, which is a reasoning step, not a capability.

Both are instances of a broader rule: a source that supports a claim has not
confirmed it. A template cell supports "this is unknown" without stating it about
this heater, and a datasheet supports a length without stating which length
convention it used.
