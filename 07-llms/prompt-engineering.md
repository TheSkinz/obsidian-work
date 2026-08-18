---
title: Prompt Engineering
created: 2026-06-29
tags: [prompt-engineering, llm, patterns]
---

# Prompt Engineering

Principles and patterns for getting reliable, high-quality output from LLMs. This is a living document — add patterns as they're validated and anti-patterns as they're encountered.

## Key principles landed on

**Specify format upfront.** LLMs default to whatever format feels natural for the content type. If you need a table, a numbered list, prose paragraphs, or JSON — say so in the prompt. Post-hoc reformatting requests add a round trip and often don't fully converge.

**Name the failure mode you're preventing.** Telling a model what you don't want (e.g., "no bullet points in prose sections") is as important as telling it what you do want. Models optimize for helpfulness, which means common patterns get over-applied unless they're explicitly excluded.

**Provide the output exemplar when quality matters.** For recurring structured outputs (heater cards, proposals, SOPs), the fastest path to correct format is a real example from the vault. Abstract descriptions of structure are interpreted differently each time; a concrete example is unambiguous.

**One ambiguity → one clarifying question, upfront.** Don't start generating and then ask mid-output. If something is unclear, ask before starting. This is especially true for documents that have a fixed format — a wrong-format first draft wastes more time than a short question.

**LLMs cannot reliably audit their own output.** This is the confabulation finding from [[gem-drawing-extraction]] but it applies universally: asking a model to check its own work produces confident explanations of what it *should* have done, not accurate descriptions of what it *did* do. Human review or a separate model pass is the only reliable check.

**Verify inputs, not outputs — the two "double-check" shapes are not the same redundancy.** A stronger model's tendency to reconcile its own arithmetic unprompted makes an instruction like "re-check your own output" genuinely redundant — but it does *not* make "verify a premise against its authoritative source" redundant, because that is checking an input, not re-doing already-completed work. A 2026-07-24 review of two skills (`adversarial-review`, `idea-triage`) that were flagged as carrying redundant self-verification scaffolding found neither actually did — both carried input-verification and honesty-guard instructions (a VERIFIED/ASSERTED tagging discipline against agreement-mistaken-for-verification, a prior-art check before dismissal, an anti-fabrication guard), none of which a stronger model's self-correction touches. The review that raised the original flag was itself an instance of the failure it described — a confident summary written *about* the skills rather than derived from reading them, and wrong. Drop "verify your output," keep "verify your inputs."

Source: Claude Code session, 2026-07-24.

## Pattern catalog

**Dependency-tree interview pattern** (analyzed via the `grilling` skill from aihero.dev, not built here). A clarifying-questions instruction degenerates into either a wall of questions or premature agreement unless it's constrained by two specific splits: (1) primitive vs. wrapper — one battle-tested interrogation skill that thin, purpose-specific wrappers invoke, so the technique isn't reinvented per use case; (2) verify vs. ask — the agent checks anything it can confirm itself from available context and only asks about genuine decisions. On top of that: one question at a time (not a batch), the plan modeled as a dependency tree so an early answer reshapes later questions, every question shipped with the agent's own recommended answer (so obvious ones get rubber-stamped and only real disagreements slow things down), and a hard gate — no implementation until shared understanding is confirmed. Candidate fit for USADebusk work: locking an RFQ/heater-card scope or an SOP's decision branches before drafting, both dependency-tree-shaped problems where premature agreement is the known failure mode.

Source: Claude Code session f4df43ad, 2026-07-09.

**Concrete negative constraints beat vague ones — name the model's specific attractor states, not the general failure.** Comparing two published skill-design approaches (the `Superpowers` plugin's process-forcing-function skills — TDD red-green-refactor, stop-and-diagnose-after-N-failures, brainstorm-before-code — against `anthropic-skills:frontend-design`'s two-pass plan-then-critique workflow) surfaced a distinction that generalizes: Superpowers guards against *process* failure (jumping to code, patching symptoms) by inserting a checkpoint at the exact point the model wants to skip ahead. `frontend-design` guards against *output homogeneity* — a harder problem, because the model doesn't experience mode collapse as a failure, it feels like taste — by forbidding its own specific attractor states by exact coordinates (e.g. blocking the hex code `#F4F1EA` with serif+terracotta, not just "avoid generic design"). "Be original" is a worthless instruction because the model already believes it's complying; a negative constraint only works when violating it is mechanically detectable (a hex code you can grep for, a phrase you can find). This vault's `01-context/output-preferences.md` already applies the technique for text register (no bullets in prose, no preamble, no closing summary — named, checkable attractor states). The caveat: hex-code-style blocklists are maintenance-bearing, not durable — once a specific pattern is widely blocked, the model's distribution moves elsewhere and the list needs a refresh; this differs from process-forcing-function rules like "write the failing test first," which don't decay the same way.

Checked against `usadebusk-estimating` (2026-07-20) on the hypothesis that proposal voice was a candidate for this treatment: it isn't. Every proposal section (opening paragraph, closing statement, disclaimer) is a literal fixed string in the skill's Section Templates, not open-ended model prose — the "extensive experience" disclaimer text this note originally flagged as a drift risk is itself the hardcoded template wording (`SKILL.md` Section 4), not something the model generates. The technique only applies where the model actually writes free text, and the estimating skill has no such surface today. Revisit only if a free-prose section (e.g. a cover letter or executive summary) gets added to the proposal template.

Source: Claude Code session a28ed43f, 2026-07-20; corrected same-day after checking the skill file directly.

**Agent fan-out pays only where a machine, not a model, can say "correct."** Reconciling the
publicly-described long-horizon agent runs (an 11-day Zig→Rust rewrite of the bun runtime, a
multi-week Electron→Swift port) against this system's own measured result resolves an apparent
contradiction. Both public successes had a **hard external verifier** the agents could not
argue with — bun's and Node.js's existing test suites in one case, pixel-by-pixel screenshot
comparison against the running original in the other. The local arm test that found a
three-agent adversarial chain scoring 3/6 against a single agent's 5/6 at 3.31× the tokens had
**no verifier at all**, only judgment. Scale multiplied noise because nothing could reject it.
The rule: before fanning work out across many agents, name the thing that will mechanically
reject a wrong answer. If it is a test suite, a diff against a frozen output, a schema, or an
arithmetic check, fan out freely. If it is "another model reads it and decides," expect the
extra agents to cost more and find less. Corollary for the vault: the regression battery's
"numerics must match exactly" bar is precisely such a verifier, which is why fixture replay
scales where reviewer stacking does not.

Note also that the same talk's "thousands of agents" figure exceeds Claude Code's documented
1,000-agent-per-run ceiling (16 concurrent) — see [[dynamic-workflows]]. Plan against the
documented caps, not the anecdote.

Source: Claude Code session, 2026-07-28 (Boris Cherny Opus 5 launch talk, reconciled against
`~/.claude/regression/adversarial-review-arm-test-2026-07-24.md`).

**A second fan-out arm test landed in the same direction, and located the difference in research
behaviour rather than in the fan-out itself.** The `adhd` skill spawns five agents under isolated
cognitive frames. Run head-to-head on 2026-08-17 against a single unstructured agent on the same
genuinely-open seed (`00-inbox/idea-smart-pig-report-as-cleaning-verification.md`), with pass criteria
pre-registered before either arm ran, the single agent won on the thing that mattered: it swept six
facility heater cards, found five prior smart-pig instances, and so **corrected a false premise in the
seed itself** — the seed's wake condition assumed F-501 was the first instance and therefore waited on
F-201 in January 2027. The five-frame arm never made the sweep and inherited the false premise into
all five frames simultaneously, which is the specific failure mode of isolation: a wrong shared brief
sends every branch down the same wrong path at once, and isolation guarantees none of them can catch
it. About forty cited specifics across both arms were then read back against the actual files, and
almost all were real, so this was not a fabrication result — it was a recon result.

The fix that follows is not fewer frames but a mandatory recon phase ahead of them, run in the
orchestrator's own context rather than delegated, because an agent told to generate will build on
whatever the brief asserts instead of checking it (config `5347158` added it as Phase 0). Recon must
be shared verbatim into every frame prompt; that does not break isolation, which forbids one agent
seeing another's *ideas*, not the frames starting from the same checked ground.

Two method defects are worth carrying forward to any future arm test. **Completion order de-blinds the
arms** whenever one of them spawns sub-agents and the other does not — the fan-out arm is
structurally slower, so unlabelled presentation is theatre. And **a parent agent's self-reported token
count excludes the agents it spawned**, so the cost axis of a fan-out-versus-single comparison cannot
be recovered from the parent's report; it has to be instrumented before the run or it is unmeasured.
The 2026-08-17 test lost its cost axis to exactly this.

The standing question the test leaves open: with recon mandatory, do five isolated frames produce
angles a single grounded pass does not? A single agent does recon for free, which is how the winning
arm won. Two independent results now point the same way.

Source: Claude Code sessions `06a84965` and `8e7a4b72`, 2026-08-17; config `475ce58`, `5347158`.

**A negative grep is not evidence that work never landed — check which direction the file moved.** A
2026-08-17 session grepped a fixture README for the rule count recorded in an orphan commit, got zero
matches, and read that as "the reconciliation never landed" — then tried to cherry-pick the orphan
commit, which conflicted. The conflict is what revealed the truth: main was at sixteen rules, the
orphan commit was the fourteen-rule version, and applying it would have deleted two rules added since.
Absence of the old value meant the file had moved *past* it, not fallen short of it. Before treating a
missing marker as missing work, read the current state of the target and establish which side is newer.

Source: Claude Code session `1cca7483`, 2026-08-17.

## Anti-patterns

(Placeholder — add observed failure modes here. Format: what goes wrong, why, what to do instead.)

**Regression fixtures find more value as a rule audit than a drift detector.** A fixture battery built to answer "did the new model break anything" (a model-transition trigger) turned out to be far more valuable at exposing defects in the rules being tested against than in the model — four of six fixtures in one battery caught a rule that was implicit, internally inconsistent, or contradicted by a real actual, none of them model regressions: a rule the skill already stated but the frozen baseline violated, a benchmark being read at the wrong granularity by the whole suite, and a wording precedence defect introduced by an unrelated same-day fix. Why this happens: a fixture forces a rule to be *executed* rather than read, and rules that survive any number of readings fail the moment something has to produce a number from them. The implication for trigger design: replay fixtures after any substantive skill edit (one that changes an output number, adds/removes a rule, or resolves an ambiguity — not a typo or reword), not only on model change — a replay run for an unrelated reason caught a real defect in its own baseline on first use under this trigger.

Source: Claude Code session, 2026-07-24, adopted 2026-07-25.

## Decision rules

**Evidence governance, not just extraction rules.** For any multi-step extraction or research task, track source family, revision/as-built status, contradiction chains, dependency chains, and calculation confidence alongside the extracted values. This prevents unsupported assumptions from silently becoming treated as facts downstream. The principle generalizes beyond heater drawing extraction — it applies to any workflow where intermediate outputs feed later decisions.

**Pre-Execution Audit pattern.** For multi-step documents or scripts, include an explicit audit section that assesses assumptions and logical flaws before generation begins, not after. Catching a bad assumption at the start costs one short exchange; catching it in a finished document costs a rewrite.

**Keep facts, assumptions, recommendations, and risks structurally separate.** In technical or decision-oriented outputs, these categories should be visually and structurally distinct — not interleaved in prose. A reader should be able to scan for assumptions without reading the full document.

**Test on real data before scaling.** Validate extraction rules or automation logic on actual examples, audit the failures, update the rules, then expand. Heavy automation built before rules are validated is low-ROI and often reduces quality relative to a manual process. The right order: real data → audit loop → rule update → scale.
