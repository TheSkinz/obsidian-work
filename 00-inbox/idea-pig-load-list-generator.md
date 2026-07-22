---
type: idea-seed
status: researched
created: 2026-07-19
related:
  - [[2026-07-22-idea-research-pig-load-list-generator]]
tags: [idea, vault-system, future, estimating, field-ops]
---

# Pig load list generator from heater cards

Idea seed captured 2026-07-19 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** Jesse said the Max Pig OD field exists to help build a **pig load list for the current project**, and that he hasn't had the chance to set that workflow up yet. Right now the card data needed to produce one is scattered and inconsistently useful: some cards carry a rule-derived max (H-2421: 6"/6.125"), some carry restriction facts plus largest-pigs-actually-run because the +0.250" rule doesn't describe the coil at all (P66 H-28/H-29 are bend-limited — 2.6" bends on 2.90"/2.75" tubes, yet 3.875" TC pigs ran through by compression). A generator that reads a job's heater cards and emits a load list — sizes, types, and quantities to put on the truck — would turn that field from a stranded number into the thing it was created for. Real quantity evidence already exists to calibrate against: the 24012 pig usage table (combined H-28/H-29, ~265 pigs across 16 sizes) and USA25041's actuals.

**To explore:** What a load list actually needs as output — sizes and counts only, or types and staging by pass. Whether quantity is derivable at all or is purely experience-driven (the 24012 distribution is heavily weighted to 2.75"/2.875", suggesting most consumption happens at the sizes where real cutting occurs, not across the whole ladder). How to handle bend-limited coils where the sizing rule doesn't apply — does the generator refuse to guess and surface the restriction plus prior actuals for a human call, which is the honest behavior. Whether it belongs in `usadebusk-equipment` (sizing authority) or `usadebusk-estimating` (job-scoped output), or is a small tool under `tools/`. Whether it should read from cards only, or also from the quote's pass count and duration plan. Related guidance already saved to agent memory: the Max Pig OD field is a general rule, not something to reference everywhere.
