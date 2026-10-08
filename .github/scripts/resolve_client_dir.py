#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Resolve the committed client directory a release version publishes from.

A release version R (from a python-vR / ts-vR / go-vR tag, or the workflow
dispatch input) publishes from the committed directory with the same
major.minor as R and the highest patch <= R's patch (ADR 0003). The directory
keeps the spec version; the workflow stamps R into package metadata.

Prints the directory, relative to --root, on stdout. With --github-output it
also appends pkg_dir, version (R) and spec_version (the directory's version,
dotted) to the file named by $GITHUB_OUTPUT.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

LANG_DIRS = {
    "python": ("python-client-generated", "."),
    "ts": ("typescript-client-generated", "."),
    "go": ("go-client-generated", "_"),
}
VERSION_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def parse_version(text: str) -> tuple[int, int, int]:
    """Parse a bare N.N.N version; raise ValueError otherwise."""
    m = VERSION_RE.fullmatch(text)
    if not m:
        raise ValueError(f"invalid version {text!r} (expected bare N.N.N, e.g. 2.0.1)")
    return int(m[1]), int(m[2]), int(m[3])


def list_candidates(lang_dir: Path, sep: str) -> list[tuple[tuple[int, int, int], str]]:
    """Return (version, dirname) for every vN<sep>N<sep>N subdirectory."""
    pattern = re.compile(
        r"^v(\d+)" + re.escape(sep) + r"(\d+)" + re.escape(sep) + r"(\d+)$"
    )
    found = []
    if lang_dir.is_dir():
        for child in lang_dir.iterdir():
            m = pattern.fullmatch(child.name)
            if m and child.is_dir():
                found.append(((int(m[1]), int(m[2]), int(m[3])), child.name))
    return sorted(found)


def resolve(lang: str, version: str, root: Path) -> tuple[str, tuple[int, int, int]]:
    """Return (dir relative to root, directory version)."""
    if lang not in LANG_DIRS:
        raise ValueError(
            f"unknown language {lang!r} (expected one of {sorted(LANG_DIRS)})"
        )
    major, minor, patch = parse_version(version)
    top, sep = LANG_DIRS[lang]
    candidates = list_candidates(root / top, sep)
    matches = [c for c in candidates if c[0][:2] == (major, minor) and c[0][2] <= patch]
    if not matches:
        avail = ", ".join(name for _, name in candidates) or "(none)"
        raise ValueError(
            f"no {top}/ directory serves release {version}: need v{major}{sep}{minor}{sep}N "
            f"with N <= {patch}. Available: {avail}. "
            f"A new major.minor needs a regenerated client first."
        )
    ver, name = matches[-1]
    return f"{top}/{name}", ver


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--lang", required=True)
    ap.add_argument("--version", required=True, help="release version R, bare N.N.N")
    ap.add_argument("--root", default=".", help="repo root (default: cwd)")
    ap.add_argument(
        "--github-output", action="store_true", help="append outputs to $GITHUB_OUTPUT"
    )
    args = ap.parse_args(argv)
    try:
        pkg_dir, ver = resolve(args.lang, args.version, Path(args.root))
    except ValueError as e:
        print(f"::error::{e}", file=sys.stderr)
        return 1
    print(pkg_dir)
    if args.github_output:
        out = os.environ.get("GITHUB_OUTPUT")
        if not out:
            print(
                "::error::--github-output given but $GITHUB_OUTPUT is unset",
                file=sys.stderr,
            )
            return 1
        with open(out, "a", encoding="utf-8") as f:
            f.write(
                f"pkg_dir={pkg_dir}\nversion={args.version}\nspec_version={'.'.join(map(str, ver))}\n"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
