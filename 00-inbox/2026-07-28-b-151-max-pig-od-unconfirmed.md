---
type: finding
status: open
created: 2026-07-28
tags: [heater-card, pig-sizing, suncor, backlog]
---

# B-151 max pig OD is still an approximation, unlike B-101

`02-facilities/Suncor/Montreal-QC/B-151.md` carries:

> Max pig OD (in) | Governed by ID ~4.03" → max pig OD ≈ 4.28" (consistent with the 4" pig family used across this package)

Its sibling `B-101.md` was confirmed from the BOM on 2026-07-07 and now reads `confirmed ID 4.026" → max pig OD ≈ 4.276"`.

## Status: not a regression

Verified 2026-07-28 — the approximate value is B-151's genuine committed state, not a silent revert. The 2026-07-19 stale-buffer incident touched B-101 only, and this was already predicted in that note's own footnote.

## The open question

Does B-151 deserve the same BOM-based ID confirmation B-101 got? The two are in the same package and the difference is currently one of evidence, not of physical fact — `~4.03"` and `4.026"` round to the same pig family, so nothing operational is riding on it today. What is unsatisfying is that two sibling heaters carry different confidence tiers for the same field with no recorded reason.

Cost is presumably one BOM read, the same as B-101's.

## Provenance

Surfaced by the pre-staging loop in [[2026-07-28-prestaged-stale-editor-buffer-guard]] and explicitly held out of scope there — it is a heater-card content decision, not a systems question, and bundling it would have muddied that review. Filed here so it is not lost with the session.
