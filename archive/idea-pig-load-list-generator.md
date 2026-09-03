---
type: idea-seed
status: unexplored
created: 2026-07-19
related:
  - [[2026-07-22-idea-research-pig-load-list-generator]]
tags: [idea, vault-system, future, estimating, field-ops]
---

# Pig load list generator from heater cards

> [!warning] Status corrected 2026-09-03 — this was NOT built
> This note sat at `status: complete` from 2026-07-22, and the filename plus that status read as
> though the pig **load list generator** exists. It does not. What shipped on 2026-07-22 was the
> shared **rollup** script, `tools/pig_usage_rollup.py` — a different thing that answers a different
> question. The **per-project pig load list is still wanted and still unbuilt** (Jesse).
>
> Set to `unexplored` rather than `researched`: the 2026-08-15 retirement sweep found that
> `researched` means "Jesse has not decided," is untouchable by the Terminal-Note Sweep, and is
> revisited by nothing — so a seed sent there has no path out. This one has never been explored to a
> decision, which is what `unexplored` says.
>
> **Discoverability caveat:** this note lives in `archive/`, which `vault_lint.py` skips via
> `SKIP_SCAN` and `INDEX.md` does not cover. The status change stops a future session concluding the
> generator exists; it does **not** make the seed surface anywhere. What carries the intent today is
> the agent-memory note `feedback-max-pig-od-field-purpose`. Moving it back to `00-inbox/` would make
> it visible but would immediately become the oldest pending inbox note — Jesse's call, not made.

Idea seed captured 2026-07-19 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** Jesse said the Max Pig OD field exists to help build a **pig load list for the current project**, and that he hasn't had the chance to set that workflow up yet. Right now the card data needed to produce one is scattered and inconsistently useful: some cards carry a rule-derived max (H-2421: 6"/6.125"), some carry restriction facts plus largest-pigs-actually-run because the +0.250" rule doesn't describe the coil at all (P66 H-28/H-29 are bend-limited — 2.6" bends on 2.90"/2.75" tubes, yet 3.875" TC pigs ran through by compression). A generator that reads a job's heater cards and emits a load list — sizes, types, and quantities to put on the truck — would turn that field from a stranded number into the thing it was created for. Real quantity evidence already exists to calibrate against: the 24012 pig usage table (combined H-28/H-29, ~265 pigs across 16 sizes) and USA25041's actuals.

**To explore:** What a load list actually needs as output — sizes and counts only, or types and staging by pass. Whether quantity is derivable at all or is purely experience-driven (the 24012 distribution is heavily weighted to 2.75"/2.875", suggesting most consumption happens at the sizes where real cutting occurs, not across the whole ladder). How to handle bend-limited coils where the sizing rule doesn't apply — does the generator refuse to guess and surface the restriction plus prior actuals for a human call, which is the honest behavior. Whether it belongs in `usadebusk-equipment` (sizing authority) or `usadebusk-estimating` (job-scoped output), or is a small tool under `tools/`. Whether it should read from cards only, or also from the quote's pass count and duration plan. Related guidance already saved to agent memory: the Max Pig OD field is a general rule, not something to reference everywhere.


---

**Closed 2026-07-26.** The 2026-07-22 park trigger ("revisit once more cards have populated
Pig Specifications data") was met — 78 job-sourced rows across 14 cards — and this was
decided together with [[idea-pig-actuals-maturation]] so the shared rollup script was built
once, not twice. Shipped: `tools/pig_usage_rollup.py` → `04-knowledge/pig-usage-rollup.md`.
The pig *load list* generator itself — per-project 1/8" load lists for the field — was not
built and is not closed by this; it now has a real usage dataset to draw on if it is
revisited. The two-consumer split — the estimate's 1/4" cost granularity against the field
load list's 1/8" increments — is in `usadebusk-estimating` under Pig Quantity Estimating.
