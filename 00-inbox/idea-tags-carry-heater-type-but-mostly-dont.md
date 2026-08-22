---
type: idea-seed
status: unexplored
created: 2026-08-22
tags: [idea, schema, heater-card, vault-lint, data-quality]
related:
  - "[[_canonical-heater-card]]"
  - "[[idea-cross-field-lint-rules]]"
---

# The schema says `tags:` carries the heater-type. Only 1 of 41 cards does it.

Found 2026-08-22 during the heater-type vocabulary migration (vault `9718b8f`), recorded then rather than fixed because it is a third conformance gap and the migration was already touching two.

**The gap.** `04-knowledge/_canonical-heater-card.md`, the template, and `usadebusk-vault-ingest` all specify:

```
tags: [heater-card, <Client>, <heater-type>]
```

Only **F-501** actually carried the heater-type there — it was the single card whose tagline needed updating when its value moved from `hydrotreater` to `other`. The other 40 use a different and more useful shape that nothing documents:

```
tags: [heater-card, CHS, McPherson-Refinery, HP-0025, split-bore]
```

That is client · **refinery name** · **heater tag** · **ad-hoc characteristic** — richer than the spec, and the ad-hoc slot is carrying real signal (`multi-bore`, `radiant-fouling`, `id-discrepancy`, `split-bore`, `source-derived`).

**So the question is which is wrong, and it is genuinely not obvious.** Three readings:

- **The spec is wrong.** The cards evolved a better convention and nobody updated the exemplar. Document what the cards actually do and drop `<heater-type>` from the spec — it is now a lint-locked frontmatter field, so duplicating it in a tag buys nothing except a second place to drift.
- **The cards are wrong.** Backfill the heater-type tag across 40 cards so tag-based search works in Obsidian.
- **Both are wrong.** The real convention is client · refinery · tag · characteristics, and the exemplar should say so — with the characteristic vocabulary either enumerated or explicitly declared free-form.

**Leaning toward the first**, on the same reasoning that settled `Condition` in DQ-026: a field that is already typed and lint-locked does not need a shadow copy in a tag. But `multi-bore` and `split-bore` are doing work no frontmatter field does, so the third reading may be the honest one.

**To explore:**
- Enumerate every distinct tag in slot 4+ across all 41 cards. Is the characteristic vocabulary coherent enough to spec, or is it genuinely per-card?
- Does anything actually *query* these tags — a saved search, a Bases view, a script? If nothing reads them, this is documentation-only and cheap either way.
- Does the new `50-dashboards/heater-fleet.base` make tag-based grouping redundant? It already groups by client and heater-type from frontmatter, which is most of what a tag would have been for.

**Gate:** None — researchable now. Cheap; the whole thing is one `ls`-and-count plus a ruling. Best folded into the next pass that opens the card schema for another reason, per the same convention DQ-017 rode.
