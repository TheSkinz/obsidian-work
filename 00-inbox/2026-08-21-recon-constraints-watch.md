---
type: note
status: inbox
created: 2026-08-21
tags: [inbox, knowledge-system, claude-code, instructions, watch]
related:
  - "[[2026-08-20-concise-output-style-watch]]"
---

# Watch — do the two new recon constraints actually change anything?

Two clauses were added to the `**Hard constraints.**` paragraph of global
`CLAUDE.md` on 2026-08-21 (config `6de47e3`, then `f43db6c`). They are the
output of an instruction audit Jesse commissioned after noticing repeated
self-corrections across sessions.

**What the evidence said.** Four sessions were mined with a fielded
self-diagnostic prompt, returning 36 wrong-then-corrected claims. 28 of 36 were
asserted without complete recon, 23 of 36 rested on inference rather than a file,
28 of 36 were stated flat with no hedge, and **1 of 36 named any instruction as a
contributor** — and that one pointed at a vault schema note, not `CLAUDE.md`, and
was already amended. The suspected causes were both ruled out: built-in Concise
was active in at most one of the four sessions, and standing context load
measured ~5,400 words. So this was not a configuration problem.

**The two clauses.** The first targets the largest bucket (`RECON: partially`,
15 of 36) with a stopping rule, and the 28 flat deliveries with inline
provenance marking. The second targets the eight `RECON: yes` cases — where the
source was read correctly and the claim was still wrong — which carried the
longest survival (5–6 turns vs 1–2) and would all have passed the first clause.
It was back-tested: the first draft caught 3 of 8 and was rejected below a
pre-set bar; the committed wording catches 6 of 8.

## The open question

Both are **self-enforced by the same mechanism as the rule they extend**, and
that rule was violated at 78% across the mined corpus. The honest theory of
change is not better compliance — it is that non-compliance becomes *visible*,
because a claim marked "read it" and one marked "inferred it" no longer look
identical. Whether that holds is untested.

**The tell.** Load-bearing claims either start arriving with provenance attached,
or they stay flat. If they stay flat across a few weeks of ordinary sessions, the
edits did not take, and the conclusion worth recording is that instruction text
cannot fix this class — which is itself a useful finding, not a failure.

**Second, weaker signal.** The `Hard constraints.` paragraph roughly doubled in
length in one session, on the strength of a finding that instructions were *not*
the problem. If adherence to the rest of that paragraph visibly loosens, the two
additions are the first suspects, and the second should be cut before the first
since it is the less-tested one.

## The deferred experiment

Whether plan mode reduces this was raised and **could not be tested in the
session that raised it** — the same session proposed the test, wrote the
constraints, and was the subject, so any plan it produced would name its sources
because it knew that was being measured. It needs a cold session: run a real
`tools/` or renderer change in plan mode and check one thing — whether the plan
names its sources or only states conclusions. If it only states conclusions,
plan mode is not buying recon and the committed clauses are doing the work alone.

Note that plan mode gates *writes*, not assertions, and most of the 36 occurred
in turns with no edit in them — so it can only ever be a partial answer.
