---
type: idea-seed
status: unexplored
created: 2026-08-21
tags: [idea, vault-lint, data-quality, DQ-017]
related:
  - "[[2026-07-30-idea-research-vault-stats-layer]]"
---

# Cross-field lint rules — the five-defects class

Split out of **DQ-017** on 2026-08-21. This is Track 1 of [[2026-07-30-idea-research-vault-stats-layer]], which was bundled into the per-coilset schema decision in 2026-08-01 because both were parked, not because they interact. Track 1 has **no dependency on the Task Durations schema** — it is a `vault_lint.py` build and rides that file's own trigger.

**The gap, confirmed by reading the linter.** None of `vault_lint.py`'s check functions do cross-field numeric or business-rule validation. The closest, `check_durations_header`, validates table *structure*, not value relationships between columns.

**The five defects, all rule-shaped rather than statistical** — a value checked against another field or a fixed rule, not against a fitted distribution:

- Pig OD vs. governing tube ID + tolerance
- Footage arithmetic (tubes × length vs. stated total)
- A length recorded in a diameter column — column type / unit mismatch
- Two spellings of one alloy — name normalization
- Rate-magnitude sanity against sibling rates

**Why rules and not stats.** Small-sample outlier methods all need *some* distribution to compare against, and most dimensions here have effectively none. None of the five defects was found that way — all five are exact checks (an inequality, an arithmetic identity, a type mismatch, a string-equality-after-normalization, a hardcoded reference rate) that need no distribution at all. This is the standard shape of the class; Pandera exists for exactly it.

**Live example already sitting in the vault:** `H19.md:100` records a Honeycomb pig at `104"` with an inline note that it "appears to be a length, not an OD (104" OD impossible on this coil)." That is the column-type rule firing by hand, in prose, on one row.

**To explore:**
- Which of the five earn a rule, and at `error` or `warning` tier?
- Does the pig-OD rule reuse the max-pig-OD cap already recorded per card, or restate it?
- Each new rule needs a fixture in `tools/fixtures/` — that is the real cost, not the check itself.

**Gate:** None — researchable and buildable now. Best scheduled the next time `vault_lint.py` is opened for a reason carrying its own weight, per the same convention DQ-017 rode. Note that a one-line regex fix does **not** meet that bar (recorded in the source note, 2026-08-01).
