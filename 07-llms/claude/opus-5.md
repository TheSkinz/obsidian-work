---
type: reference
status: active
source_authority: verified
confidence: high
created: 2026-07-24
review_after: 2026-10-24
related:
  - [[code]]
  - [[command-reference]]
tags: [reference, claude, models, opus-5, routing]
---

# Claude Opus 5 — Release Capture

Post-cutoff model facts, captured the day of release. Follows the durable-capture
convention established in [[command-reference]].

> **Provenance & freshness.** Verified against `anthropic.com/news/claude-opus-5` on
> **2026-07-24** (release day), cross-checked against CNBC, VentureBeat, and Fortune
> coverage the same day. API-surface details (breaking changes, effort semantics,
> cache minimums) come from the bundled `claude-api` skill shipped with CLI 2.1.219,
> whose model table is stamped 2026-06-24 with Opus 5 sections added at launch.
> **This is a dated snapshot, not a live feed** — re-verify anything version-sensitive
> against the docs before relying on it.

## What it is

Claude Opus 5 released **2026-07-24**, API ID `claude-opus-5` (no date suffix).
Anthropic positions it as coming close to Fable 5's frontier intelligence at half the
price. It is the **new default on Claude Max**, the strongest model available on Claude
Pro, and the default for coding in Claude Code. Available same-day on the Claude API,
Amazon Bedrock (`anthropic.claude-opus-5`), Google Cloud, and Microsoft Foundry.

Pricing is **$5 / $25 per million tokens — unchanged from Opus 4.8**, which makes this
a straight capability upgrade at flat cost rather than a new price tier. Context window
is 1M (both default and maximum), max output 128K.

Fast mode is supported at 2.5× output speed for 2× base cost ($10 / $25 → $10 / $50 per
MTok), Claude API only — not Bedrock, Google Cloud, or Foundry.

## Benchmarks as claimed

Anthropic's own numbers, not independently verified:

| Benchmark | Claim |
|---|---|
| Frontier-Bench v0.1 | Surpasses all models; roughly doubles Opus 4.8 at lower cost |
| CursorBench 3.2 | Within 0.5% of Fable 5's peak, at half the cost |
| ARC-AGI 3 | ~3× the next-best model |
| Zapier AutomationBench | 1.5× the pass rate of next-best at the same cost |
| OSWorld 2.0 | Beats Fable 5 at one-third the cost |
| Organic chemistry | +10.2 percentage points over Opus 4.8 |

Anthropic also calls it their most-aligned Opus, and says cyber classifiers intervene
about 85% less often than on Fable 5 — relevant because false-positive refusals on
benign adjacent work were a Fable 5 friction point. It remains behind Mythos 5 on cyber
exploitation and biology research.

## Two breaking API changes

Both matter for anything that builds on the API rather than just using Claude Code.

**Thinking is on by default.** Omitting the `thinking` parameter now runs adaptive
thinking; on Opus 4.8 and 4.7 omitting it meant *no* thinking. Since `max_tokens` caps
thinking plus response text together, a call sized tightly around its answer can now
truncate mid-response.

**Disabling thinking is capped at `high` effort.** `thinking: {type: "disabled"}` paired
with `xhigh` or `max` returns a 400. Validated per request, so a later call that raises
effort while thinking is still off fails even if earlier calls succeeded.

Unchanged from 4.7/4.8: `budget_tokens` still 400s, sampling parameters
(`temperature`/`top_p`/`top_k`) are still rejected, and last-assistant-turn prefills
still 400.

## Two new API features

**Mid-conversation tool changes** (beta `mid-conversation-tool-changes-2026-07-01`) add
or remove tools between turns without invalidating the prompt cache. Previously any edit
to the tool set re-billed the entire prefix, because tools render at position 0.

**Automatic fallbacks** (beta `server-side-fallback-2026-07-01`) route a safety-declined
request to a substitute model server-side rather than just stopping. `fallbacks:
"default"` picks the substitute by refusal category — cyber-category refusals land on
Opus 4.8. This is already wired into claude.ai, Claude Code, and Cowork.

Smaller but useful: the **minimum cacheable prompt drops to 512 tokens** (from 1024 on
Opus 4.8), so prompts previously too short to cache now create entries with no code
change. Opus 5 also draws on a **separate rate-limit bucket** from the combined Opus 4.x
pool — shifting traffic neither frees headroom on the old pool nor inherits it.

## Behavioral shifts that drive prompt tuning

Anthropic's own migration guidance, and the part most likely to affect vault and skill
work. Opus 5 verifies its own work unprompted, so explicit "double-check your answer"
scaffolding now causes redundant work rather than helping — the guidance is to **delete**
it, which inverts the usual self-check best practice. It writes longer user-facing
responses and longer files to disk, and `effort` is explicitly *not* the lever for
shortening visible output; prompting is. It narrates more between steps than 4.8, can
expand task scope beyond what was asked, and narrates its own self-corrections at
length.

It also **delegates to subagents more readily** — the opposite direction from Opus 4.8,
which under-reached and needed prompting to delegate. Any "delegate more" guidance
written for 4.8 should come out, and a spawn cap is the reliable lever.

## Routing implication

This supersedes the prior rule that Fable 5 is the tier above Opus and gets the hard
work. Opus 5 closes most of that gap at half Fable's cost, so the working rule is now
**Opus 5 for essentially everything including hard reasoning and long-horizon agentic
work, Fable 5 only for genuinely maximal runs**. Constraint remains rate limits, not
availability.

## Not part of this launch

The doubled Claude Code 5-hour limits and the removed peak-hours reduction were a
**2026-05-06** change and surface in searches near the release date. Nothing in the Opus
5 announcement changes plan-level usage limits.
