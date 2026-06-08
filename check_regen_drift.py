#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Detect dependency-version drift in the regeneration scripts.

The clients are auto-generated, so the regenerate_*.py scripts -- not the
generated output -- own the dependency versions. This checker flags when a
script's pin has fallen a major version behind the latest published release,
which is the case a caret range (^MAJOR.MINOR) cannot absorb on its own.

Currently scoped to the npm dev-dependency pins in regenerate_ts.py (the only
script that pins caret ranges; regenerate_python.py uses floors and
regenerate_go.py resolves modules via `go mod tidy`).

Exit code 0 = no drift, 1 = drift found, 2 = checker error.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
TS_SCRIPT = REPO_ROOT / "regenerate_ts.py"

# Matches lines like:   "vitest": "^4.1",   or   "@eslint/js": "^10.0"
PIN_RE = re.compile(r'"(?P<name>@?[\w./-]+)":\s*"\^?(?P<major>\d+)\.\d+')


def latest_major(pkg: str) -> int:
    """Return the latest published major version for an npm package."""
    # Scoped names (@scope/name) must have the slash percent-encoded.
    encoded = pkg.replace("/", "%2F")
    url = f"https://registry.npmjs.org/{encoded}/latest"
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = json.load(resp)
    return int(data["version"].split(".", 1)[0])


def extract_dev_pins(text: str) -> dict[str, int]:
    """Pull the devDependencies block out of regenerate_ts.py and parse pins."""
    block = re.search(r'"devDependencies":\s*\{(.*?)\}', text, re.DOTALL)
    if not block:
        raise RuntimeError("could not locate devDependencies block in regenerate_ts.py")
    return {m["name"]: int(m["major"]) for m in PIN_RE.finditer(block.group(1))}


def main() -> int:
    if not TS_SCRIPT.exists():
        print(f"error: {TS_SCRIPT} not found", file=sys.stderr)
        return 2

    try:
        pins = extract_dev_pins(TS_SCRIPT.read_text())
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if not pins:
        print("error: no dev-dependency pins parsed from regenerate_ts.py", file=sys.stderr)
        return 2

    drift = []
    for pkg, pinned in sorted(pins.items()):
        try:
            current = latest_major(pkg)
        except (urllib.error.URLError, KeyError, ValueError) as exc:
            print(f"warning: could not check {pkg}: {exc}", file=sys.stderr)
            continue
        status = "DRIFT" if current > pinned else "ok"
        print(f"  {pkg:<20} pinned ^{pinned}.x  latest {current}.x  [{status}]")
        if current > pinned:
            drift.append((pkg, pinned, current))

    if drift:
        print("\nregenerate_ts.py is a major version behind on:", file=sys.stderr)
        for pkg, pinned, current in drift:
            print(f"  - {pkg}: pinned ^{pinned}.x, latest {current}.x", file=sys.stderr)
        return 1

    print("\nNo regen-script dependency drift.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
