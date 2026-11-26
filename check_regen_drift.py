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

A deliberate hold (HOLDS below) is reported as HELD rather than DRIFT, but only
while the package that forces it still rejects the new major: each run reads the
blocker's published peerDependencies range, so a hold whose reason has gone away
turns back into DRIFT instead of hiding the update forever.

Exit code 0 = no drift, 1 = drift found, 2 = checker error.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
TS_SCRIPT = REPO_ROOT / "regenerate_ts.py"

# Matches lines like:   "vitest": "^4.1",   or   "@types/node": "^22.0"
PIN_RE = re.compile(r'"(?P<name>@?[\w./-]+)":\s*"\^?(?P<major>\d+)\.\d+')


@dataclass(frozen=True)
class Hold:
    blocker: str  # npm package whose peerDependencies range forces the hold
    reason: str


# Pins deliberately held below an upstream major, keyed by package name. Empty
# while nothing is held. When adding a hold, keep it in sync with a matching
# rule in .github/renovate.json and a comment next to the pin in regenerate_ts.py.
HOLDS: dict[str, Hold] = {}

Version = tuple[int, int, int]
_COMPARATOR_RE = re.compile(
    r"^(>=|<=|>|<|\^|~|=)?v?(\d+)(?:\.(\d+|[xX*]))?(?:\.(\d+|[xX*]))?(?:-[\w.]+)?$"
)


def latest_manifest(pkg: str) -> dict:
    """Return the npm registry manifest of a package's `latest` release."""
    # Scoped names (@scope/name) must have the slash percent-encoded.
    encoded = pkg.replace("/", "%2F")
    url = f"https://registry.npmjs.org/{encoded}/latest"
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.load(resp)


def latest_major(pkg: str) -> int:
    """Return the latest published major version for an npm package."""
    return int(latest_manifest(pkg)["version"].split(".", 1)[0])


def _bounds(comparator: str) -> tuple[Version, bool, Version | None, bool]:
    """Turn one comparator into (low, low_inclusive, high, high_inclusive).

    Only the forms npm peer ranges actually use are accepted; anything else
    raises ValueError so an unparsed range never silently counts as "blocked".
    """
    if comparator in ("*", "x", ""):
        return (0, 0, 0), True, None, False
    m = _COMPARATOR_RE.match(comparator)
    if not m:
        raise ValueError(f"unsupported semver comparator {comparator!r}")
    op, major, minor, patch = m.group(1) or "=", int(m[2]), m[3], m[4]
    # "6.x" / "6.1.*" wildcards behave like the part being left out.
    if minor is not None and not minor.isdigit():
        minor = patch = None
    elif patch is not None and not patch.isdigit():
        patch = None
    ver: Version = (major, int(minor or 0), int(patch or 0))
    if op in (">=", ">"):
        # An exclusive low bound still admits later patches, so it is treated
        # like an inclusive one: only the major window matters here.
        return ver, True, None, False
    if op == "<":
        return (0, 0, 0), True, ver, False
    if op == "<=":
        return (0, 0, 0), True, ver, True
    if op == "^":
        if major > 0:
            return ver, True, (major + 1, 0, 0), False
        raise ValueError(f"unsupported 0.x caret comparator {comparator!r}")
    if op == "~" or minor is None or patch is None:
        # ~1.2.3, a bare "1.2" or "1": everything up to the next unspecified part.
        if minor is None:
            return ver, True, (major + 1, 0, 0), False
        return ver, True, (major, int(minor) + 1, 0), False
    return ver, True, ver, True  # exact version


def range_admits_major(spec: str, major: int) -> bool:
    """True if some version with the given major satisfies the npm range `spec`."""
    window_lo: Version = (major, 0, 0)
    window_hi: Version = (major + 1, 0, 0)
    for alternative in spec.split("||"):
        # Join operators to their versions (">= 4.8" -> ">=4.8").
        tokens = re.sub(r"(>=|<=|>|<|\^|~|=)\s+", r"\1", alternative.strip()).split()
        if " - " in alternative:
            raise ValueError(f"unsupported hyphen range {alternative.strip()!r}")
        lo, hi, hi_inc = (0, 0, 0), None, False
        for tok in tokens or [""]:
            t_lo, _, t_hi, t_hi_inc = _bounds(tok)
            lo = max(lo, t_lo)
            if t_hi is not None and (
                hi is None or t_hi < hi or (t_hi == hi and not t_hi_inc)
            ):
                hi, hi_inc = t_hi, t_hi_inc
        above_window_start = (
            hi is None or hi > window_lo or (hi == window_lo and hi_inc)
        )
        below_window_end = lo < window_hi
        if above_window_start and below_window_end:
            return True
    return False


def hold_still_needed(pkg: str, major: int, hold: Hold) -> bool:
    """True while the hold's blocker still rejects `major` of `pkg`."""
    peers = latest_manifest(hold.blocker).get("peerDependencies") or {}
    spec = peers.get(pkg)
    if spec is None:
        return False  # the blocker no longer constrains pkg at all
    return not range_admits_major(spec, major)


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
        print(
            "error: no dev-dependency pins parsed from regenerate_ts.py",
            file=sys.stderr,
        )
        return 2

    stale_holds = sorted(set(HOLDS) - set(pins))
    if stale_holds:
        print(
            f"error: HOLDS names packages regenerate_ts.py does not pin: {', '.join(stale_holds)}",
            file=sys.stderr,
        )
        return 2

    drift = []
    errors = []
    for pkg, pinned in sorted(pins.items()):
        try:
            current = latest_major(pkg)
        except (urllib.error.URLError, KeyError, ValueError) as exc:
            print(f"warning: could not check {pkg}: {exc}", file=sys.stderr)
            continue
        status, note = "ok", ""
        if current > pinned:
            status = "DRIFT"
            hold = HOLDS.get(pkg)
            if hold is not None:
                try:
                    needed = hold_still_needed(pkg, current, hold)
                except (urllib.error.URLError, KeyError, ValueError) as exc:
                    errors.append(
                        f"could not verify the hold on {pkg} via {hold.blocker}: {exc}"
                    )
                    needed = False
                    status = "ERROR"
                if needed:
                    status, note = "HELD", f"  ({hold.reason})"
                elif status == "DRIFT":
                    note = f"  (hold no longer needed: {hold.blocker} now accepts {pkg} {current}.x)"
        print(f"  {pkg:<20} pinned ^{pinned}.x  latest {current}.x  [{status}]{note}")
        if status == "DRIFT":
            drift.append((pkg, pinned, current, note))

    if errors:
        for err in errors:
            print(f"error: {err}", file=sys.stderr)
        return 2

    if drift:
        print("\nregenerate_ts.py is a major version behind on:", file=sys.stderr)
        for pkg, pinned, current, note in drift:
            print(
                f"  - {pkg}: pinned ^{pinned}.x, latest {current}.x{note}",
                file=sys.stderr,
            )
        return 1

    print("\nNo regen-script dependency drift.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
