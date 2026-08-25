---
type: idea-seed
status: unexplored
created: 2026-08-24
tags: [idea, vault-system, lint, future]
---

# Lint repo-relative paths cited in prose

Idea seed captured 2026-08-24 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** A repo-relative path written in backticks is invisible to every check the vault has. `04-knowledge/vault-capture-loop-spec.md:124` recorded this as a known hazard on 2026-07-29 and nothing closed it; POINTER-DEAD covers only *absolute* recorded paths, and DEAD-LINK covers only `[[wikilinks]]`. Two live instances surfaced on 2026-08-24: `apps/pig-tracker/pig-tracker.html:393` is cited by approved unexecuted work in three notes with nothing protecting it, and `02-facilities/HF-Sinclair/Artesia-NM/H-2501.md:19` had been pointing at a file that moved to `archive/` — dead, and unnoticed.

**To explore:** Whether the false-positive rate is tolerable — prose mentions paths that never existed (proposals, examples, illustrative snippets), and a rule firing on those becomes wallpaper, which the linter's own docstrings warn against repeatedly. Whether to scope it narrowly (only paths ending in a real extension, only under named folders) or accept warnings-as-backlog. Whether `:NNN` line suffixes should be checked for existence too, or only the file — the pig-tracker case is a *line* reference, and a function moving is the failure mode that reference has. Note the standing contract: **no fixture, no rule** (`tools/fixtures/README.md`), so this owes a fixture at build time.

**Gate:** Delete if researchable now — no external condition blocks it. Deferred on 2026-08-24 by decision, not oversight: it was scoped out of the `apps/` job as its own decision rather than a rider.
