---
title: Skill/vault drift — rig-in method, caught by hand not by the loop
created: 2026-09-06
status: resolved
tags: [review, drift, estimating, lane-4]
related:
  - "[[estimating-approach]]"
  - "[[system-workflow-reference]]"
---

# Skill/vault drift — rig-in, 2026-09-05 to 2026-09-06

**Found while porting the estimating skill to Grok Bot, not by the skill-drift loop.**

## What drifted

The config repo replaced the rig-in method on **2026-09-05** — commit `[Lane 4] estimating: rig-in
is 6 hours -- replace the tier machinery with Jesse's method`. `01-context/estimating-approach.md`
did not receive it. Its last duration-model edit was 2026-08-23; the 2026-09-02 commit that touched
the file was the CAD/CND rename and left the rig-in passage alone.

For 24 hours the two artifacts described **different models**, not different values:

| | Vault (stale) | Skill (current) |
|---|---|---|
| Shape | Four tiers: Small 4 / Moderate 6 / Large 8 / Very large 12 | One default of 6, two conjunctive departures |
| Drivers | **Three** — elevation, run distance, mode | **Two**, and named as background, not a calculation |
| Combination | They **multiply**; a low reading does not offset a high one | Not combined at all — *"do not tier from an arithmetic result"* |
| Posture | Tier the line from the connection points | *"Use the default. Do not build a method for this line."* |

Corrected in the vault 2026-09-06. The skill was already right and was not touched.

## Why it matters more than a one-day gap suggests

**A session reading `01-context/` would have priced rig-in by the retired method and had no way to
know.** The file loads every session; the skill loads only when the task is recognised as
estimating-shaped. So the stale copy is the one with the wider blast radius, which is the opposite
of the usual assumption that skills are the fragile layer.

It surfaced here because a Grok Bot Librarian, asked what the primary rig-in drivers were, answered
**three, and they multiply** — quoting `estimating-approach.md:24` correctly. The citation was real
and the quote was verbatim; the source was wrong. **A passing citation audit does not detect a
stale source**, and that is worth remembering before treating "every answer was cited" as
sufficient.

## Why the loop did not catch it

The skill-drift loop runs **monthly, on the 1st** (`system-workflow-reference.md`). The drift was
created on the 5th, so the next scheduled run would have been **2026-10-01** — 26 days of exposure
on a Lane 4 number that appears in every quote.

This is the known shape from the 2026-08-21 architecture audit: schedule-triggered checks run at
about half the effect rate of defect-triggered ones. The loop is not misconfigured; a monthly
cadence simply cannot cover a same-week edit.

**Cheap defect-triggered alternative, not built and not proposed as work:** a Lane 4 commit in the
config repo that touches a rule the vault also states is a detectable event. Nothing currently
compares the two repos at commit time. Recorded here as an observation, not a build request — the
last thing this system needs is another gate that fires on nothing.

## Decision

- [x] Vault corrected to the 2026-09-05 skill ruling — 2026-09-06.
- [x] Retired model named explicitly in the corrected passage, with the dates it was live, so a
      document written from it during the gap can be recognised rather than silently trusted.
- [ ] No new automation. Revisit only if a second same-week Lane 4 drift appears.
