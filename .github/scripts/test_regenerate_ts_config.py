"""Tests for the config constants and helpers in regenerate_ts.py (repo root)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO))

import regenerate_ts


def test_dev_dependencies():
    dev = json.loads(regenerate_ts.PACKAGE_JSON)["devDependencies"]
    assert set(dev) == {"oxlint", "typescript", "vitest"}
    assert dev["typescript"].startswith("^7")


def test_committed_clients_match_generator():
    """Every committed client's scripts and devDependencies match what regenerate_ts writes."""
    expected = json.loads(regenerate_ts.PACKAGE_JSON)
    paths = sorted((REPO / "typescript-client-generated").glob("v*/package.json"))
    assert paths
    for path in paths:
        actual = json.loads(path.read_text())
        assert actual["scripts"] == expected["scripts"], path
        assert actual["devDependencies"] == expected["devDependencies"], path


def test_lint_script():
    scripts = json.loads(regenerate_ts.PACKAGE_JSON)["scripts"]
    assert scripts["lint"] == "oxlint --deny-warnings test"


def test_no_eslint_remnants():
    assert not hasattr(regenerate_ts, "ESLINT_CONFIG")
    assert not hasattr(regenerate_ts, "LINT_TS7_MARKER")
    assert "eslint" not in regenerate_ts.PACKAGE_JSON


def test_remove_stale_configs_deletes_eslint_config(tmp_path):
    (tmp_path / "eslint.config.mjs").write_text("export default [];\n")
    (tmp_path / "vitest.config.ts").write_text("export default {};\n")
    removed = regenerate_ts.remove_stale_configs(tmp_path)
    assert removed == [tmp_path / "eslint.config.mjs"]
    assert not (tmp_path / "eslint.config.mjs").exists()
    assert (tmp_path / "vitest.config.ts").exists()


def test_remove_stale_configs_noop(tmp_path):
    assert regenerate_ts.remove_stale_configs(tmp_path) == []


def test_lint_status_for():
    assert regenerate_ts.lint_status_for(0) == ("PASS", False)
    assert regenerate_ts.lint_status_for(1) == ("FAIL", True)
    assert regenerate_ts.lint_status_for(2) == ("FAIL", True)
