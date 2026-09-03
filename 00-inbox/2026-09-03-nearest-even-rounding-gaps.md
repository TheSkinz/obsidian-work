---
type: finding
status: open
created: 2026-09-03
tags: [inbox, estimating, duration-model, regression, needs-ruling]
---

# Two gaps in the nearest-even rounding rule

`5d38984` (2026-08-23) replaced always-round-up with *"Round the per-coil figure to the NEAREST EVEN HOUR — up or down — once, at the coil level."* Both F1 and F6 exercised it on 2026-09-03 and it worked. Two edges are undefined. **Nothing has been changed; neither gap touches any figure currently in a baseline.**

## 1. Ties are undefined

An exact `.0` odd quotient sits equidistant between two even hours and the rule does not say which way it breaks. The F6 run hit this in an aside, computing the counterfactual at the ungated default as `900 ÷ 100 = 9 → 10 hrs` — but 9 is exactly 1 from both 8 and 10, and nothing licenses 10 over 8.

It changed nothing there (F6's stated 75 ft/hr gives 12.0, which needs no tie-break) and nothing in F1 (11.2 → 12 is unambiguous). But at 100 ft/hr — now the default for every gate-unmet heater — **a tie lands on any coil that is an odd multiple of 100 ft**: 900, 1,100, 1,300, 1,500 ft. Those are ordinary coil lengths, so this will recur.

Two hours on a pigging line is real money once it propagates through Trimax, filtration, labor and per diem.

## 2. The discretionary escape hatch is unbounded

The same rule adds:

> the estimator may shave to a rounder figure and does not have to justify it

worked from DSP#26100, where `17.75 → 18` is nearest-even and `25.61 → 24` is not, both being Jesse's.

**This is an open judgment call sitting in the most load-bearing arithmetic in the battery.** The concern is specific and has a precedent: open judgment on the parallel-friction question returned 15%, 25% and 40% across three runs of two fixtures, and the response was to invent a 25–40% band to suppress the variance — a band that then carried Jesse's name for a month, priced real work, and was struck on 2026-08-23.

Both 2026-09-03 runs happened to land on the mechanical answer and neither invoked the hatch, so no variance was observed. That is one data point per fixture, not evidence the hatch is safe.

## What is NOT being proposed

Not a tie-break rule and not a bound on the discretion. Both are Lane 4 and inventing either here would repeat the exact failure this session was called to clean up.

## For Jesse — two questions

1. On an exact tie, does the estimate go up or down? (Up is the safer default under the stated T&M asymmetry — but that asymmetry argument is the one used to justify *not* padding, so it may cut the other way.)
2. Should a run that shaves off the nearest-even figure be required to *say that it did*, without having to justify why? That would keep your discretion completely intact while making the variance visible in a diff instead of invisible — which is the specific thing that let the parallel allowance hide.

Related: [[2026-09-03-regression-battery-findings]], [[2026-07-24-parallel-friction-factor-deferred]]
