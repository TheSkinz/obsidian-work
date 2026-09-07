---
type: reference
status: active
source_authority: verified
confidence: high
created: 2026-09-06
review_after: 2026-12-06
related:
  - [[code]]
  - [[opus-5]]
tags: [reference, claude, models, fable-5-1, prompting]
---

# Claude Fable 5.1 — Prompting Behavior

Post-cutoff prompting facts for Fable 5.1, captured while writing the Steady Flux pipeline
build prompt.

> **Provenance & freshness.** Read from Anthropic's own docs on **2026-09-06**:
> `platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1`.
> Everything below is quoted or paraphrased from that page unless marked otherwise.
> **A dated snapshot, not a live feed** — re-verify before relying on it.

This supplements, and does not replace, the Fable 5 note at [[code]] ("Fable 5 skill-design
guidance", sourced from Claude Code session 6601b270, 2026-07-02). That note's core finding —
over-prescriptive step-enumerated prompts measurably reduce output quality, and stating goals
and constraints beats scripting the conversation — is corroborated by the 5.1 doc: "Claude Fable
5.1 can execute very long tasks without much guidance on methodology, especially when the goal is
clear."

## Effort is the primary lever, and higher is not always better

Start at **`high`**, the default, then sweep `low` / `medium` / `xhigh` / `max` against real evals.
Effort-level names do not correspond to the same amount of thinking across models, so a sweep run
on Fable 5 does not transfer. At `medium`, 5.1 roughly matches Fable 5 at lower cost. At `low` it
is often competitive with Opus and Sonnet on cost per task while scoring higher.

**The counterintuitive one, and the reason this note exists.** For a single request asking for one
long deliverable — a large document, a big table, a complete code file — Anthropic recommends
running at `high` and moving up only where a gain has been measured. At `xhigh` and especially
`max`, 5.1 can draft most of the deliverable inside its thinking and then write it out again as the
reply: longer wait, more output tokens, no better result. If you do run at those levels, set
`max_tokens` to cover thinking *and* reply, and append the doc's note telling the model that
reasoning and reply share one budget.

## Behaviors that need a prompt line to correct

**It goes quiet.** 5.1 writes fewer user-facing updates during long tool chains than Fable 5, more
so at higher effort and in longer chains. Users see minutes of silence. Before adding anything,
check whether the client even renders progress-update thinking blocks, and strip any legacy prompt
line like "hold all findings for the final response."

**It stops short on long autonomous work.** Without a nudge it may describe the next step instead
of doing it, or ask permission for something the original request already covered. Anthropic's fix
is two system-prompt blocks; the first carries most of the effect and its opening sentence — "You
are operating autonomously. The user is not watching in real time" — is the load-bearing part.
Worth pasting near-verbatim into any single-shot long build.

**It rewrites whole files.** More likely than Fable 5 to rewrite an entire file for a small change.
The result is usually the same file, but it costs output tokens and time. One line fixes it: "when
it will not affect the end result, try to surgically edit a file rather than rewrite the entire
thing."

**It formats less, not more.** Earlier models overused bullets and bold, and many older prompts
carry anti-formatting rules written to hold that down. 5.1 leans the other way — less bold, less
likely to reach for headers or lists. Old anti-formatting language should be removed or replaced
with a rule about when formatting *is* appropriate.

**Its prose can get dense.** Generally a step up — fewer stock phrases, less unexplained jargon —
but sentences run longer with fewer paragraph breaks. The doc's fix is to define the anti-pattern
(mannered prose) rather than to ask for shorter sentences.

**It quotes sources without marking them.** More likely than Fable 5 to reproduce passages from a
retrieved document unmarked. The fix is one complete worked example in the system prompt: request,
correct response, and a sentence saying why it is correct.

**It does extra work.** On open-ended feature requests it may fix nearby code or extend behavior the
task didn't mention. Explicit instructions about what to leave out reduce this substantially with no
measured drop in task success.

**At `low` it searches less.** More likely to answer from memory instead of calling a retrieval
tool. Often the cleanest fix is raising effort for the affected turns rather than the whole
conversation.

## Two things that change how work is set up

**Vision gains show up when it can crop and zoom.** On dense visual inputs 5.1 does its best work
when it can iteratively analyze, crop, and visually verify. An image-cropping tool alone delivers
most of the uplift. Practical consequence: for anything that produces a visual artifact, tell it to
open its own output, screenshot it, and look — that is not busywork, it is where the capability
lives.

**Let the lead agent keep working while subagents run.** On coding tasks, not blocking the lead on
each subagent lowers average time to completion at similar quality and cost.

## Not covered here

The API-surface material on the same page — turn-scoped system messages, append-only conversation
history and thinking-block prefix binding, client-side compaction — is integration engineering, not
prompting, and is not summarized above. Go to the source page if that becomes relevant.

## Applied, and what the run actually showed

First use: [[steadyflux-pipeline-inspection-build-prompt]] (2026-09-06). That prompt carries the
autonomy block near-verbatim, requires browser self-verification on the vision finding, and holds
the whole-file-rewrite nudge in its wrapper rather than the payload. It leans hard on the
goal-over-script finding: reconciled data, hard constraints and a quality bar, with the *form* of
the visualization left entirely open — the concept that prompted the request named as a direction
to beat, not a specification to reproduce.

**The run happened 2026-09-06** (session `local_b8cd9eb1`, "Pipeline inspection visualization") and
produced `apps/steadyflux-wharf-line/` — a 968 KB self-contained page with three.js r158 vendored
inline, a companion note, a recorder script, and a 5.2 MB MP4. Verified against the running page and
the source data 2026-09-07, not taken from the session's own report.

**The latitude produced a hybrid, not a copy and not a departure.** It combined the named direction
with one of the alternatives the prompt sketched: an x-ray flight along the surveyed centreline
*married to* an unrolled-wall strip, plus a 2D cross-section ring. Neither the prompt nor the prior
build specified that combination. This is the answer to the question the run was set up to ask —
open-form latitude got something neither party would have specified, rather than defaulting to the
example.

**It overrode a wrong fact in the briefing by checking the source.** The prompt asserted Steady
Flux's identity "runs teal/cyan against dark neutrals." It read the live site and used navy. The
site's computed styles confirm it exactly — `#22518B`, `#4293DD`, `#ADC9EB`, `#E0E0E0`, `#BBBBBB`,
`"Helvetica Neue", Arial` — with no teal anywhere. **The lesson is mine, not the model's: never put
a palette derived from an image summary into a prompt as fact. Say "read the site" and stop there.**
A stated fact competes with the source; an instruction to look does not.

**It found a defect in the source document that the briefing session missed** — the surveyed route's
endpoints do not close, contradicting the report's own claim that launch and receive were one site.
Correct finding, but its write-up understated the gap by 28% (3,300 ft against an actual 4,238 ft),
which is the reminder that a model checking someone else's work still needs its arithmetic checked.

**Self-verification instructions were followed past the letter.** The prompt asked for at least two
look-and-improve cycles. The page ships ten startup assertions that run on every load and print to
console, a `?debug` flag to surface them, a sweep of every 0.1 s of the 178 s cycle for a finite
camera, and checks at three viewport widths. All ten assertions pass and every expected value
matches an independent extraction of the source report, including the eight full-bore records at
25.07 in — a figure an adversarial reviewer had gotten wrong.

**The hard domain calls came out right without being specified**: full-bore records drawn as 360°
patches with no gap, the odometer-to-route mapping stated as ×0.9521 with every distance labelled by
system, the clock convention mirrored on the return leg, the two overlapping records at girth weld
176 merged as one feature, and the two anomalies with bad report labels shown with both the report's
figure and the resolved one.

**Effort: unresolved, and worth resolving before citing this run.** The session metadata reads
`effort: "low"`, while the operator set out to run it at `high`. If it was in fact `low`, this
result is a much stronger data point than it currently reads as. Do not cite the run as evidence
about a particular effort level until that is settled.
