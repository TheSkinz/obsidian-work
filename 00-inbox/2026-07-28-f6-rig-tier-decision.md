<!-- vault-loop: operational — F6 regression-fixture rig-tier decision, Lane 4 (04-knowledge, usadebusk-estimating scope). Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
---
type: note
status: open
created: 2026-07-28
tags: [regression, estimating, open-item, decision-needed]
---

# F6's rig tier — a decision for Jesse, and it is a fixture problem not a heater problem

**Read this first: ExxonMobil Beaumont F-42 is synthetic.** It does not exist. There is no such
job, no such heater, no job walk and nobody to call. Every real ExxonMobil card in the vault is
Baytown (F-201, F-301, F-371A, F-501, F-802, F-901). The fixture was authored 2026-07-19 by
Fable 5 in `7d5eebd`, the commit that created the whole regression suite, and its first line has
said "(Synthetic)" ever since.

I described this during the session as "worth a phone call to whoever walked that heater," which
implied live commercial exposure. It is not. Nothing in the regression battery is a real bid —
DSP26900, DSP26901, USA26900, CITGO Lake Charles H-101, Delek Tyler H-201 and ExxonMobil Beaumont
F-42 are all invented, deliberately outside the real quote sequences, and none of it should reach
a customer or be ingested into the vault.

## What is actually open

F6's rig-in tier is not derivable from the fixture text. The paragraph reads "Trimax set-out is
well back from the heater; a long hard-pipe and hose run is needed to reach all six launcher
positions," against a walk-up 8 ft elevation with no crane. That is honestly readable as **Large**
(8, giving 10 with the fitter adder) or **Very large** (12, giving 14). Four replays since the
2026-07-28 patches have split three-to-one Large over Moderate. Jesse's own stated figure for this
heater shape is **rig-in 12**, which matches neither computed result.

It moves the F6 quote by a full shift, so it is the largest remaining source of legitimate
re-diff in the battery's duration fixture.

## Why this is a fixture-authoring miss, not a knowledge gap

The original 2026-07-19 fixture had **no job walk paragraph at all**. The ambiguous text was added
2026-07-25 in `98ac964`, and that commit's own fixture note states the intent:

> The launcher-access paragraph above was added at the same time so the rig tier is derivable from
> the rule that now governs it (connection elevation, run distance from the pumper, pipefitter
> wait) rather than left to free judgment.

It was written specifically to remove the ambiguity and it did not. It replaced "no information"
with "qualitative information that reads two ways." Prose was used where a number was needed.

Worth noting the same commit's *other* change — rewording the rate instruction so the job-stated
$64.00/hr governs — worked and has been stable on every replay since. The technique is sound; this
one paragraph just was not specific enough.

## The two ways to close it

**Amend the fixture** — replace "a long hard-pipe and hose run" with a run distance in feet, or
state the tier outright. F6's frontmatter has said since 2026-07-25 that this makes the rig line
deterministic. Finishes what `98ac964` set out to do. Cost: F6 stops exercising tier *selection*.

**Or rule the tier as judgment** — say which tier that description should select and it becomes the
recorded expected reading, leaving F6 testing judgment as it does now.

**My recommendation is to amend.** The tier *reasoning* is already well covered — replays correctly
set aside the fallback ladder because a job walk was completed, named both drivers, said which
dominates, stacked the adder rather than promoting the tier, and mirrored rig-out in full. Those
are all diff keys and they hold. What the ambiguity adds is a rig line that can swing four hours
between runs for a reason the battery cannot detect, which is noise in the one fixture whose whole
job is duration arithmetic. Pin the number; keep the reasoning requirements as diff keys.

Either way this changes what F6 measures and one option changes a quoted duration, so it is not
mine to do unasked.

## Small item riding along

F5's frozen frontmatter does not record a config commit in the `@ <hash>` format the other five now
use. Content is fine and it is current, but it is not greppable with the others. Cosmetic —
worth folding into whichever session next touches the battery.
