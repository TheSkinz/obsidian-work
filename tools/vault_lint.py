#!/usr/bin/env python3
"""vault_lint.py — the vault's one standing automated check.

Pure standard library. Runs anywhere Python 3.11+ runs; no Obsidian, no
model, no network required. This is the "scripts over attention" floor:
every check here used to be something an agent had to notice while reading.

Rules (code | severity):
    OP-FRONTMATTER  warning  operational notes should carry source + verified
    DEAD-LINK       warning  [[wikilink]] whose target exists nowhere in repo
    SECRET          error    credential-shaped string committed to the vault
    INBOX-AGE       warning  inbox item older than 14 days, or untracked in git
    STATUS-VOCAB    warning  status: value outside the known vocabulary
    CONF-CONFLICT   error    confidence: high on an AI-inferred source
    ORPHAN          warning  knowledge-layer note with no inbound wikilinks
    REVIEW-OVERDUE  warning  live note whose review_after date has passed
    SUPERSEDED      warning  note declares superseded_by but is still marked live
    DURATIONS-HEADER warning heater-card Task-Durations header off the canonical schema
    POINTER-DEAD    warning  recorded absolute source path no longer resolves

Only SECRET and CONF-CONFLICT are errors (exit 1). Everything else is a
warning so the vault is never "failing" for want of a bulk backfill —
warnings are the to-do list, errors are the stop-the-line list. New lint
rules require a fixture under tools/fixtures/ (no fixture, no rule).

Usage:
    python tools/vault_lint.py               lint the vault, print findings
    python tools/vault_lint.py --report      also write 50-dashboards/lint-report.md
    python tools/vault_lint.py --self-test   verify every rule fires on its fixture
    python tools/vault_lint.py --root PATH   lint a different tree (used by self-test)

Windows: `py tools/vault_lint.py` if `python` is not on PATH.

Exit codes: 0 = no errors (warnings allowed), 1 = errors found, 2 = self-test failure.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

# --- configuration -----------------------------------------------------------

OPERATIONAL_DIRS = ("02-facilities", "04-knowledge/pricing")
INBOX_DIR = "00-inbox"
INBOX_SKIP_SUBDIRS = ("preserved-dsps",)  # deliberately held, per README there
INBOX_MAX_AGE_DAYS = 14

# Folders never scanned for problems (archive is history; templates are blanks;
# fixtures contain deliberate violations; .obsidian is app state).
SKIP_SCAN = ("archive", "templates", "tools/fixtures", ".obsidian", ".git")

# Status vocabulary actually in use across the vault as of 2026-07-05, plus the
# decision-queue's `expired`. Keep this list honest — it is the vocabulary, not
# an aspiration. A value not here is a warning, not a crash.
ALLOWED_STATUS = {
    # lifecycle
    "inbox", "draft", "active", "reviewed", "for-review", "stale",
    "deprecated", "complete", "open", "closed-unactioned", "expired",
    # review/decision outcomes
    "resolved", "unresolved", "pending", "superseded",
    "decided-blocked", "approved-blocked", "awarded", "lost",
    # research
    "unexplored", "researched",
}

# Terminal statuses: a note in one of these is resolved and is *meant* to sit
# past its review_after date — REVIEW-OVERDUE skips them, and the health
# dashboard's "review notes awaiting decision" count skips them too (imported
# there). Everything else in ALLOWED_STATUS is treated as a live note.
TERMINAL_STATUS = {
    "deprecated", "complete", "closed-unactioned", "expired",
    "resolved", "superseded", "decided-blocked", "approved-blocked", "awarded", "lost",
}

SECRET_PATTERNS = [
    ("aws-access-key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("github-token", re.compile(r"\b(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,}\b")),
    ("github-pat", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{22,}\b")),
    ("private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("generic-credential", re.compile(
        r"(?i)\b(api[_-]?key|secret[_-]?key|access[_-]?token|password)\b\s*[:=]\s*['\"]?[A-Za-z0-9+/_\-]{20,}")),
]

WIKILINK_RE = re.compile(r"\[\[([^\[\]|#]+)(?:#[^\[\]|]*)?(?:\|[^\[\]]*)?\]\]")
FENCE_RE = re.compile(r"^\s*(```|~~~)")

# ORPHAN check scope: layers where an unlinked note is write-only memory.
# Excluded by design: 00-inbox (transient), 01-context (auto-loaded every
# session), 02-facilities (navigated by folder path, not links),
# 50-dashboards (generated). Files starting with "_" are exemplars/indexes.
ORPHAN_DIRS = ("04-knowledge", "06-insights", "07-llms", "08-systems", "09-interests")

# Canonical heater-card Task-Durations header — mirrors the exemplar
# `04-knowledge/_canonical-heater-card.md`. The exemplar is the human-facing
# authority; this tuple is the machine-checked copy the DURATIONS-HEADER lock
# enforces. Keeping the two in step IS the point of the lock — if the schema
# ever changes, change it in the exemplar and here in the same commit.
DURATIONS_HEADER = (
    "Date", "Job #", "Rigs", "Rig-In", "Pig", "Smart Pig",
    "Rig-Over", "Rig-Out", "Stand-By", "Total", "Condition", "Mode",
)
# `Mode` is an optional trailing column (added 2026-07-22): cards predating it
# carry 11 columns and stay valid, so the check accepts the header with or
# without the trailing `Mode`.
# The header lives under a `## Task Durations` heading in each heater card. Anchor
# on that heading rather than on any token like "Rig-In", which also appears in
# proposal cost tables, rate tables, and prose all over the vault.
DURATIONS_HEADING_RE = re.compile(r"^#{1,6}\s+Task Durations\s*$", re.IGNORECASE)
MD_HEADING_RE = re.compile(r"^#{1,6}\s+")
MD_TABLE_SEP_RE = re.compile(r"^\|[\s|:\-]*-[\s|:\-]*$")  # the |---|---| divider row (needs a dash)

# POINTER-DEAD scope: the vault-as-index boundary is only recorded in
# 02-facilities notes (quote notes' Source Files sections, heater cards).
# The regex takes a backticked absolute path — Windows drive form or POSIX —
# with at least two separators, so backticked slash-commands (`/extract`)
# and relative fragments (`OneDrive/Desktop/…`) never match.
POINTER_DIRS = ("02-facilities",)
POINTER_RE = re.compile(r"`((?:[A-Za-z]:\\|/)[^`\n]{3,})`")

ERROR_CODES = {"SECRET", "CONF-CONFLICT"}


class Finding:
    def __init__(self, code: str, path: Path, detail: str):
        self.code = code
        self.path = path
        self.detail = detail
        self.severity = "error" if code in ERROR_CODES else "warning"

    def __str__(self) -> str:
        return f"[{self.severity.upper():7}] {self.code:14} {self.path}: {self.detail}"


# --- helpers ------------------------------------------------------------------

def parse_frontmatter(text: str) -> dict[str, str]:
    """Minimal YAML-subset parser: top-level `key: value` between --- fences."""
    fm: dict[str, str] = {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return fm
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            fm[m.group(1).strip()] = m.group(2).strip().strip("'\"")
    return fm


def skip(path: Path, root: Path) -> bool:
    rel = path.relative_to(root).as_posix()
    return any(rel == s or rel.startswith(s + "/") for s in SKIP_SCAN)


def body_lines_outside_fences(text: str):
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield line


def split_table_row(line: str) -> list[str]:
    """Cells of a markdown table row, with the outer pipes stripped."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def git_last_commit_date(root: Path, path: Path) -> date | None:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(path.relative_to(root))],
            cwd=root, capture_output=True, text=True, timeout=30,
        ).stdout.strip()
        return datetime.strptime(out, "%Y-%m-%d").date() if out else None
    except Exception:
        return None


# --- rules --------------------------------------------------------------------

def check_operational_frontmatter(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """OP-FRONTMATTER: operational notes should carry `source` and `verified`.

    Warning, not error: this is the provenance backfill to-do list, and the
    vault should not read as failing until that separate session runs.
    """
    findings = []
    for path, text in notes.items():
        rel = path.relative_to(root).as_posix()
        if not any(rel.startswith(d + "/") for d in OPERATIONAL_DIRS):
            continue
        if path.name.startswith("_"):  # indexes/directories, not fact carriers
            continue
        fm = parse_frontmatter(text)
        missing = [k for k in ("source", "verified") if k not in fm]
        if missing:
            findings.append(Finding("OP-FRONTMATTER", path,
                                    f"operational note missing frontmatter: {', '.join(missing)}"))
    return findings


def check_dead_links(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """DEAD-LINK: [[wikilink]] whose target note exists nowhere in the repo."""
    known = set()
    for p in root.rglob("*.md"):  # resolution set includes archive/ deliberately
        rel = p.relative_to(root).as_posix()
        if rel.startswith((".git/", ".obsidian/", "tools/fixtures/")):
            continue
        known.add(p.stem.lower())
    findings = []
    for path, text in notes.items():
        for line in body_lines_outside_fences(text):
            for m in WIKILINK_RE.finditer(line):
                target = m.group(1).strip()
                if not target or "<" in target:  # template placeholders
                    continue
                # Obsidian resolves path-style links by their final segment.
                stem = target.rsplit("/", 1)[-1].lower()
                if stem not in known:
                    findings.append(Finding("DEAD-LINK", path, f"[[{target}]] not found"))
    return findings


def check_secrets(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """SECRET: credential-shaped strings must never be committed."""
    findings = []
    for path, text in notes.items():
        for name, pat in SECRET_PATTERNS:
            if pat.search(text):
                findings.append(Finding("SECRET", path, f"matches {name} pattern"))
    return findings


def check_inbox_age(root: Path) -> list[Finding]:
    """INBOX-AGE: inbox items older than 14 days (by last git commit), or untracked."""
    findings = []
    inbox = root / INBOX_DIR
    if not inbox.is_dir():
        return findings
    today = date.today()
    for p in sorted(inbox.rglob("*")):
        if not p.is_file() or p.name.startswith("."):
            continue
        rel = p.relative_to(inbox).as_posix()
        if any(rel.startswith(s + "/") for s in INBOX_SKIP_SUBDIRS):
            continue
        d = git_last_commit_date(root, p)
        if d is None:
            findings.append(Finding("INBOX-AGE", p, "untracked in git — file it or commit it"))
        elif (today - d).days > INBOX_MAX_AGE_DAYS:
            findings.append(Finding("INBOX-AGE", p, f"in inbox {(today - d).days} days"))
    return findings


def check_status_vocab(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """STATUS-VOCAB: `status:` values come from the fixed vocabulary."""
    findings = []
    for path, text in notes.items():
        fm = parse_frontmatter(text)
        status = fm.get("status")
        if status and status not in ALLOWED_STATUS:
            findings.append(Finding("STATUS-VOCAB", path, f"unknown status '{status}'"))
    return findings


def check_confidence_conflict(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """CONF-CONFLICT: AI-inferred sources may never claim high confidence."""
    findings = []
    for path, text in notes.items():
        fm = parse_frontmatter(text)
        if fm.get("confidence") == "high" and fm.get("source_authority") == "inferred":
            findings.append(Finding("CONF-CONFLICT", path,
                                    "confidence: high with source_authority: inferred"))
    return findings


def check_orphans(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """ORPHAN: a knowledge-layer note no other note links to.

    Unlinked notes don't compound — nothing rediscovers them. Inbound links
    are counted across the whole text of every hand-written note (frontmatter
    `related:` entries included). Generated files (INDEX.md, dashboards) are
    already excluded as sources by the GENERATED marker, so a generated index
    can't satisfy this check — only a real link from a real note does.
    """
    inbound: set[str] = set()
    for path, text in notes.items():
        own = path.stem.lower()
        for m in WIKILINK_RE.finditer(text):
            target = m.group(1).strip()
            if not target or "<" in target:
                continue
            stem = target.rsplit("/", 1)[-1].lower()
            if stem != own:  # self-links don't count
                inbound.add(stem)
    findings = []
    for path, text in notes.items():
        rel = path.relative_to(root).as_posix()
        if not any(rel.startswith(d + "/") for d in ORPHAN_DIRS):
            continue
        if path.name.startswith("_") or path.name.upper() == "README.MD":
            continue
        if path.stem.lower() not in inbound:
            findings.append(Finding("ORPHAN", path,
                                    "no inbound wikilinks from any note — link it or archive it"))
    return findings


def check_review_overdue(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """REVIEW-OVERDUE: a live note whose `review_after` date has passed.

    The scripted half of self-obsolescence detection — the `review_after`
    field already sits on every governance note; this rule finally reads it.
    Fires only on non-terminal notes: a superseded/complete/resolved review is
    meant to rest past its review date. Warning, not error — it's a nudge list.
    """
    findings = []
    today = date.today()
    for path, text in notes.items():
        fm = parse_frontmatter(text)
        raw = fm.get("review_after")
        if not raw or fm.get("status") in TERMINAL_STATUS:
            continue
        try:
            due = datetime.strptime(raw, "%Y-%m-%d").date()
        except ValueError:
            continue  # non-date sentinels like "never" are never overdue
        if due < today:
            findings.append(Finding("REVIEW-OVERDUE", path,
                                    f"review_after {raw} passed ({(today - due).days} days ago)"))
    return findings


def check_superseded(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """SUPERSEDED: a note carrying `superseded_by:` that is still marked live.

    `superseded_by` is a human-set declaration, made at the moment of a
    reversal, that a newer note replaces this one. Once set, the note's own
    status should move to `superseded` (or `deprecated`). This rule flags the
    gap — a cheap structural check standing in for a hard semantic problem.
    """
    findings = []
    retired = {"superseded", "deprecated"}
    for path, text in notes.items():
        fm = parse_frontmatter(text)
        if fm.get("superseded_by") and fm.get("status") not in retired:
            findings.append(Finding("SUPERSEDED", path,
                                    f"declares superseded_by but status is "
                                    f"'{fm.get('status', '(none)')}' — set status: superseded"))
    return findings


def check_durations_header(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """DURATIONS-HEADER: heater-card Task-Durations header must match the
    canonical schema exactly (column set and order); the trailing `Mode`
    column is optional, so 11- and 12-column headers both pass.

    This locks a drift that actually happened — a stale copy dropped the
    trailing `Condition` column and diverged from the exemplar (see the
    2026-07-20 harness map). Anchored on the `## Task Durations` heading and
    checks only the first table row beneath it, so it can't false-positive on
    the many other tables that mention Rig-In (proposals, rate tables, prose).
    Comparison ignores case only; a missing, extra, reordered, or renamed
    column all fire. Warning, not error: a header fix is a to-do, not a
    stop-the-line.
    """
    canon = tuple(c.casefold() for c in DURATIONS_HEADER)
    canon_no_mode = canon[:-1]  # Mode optional — accept the pre-Mode 11-col header too
    findings = []
    for path, text in notes.items():
        in_section = False
        for line in body_lines_outside_fences(text):
            if MD_HEADING_RE.match(line):
                in_section = bool(DURATIONS_HEADING_RE.match(line))
                continue
            if not in_section:
                continue
            s = line.strip()
            if not s.startswith("|") or MD_TABLE_SEP_RE.match(s):
                continue
            # first real table row under the heading is the header row
            cells = split_table_row(line)
            got = tuple(c.casefold() for c in cells)
            if got != canon and got != canon_no_mode:
                findings.append(Finding("DURATIONS-HEADER", path,
                    f"Task-Durations header does not match canonical schema: "
                    f"got {cells}, expected {list(DURATIONS_HEADER)} "
                    f"(trailing 'Mode' optional)"))
            in_section = False  # only the header row matters; done with this card
    return findings


def check_pointer_dead(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """POINTER-DEAD: a recorded absolute source-file path that no longer resolves.

    The vault is the index, the file estate (OneDrive/SharePoint) is the store,
    and the recorded path is the only pointer — nothing syncs it, so a moved or
    renamed folder silently kills the bid trail. Portable by base-gating: a path
    is only judged when its first three components (e.g. C:\\Users\\<name>) exist
    on this machine; on any other machine the check skips silently, keeping the
    marker-based vault-source-of-truth portability intact. Ellipsis fragments and
    replacement-char mojibake are unverifiable and skipped; repeated paths in one
    note are reported once. Warning, not error: a moved folder is a to-do
    (re-point the note), not a stop-the-line.
    """
    findings = []
    for path, text in notes.items():
        rel = path.relative_to(root).as_posix()
        if not any(rel.startswith(d + "/") for d in POINTER_DIRS):
            continue
        seen: set[str] = set()
        for line in body_lines_outside_fences(text):
            for m in POINTER_RE.finditer(line):
                # strip plain spaces only: real estate folder names can end in
                # U+00A0 (observed on DSP26080's folder), and .strip() would
                # eat it and break an accurately recorded path
                raw = m.group(1).strip(" ")
                if raw in seen or "…" in raw or "�" in raw:
                    continue
                seen.add(raw)
                p = Path(raw)
                if len(p.parts) < 3:
                    continue
                try:
                    if not Path(*p.parts[:3]).exists():
                        continue  # base absent — different machine, not a finding
                    if not p.exists():
                        findings.append(Finding("POINTER-DEAD", path,
                                                f"recorded path does not resolve: {raw}"))
                except OSError:
                    continue
    return findings


# --- driver -------------------------------------------------------------------

GENERATED_MARKER = "GENERATED by tools/"


def collect_notes(root: Path) -> dict[Path, str]:
    notes = {}
    for p in sorted(root.rglob("*.md")):
        if skip(p, root):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"[WARN] unreadable: {p}: {e}", file=sys.stderr)
            continue
        # Generated files (lint-report, health) echo link text and status values;
        # scanning them as sources would re-flag their own quoted findings. They
        # self-declare with a marker on the first line — skip them as sources.
        if GENERATED_MARKER in text[:200]:
            continue
        notes[p] = text
    return notes


def run_lint(root: Path, with_git: bool = True) -> list[Finding]:
    notes = collect_notes(root)
    findings = []
    findings += check_operational_frontmatter(root, notes)
    findings += check_dead_links(root, notes)
    findings += check_secrets(root, notes)
    if with_git:
        findings += check_inbox_age(root)
    findings += check_status_vocab(root, notes)
    findings += check_confidence_conflict(root, notes)
    findings += check_orphans(root, notes)
    findings += check_review_overdue(root, notes)
    findings += check_superseded(root, notes)
    findings += check_durations_header(root, notes)
    findings += check_pointer_dead(root, notes)
    return findings


def write_report(root: Path, findings: list[Finding]) -> Path:
    out = root / "50-dashboards" / "lint-report.md"
    out.parent.mkdir(exist_ok=True)
    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]
    lines = [
        "<!-- GENERATED by tools/vault_lint.py --report — do not edit; rerun to refresh -->",
        "# Vault Lint Report",
        f"**Generated:** {date.today().isoformat()} | **Errors:** {len(errors)} | **Warnings:** {len(warnings)}",
        "",
    ]
    if not findings:
        lines.append("Clean — no findings.")
    for group, title in ((errors, "Errors"), (warnings, "Warnings")):
        if group:
            lines += [f"## {title}", "", "| Code | File | Detail |", "|---|---|---|"]
            lines += [f"| {f.code} | `{f.path.relative_to(root)}` | {f.detail} |" for f in group]
            lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def self_test() -> int:
    """Every rule must fire on its fixture. Fixture tree mimics vault layout."""
    fixtures = Path(__file__).resolve().parent / "fixtures"
    findings = run_lint(fixtures, with_git=False)
    # INBOX-AGE: an untracked inbox file must be flagged. Committed fixtures are
    # tracked (and fresh), so create a throwaway untracked file for this check.
    temp = fixtures / INBOX_DIR / "untracked-temp-selftest.md"
    temp.parent.mkdir(parents=True, exist_ok=True)
    temp.write_text("self-test scratch — safe to delete\n", encoding="utf-8")
    try:
        findings += check_inbox_age(fixtures)
    finally:
        temp.unlink(missing_ok=True)
    # POINTER-DEAD needs a machine-local absolute path, so its fixture is built
    # at runtime too (same pattern as the INBOX-AGE untracked check above).
    pd_note = fixtures / "02-facilities" / "pointer-dead-temp-selftest.md"
    pd_note.parent.mkdir(parents=True, exist_ok=True)
    missing = fixtures / "02-facilities" / "missing-target-selftest.pdf"
    pd_note.write_text(f"# self-test scratch — safe to delete\n\n`{missing}`\n",
                       encoding="utf-8")
    try:
        findings += check_pointer_dead(
            fixtures, {pd_note: pd_note.read_text(encoding="utf-8")})
    finally:
        pd_note.unlink(missing_ok=True)
    fired = {f.code for f in findings}
    expected = {"OP-FRONTMATTER", "DEAD-LINK", "SECRET", "STATUS-VOCAB",
                "CONF-CONFLICT", "INBOX-AGE", "ORPHAN",
                "REVIEW-OVERDUE", "SUPERSEDED", "DURATIONS-HEADER",
                "POINTER-DEAD"}
    missing = expected - fired
    for f in findings:
        print(f"  fixture: {f}")
    if missing:
        print(f"SELF-TEST FAILED — rules did not fire: {', '.join(sorted(missing))}")
        return 2
    print(f"SELF-TEST OK — all {len(expected)} rules fired on their fixtures.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=None)
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    root = (args.root or Path(__file__).resolve().parent.parent).resolve()
    if not (root / "CLAUDE.md").exists():
        print(f"ERROR: {root} does not look like the vault root (no CLAUDE.md).")
        return 1

    findings = run_lint(root)
    for f in findings:
        print(f)
    errors = sum(1 for f in findings if f.severity == "error")
    warnings = len(findings) - errors
    print(f"\n{errors} error(s), {warnings} warning(s).")
    if args.report:
        print(f"Report written: {write_report(root, findings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
