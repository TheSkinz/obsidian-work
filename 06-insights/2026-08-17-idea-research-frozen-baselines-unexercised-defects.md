---
type: review
status: open
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-08-17
review_after: 2026-09-17
related:
  - "[[2026-08-15-idea-frozen-baselines-may-carry-unexercised-convention-defects]]"
  - "[[2026-07-31-idea-research-replay-ordering-discipline]]"
  - "[[2026-08-08-prestaged-f6-rig-tier-decision]]"
  - "[[vault-idea-loop-spec]]"
tags: [review, knowledge-system, idea-research, regression, testing]
---

# Idea Research — Frozen Baselines Can Carry Defects No Replay Will Ever Surface

## Trigger

Scheduled nightly run of the Vault Idea Research Loop, 2026-08-17. Oldest unexplored seed by
actual creation time (git first-commit, resolving a same-`created`-date tie among three
2026-08-15 seeds): `2026-08-15-idea-frozen-baselines-may-carry-unexercised-convention-defects.md`,
added 18:45:27 local, ahead of `2026-08-15-idea-researched-status-outlives-the-build-it-gated.md`
(20:03:51) and `idea-smart-pig-report-as-cleaning-verification.md` (22:34:39).

**Gate check.** The seed's `**Gate:**` line reads "None — researchable now." No settlement needed;
proceeded directly to research.

## Evidence

**1. This vault has already produced two real instances of the exact failure mode, one of them
after the seed was filed.** The seed's own trigger was the F1 crew-truck case (2 × 48 = 96
truck-hours billed instead of the intended figure, surviving four promotions because every replay
happened to read the ambiguous singular-item sentence the same way). Independently,
[[2026-08-08-prestaged-f6-rig-tier-decision]] recorded a second, structurally identical case
resolved 2026-08-15: F6's rig-tier rule was missing its dominant driver (mode/pump count), so
three of four replays landed on "Large" by splitting the difference between two other drivers,
and the regression suite defended that reading as correct until Jesse's own stated figure for the
heater shape (rig-in 12) forced the question. Two independent incidents in three weeks is enough
to call this a recurring structural gap in this vault's fixture practice, not a one-off.

**2. The standard, well-established mitigation for "tests exercise only the axes where runs
already disagree" is mutation testing, and it is specifically documented as the companion
practice to golden-master/characterization testing for this exact blind spot.** A [characterization
test](https://en.wikipedia.org/wiki/Characterization_test) (the formal name for what this vault
calls a frozen baseline — Michael Feathers' term from *Working Effectively with Legacy Code*)
captures what code currently does, not what it should do, by design. The documented pairing fix:
"100% test coverage is not enough to trust in approval tests, so combining them with mutation
testing is recommended... if you change a line and the tests remain green even though the code
changed, it reveals the problem — the tests execute that line but something else happens later
that makes this change have no consequence for the result." That is precisely the seed's failure
shape restated in testing-literature terms: a frozen baseline only proves it noticed an axis, not
that it would notice the axis reading differently. [Golden Master Pattern](https://blexin.com/en/blog-en/golden-master-pattern-dont-fear-the-legacy-code/),
[Characterization test](https://en.wikipedia.org/wiki/Characterization_test)

**3. For this vault's fixtures specifically, mutation testing translates to a concrete, cheap
manual analog: deliberately flip the quantity-bearing word in a fixture's input text (crew truck
singular→plural, "a pump" → "two pumps," a named count → an unstated one) and rerun. If the frozen
diff key doesn't move, the rule that should have driven it either doesn't exist or isn't wired to
that noun — which is exactly what happened in both the F1 and F6 incidents.** This is lighter than
building an automated mutation-testing harness (not warranted at this vault's fixture count) and
matches the seed's own framing of wanting "closer to a checklist than a build."

**4. The seed's proposed cheap audit — "rules that name a countable item without saying how
quantity behaves" — is a named, actively researched category in requirements engineering, not a
novel idea, which is independent confirmation it is a real and tractable signal rather than a
hunch.** NLP-for-requirements-engineering tooling (QuARS and successors) explicitly targets
"multiplicity" and "under-specification" ambiguity via POS-tagging patterns — singular countable
nouns with no stated quantifier are one of the standard detected classes.
[Using NLP Tools to Detect Ambiguities in System Requirements](https://ceur-ws.org/Vol-3122/NLP4RE-paper-3.pdf)
The existing research tooling is built for prose requirements documents at a scale this vault
doesn't have (a handful of skills, not a corpus), so adopting a research NLP pipeline would be
over-engineering, but the underlying pattern-class ("singular countable noun, no quantity
statement, feeds a computed total") is a legitimate, cheap grep target scoped to skill files that
drive fixture math.

**5. The seed's third bullet (self-confirming diff keys — F6's diff key 5 naming the same fixture
its worked example uses) is the inverse failure and was already raised, discussed, and explicitly
left unfixed by Jesse in-session** ("precision engineering on a line that does not warrant it," per
the seed's own citation). No new prior art changes that call; it is a closed, deliberate call, not
an open question this research should reopen. Testing-anti-pattern literature names circular
test-oracle patterns generically (e.g., extracted/shared-fixture anti-patterns in
[Testing Anti-Patterns](https://medium.com/@jameskbride/testing-anti-patterns-b5ffc1612b8b)) but
nothing found there is more specific to the self-referencing-worked-example shape than what this
vault already identified on its own.

## Interpretation

**Sound, and already twice-validated by this vault's own incident history — but the fix is a
lightweight manual habit, not a build.** The seed correctly identifies a real, recurring class of
defect (F1, F6) and correctly senses that the right-sized fix is "closer to a checklist than a
build" — external prior art confirms both halves: mutation testing is the standard, literature-
backed way to expose exactly this blind spot, and a manual "flip the quantity word, rerun, see if
anything moves" pass is mutation testing scaled down to this vault's actual fixture count rather
than an automated harness. The requirements-ambiguity research (point 4) independently confirms
the seed's proposed grep pattern ("countable item, no quantity statement") is a real, named
ambiguity class, not a guess — which raises confidence that a manual audit built around it would
catch real cases, not chase noise. This is not "already covered": nothing in this vault's existing
tooling (`vault_lint.py`, `baseline_staleness.py`, the fixture-replay-guard hook) checks for this
axis at all — those check freshness and format, not whether a frozen number is traceable to a
stated rule.

## Recommended Action

**Bounded one-shot investigation, not a build.** A single manual pass over each frozen baseline's
line-item math, checklist-style: for every computed figure, ask "is this number traceable to a
stated rule with an explicit quantity, or is it a reading that happens to be consistent across
existing replays?" Any "reading" hit becomes a one-line finding (which skill sentence, which
fixture, what the ambiguous reading currently resolves to) — not an auto-fix, since resolving the
ambiguity is a domain-rule decision reserved for Jesse, exactly as the F6 case required his
adjudication (rig-in 12 vs. the baseline's 10). This is scoped as an audit-and-report exercise, not
a skill or tooling change, and does not require Jesse's Lane 4 sign-off to *run* — only to *act on*
any finding it produces, same as the F6 precedent. Estimate: comparable cost to the F1/F6
incidents' own discovery, i.e., a few fixtures' worth of read-and-cross-check, not a new hook or
script.

## Decision

- [ ] Approved — run the one-shot audit pass now
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more source material

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
|  |  |  |  |
