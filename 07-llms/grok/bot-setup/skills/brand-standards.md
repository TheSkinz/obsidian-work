# Brand Standards — USADebusk documents

**Use whenever you build a customer-facing document.** Project Report and Proposal Assembly both
depend on this file. Any skill that says "branded", "amber", or "the house style" means these values.

⚠ **This file is a MIRROR, not the authority.** The canonical source is the Brand Standards section
of the `usadebusk-core` skill, which lives at `~/.claude/skills/usadebusk-core/SKILL.md` on Jesse's
machine and **cannot be read from here** — that is the only reason this copy exists. **Synced
2026-09-07.** If a value here ever disagrees with `usadebusk-core`, `usadebusk-core` wins. A brand
change has to be made in both places or this copy goes silently stale.

## The values

| Element | Spec |
|---|---|
| Font | Helvetica — **Arial is the accepted fallback for DOCX generation** |
| H1 | 13pt bold `#222222`, gold `#FCC30A` bottom border |
| H2 | 11pt bold `#FCC30A` |
| Body | 10pt `#555555` |
| Footer / header | 8.5pt `#888888` |
| Table header | `#222222` fill |
| Alt row background | `#F7F7F7` |
| Callout background | `#FFFBE6` with a `#FCC30A` accent |

**"Amber" means `#FCC30A`.** Every amber eyebrow, amber sub-header and amber callout in the other
skills is this gold. Nothing in a USADebusk document is blue.

**Never accept a library default.** python-docx applies its own table style if you do not set one,
and that default is blue — which shipped in the 2026-09-07 build and is exactly what this file
exists to prevent. Set the header fill, the alt-row shading and the fonts explicitly on every table.

## The logo

| Job prefix | Trades as | File |
|---|---|---|
| `USA` | USADebusk | `/workspace/vault/assets/brand/usadebusk-logo.png` |
| `CAD` | DeBusk Services Canada | `/workspace/vault/assets/brand/debusk-services-canada-logo.png` |

Place it with `run.add_picture(path, width=Inches(1.6))` and let the height follow the aspect ratio.
**Never reconstruct either wordmark** from shapes or text — a rebuilt logo that looks close is worse
than a placeholder, because it ships. If the file is genuinely missing, write `[logo]` and say so.

Canadian work is sold, planned and executed identically to US work. **The trade name and the logo
are the only differences.** `CAD` is the only Canadian prefix — `CND` is not valid, and you will
meet it in older documents written while a wrong convention circulated.

## The name in body text

**`USADebusk`** — closed form, capital U-S-A, lowercase b. **Never `USADeBusk`.**

**One exception, and it is customer-facing:** the spaced legal form **`USA DeBusk, LLC` keeps its
capital B** and is reproduced verbatim in contracts, signature blocks and anywhere the legal entity
is named. It is the family surname; lowercasing it there misspells the company.
