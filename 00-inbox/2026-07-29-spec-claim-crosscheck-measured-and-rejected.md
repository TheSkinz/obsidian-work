---
type: insight
status: resolved
created: 2026-07-29
tags: [inbox, vault-system, lint, measurement, negative-result]
---

# Cross-checking specs against code: measured, and not worth a lint rule

Proposed after the loop-spec audits found a spec asserting a `scheduled` flag in
`tools/vault_health.py` that has never existed. The idea: lint every backticked claim a note
makes about the tooling — file paths, rule names, identifiers, commit prefixes — against the
code. Built as a one-off audit first rather than a rule, per the back-test-before-build rule.

## Result

**Rejected. The claim surface is not regular enough to check lexically.**

A broad pass over 465 backticked spans produced ~55 hits, nearly all noise. A tightened pass
keeping only the two shapes that had shown any yield — vault-relative file paths and lint rule
names — checked 278 claims and produced **4 hits, all four false positives on inspection**:

| Hit | Why it was correct as written |
|---|---|
| `TUBE-GEOM-HEADER` not a rule | The note proposes it and says "Not built" — a proposal, not an assertion. |
| `templates/_facility-template.md` missing | The sentence states it **was removed 2026-07-06**. A negative claim; the checker inverted it. |
| `tools/render_drawing_snippets.py` missing | Path is in the **Grok repo**, not the vault. Same `tools/` prefix, different root. |
| `00-inbox/<name>.md` missing | An illustrative placeholder inside a spec's prose. |

Backticks in this vault carry frontmatter keys (`status:`), job and quote numbers (`R501`,
`USA26031`), format placeholders (`DSPNNNNN`, `DQ-NNN`), other repos' paths, proposed-but-unbuilt
rule names, and negative existence claims. Separating an assertion from a negation from a
proposal is semantic, not lexical — which is precisely what a lint rule cannot do.

Same shape as the WORD-DELTA diff-shape gate killed on 2026-07-28: an intent-vs-effect check
needs the stated intent as input and cannot recover it from the artifact alone.

## What did have yield, and is now procedure not tooling

Two real defects came out of the exercise, and neither was found by the generic checker:

1. The `scheduled`-flag claim — found by **reading the spec against the code**, which is what the
   loop-spec review already does. No rule needed; the review is the mechanism.
2. A live broken path pointer on [[DSP26085]] created by the same day's Terminal-Note Sweep —
   found by grepping the ten moved basenames specifically. That narrow check is unambiguous and
   cheap, so it is now a step in the sweep procedure in [[vault-capture-loop-spec]] rather than a
   rule. It also corrected a false safety claim in that spec: a plain move keeps *wikilinks*
   green, not backticked path references, and nothing lints the latter.

## Durable finding

A check is worth automating when the thing being checked has one unambiguous form. Wikilinks
have one. Absolute source paths have one. "A sentence mentioning a file" does not — and the
tell is that the false-positive classes are *semantic categories*, not parsing edge cases.
