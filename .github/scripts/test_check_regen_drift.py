"""Tests for check_regen_drift.py (repo root); the npm registry is stubbed."""

from __future__ import annotations

import sys
import urllib.error
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO))

import check_regen_drift as crd

TS_SCRIPT_TEXT = """
    "devDependencies": {
        "eslint": "^10.0",
        "typescript": "^6.0",
        "typescript-eslint": "^8.0",
    },
"""


@pytest.mark.parametrize(
    "spec,major,expected",
    [
        (">=4.8.4 <6.1.0", 6, True),
        (">=4.8.4 <6.1.0", 7, False),
        ("<7.0.0", 7, False),
        ("<=7.0.0", 7, True),
        (">= 4.8.4 < 7.1.0", 7, True),
        ("^6.0.0", 7, False),
        ("^7.0.0", 7, True),
        ("^5.0.0 || ^6.0.0", 7, False),
        ("^6.0.0 || ^7.0.0", 7, True),
        (">=4.8.4", 7, True),
        (">8.0.0", 7, False),
        ("~7.1.0", 7, True),
        ("7", 7, True),
        ("6.x", 7, False),
        ("7.0.0-beta", 7, True),
        ("*", 7, True),
        ("", 7, True),
    ],
)
def test_range_admits_major(spec: str, major: int, expected: bool) -> None:
    assert crd.range_admits_major(spec, major) is expected


@pytest.mark.parametrize("spec", ["6.0.0 - 7.0.0", "^0.5.0", "latest", ">=foo"])
def test_range_admits_major_rejects_unsupported(spec: str) -> None:
    with pytest.raises(ValueError):
        crd.range_admits_major(spec, 7)


@pytest.fixture
def registry(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    """Stub regenerate_ts.py and the npm registry; return the manifest table."""
    script = tmp_path / "regenerate_ts.py"
    script.write_text(TS_SCRIPT_TEXT)
    monkeypatch.setattr(crd, "TS_SCRIPT", script)
    monkeypatch.setitem(
        crd.HOLDS,
        "typescript",
        crd.Hold(
            blocker="typescript-eslint",
            reason="typescript-eslint does not support TypeScript 7 yet (typescript-eslint#10940)",
        ),
    )
    manifests: dict[str, object] = {
        "eslint": {"version": "10.2.0"},
        "typescript": {"version": "7.0.1"},
        "typescript-eslint": {
            "version": "8.74.0",
            "peerDependencies": {"typescript": ">=4.8.4 <6.1.0"},
        },
    }

    def fake(pkg: str) -> dict:
        value = manifests[pkg]
        if isinstance(value, Exception):
            raise value
        return value  # type: ignore[return-value]

    monkeypatch.setattr(crd, "latest_manifest", fake)
    return manifests


def test_hold_reported_as_held(registry, capsys) -> None:
    assert crd.main() == 0
    out = capsys.readouterr().out
    assert "[HELD]" in out and "typescript-eslint#10940" in out


def test_hold_lifted_when_blocker_accepts_new_major(registry, capsys) -> None:
    registry["typescript-eslint"]["peerDependencies"]["typescript"] = ">=4.8.4 <7.1.0"
    assert crd.main() == 1
    captured = capsys.readouterr()
    assert "[DRIFT]" in captured.out and "hold no longer needed" in captured.err


def test_hold_lifted_when_blocker_drops_peer(registry) -> None:
    registry["typescript-eslint"]["peerDependencies"] = {}
    assert crd.main() == 1


def test_hold_unverifiable_is_checker_error(registry, capsys) -> None:
    registry["typescript-eslint"] = urllib.error.URLError("offline")
    assert crd.main() == 2
    assert "could not verify the hold on typescript" in capsys.readouterr().err


def test_hold_with_unparseable_peer_range_is_checker_error(registry) -> None:
    registry["typescript-eslint"]["peerDependencies"]["typescript"] = "6.0.0 - 7.0.0"
    assert crd.main() == 2


def test_unheld_drift_fails(registry, capsys) -> None:
    registry["eslint"] = {"version": "11.0.0"}
    assert crd.main() == 1
    assert "eslint: pinned ^10.x, latest 11.x" in capsys.readouterr().err


def test_no_drift(registry, capsys) -> None:
    registry["typescript"] = {"version": "6.0.3"}
    assert crd.main() == 0
    assert "No regen-script dependency drift." in capsys.readouterr().out


def test_hold_for_unpinned_package_is_checker_error(
    registry, monkeypatch, capsys
) -> None:
    monkeypatch.setitem(crd.HOLDS, "left-pad", crd.Hold(blocker="x", reason="y"))
    assert crd.main() == 2
    assert "left-pad" in capsys.readouterr().err


def test_real_script_pins_cover_every_hold() -> None:
    pins = crd.extract_dev_pins((REPO / "regenerate_ts.py").read_text())
    assert set(crd.HOLDS) <= set(pins)
