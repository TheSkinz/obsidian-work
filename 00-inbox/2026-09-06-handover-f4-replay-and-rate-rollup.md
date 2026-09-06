---
type: review
status: open
review_type: handover
source_authority: session
confidence: high
created: 2026-09-06
review_after: 2026-10-06
related:
  - "[[rfq-intake-protocol]]"
  - "[[equipment-library]]"
tags: [handover, regression, estimating, rates]
---

# Handover — two items left open by the 2026-09-06 Waterous session

Neither is urgent and neither blocks anything. Both are executable from this note by a fresh
session with no other context. They are unrelated to each other.

---

## Item 1 — Replay fixture F4 against the equipment-skill edit

### Why

Config commit `35e53c6` added a **Pump** line to the Trimax block of
`~/.claude/skills/usadebusk-equipment/SKILL.md` — Waterous CMU two-stage centrifugal, one per
assembly, with NFPA and max-pressure ratings. The registry had never named the pump
manufacturer at all.

`baseline_staleness.py` flagged F4 and F5 as loading that skill with no replay dated
2026-09-06.

**F5 is already settled and needs nothing.** Its frozen output
(`regression/frozen/f5-pig-sizing-output.md`) contains zero occurrences of `waterous`, `pump`,
`stage` or `GPM` — checked directly. The pump is entirely absent from what F5 produces, so a
pump line in the skill cannot move it.

**F4 is the open one.** Its frozen output names the Trimax and its three pump *assemblies* but
never the manufacturer, model, or any pump rating — `frozen/f4-sop-output.md:105` renders the
equipment-table row as "Three independent pump/engine assemblies, shared 3,000 gal clean tank
and 2,000 gal dirty tank, three operator stations." That row is exactly where new manufacturer
detail would surface.

No number changes and no rule reverses. The risk is **additive drift into one table row**,
which is the class this check exists to catch. That is why it was not waved through as
non-substantive.

### How

Procedure is canonical at `regression/README.md:196` ("How to replay on another model") and
`regression/runs/claude-opus-5/REPLAY-CHECKLIST.md`. The essentials:

1. Fresh session, vault as working directory.
2. Load **exactly** `usadebusk-core` + `usadebusk-equipment` + `usadebusk-sop` and nothing
   else. The run must read `04-knowledge/sops/sop-formatting-standard.md` from the vault.
3. Paste the replay prompt and fixture body from `regression/fixtures/f4-sop-input.md`
   verbatim. Do not coach, do not correct mid-run, do not supply anything the fixture omits.

**Use an allowlist, not a denylist** (README, 2026-09-03). Name what the run MAY read and deny
everything else — **including the project `CLAUDE.md` session-startup routine**, which would
otherwise send the agent into `01-context/`, `50-dashboards/health.md` and `INDEX.md` before it
does anything. `health.md` publishes the fixture roster by name. Fence *reads*, not just
citations: no Grep, Glob, find or directory listing over a denied path. Worked example of a
clean run's disclosure is in `frozen/f4-sop-output.md` § `run_context`.

If something leaks anyway, **disclose it in the promoted file's frontmatter rather than
quietly discarding the run** — F6's `blinding_leak_DISCLOSED` is the precedent, and it argues
*for* that run rather than against it.

### What to look for

One question: does the equipment table now name the Waterous pump where the frozen baseline
does not? If it does, that is expected additive drift from `35e53c6` and the baseline gets
re-promoted. If the output is otherwise unchanged, that is the whole finding.

Do not advance `baseline_commits:` without an actual replay — the README calls that "a lie
about what was verified."

Run `python tools/baseline_staleness.py --verbose` from the vault rather than reading the
commit table in the README; that table has been wrong four times and the frontmatter is
authoritative.

---

## Item 2 — The rate-history rollup trigger fired, but only half of it did

### The finding that matters

`50-dashboards/health.md` shows `rfq-intake-protocol` as **FIRED** at 13 quote notes against a
threshold of 12. **Do not start building on that.**

The trigger reads: *"About 12 quote notes **under a settled rate-table heading convention** →
build the cross-quote rate-history rollup [machine: quote-count>=12]."* Two conditions. The
machine gate measures only the count. The heading condition — the thing the note itself named
as the blocker — is still unmet.

Checked across all 13 `type: quote` notes on 2026-09-06:

| Heading | Count |
|---|---|
| `## Hourly Rates (T&M)` | 6 |
| `## Hourly Charge-Out Rates` | 2 |
| `## Rate Schedule — DSP#26006` | 1 |
| `## Rates` | 1 |
| *(no rate heading at all)* | 3 |

Four heading forms across ten notes, three notes with none (DSP24005, DSP26092,
DSP26030_H28_H29). `## Hourly Rates (T&M)` is the plurality at 6 of 13 and is the obvious
target if these get normalized.

**DONE 2026-09-06 — this precondition is now clear.** Jesse ruled normalize rather than write a
tolerant parser, on his own recorded test of whether the work terminates (ten headings does;
per-note hygiene forever does not). Settled name is **`## Hourly Charge-Out Rates`** across all
ten notes carrying a rate table.

The name was *not* the plurality. `## Hourly Rates (T&M)` had six of ten, but
`usadebusk-estimating` SKILL.md:478 already names the proposal's **Section 9 — Hourly Charge Out
Rates**, and `04-knowledge/workup-to-proposal-generator-build-spec.md:81` maps the generator
against it — so the two-note minority form was the one aligned with canon and the six were the
drift. The `(T&M)` parenthetical was dropped as well: it asserts a contract basis, and DSP26058
is `Basis: Lump Sum` under a heading that claimed T&M. Basis lives in the `billing-basis` /
`rate-basis` frontmatter, which is where the rollup should read it.

The convention is now written into `rfq-intake-protocol.md` step 9 — there is no quote-note
template, so without that it would simply drift again on the next bid.

**The rollup itself is still unbuilt.** Everything below still applies to building it.

### Design constraints already ruled on — read before building

All from `04-knowledge/concepts/rfq-intake-protocol.md` § Open Questions, and they are not
optional:

- **Pattern to follow:** `tools/estimating_rollup.py`. The note names it explicitly.
- **Show the spread, do not collapse it.** The unit of truth is the quote note; the rollup
  date-orders and compares, it does not resolve.
- **Anchor to the house standard.** USADebusk *prefers* to run the same rates everywhere — the
  house standard is the intended rate, not a starting point. So a `House standard` column
  alongside the per-quote columns is the honest shape, and a cell that **differs** from it
  reads as a flag, not an equally-valid alternative.
- **Two legitimate drivers of divergence, per Jesse 2026-07-26:** contract term (a short-form
  scope contract freezes its rates and ends with the scope, so two old quotes differing can be
  two moments in time rather than two policies) and competitive pressure (rates cut to win a
  contested RFQ — a deliberate commercial act, not drift).
- **Department/division is NOT the discriminator.** An earlier reading attributed the spread to
  different groups issuing bids at one site; Jesse walked that back. Department correlates, it
  does not cause. Recorded so it is not re-derived.
- **Target shape already exists as a worked example:**
  `02-facilities/ExxonMobil/Baytown-TX/_facility.md` § `## Rate History — Baytown`.

### Why it is worth building at all

`DSP25123` (F-901, Baytown) carried Filtration Standby at **$35/hr** against the $150/hr on
every other quote that has the row — the sheet was built from the F-802 template and a deleted
Support Unit row pulled the $35 up one cell. It was caught only by cross-reading three Baytown
quotes side by side, which is precisely the manual work this rollup replaces.

### One stale figure to fix while there

`rfq-intake-protocol.md` § Open Questions still reads *"Quote-note count is now 7 of the ~12."*
It is 13. Correct it whenever that note is next touched.

---

## Not in scope for either item

- The two long-overdue inbox notes (`2026-08-11-outlook-doc-three-copies`,
  `2026-08-11-quote-notes-missing-date-submitted`). Jesse ruled on 2026-09-06 to leave both
  alone. Both are blocked externally: the first needs a `.docx` read inside the M365 tenant,
  the second needs two questions put to Jason about DSP26085's submission date and whether
  DSP26080 has drawn any response since 2026-06-26.
- The inverted wordmark in `02-facilities/HF-Sinclair/Artesia-NM/USA26040-job-sheet.html` and
  the Syncrude `CAD26001-job-sheet.html` — both render `USA` dark and `DEBUSK` gold, where the
  real logo (now at `assets/brand/usadebusk-logo.png`) is `USA` gold and `DEBUSK` dark.
  Internal-only sheets, so cosmetic.
