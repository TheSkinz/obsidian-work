# Lint fixtures

Deliberately broken notes proving each `vault_lint.py` rule fires. One file per
rule. Excluded from normal vault lint (`tools/fixtures` is in `SKIP_SCAN`);
exercised only by `python tools/vault_lint.py --self-test`.

Any new lint rule must add a fixture here that fails without the rule and is
caught with it — **no fixture, no rule** (contract stated in the `vault_lint.py`
module docstring). A lint-rule change is a structural change: ship it with its
passing fixture.

| Fixture | Rule it trips | Severity |
|---|---|---|
| `02-facilities/TestClient/Test-City-TX/T-100.md` | OP-FRONTMATTER | warning |
| `02-facilities/TestClient/Test-City-TX/T-200.md` | DURATIONS-HEADER | warning |
| `02-facilities/TestClient/Test-City-TX/T-300.md` | TUBE-GEOM-HEADER | warning |
| `02-facilities/TestClient/Test-City-TX/T-400.md` | LINK-FACILITY (both halves) | warning |
| `06-insights/dead-link-note.md` | DEAD-LINK | warning |
| `08-systems/secret-note.md` | SECRET | error |
| `04-knowledge/bad-status.md` | STATUS-VOCAB | warning |
| `06-insights/conf-conflict.md` | CONF-CONFLICT | error |
| (created at self-test runtime in `00-inbox/`) | INBOX-AGE | warning |
| `06-insights/yaml-comment-note.md` | YAML-COMMENT | error |
| `word-delta/before.md` + `after.md` | WORD-DELTA | warning |

The secret fixture uses AWS's documented example key — it is not a live
credential.

`word-delta/` is a pair, not a single broken note: WORD-DELTA compares two
revisions rather than reading the tree, so its fixture is a before/after pair fed
straight to the comparison (same reason INBOX-AGE and POINTER-DEAD build theirs
at runtime). The pair is a reflow that also reworded — every line rewraps, so a
line diff is useless, while `concurrently`, `Mode = 3` and a closed ruling
vanish. That is the F-501 failure in miniature. Editing either file so those
tokens survive fails the self-test on purpose.
