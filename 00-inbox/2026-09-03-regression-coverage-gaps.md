---
type: finding
status: open
created: 2026-09-03
tags: [inbox, regression, coverage, fieldpm, vault-ingest, needs-ruling]
---

# Three regression coverage gaps a replay cannot surface

From the 2026-09-03 battery. These are gaps in what the fixtures *test*, not failures of what they tested — no replay will ever report them, because the battery can only measure what a prompt makes a run emit. The README's own name for this failure mode is **"coverage by elaboration is not coverage."**

## 1. F2 does not compel the two newest card-schema changes

F2's replay prompt names only the Tube Geometry and Config Rollup sections. Two schema changes have landed since its baseline and neither is compelled by that prompt:

- `2f3e446` added `source:` and `verified:` as heater-card **frontmatter** fields, with `verified:` lint-locked to a date or the literal `never`. The prompt does not ask for frontmatter.
- `123f4bb` added the optional `## Coilset Durations` section. It fills only from a job report carrying a per-coilset breakdown; F2's source is a DSP quote, so a *correct* run omits it entirely. The section can never be exercised by this fixture as written.

The 2026-09-03 run did emit `source: DSP#26901` / `verified: never` correctly and did correctly omit Coilset Durations — **but only by volunteering a completeness section it was not asked for.** The next run need not volunteer. This is the same shape as the 2026-07-27 Tube Geometry problem that took three passes to diagnose, and the fix then was to name the sections in the prompt.

**Proposal:** extend F2's replay prompt to also name the proposed card's frontmatter block. **Cost, stated honestly:** an amended prompt makes the next run not strictly comparable to earlier baselines on scope, though the numeric diff keys are unaffected. That trade was accepted once before, on 2026-07-28, for exactly this reason.

**Coilset Durations needs a different answer** — no DSP-sourced fixture can reach it. It would need a job-report fixture, which is gap 2.

## 2. The job-report generator has no fixture at all

`3fab7fe` rewrote fieldpm's job-class and per-coilset-hours capture rules, and they live in the `/report` section. **F3 is `/extract` only.** Twenty-one commits have landed on `skills/usadebusk-fieldpm/scripts/`, `back-test/` and `references/report-structure.md` since F3's baseline — the renderer, its config format, the refuse-to-overwrite guard, the KPI gold rules, section ordering — and this battery measures none of it. F3 reads 25 commits `behind` almost entirely because of work it does not touch.

**For Jesse:** is a seventh fixture worth building, or does the generator's own tier-one structural back-test (`0f64003`, `back-test/assert_structure.py`) already carry that load? The back-test checks structure; it does not check whether the *rules about what to capture* still produce the right content. Those are different questions, but the second may not be worth a fixture.

## 3. `baseline_staleness.py` cannot express "judged, not owed"

F3 and F5 were both judged this session as not needing a replay, with the evidence recorded in the session plan and the README. The tool still reports them `behind`, because it counts commits touching declared paths and takes no position on substance — deliberately, per its own docstring: *a false alarm costs a glance, a missed one costs a wrong number in a customer's quote.*

Consequence: **F3 and F5 read red on the health dashboard indefinitely**, and a permanently-red row is one people learn to click through — the same wallpaper problem the fixture-replay guard's own design notes reject at 70% firing.

**Do not fix this by advancing their `baseline_commits:` without a replay.** That would assert a verification that never happened, which is the one thing this battery exists to prevent.

Possible shapes, none designed: a `staleness_reviewed:` frontmatter field carrying a hash and a date, so the tool can report `reviewed (n behind)` distinctly from `behind`; or a separate acknowledgement file; or accept the red and document it. The first is the obvious one but it introduces a way to silence the detector, which needs thinking about before it is built.

Related: [[2026-09-03-regression-battery-findings]]
