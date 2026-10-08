#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Stamp a release version into the Python client's package-version sites.

The committed client carries the spec version (--from). A client-only fix
release publishes under a different version (--to), so the CI checkout is
rewritten before building (ADR 0003). Only package-version sites change; the
"version of the OpenAPI document" headers, API-version strings, docs, tests
and uv.lock are left alone. Every site must match exactly once or the script
fails without writing anything. It is a no-op when --from equals --to.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")

# (file relative to the client dir, regex with one group for the version)
SITES = [
    ("pyproject.toml", r'^version = "([^"]*)"$'),
    ("setup.py", r'^VERSION = "([^"]*)"$'),
    ("tmi_client/__init__.py", r'^__version__ = "([^"]*)"$'),
    ("tmi_client/api_client.py", r"'OpenAPI-Generator/([^/']*)/python'"),
    ("tmi_client/configuration.py", r'"SDK Package Version: ([^"\\]*)"'),
]


def stamp(directory: Path, from_version: str, to_version: str) -> list[str]:
    """Rewrite the sites; return the files changed. Raises ValueError on any problem."""
    for label, v in (("--from", from_version), ("--to", to_version)):
        if not VERSION_RE.fullmatch(v):
            raise ValueError(f"{label} {v!r} is not a bare N.N.N version")
    if from_version == to_version:
        return []
    updates: dict[Path, str] = {}
    for rel, pattern in SITES:
        path = directory / rel
        if not path.is_file():
            raise ValueError(f"expected version site file missing: {path}")
        text = path.read_text(encoding="utf-8")
        matches = list(re.finditer(pattern, text, flags=re.MULTILINE))
        if len(matches) != 1:
            raise ValueError(
                f"{rel}: expected exactly 1 package-version site, found {len(matches)}"
            )
        found = matches[0].group(1)
        if found != from_version:
            raise ValueError(f"{rel}: version is {found!r}, expected {from_version!r}")
        s, e = matches[0].span(1)
        updates[path] = text[:s] + to_version + text[e:]
    for path, text in updates.items():
        path.write_text(text, encoding="utf-8")
    return [str(p.relative_to(directory)) for p in updates]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--dir", required=True, help="Python client directory")
    ap.add_argument(
        "--from",
        dest="from_version",
        required=True,
        help="spec version the directory carries",
    )
    ap.add_argument(
        "--to", dest="to_version", required=True, help="release version to stamp"
    )
    args = ap.parse_args(argv)
    try:
        changed = stamp(Path(args.dir), args.from_version, args.to_version)
    except ValueError as e:
        print(f"::error::{e}", file=sys.stderr)
        return 1
    if changed:
        print(f"stamped {args.to_version} into: {', '.join(changed)}")
    else:
        print(f"version {args.from_version} unchanged; nothing to stamp")
    return 0


if __name__ == "__main__":
    sys.exit(main())
