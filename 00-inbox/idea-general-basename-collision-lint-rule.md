---
type: idea-seed
status: unexplored
created: 2026-08-19
related:
  - "[[obsidian-setup]]"
  - "[[2026-08-14-prestaged-obsidian-link-retargeting-guard]]"
tags: [idea, vault-system, lint, obsidian, future]
---

# One lint rule for ambiguous basename links instead of one rule per note type

Idea seed captured 2026-08-19 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** `vault_lint.py` guards ambiguous wikilinks one note type at a time. `LINK-FACILITY` fires only on bare `[[_facility]]` links, which is why it caught `DSP26095.md` on 2026-08-19 and was blind, the same day, to four notes named `overview.md` whose bare `[[overview]]` links in `INDEX.md` sent the ChatGPT row to Grok's file. `DEAD-LINK` cannot see either case, because it reports links resolving to nothing rather than links resolving to the wrong thing. A single rule — flag any `[[stem]]` whose stem matches more than one file vault-wide — would subsume `LINK-FACILITY` and catch every future collision without a new rule per note type.

**To explore:** What the rule's false-positive rate looks like against the vault as it stands, since a collision is only a defect when the link is genuinely ambiguous to a reader and `INDEX.md` historically disambiguated `_facility` rows with trailing plain-text annotations rather than link paths. Whether the rule belongs at error or warning severity, given that the 2026-08-14 pre-staging review anticipated a facility-match rule would need to *exclude* generated index files to avoid misfiring, whereas the actual 2026-08-19 fix went the opposite way and made the generator emit qualified links — which would make generated files the cleanest input, not the exception. Whether `LINK-FACILITY` is then retired or kept as a narrower, higher-severity case. And whether the check is cheap enough to run on every lint invocation, since it needs a vault-wide basename index that `vault_lint.py` may already build for `DEAD-LINK`.

*Source: session 2026-08-19 (`5bbaa6a0`), seeded by the Vault Capture Loop. Commits `55c0b28` (generator fix) and `1fde1d5` (Westlake hand fix) closed the two instances; the general rule was recommended in-session and never recorded.*
