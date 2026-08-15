---
type: note
status: inbox
created: 2026-08-15
tags: [inbox, leverage-repo, runbook, handover, approved-unexecuted]
related:
  - "[[2026-08-01-thesis-v2-rerun-owed]]"
  - "[[2026-07-30-prestaged-portfolio-revival-still-worth-doing]]"
---

# Hand-over — running the thesis experiment v2 re-run

Everything needed to execute the work owed at [[2026-08-01-thesis-v2-rerun-owed]] (approved by Jesse 2026-08-01 under DQ-004). Written 2026-08-15 from the repo as it stands; every path, flag and threshold below was read from the files, not recalled.

## What you are running and why

The 2026-07-06 full run showed condition A (frontier) scoring **0.795** against B/C at **0.962** on pass@1 — frontier apparently far worse than cheap. An audit of every failing field found **100% were a scoring artifact**: correct values carrying a natural-language unit ("22 dollars" vs reference "22", "two years" vs "two-year"). Not one genuinely wrong or hallucinated value.

`DESIGN.md:130-132` therefore rules that run's headline **superseded and not citable**. The v2 scoring fix — bare-numeric-core extraction, plus hyphen/space equivalence for text — was authored the same day but sat uncommitted until `6febf55` (2026-07-22).

**So there is no v2 verdict yet. The owed work is the run itself.** The plausible outcome is that the frontier condition does not trail at all, which changes what the whole experiment says.

## Preconditions

- Repo: `C:\Users\Jwuts\leverage`, experiment at `experiments\thesis\`.
- Corpus is already in place and verified: **30 items** — `e01`–`e10`, `h01`–`h10`, `p01`–`p10` under `items\` (the 31st entry there is `manifest.yaml`, not an item).
- Confirm the v2 scoring is actually in your working tree before spending anything — it is the entire point of the re-run:

```bash
git -C C:/Users/Jwuts/leverage log --oneline -1 6febf55 && git -C C:/Users/Jwuts/leverage merge-base --is-ancestor 6febf55 HEAD && echo "v2 scoring present"
```

- `ANTHROPIC_API_KEY` in the environment. Paid calls fire **only** with a live backend *and* `--allow-live-calls`; without both, nothing bills.

## Sequence

**1 — Mock dry run.** Proves the harness works before any spend.

```bash
py experiments\thesis\run.py --dry-run --mock-model --output-dir C:\tmp\leverage-thesis-dry-run
```

**2 — Live smoke test, 3 items.** The README is explicit: start here, never go straight to the full run.

```bash
py experiments\thesis\run.py --backend anthropic --allow-live-calls --frontier-model claude-fable-5 --cheap-model claude-haiku-4-5-20251001 --output-dir C:\tmp\leverage-thesis-smoke --max-items 3 --max-retries 1 --max-output-tokens 800
```

**3 — Full run, all 30 items.** Only after the smoke test looks sane.

```bash
py experiments\thesis\run.py --backend anthropic --allow-live-calls --frontier-model claude-fable-5 --cheap-model claude-haiku-4-5-20251001 --output-dir C:\Users\Jwuts\leverage\experiments\thesis --max-retries 2 --max-output-tokens 800 --max-estimated-cost-usd 40
```

Set `--max-estimated-cost-usd` to whatever ceiling you want; it is a hard guard, not an estimate to beat. **Do not pass `--temperature`** — it defaults to 1.0 to match the pre-registered design, and some models reject an explicit non-default value outright.

Call volume, from the frozen design (3 trials per item): A = 30 × 3 × 1 attempt = 90, B = 90, C = 30 × 3 × up to 3 attempts = up to 270. **Roughly 450 calls worst case**, most of them cheap-model.

Outputs land as `runs.jsonl` and `report.md` in `--output-dir`.

## Conditions (frozen, do not change)

| | Model | Attempts |
|---|---|---|
| **A** — frontier, direct | `claude-fable-5` | 1 |
| **B** — cheap, direct | `claude-haiku-4-5-20251001` | 1 |
| **C** — cheap + verifier + feedback retry | `claude-haiku-4-5-20251001` | up to 3 |

The hypothesis under test: **C approaches A at a fraction of the cost.** That is the load-bearing claim of the Verification Layer.

## How to judge it — pre-registered, frozen 2026-07-02

Do not re-derive these or soften them after seeing results; `DESIGN.md:3-4` says changing them post-hoc requires a new version of the file and a stated reason.

**Validates the Verification Layer — all four required:**
1. C final-pass within 10pp of A pass@1
2. Retry conversion ≥ 40% of first-attempt failures (non-trap)
3. Gate false-pass ≤ 5%
4. C cost per correct output ≤ ⅓ of A

**Falsifies — any one suffices:**
1. C final-pass minus B pass@1 < 10pp (feedback not convertible by the cheap model)
2. Gate false-pass > 15% (the verifier itself is untrustworthy)
3. C cost per correct output ≥ A (retry burn erased the economics)

**Inconclusive:** B pass@1 within 10pp of A pass@1 means no headroom — the verdict is "items too easy," not "validated." That calls for harder items, not a re-interpretation.

Watch for the inconclusive branch specifically. If the v2 fix lifts A back up to where B already sits, that is the likely landing, and it is a real result about the corpus rather than a failed experiment.

## After the run

1. Record the outcome against the four/three/one thresholds above — which branch fired, with the numbers.
2. Say what it means for the infrastructure bet. That is the actual deliverable; the run is just how you get there.
3. Retire [[2026-08-01-thesis-v2-rerun-owed]] and note the closure on DQ-004 in `50-dashboards/decision-queue.md`.
4. If the result is citable, the v1 headline stops being the thing anyone remembers — update the leverage-repo context accordingly (assistant memory `project-leverage-repo`, which currently records the v1 run and its scoring-artifact lesson; not a vault note, so it will not turn up in a vault search).

## Explicitly out of scope

Dropped at the same 2026-08-01 ruling and **not** to be revived as part of this: the Knowledge Loop OS C/D/F re-verification, and routing pass output as decision-queue rows. Both were judged bookkeeping with no forcing function. This owes one thing — the run.
