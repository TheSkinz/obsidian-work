# Lint fixtures

Deliberately broken notes proving each `vault_lint.py` rule fires. One file per
rule. Excluded from normal vault lint (`tools/fixtures` is in `SKIP_SCAN`);
exercised only by `python tools/vault_lint.py --self-test`.

Any new lint rule must add a fixture here that fails without the rule and is
caught with it — **no fixture, no rule** (contract stated in the `vault_lint.py`
module docstring). A lint-rule change is a structural change: ship it with its
passing fixture.

All 21 rules, each with the fixture that proves it fires. Severity comes from
`ERROR_CODES` in `vault_lint.py` — SECRET, CONF-CONFLICT, YAML-COMMENT, DEAD-LINK,
HEATER-TYPE-VOCAB, VERIFIED-FORMAT and DEAD-STRING are errors, every other rule is
a warning.

| Fixture | Rule it trips | Severity |
|---|---|---|
| `02-facilities/TestClient/Test-City-TX/T-100.md` | OP-FRONTMATTER | warning |
| `02-facilities/TestClient/Test-City-TX/T-200.md` | DURATIONS-HEADER | warning |
| `02-facilities/TestClient/Test-City-TX/T-300.md` | TUBE-GEOM-HEADER | warning |
| `02-facilities/TestClient/Test-City-TX/T-400.md` | LINK-FACILITY (both halves) | warning |
| `02-facilities/TestClient/Test-City-TX/T-500.md` | ROLLUP-SCALE | warning |
| `02-facilities/TestClient/Test-City-TX/T-600.md` | HEATER-TYPE-VOCAB | error |
| `02-facilities/TestClient/Test-City-TX/T-700.md` | VERIFIED-FORMAT | error |
| `02-facilities/TestClient/Test-City-TX/T-800.md` | PATH-DEAD | warning |
| `04-knowledge/bad-status.md` | STATUS-VOCAB | warning |
| `04-knowledge/dead-string.md` | DEAD-STRING | error |
| `00-inbox/marker-before-frontmatter.md` | STATUS-VOCAB (regression) | warning |
| `06-reviews/dead-link-note.md` | DEAD-LINK | error |
| `06-reviews/conf-conflict.md` | CONF-CONFLICT | error |
| `06-reviews/review-overdue.md` | REVIEW-OVERDUE | warning |
| `06-reviews/superseded-note.md` | SUPERSEDED | warning |
| `06-reviews/yaml-comment-note.md` | YAML-COMMENT | error |
| `07-llms/orphan-fixture-note.md` | ORPHAN | warning |
| `08-systems/secret-note.md` | SECRET | error |
| `02-facilities/pointer-dead-temp-selftest.md` (built at runtime) | POINTER-DEAD | warning |
| `02-facilities/TestClient/USA00000-job-sheet.{html,pdf}` (built at runtime) | JOBSHEET-PDF-STALE | warning |
| `word-delta/before.md` + `after.md` | WORD-DELTA | warning |
| `checkbox-delta/before.md` + `after.md` | CHECKBOX-DELTA | warning |

Twenty-two rows for twenty-one rules: STATUS-VOCAB has two fixtures. `bad-status.md`
is the plain case; `marker-before-frontmatter.md` is a regression test for
`frontmatter_start()`, where a capture-loop marker on line 1 once hid the whole
frontmatter block from every frontmatter rule.

**This table was five rules behind on 2026-09-05** — ROLLUP-SCALE, HEATER-TYPE-VOCAB,
VERIFIED-FORMAT, DEAD-STRING and JOBSHEET-PDF-STALE all had committed or runtime
fixtures and no row, DEAD-LINK's severity was stale (promoted to error 2026-08-21),
and the retired INBOX-AGE still had one. Reconciled while adding PATH-DEAD. The
drift is the reason for the section at the bottom of this file; run that check.

The rows marked *built at runtime* are **not committed** — `self_test()` writes
them, asserts, then deletes them. POINTER-DEAD needs a machine-local absolute
path, which cannot be committed; JOBSHEET-PDF-STALE compares mtimes, and git does
not store mtimes, so a committed pair would arrive with identical checkout times
and never fire. Do not add either to the tree. INBOX-AGE had a third such fixture
until the rule was retired on 2026-08-21.

PATH-DEAD's fixture is committed rather than built at runtime, unlike its
absolute-path sibling POINTER-DEAD: a repo-relative path is machine-independent,
so it resolves — or fails to — identically on any checkout. Most of `T-800.md` is
the cases that must **not** fire (line citations, brace expansions, bracketed
placeholders, an absolute path that is POINTER-DEAD's job). Those matter more than
the two that do: the rule's whole design problem is false positives, and the vault
run was measured at 100 findings before scoping and 3 after.

The self-test prints more findings than there are rules, because ORPHAN and
INBOX-AGE scan the whole fixture tree and so also fire incidentally on fixtures
built for other rules — ORPHAN on nearly every one (fixtures are unlinked by
nature), INBOX-AGE on `marker-before-frontmatter.md` for its age. Only the
dedicated fixture for each rule is listed above.

The secret fixture uses AWS's documented example key — it is not a live
credential.

`word-delta/` is a pair, not a single broken note: WORD-DELTA compares two
revisions rather than reading the tree, so its fixture is a before/after pair fed
straight to the comparison (same reason INBOX-AGE and POINTER-DEAD build theirs
at runtime). The pair is a reflow that also reworded — every line rewraps, so a
line diff is useless, while `concurrently`, `Mode = 3` and a closed ruling
vanish. That is the F-501 failure in miniature. Editing either file so those
tokens survive fails the self-test on purpose.

`checkbox-delta/` is the other pair, for the same reason — CHECKBOX-DELTA is also
a diff rule. Its pair loses no words at all: that is the point, proving the two
diff rules catch different failures rather than one shadowing the other. Here a
decision box flips `[ ]` → `[x]` on a note whose status is already closed, which
is the silent-approval failure rather than the silent-deletion one.

## Keeping this table honest

`vault_lint.py`'s `self_test()` asserts against its own `expected` set of rule
codes — that set is the authority, not this table, and the two have drifted
before. After any rule change, run the self-test and reconcile every code it
names against a row here.
