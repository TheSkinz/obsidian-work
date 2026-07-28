"""Word-level audit of a commit: find content lost/added behind reflowing.

Rewrapping prose changes every line, so a line diff cannot distinguish a pure
reflow from a reflow that also dropped a sentence. Comparing word multisets
ignores line structure entirely, so only real content changes survive.
"""
import collections
import re
import subprocess
import sys

VAULT = r"C:\Users\Jwuts\obsidian-work"
SHA = sys.argv[1]


def run(args):
    return subprocess.run(args, cwd=VAULT, capture_output=True).stdout


files = run(["git", "show", "--stat", "--name-only", "--format=", SHA]).decode(
    "utf-8", "replace").split("\n")
files = [f.strip() for f in files if f.strip().endswith(".md")]

WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9._#/'-]*")

for f in files:
    before = run(["git", "show", SHA + "~:" + f]).decode("utf-8", "replace")
    after = run(["git", "show", SHA + ":" + f]).decode("utf-8", "replace")
    if not before and not after:
        continue
    b = collections.Counter(WORD.findall(before))
    a = collections.Counter(WORD.findall(after))
    lost, gained = b - a, a - b
    if not lost and not gained:
        print("  OK (pure reformat)  %s" % f)
        continue
    print("\n>>> %s" % f)
    if lost:
        print("    LOST  : %s" % " ".join(
            "%s%s" % (w, "" if n == 1 else "x%d" % n)
            for w, n in sorted(lost.items())[:40]))
    if gained:
        print("    GAINED: %s" % " ".join(
            "%s%s" % (w, "" if n == 1 else "x%d" % n)
            for w, n in sorted(gained.items())[:40]))
