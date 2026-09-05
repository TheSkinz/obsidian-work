---
type: review
status: open
review_type: contradiction
source_authority: measured
confidence: high
created: 2026-09-05
review_after: 2026-10-05
related:
  - "[[2026-09-05-harness-audit-number-verification]]"
  - "[[2026-09-04-harness-audit-evidence]]"
tags: [review, knowledge-system, harness, exec-guard]
---

# Review — the `exec-ok` sentinel, back-tested before narrowing it

## Trigger

The 2026-09-05 harness verification found the `exec-ok` escape had gone reflexive: roughly a third of its
uses were on commands `usadebusk-exec-guard` would never have touched. The standing rule is that a gate
change gets its fire rate replayed over real history **before** it is made — the discipline that killed the
WORD-DELTA diff-shape gate when its replayed rate came in at 7% against a predicted 70%. This is that
replay. It recommends; it changes nothing.

Recon also turned up a hole nobody had named: `hooks/usadebusk-exec-guard.mjs:49` tests `/exec-ok/i`
against the **whole command string**, before any rule is evaluated and without segmenting it. On its face
the literal text `exec-ok` anywhere — a commit message, a grep pattern, a filename — disarms the guard for
a `python -c` in the same command. Whether that has ever actually happened was the second question.

## Method

`decide()` was **imported from the live hook**, not reimplemented — a back-test against a reimplementation
tests the copy rather than the gate. Each command was evaluated twice: once as written, and once with the
sentinel neutralised (replaced, not deleted, so token boundaries survive) to see what the rules would have
done on their own.

Corpus is the **full** transcript scope, all 23 project directories under `~/.claude/projects/`: 213
top-level `*.jsonl` plus 119 `<sessionId>/subagents/agent-*.jsonl`. The subagent directory is one level
outside the `*.jsonl` glob both harness audits used, and it carries 859 of the 9,283 Bash calls (9.3%) —
omitting it is what broke the 2026-09-04 audit's structural finding.

The hook was installed **2026-07-29** (`529ba04`). Everything before that date is a counterfactual: the
gate did not exist to fire on it. Both windows are below, and the live window is the one that governs.
As a check on the method, all 572 sentinel uses fall inside the live window — nobody typed `exec-ok`
before the hook existed, which is what should be true.

## Evidence

**Since install, 2026-07-29 — 6,784 Bash calls.**

| Bucket | Count | Share of all commands |
|---|---|---|
| sentinel present, a rule would fire — the escape doing its job | 388 | 5.7% |
| sentinel present, no rule would fire — reflexive noise | 184 | 2.7% |
| no sentinel, a rule fires — real blocks | 134 | 2.0% |
| neither — untouched traffic | 6,078 | 89.6% |

**572 sentinel uses in total, of which 184 are reflexive — 32.2%.** Whole-corpus figures are the same 572
and 184; only the real-block count moves (530 across the whole corpus, 134 since install), which is
entirely the pre-install counterfactual.

Which rule does the work, since install: `python -c` 300, `python -` on stdin 229, `node -e` 8,
`gh repo` mutation **0**.

The reflexive uses are one habit, not scattered: 183 of the 185 put the sentinel in a trailing comment on
a plain script invocation the gate has no rule for. The three most common are literally

```text
cd "C:\Users\Jwuts\obsidian-work" && python tools/vault_lint.py 2>&1 | tail -30 # exec-ok
cd "C:\Users\Jwuts\obsidian-work" && python tools/vault_index.py # exec-ok
cd "C:\Users\Jwuts\obsidian-work" && python tools/vault_health.py # exec-ok
```

That 183 is the figure the 2026-09-05 verification reported as "183 of 558" — it is the comment-form
subset, and this replay reproduces it at a slightly wider corpus scope (184 of 572).

**The whole-string match has never been exploited. Of the 388 real escapes, 0 had the sentinel anywhere
other than in comment form.** Stated plainly because it is the honest result: the hole is real in the code
and has a fire rate of zero in the history. It is a latent hazard, not an active one — the same shape as
the frontmatter finding on 2026-09-05, and it should be reported the same way rather than dressed up as a
fix that was needed.

## Proposed Change

**These are alternatives, not components — pick one.**

**Option A — require the documented comment form.** Honour the sentinel only when it appears as a comment
(`# exec-ok`), not anywhere in the string. Replayed against all 388 historical escapes this changes **zero
decisions**, because every one of them was already comment-form. It closes the whole-string hole outright.
Cost: one line. Risk: a future escape typed in some other position would be refused, and the block message
already tells the operator the exact form to use.

**Option B — warn when the sentinel is present and no rule fires.** Attacks the reflex directly by telling
the operator the escape was unnecessary. It would have fired 184 times, 2.7% of all commands. It cannot
block anything real, so it is a nag rather than a gate, and the habit it corrects has a measured cost of
zero.

**Option C — do nothing.** The reflex is untidy but the guard has never actually been disarmed by it.

**Recommended: A, and not B.** A is free and provably behaviour-neutral over 6,784 commands. B spends
standing friction on a habit with no measured consequence, which is the failure mode the WORD-DELTA replay
exists to prevent.

## Risks / Open Questions

- The replay measures what the rules *would* decide, not what the hook actually did at the time. Hook
  firings are recorded in the transcripts only as their effects, so a command that was blocked and then
  re-issued with the sentinel appears in this corpus twice — once in `real blocks`, once in
  `escape doing its job`. The bucket shares are therefore about the operator's behaviour, which is the
  question here, not about a count of distinct intentions.
- `gh repo` mutation has fired **0** times since install. That rule is carrying no load. Not proposed for
  removal — a gate that never fires on a rare destructive verb is doing its job by deterrence — but it is
  worth knowing it is untested in practice.
- Option A's replay covers the escapes that exist. It cannot cover an escape form nobody has typed yet.

## Decision

- [ ] **Option A** — sentinel honoured only in comment form
- [ ] **Option B** — warn on unnecessary sentinel use
- [ ] **Option C** — no change
- [ ] Needs more research

## Apply Log

_(empty — nothing applied; this note is the measurement.)_
