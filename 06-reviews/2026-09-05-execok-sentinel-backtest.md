---
type: review
status: resolved
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

## Addendum — is the guard itself worth its friction? (2026-09-05, Jesse asked)

Separate question from the sentinel: the gate is noticeable in daily use, so does it earn that. Measured
from the hook's own block message in `tool_result` records — **102 real block events across 296 sessions**,
about 1.1% of Bash traffic. Each block's next command in the same transcript was classified by asking the
live `decide()` whether the follow-up still trips a rule:

| Outcome | Count | Share |
|---|---|---|
| Same task, simpler tool — the gate improved the command | 40 | 39.2% |
| Re-authorised identically with `# exec-ok` — pure latency | 32 | 31.4% |
| Moved on to a different subject | 20 | 19.6% |
| Reworked but still inline interpreter code | 8 | 7.8% |
| Abandoned entirely | 2 | 2.0% |

**A correction worth keeping, because it is this note's own subject matter.** The first pass counted 110
blocks by matching any `tool_result` *containing* the block message. The hook's source file contains that
string, so every `cat hooks/usadebusk-exec-guard.mjs` was scored as a rejection — the measurement matched a
quotation of the thing instead of the thing, which is the same error class as PATH-DEAD firing on a note
that names a retired folder, and as DEAD-LINK before `strip_inline_code()`. Discriminating on `is_error`
gives 102. The conclusion did not move; the number did.

The 39% is substantive, not cosmetic: `python -c` + `zipfile` → `unzip -p`; `python3 -c` + `json` →
`grep -o`; `python -c "ast.parse(...)"` → `python -m py_compile`; `python -c` + `pathlib` walking markdown
→ a shell `for` loop. The gate reads in practice as *"do you actually need an interpreter here?"*, and
about two-fifths of the time the answer is no.

**Verdict: keep it, unchanged.** Against the WORD-DELTA precedent — a gate firing on 70% of commits was
killed, one firing on 7% was kept — this fires on 1.2% of traffic and improves the command in 39% of
firings.

**Stated limits.** "Same task" is a token-overlap proxy (shared filenames and path segments between the
blocked command and its follow-up), not a semantic judgment. The 21% "moved on" bucket is genuinely
ambiguous — the blocked action never happened, which may be a saved mistake or a lost thread; nothing here
distinguishes them.

**The founding premise cannot be re-tested from here, and should not be reported as dead.** The hook's
comment justifies itself by auto mode re-adding `Bash(python -c ' *)` to the allow list (61 rules → 36 →
back to 59 by 2026-07-29). Today `settings.json` carries 17 `Bash(` rules and `settings.local.json` 13,
with zero arbitrary-execution entries — the only python rule is `Bash(python tools/vault_lint.py)`, one
named script. But the hook exits 2 *before* the permission system runs, so no prompt is raised and no rule
can be added. The clean allow list is exactly what a working guard produces, and exactly what a retired
problem produces. Unresolvable without disabling the hook, which is not worth doing to answer it.

**One real false positive, observed rather than measured.** Committing this addendum was itself blocked:
the commit message body quotes the gated pattern as prose, inside a `git commit -F -` heredoc, with no
interpreter invoked anywhere in the command. The rule matches the text of the message, not an invocation.
That is a genuine defect of the same family the lint rules already carry `strip_inline_code()` for — a rule
firing on writing *about* the thing it guards. **Frequency unmeasured**: the pass that would have counted it
is the buggy one corrected above, so the honest statement is that it happened once, today, and nothing here
establishes a rate. Worked around by passing the message as a file, not by reaching for the sentinel. If
option A is adopted, this case is worth re-checking, since a prose match can never be in comment form.

**The avoidable cost is behavioural, not configurable.** The 31% pure-latency bucket is inline interpreter
code reached for where the shell would have done. Note also that `Write scratch.py && python scratch.py`
is ungated and strictly more capable than `python -c`. That is not a hole to plug: it channels a genuine
one-off computation into a form that can be read and re-run, instead of an opaque one-liner. Both scripts
behind this note were written that way.

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

**Option D was added after this note was first written**, when the addendum's own commit was blocked by the
prose defect. A and D compose rather than compete, and Jesse ruled them together on 2026-09-05.

- [x] **Option A** — sentinel honoured only in comment form
- [ ] **Option B** — warn on unnecessary sentinel use — **rejected**: 184 firings of standing friction
      against a habit with no measured consequence
- [ ] **Option C** — no change
- [x] **Option D** — rules no longer match inside a heredoc body fed to a non-interpreter
- [ ] Needs more research

## Apply Log

**2026-09-05 — applied, config repo `f206ecc`.** `hooks/usadebusk-exec-guard.mjs` +
`hooks/usadebusk-exec-guard.test.mjs`.

`SENTINEL` is now `/#[^\n]*exec-ok/i` and `decide()` strips data-heredoc bodies *before* testing it, so a
`# exec-ok` planted in a commit message cannot stand the gate down. `stripDataHeredocs()` removes the body
of any heredoc whose receiving command is not an interpreter; one fed to `python`/`node` is a program and
stays fully visible to the rules.

**The replay caught a real bug before it shipped, and it is the reason this note's method mattered.** The
first classifier draft omitted env-var assignments. Six real commands read
`PYTHONIOENCODING=utf-8 python - <<'PYEOF'` with `# exec-ok` as the **Python program's own first line** —
without env-var tolerance those heredocs are misread as *data*, their bodies stripped, the sentinel deleted
with them, and all six newly blocked. Misreading code as data is the dangerous direction. Fixed and locked
by two tests.

**Verified against the live hook, not the simulation:** 0 newly blocked of 577 sentinel-carrying commands;
101 of 102 historical blocks still block; the single freed block is the prose case (a `git add` naming
`exec-guard-gh-api-gap.md` beside a commit heredoc), not an invocation. Test suite 28 cases, all pass.

**End-to-end proof rather than a unit test:** the commit applying this change quotes the gated pattern in
its own message and carries no sentinel. Under the old hook that exact commit was blocked.

The guard itself is unchanged in scope and stays as it is — see the addendum above, which measured it at
39.2% of blocks producing a better command.
