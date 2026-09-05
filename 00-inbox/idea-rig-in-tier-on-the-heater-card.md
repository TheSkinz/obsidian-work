---
type: idea-seed
status: unexplored
created: 2026-09-05
revisit-trigger: three or more heater cards carrying rig-in access facts (pumper set-out distance, connection elevation) in `## Notes`, with at least one estimate having read one
tags: [idea, estimating, heater-card, schema, future]
---

# Carry the rig-in tier on the heater card

Idea seed captured 2026-09-05 for a future exploration session. **This one is Jesse's own, stated in his
words**, so the read below is less tentative than most — but he also said he is unsure how to approach it
and that the subject "really isn't worth the effort," which is why it is a seed and not a build.

> *"I don't know why we couldn't just assign tiers to go on the heater card; light rig-in - 4, medium - 6,
> large - 8, very large - 12. Or something similar."*

**Tentative read:** rig-in hours are currently re-derived at estimate time from job-walk facts, which is
judgment work repeated on every bid for a figure Jesse deliberately does not fine-tune. The tier is a
property of the *heater and its surroundings* — where the pumper can park, how high the connections sit —
not of the job, so it changes rarely and could be recorded once per heater and read thereafter. That would
turn a recurring estimate-time judgment into a lookup, which is the shape of thing worth doing.

**What prompted it:** the 2026-09-05 session found the estimating skill carrying ~28 lines of rig-in tier
machinery — three multiplying drivers, per-mode hose-count calibration, a 12-hr ceiling — against a stated
practice of "default 6, sometimes 8." Worse, the machinery produced 12 for a heater whose real answer under
Jesse's method is 6. The rule has since been cut back to the default plus two named departures
(`b449e63`). This seed is the other half: if the tier lived on the card, the estimate would not need to
select one at all.

**To explore:**

- **Where on the card.** `Connection Info (Facts)` is the natural home — it already holds launcher and
  receiver flange facts — but it currently carries no access, elevation or set-out field at all, so this
  would be a schema addition to `04-knowledge/_canonical-heater-card.md`, the template, and the ingest
  skill's mirror. That is a Lane 4 change across several files for one field.
- **One field or three.** A bare `Rig-in tier: medium` is a lookup but hides its reasoning and will rot
  silently when a unit is re-piped. Recording the two facts Jesse actually reads — pumper-to-base distance
  and connection elevation — lets the tier be re-derived and audited, at the cost of two fields nobody may
  fill. His own framing was the single tier.
- **Who fills it, and from what.** Elevation and set-out come from a job walk. Most heater cards are built
  from a DSP or a bid package with no walk, so the field would start empty on nearly every card and
  populate only after a job runs. An always-empty field is worse than no field.
- **Whether it earns the schema change at all.** The line is 4–12 hours on jobs that run 30–50, Jesse
  says a couple of hours either way is not worth chasing, and it is the least commercially significant
  line in the duration model. The honest case for doing it is not accuracy — it is deleting a recurring
  judgment, and that case should be made explicitly rather than assumed.
- **The cheap alternative first.** `## Notes` on a card can already hold "pumper sets out ~80 ft, launchers
  at grade" as prose today, with no schema change and no lint rule. If two or three cards carry that note
  and it gets used, the field is justified; if nobody writes it, that is the answer.

**Gate:** do not spend a research cycle on this until at least three heater cards carry rig-in access facts
in `## Notes` and at least one estimate has actually read one. Until then there is no evidence the lookup
would be populated or consulted, and the field would be schema for its own sake. Mirrored into
`revisit-trigger:` so the health dashboard keeps it visible while it waits.
