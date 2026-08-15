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
    TUBE-GEOM-HEADER warning heater-card Tube-Geometry header off the canonical schema
    POINTER-DEAD    warning  recorded absolute source path no longer resolves
    YAML-COMMENT    error    unquoted frontmatter value silently truncated by a ` #` comment
    WORD-DELTA      warning  words left a note (--staged / --worktree only; see below)
    CHECKBOX-DELTA  warning  a decision box moved on an already-closed note (ditto)

Only SECRET, CONF-CONFLICT and YAML-COMMENT are errors (exit 1). Everything
else is a warning so the vault is never "failing" for want of a bulk backfill —
warnings are the to-do list, errors are the stop-the-line list. YAML-COMMENT
earns error status because it is silent data loss, not a backfill: the value
is already gone from Obsidian and from every script, and the fix is one pair
of quotes. New lint rules require a fixture under tools/fixtures/ (no fixture,
no rule).

WORD-DELTA and CHECKBOX-DELTA are diff rules, not tree rules: they compare
against HEAD, so they run only under --staged or --worktree and never appear in
a normal lint pass or in the generated report.

CHECKBOX-DELTA covers what WORD-DELTA structurally cannot. Ticking a box *adds*
an "x", and WORD-DELTA reports only losses — so a silently recorded decision was
invisible to every guard the vault had. It fires only when the note's status was
ALREADY resolved or superseded before the edit: closing a review note means
ticking its boxes and setting the status in one go, which is the workflow, not a
defect. A record that was already closed changing its mind is the anomaly.
Added 2026-07-28 after a stray Live Preview click ticked "Approve CND25004.md as
first pilot item" on a superseded note and --worktree passed it clean.

    --staged    HEAD vs the git index — the pre-commit shape, what is about to
                be committed. Driven unprompted by the PreToolUse commit hook.
    --worktree  HEAD vs the files on disk, staged or not. Added 2026-07-28.

The two modes exist because the index and the working tree fail differently.
--staged was the original rule and it could not see the incident that motivated
the whole idea: on 2026-07-19 B-101.md sat *dirty in the working tree* carrying
an exact content reversal, never staged, camouflaged by table auto-formatting.
Nothing staged, nothing to compare, no finding. --worktree is that gap closed —
run it at session start to catch a revert that is sitting on disk right now.
(Jesse's approval of proposal A, 06-insights/2026-07-28-prestaged-stale-editor-
buffer-guard.md.)

Usage:
    python tools/vault_lint.py               lint the vault, print findings
    python tools/vault_lint.py --report      also write 50-dashboards/lint-report.md
    python tools/vault_lint.py --staged      WORD-DELTA only: what left the staged notes
    python tools/vault_lint.py --worktree    WORD-DELTA only: what left uncommitted notes
    python tools/vault_lint.py --self-test   verify every rule fires on its fixture
    python tools/vault_lint.py --root PATH   lint a different tree (used by self-test)

--staged reports every staged note that lost words, unfiltered — you asked, so
you get all of it. The unprompted path is the PreToolUse commit hook in
~/.claude/hooks/, which gates on the commit message first and only runs this
when a commit *claims* a presentation-only scope (format / reflow / whitespace /
typo / house style). That gate is the whole design: measured across 120 commits,
firing on any word loss would have hit 70% of them and firing on lost
numbers/rulings still hit 50%, because this vault legitimately rewrites numbers
constantly. Gating on the declared scope drops it to 7% while still catching the
render-drift commit that motivated the rule. The signal is not the shape of the
diff — it is a session claiming it only touched presentation while content moved.

Windows: `py tools/vault_lint.py` if `python` is not on PATH.

Exit codes: 0 = no errors (warnings allowed), 1 = errors found, 2 = self-test failure.
"""

from __future__ import annotations

import argparse
import collections
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
SKIP_SCAN = ("archive", "templates", "tools/fixtures", ".obsidian", ".git", ".claude")
# `.claude` added 2026-08-15. It carries only json config of its own, but Claude
# Code checks out task worktrees under `.claude/worktrees/<name>/` — a complete
# second copy of the vault. Scanning one double-counts every warning AND re-reads
# the deliberately-broken lint fixtures as if they were real notes, because the
# `tools/fixtures` skip is root-relative and does not match the nested copy. That
# takes the vault from 0 errors to 6 (the SECRET and CONF-CONFLICT fixtures) and
# flips the health dashboard's Lint-errors row to FAIL for the lifetime of the
# worktree. Found while a spawned task happened to have a worktree open.

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
    "unexplored", "researched", "gated",
}

# An idea-seed whose own stated gate is not yet met. The idea-research loop
# skips these when picking a seed instead of burning a research cycle
# rediscovering a closed gate (added 2026-07-25 after two consecutive seeds
# were queued with gates that were already shut). A gated seed is NOT
# terminal and NOT researched — it is live and waiting. It stays visible via
# its `revisit-trigger:` field, which the health dashboard's dormant-trigger
# registry already renders, and INBOX-AGE skips it so a legitimately-parked
# seed does not decay into permanent lint noise.
GATED_STATUS = "gated"

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

# The alias pipe may be backslash-escaped (`[[Target\|Alias]]`) — required by
# Obsidian inside a Markdown table cell, where a bare `|` would split the row.
# Excluding `\` from the target capture and allowing it before the pipe keeps
# the escape out of the looked-up name; without this, `[[DSP26071\|DSP26071.2]]`
# in 01-context/active-jobs.md reported a phantom DEAD-LINK on `DSP26071\`.
WIKILINK_RE = re.compile(r"\[\[([^\[\]|#\\]+)(?:#[^\[\]|]*)?(?:\\?\|[^\[\]]*)?\]\]")
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

# Canonical heater-card Tube-Geometry header — same contract as DURATIONS_HEADER
# above: the exemplar `04-knowledge/_canonical-heater-card.md` is the human-facing
# authority, this tuple is the machine-checked copy, and a schema change edits
# both in one commit.
#
# Locked 2026-08-15. Config commit e4de4a5 (2026-07-27) dropped the old trailing
# `Notes` column and moved 75 notes across 39 cards into keyed blocks. The only
# protection afterwards was a dead-string rule in `usadebusk-core`, which catches
# an agent re-adding `Notes` but is blind to a hand edit or a card authored from a
# pre-e4de4a5 template. This closes that gap. Unlike DURATIONS_HEADER there is no
# optional column: all 41 cards plus the exemplar and template carried this exact
# 11-column header when the lock was written, so it fires on zero existing files
# and is pure drift protection with no backlog to burn down.
TUBE_GEOM_HEADER = (
    "Section", "Arrangement", "Metallurgy", "OD (in)", "Sched", "Wall (in)",
    "ID (in)", "Tubes/Circuit", "Avg Length (ft)", "Length/Circuit (ft)",
    "Return Bend Type",
)
TUBE_GEOM_HEADING_RE = re.compile(r"^#{1,6}\s+Tube Geometry\s*$", re.IGNORECASE)
MD_TABLE_SEP_RE = re.compile(r"^\|[\s|:\-]*-[\s|:\-]*$")  # the |---|---| divider row (needs a dash)

# POINTER-DEAD scope: the vault-as-index boundary is only recorded in
# 02-facilities notes (quote notes' Source Files sections, heater cards).
# The regex takes a backticked absolute path — Windows drive form or POSIX —
# with at least two separators, so backticked slash-commands (`/extract`)
# and relative fragments (`OneDrive/Desktop/…`) never match.
POINTER_DIRS = ("02-facilities",)
POINTER_RE = re.compile(r"`((?:[A-Za-z]:\\|/)[^`\n]{3,})`")

# WORD-DELTA: a token is anything that can carry a fact. Interior punctuation is
# kept because it is load-bearing here — `4.026`, `A106`, `Gr.B`, `ft/hr`,
# `DSP26039` are all single tokens. Trailing punctuation is stripped: without
# that, reflowing a paragraph so a period lands on a different word reports
# `3.` lost and `3` gained, which is pure noise in a rule whose whole job is to
# be silent on pure reformats.
WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._#/'-]*")
TRAILING_PUNCT = ".,;:'-"

ERROR_CODES = {"SECRET", "CONF-CONFLICT", "YAML-COMMENT"}


class Finding:
    def __init__(self, code: str, path: Path, detail: str):
        self.code = code
        self.path = path
        self.detail = detail
        self.severity = "error" if code in ERROR_CODES else "warning"

    def __str__(self) -> str:
        return f"[{self.severity.upper():7}] {self.code:14} {self.path}: {self.detail}"


# --- helpers ------------------------------------------------------------------

def frontmatter_start(lines: list[str]) -> int | None:
    """Index of the opening `---`, or None if the note has no frontmatter.

    Tolerates leading blank lines and full-line HTML comments. That tolerance
    is not cosmetic: the capture loop writes `<!-- vault-loop: -->` and the
    pre-staging loop writes `<!-- vault-prestaged: -->` as the *first* line of
    an inbox note, and Obsidian still renders the properties below them. A
    strict line-0 check made 26 of the vault's 202 notes invisible to every
    frontmatter rule — STATUS-VOCAB, REVIEW-OVERDUE, SUPERSEDED, OP-FRONTMATTER
    and CONF-CONFLICT (an *error* rule) all silently skipped exactly the notes
    the loops touch most. Found 2026-07-29 auditing the capture loop spec.
    """
    for i, line in enumerate(lines):
        s = line.strip()
        if not s or (s.startswith("<!--") and s.endswith("-->")):
            continue
        return i if s == "---" else None
    return None


def parse_frontmatter(text: str) -> dict[str, str]:
    """Minimal YAML-subset parser: top-level `key: value` between --- fences."""
    fm: dict[str, str] = {}
    lines = text.splitlines()
    start = frontmatter_start(lines)
    if start is None:
        return fm
    for line in lines[start + 1:]:
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
        # A gated idea-seed is meant to sit until its trigger fires; it is
        # tracked by the dormant-trigger registry, not by inbox age.
        if p.suffix == ".md":
            try:
                if parse_frontmatter(p.read_text(encoding="utf-8", errors="replace")
                                     ).get("status") == GATED_STATUS:
                    continue
            except OSError:
                pass
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


def check_tube_geom_header(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """TUBE-GEOM-HEADER: heater-card Tube-Geometry header must match the
    canonical schema exactly (column set and order). No optional columns.

    Same anchor-and-compare shape as check_durations_header(), for the same
    reason: `Section` and `Metallurgy` appear in prose and proposal tables all
    over the vault, so the heading is the only safe anchor. Only the first table
    row under `## Tube Geometry` is read. Comparison ignores case only; a
    missing, extra, reordered, or renamed column all fire. Warning, not error —
    a header fix is a to-do, not a stop-the-line.
    """
    canon = tuple(c.casefold() for c in TUBE_GEOM_HEADER)
    findings = []
    for path, text in notes.items():
        in_section = False
        for line in body_lines_outside_fences(text):
            if MD_HEADING_RE.match(line):
                in_section = bool(TUBE_GEOM_HEADING_RE.match(line))
                continue
            if not in_section:
                continue
            s = line.strip()
            if not s.startswith("|") or MD_TABLE_SEP_RE.match(s):
                continue
            cells = split_table_row(line)
            if tuple(c.casefold() for c in cells) != canon:
                findings.append(Finding("TUBE-GEOM-HEADER", path,
                    f"Tube-Geometry header does not match canonical schema: "
                    f"got {cells}, expected {list(TUBE_GEOM_HEADER)}"))
            in_section = False  # only the header row matters; done with this card
    return findings


def check_yaml_comment(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """YAML-COMMENT: an unquoted frontmatter value YAML will not read as written.

    Two failure modes, both from writing prose into an unquoted scalar:

      ` #`  truncates the value. YAML opens a comment at a `#` preceded by
            whitespace, so `source: DSP #26035 Foo.pdf` silently ends at `DSP`.
            Found 2026-07-27 on H-102A/H-102B (a whole source document lost)
            plus five other notes.

      `: `  breaks the whole block. A colon-space inside an unquoted scalar is
            a nested mapping, which is illegal there — YAML raises and Obsidian
            shows NO properties for the note, not merely a short one. Found the
            same day on H-101 (`Not field-verified: launcher elevation`).

    Nothing caught either because `parse_frontmatter` above is a line splitter,
    not a YAML parser: the vault's own tooling read the full text while Obsidian
    read a truncated value or nothing at all.

    Detection is lexical rather than a real parse, keeping this module pure
    stdlib. Quoted values are safe and skipped — the quote is exactly the fix.
    Flow collections, block scalars and comment-only lines are skipped too; a
    `#` opening a line is a genuine YAML comment, and a URL's `://` is not a
    mapping. Reported as an error: this is silent data loss with a one-character
    fix, not a backfill to defer.
    """
    findings = []
    for path, text in notes.items():
        lines = text.splitlines()
        start = frontmatter_start(lines)
        if start is None:
            continue
        for raw in lines[start + 1:]:
            if raw.strip() == "---":
                break
            m = re.match(r"^([A-Za-z0-9_-]+):[ \t]+(.*)$", raw)
            if not m:
                continue
            key, value = m.group(1), m.group(2).rstrip()
            if not value or value.startswith(("'", '"', "#", "[", "{", "|", ">", "&", "*", "!")):
                continue
            cut = re.search(r"[ \t]#", value)
            if cut:
                findings.append(Finding(
                    "YAML-COMMENT", path,
                    f"`{key}` truncates at '{value[:cut.start()].strip()}' — "
                    f"YAML reads ' #' as a comment, dropping "
                    f"'{value[cut.start():].strip()}'. Quote the value.",
                ))
            # `://` is a scheme separator, not a mapping — exempt it before
            # judging, or every recorded URL trips this.
            if re.search(r":[ \t]", re.sub(r"://", "", value)):
                findings.append(Finding(
                    "YAML-COMMENT", path,
                    f"`{key}` contains an unquoted ': ' — YAML reads that as a "
                    f"nested mapping and fails to parse the WHOLE frontmatter "
                    f"block, so Obsidian shows no properties at all. "
                    f"Quote the value.",
                ))
    return findings


def tokenize(text: str) -> list[str]:
    """Fact-bearing tokens, with trailing punctuation trimmed."""
    out = []
    for w in WORD_RE.findall(text):
        w = w.rstrip(TRAILING_PUNCT)
        if w:
            out.append(w)
    return out


def word_delta(before: str, after: str) -> tuple[dict[str, int], dict[str, int]]:
    """Words lost and gained between two revisions, ignoring line structure.

    The whole point of the rule. Rewrapping a paragraph changes every line, so a
    line diff cannot tell a reflow from a reflow that also dropped a sentence —
    and `git diff -w` does not help, because it ignores whitespace *within* a
    line while a reworded sentence moves words *across* lines. Comparing counted
    multisets throws line structure away entirely, so a pure reformat nets to
    zero lost and zero gained and only real content changes survive.
    """
    b = collections.Counter(tokenize(before))
    a = collections.Counter(tokenize(after))
    return dict(b - a), dict(a - b)


def format_delta(lost: dict[str, int], cap: int = 40) -> str:
    items = sorted(lost.items())
    shown = " ".join(f"{w}" if n == 1 else f"{w}x{n}" for w, n in items[:cap])
    return shown + (f" ... (+{len(items) - cap} more)" if len(items) > cap else "")


CHECKBOX_RE = re.compile(r"^[ \t]*[-*][ \t]+\[([ xX])\][ \t]*(.*?)[ \t]*$", re.M)
CLOSED_STATUSES = {"resolved", "superseded"}


def checkbox_delta(before: str, after: str) -> list[str]:
    """Decision boxes that changed state between two revisions.

    Exists because WORD-DELTA structurally cannot see this: ticking a box adds
    an "x", and WORD-DELTA reports only losses. In a vault whose governance runs
    on decision checkboxes, a silently *recorded* decision is at least as bad as
    a silently reverted sentence. Found 2026-07-28 when a stray Live Preview
    click ticked "Approve CND25004.md as first pilot item" on an already-
    superseded note and every existing guard passed it clean.

    Labels repeat — a review note with proposals A/B/C carries three identical
    "Approved" lines — so comparison is positional, not label-keyed. When the
    checkbox structure itself changes (lines added or removed) positions no
    longer correspond, so the check falls back to reporting the tick count.
    """
    b = [(m.group(2), m.group(1).lower() == "x") for m in CHECKBOX_RE.finditer(before)]
    a = [(m.group(2), m.group(1).lower() == "x") for m in CHECKBOX_RE.finditer(after)]
    if not b and not a:
        return []
    if len(b) == len(a) and [x[0] for x in b] == [x[0] for x in a]:
        return [f"{lbl!r} {'[ ]->[x]' if now else '[x]->[ ]'}"
                for (lbl, was), (_, now) in zip(b, a) if was != now]
    b_ticked, a_ticked = sum(1 for _, s in b if s), sum(1 for _, s in a if s)
    if b_ticked != a_ticked or len(b) != len(a):
        return [f"checkbox structure changed ({len(b)} boxes/{b_ticked} ticked "
                f"-> {len(a)} boxes/{a_ticked} ticked)"]
    return []


def check_diff_rules(root: Path, mode: str = "staged") -> list[Finding]:
    """Words that left a pre-existing note, HEAD -> staged index or working tree.

    Additions are never reported: a note that only gains words has lost nothing,
    and this vault mostly accretes. Newly added files are skipped for the same
    reason — there is no prior revision to lose anything from.

    Two modes, because the index and the working tree fail differently:

    - "staged"   HEAD vs the git index. The pre-commit shape: what is about to
                 be committed.
    - "worktree" HEAD vs the files on disk, staged or not. This is the shape the
                 2026-07-19 B-101 incident actually took — a note sat dirty in
                 the working tree carrying a content reversal, never staged, so
                 the staged-only rule could not see it. Added 2026-07-28 on
                 Jesse's approval of proposal A in
                 06-insights/2026-07-28-prestaged-stale-editor-buffer-guard.md.
    """
    findings: list[Finding] = []
    listing = (["git", "diff", "--cached", "--name-only", "--diff-filter=M", "--", "*.md"]
               if mode == "staged" else
               ["git", "diff", "HEAD", "--name-only", "--diff-filter=M", "--", "*.md"])
    try:
        out = subprocess.run(listing, cwd=root, capture_output=True, text=True, timeout=60)
        if out.returncode != 0:
            return findings  # not a git repo / no HEAD yet — fail open
        changed = [f.strip() for f in out.stdout.splitlines() if f.strip()]
    except Exception:
        return findings  # a lint rule must never wedge a commit

    for rel in changed:
        try:
            before = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=root,
                                    capture_output=True, timeout=30)
            if before.returncode != 0:
                continue
            before_text = before.stdout.decode("utf-8", "replace")
            if mode == "staged":
                after = subprocess.run(["git", "show", f":{rel}"], cwd=root,
                                       capture_output=True, timeout=30)
                if after.returncode != 0:
                    continue
                after_text = after.stdout.decode("utf-8", "replace")
            else:
                # Read the working tree itself — the whole point of this mode.
                after_text = (root / rel).read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        lost, _ = word_delta(before_text, after_text)
        if lost:
            where = "staged note" if mode == "staged" else "note (working tree, uncommitted)"
            findings.append(Finding(
                "WORD-DELTA", root / rel,
                f"{sum(lost.values())} word(s) left this {where} — "
                f"confirm each was meant to go: {format_delta(lost)}"))

        # CHECKBOX-DELTA gates on the *prior* status, not the current one:
        # closing a review note legitimately means ticking its boxes and setting
        # status to resolved in the same edit. What is anomalous is a record that
        # was ALREADY closed changing its mind.
        if parse_frontmatter(before_text).get("status", "").strip().lower() in CLOSED_STATUSES:
            moved = checkbox_delta(before_text, after_text)
            if moved:
                findings.append(Finding(
                    "CHECKBOX-DELTA", root / rel,
                    f"decision box changed on an already-closed note — "
                    f"{'; '.join(moved)}"))
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
    findings += check_tube_geom_header(root, notes)
    findings += check_pointer_dead(root, notes)
    findings += check_yaml_comment(root, notes)
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
    # WORD-DELTA compares two revisions rather than reading the tree, so its
    # fixture is a before/after pair fed straight to the comparison — the same
    # reason INBOX-AGE and POINTER-DEAD build theirs outside run_lint. The pair
    # is a reflow that also reworded: every line rewraps (so a line diff is
    # useless) while "concurrently", "Mode = 3" and a closed ruling vanish.
    wd = Path(__file__).resolve().parent / "fixtures" / "word-delta"
    lost, _ = word_delta(wd.joinpath("before.md").read_text(encoding="utf-8"),
                         wd.joinpath("after.md").read_text(encoding="utf-8"))
    for token in ("3", "concurrently", "simultaneously"):
        if token not in lost:
            print(f"SELF-TEST FAILED — WORD-DELTA fixture no longer drops {token!r}")
            return 2
    if lost:
        findings.append(Finding("WORD-DELTA", wd / "after.md",
                                f"{sum(lost.values())} word(s) left this note — "
                                f"confirm each was meant to go: {format_delta(lost)}"))

    # CHECKBOX-DELTA is a diff rule like WORD-DELTA, so its fixture is also a
    # before/after pair. The pair loses no words — that is the point: it proves
    # the two rules cover different failures rather than one shadowing the other.
    cb = Path(__file__).resolve().parent / "fixtures" / "checkbox-delta"
    cb_before = cb.joinpath("before.md").read_text(encoding="utf-8")
    cb_after = cb.joinpath("after.md").read_text(encoding="utf-8")
    moved = checkbox_delta(cb_before, cb_after)
    if len(moved) != 1 or "[ ]->[x]" not in moved[0]:
        print(f"SELF-TEST FAILED — CHECKBOX-DELTA fixture no longer yields one tick: {moved}")
        return 2
    cb_lost, _ = word_delta(cb_before, cb_after)
    if cb_lost:
        print(f"SELF-TEST FAILED — CHECKBOX-DELTA fixture should lose no words: {cb_lost}")
        return 2
    if parse_frontmatter(cb_before).get("status", "").strip().lower() in CLOSED_STATUSES:
        findings.append(Finding("CHECKBOX-DELTA", cb / "after.md",
                                f"decision box changed on an already-closed note — "
                                f"{'; '.join(moved)}"))

    fired = {f.code for f in findings}
    expected = {"OP-FRONTMATTER", "DEAD-LINK", "SECRET", "STATUS-VOCAB",
                "CONF-CONFLICT", "INBOX-AGE", "ORPHAN",
                "REVIEW-OVERDUE", "SUPERSEDED", "DURATIONS-HEADER", "TUBE-GEOM-HEADER",
                "POINTER-DEAD", "YAML-COMMENT", "WORD-DELTA", "CHECKBOX-DELTA"}
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
    ap.add_argument("--staged", action="store_true")
    ap.add_argument("--worktree", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    root = (args.root or Path(__file__).resolve().parent.parent).resolve()
    if not (root / "CLAUDE.md").exists():
        print(f"ERROR: {root} does not look like the vault root (no CLAUDE.md).")
        return 1

    if args.staged or args.worktree:
        mode = "worktree" if args.worktree else "staged"
        hits = check_diff_rules(root, mode)
        for f in hits:
            print(f)
        noun = "staged" if mode == "staged" else "uncommitted"
        lost = sum(1 for f in hits if f.code == "WORD-DELTA")
        ticked = sum(1 for f in hits if f.code == "CHECKBOX-DELTA")
        print(f"\n{lost} {noun} note(s) lost words; "
              f"{ticked} changed a decision box on an already-closed note."
              if hits else
              f"\nNo {noun} note lost words or moved a closed decision box.")
        return 0  # advisory only — never blocks a commit

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
