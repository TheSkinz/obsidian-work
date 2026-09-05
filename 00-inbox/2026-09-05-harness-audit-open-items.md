---
type: note
status: open
created: 2026-09-05
review_after: 2026-09-19
tags: [harness, audit, open-items]
related:
  - "[[2026-09-05-harness-audit-number-verification]]"
  - "[[2026-09-05-harness-route-usage-rescoped]]"
---

# Harness audit — what is still open

Four items left over from the 2026-09-05 verification and re-measurement. Filed as one note rather than
four because inbox median age is already a FAIL row. The path-checker item is **not** here — it was picked
up in a fresh session the same day.

**1. `exec-ok` has gone reflexive — narrow it.** 183 of 558 uses were on commands
`usadebusk-exec-guard` would never have touched, overwhelmingly `python tools/vault_lint.py # exec-ok` — a
habitual suffix on invocations the gate never gated. A third of all uses are cargo-culted, which is slow
erosion of the only property the gate exists to protect. A gate change needs its fire rate replayed over
real history *before* it is made — the standing rule that killed the WORD-DELTA diff-shape gate when its
replayed rate came in at 7% against a predicted 70% — so this is a session of its own, not a batch item. The measurement backing the 183 is in [[2026-09-05-harness-audit-number-verification]].

**2. `01-context/system-workflow-reference.md` is stale on the review loop.** Line 16 still reads
"On-demand only — you say 'run the Vault Review Loop'", and the line-5 header repeats it, thirteen days
after the loop was put on a monthly schedule (2026-08-21). That file loads every session, so the wrong
description propagates. `04-knowledge/vault-agent-loop-spec.md:36` has it right and is the model to copy.
Small fix; it just needs doing.

**3. Revisit the loop `01-context` question after 2026-09-08.** Six of the seven loop prompts never mention
`01-context` and neither `CLAUDE.md` exempts unattended sessions, so 0 of 88 loop runs reading all five is
a gap rather than a design choice. `vault-review-loop` is the exception — it mandates the read, citing the
2026-08-20 finding that context-blind loops proposed work that did not matter at a ~53% effect rate — and
it fires for the first time on **2026-09-08**. Jesse's ruling on 2026-09-05 was to let it run and get one
real observation of a context-reading loop against five that do not, rather than assume. That evidence
should exist by the time this note comes up for review.

**4. `totalToolUseCount` has a 60% coverage hole.** Only 47 of 117 `Agent` tool results carry the field.
Where present it is exact — those 47 sum to 513 against 513 actual subagent tool calls, per-agent delta
zero — but it is simply absent on the other 70, with no signal that anything is missing. Summing it is the
natural way to size delegated work and it under-counts by 63%. All 5 `spawnDepth: 2` agents lack it, which
explains 5 of 70; the rest is unexplained. Worth a `claude-code-guide` question: is the omission
documented? Low stakes, but it silently corrupts any future measurement of subagent volume.
