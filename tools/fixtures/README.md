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
| `06-insights/dead-link-note.md` | DEAD-LINK | warning |
| `08-systems/secret-note.md` | SECRET | error |
| `04-knowledge/bad-status.md` | STATUS-VOCAB | warning |
| `06-insights/conf-conflict.md` | CONF-CONFLICT | error |
| (created at self-test runtime in `00-inbox/`) | INBOX-AGE | warning |

The secret fixture uses AWS's documented example key — it is not a live
credential.
