"""Tests for resolve_client_dir.py and stamp_python_version.py."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import resolve_client_dir as rcd
import stamp_python_version as spv

REPO = HERE.parent.parent
_REAL_CANDIDATES = rcd.list_candidates(REPO / "python-client-generated", ".")
assert _REAL_CANDIDATES, "no committed python-client-generated/vX.Y.Z directory"
_REAL_VER, _REAL_NAME = _REAL_CANDIDATES[-1]
REAL_PY = REPO / "python-client-generated" / _REAL_NAME
SPEC_VER = ".".join(map(str, _REAL_VER))


def make_tree(tmp_path: Path, python=(), ts=(), go=(), extra=()) -> Path:
    for top, names in (
        ("python-client-generated", python),
        ("typescript-client-generated", ts),
        ("go-client-generated", go),
    ):
        for n in names:
            (tmp_path / top / n).mkdir(parents=True)
    for rel in extra:
        (tmp_path / rel).mkdir(parents=True)
    return tmp_path


@pytest.mark.parametrize(
    "version,dirs,expected",
    [
        ("2.0.0", ["v2.0.0"], "v2.0.0"),
        ("2.0.1", ["v2.0.0"], "v2.0.0"),
        ("2.0.2", ["v2.0.0", "v2.0.3"], "v2.0.0"),
        ("2.0.5", ["v2.0.0", "v2.0.3"], "v2.0.3"),
        ("2.0.3", ["v2.0.0", "v2.0.3"], "v2.0.3"),
        ("2.0.10", ["v2.0.2", "v2.0.9"], "v2.0.9"),  # numeric, not lexical
        ("2.1.4", ["v2.0.9", "v2.1.0"], "v2.1.0"),
    ],
)
def test_python_and_ts_resolution(tmp_path, version, dirs, expected):
    make_tree(tmp_path, python=dirs, ts=dirs)
    assert (
        rcd.resolve("python", version, tmp_path)[0]
        == f"python-client-generated/{expected}"
    )
    assert (
        rcd.resolve("ts", version, tmp_path)[0]
        == f"typescript-client-generated/{expected}"
    )


def test_go_underscore_naming(tmp_path):
    make_tree(tmp_path, go=["v2_0_0", "v2_0_3", "v2_1_0"])
    assert rcd.resolve("go", "2.0.1", tmp_path) == (
        "go-client-generated/v2_0_0",
        (2, 0, 0),
    )
    assert rcd.resolve("go", "2.0.9", tmp_path)[0] == "go-client-generated/v2_0_3"
    assert rcd.resolve("go", "2.1.0", tmp_path)[0] == "go-client-generated/v2_1_0"


def test_go_ignores_dotted_and_python_ignores_underscored(tmp_path):
    make_tree(tmp_path, python=["v2_0_0"], go=["v2.0.0"])
    with pytest.raises(ValueError, match="no python-client-generated"):
        rcd.resolve("python", "2.0.0", tmp_path)
    with pytest.raises(ValueError, match="no go-client-generated"):
        rcd.resolve("go", "2.0.0", tmp_path)


def test_ignores_non_version_dirs(tmp_path):
    make_tree(
        tmp_path,
        python=["v2.0.0", "scripts", "v2.0", "v2.0.1-rc1", "vX.Y.Z", "2.0.2"],
        extra=[
            "typescript-client-generated/node_modules",
            "typescript-client-generated/dist",
        ],
    )
    (tmp_path / "python-client-generated" / "v2.0.3").write_text("a file, not a dir")
    assert (
        rcd.resolve("python", "2.0.9", tmp_path)[0] == "python-client-generated/v2.0.0"
    )
    with pytest.raises(ValueError, match="Available: \\(none\\)"):
        rcd.resolve("ts", "2.0.0", tmp_path)


def test_no_same_minor_dir_lists_available(tmp_path):
    make_tree(tmp_path, python=["v2.0.0", "v2.2.0"])
    with pytest.raises(ValueError) as e:
        rcd.resolve("python", "2.1.0", tmp_path)
    msg = str(e.value)
    assert "2.1.0" in msg and "v2.0.0" in msg and "v2.2.0" in msg


def test_different_major_does_not_match(tmp_path):
    make_tree(tmp_path, python=["v2.0.0"])
    with pytest.raises(ValueError):
        rcd.resolve("python", "3.0.1", tmp_path)


def test_release_below_every_dir(tmp_path):
    make_tree(tmp_path, python=["v2.0.1"])
    with pytest.raises(ValueError, match="N <= 0"):
        rcd.resolve("python", "2.0.0", tmp_path)


def test_missing_language_dir(tmp_path):
    with pytest.raises(ValueError, match="Available: \\(none\\)"):
        rcd.resolve("go", "2.0.0", tmp_path)


@pytest.mark.parametrize(
    "bad",
    [
        "2.0",
        "v2.0.1",
        "2.0.1-rc1",
        "2.0.1; rm -rf /",
        "",
        "2.0.1\n",
        " 2.0.1",
        "2.0.1.1",
        "a.b.c",
        "2.0.01",
        "02.0.1",
        "2.00.1",
    ],
)
def test_invalid_versions_rejected(tmp_path, bad):
    make_tree(tmp_path, python=["v2.0.0"])
    with pytest.raises(ValueError, match="invalid version"):
        rcd.resolve("python", bad, tmp_path)


def test_unknown_lang_rejected(tmp_path):
    with pytest.raises(ValueError, match="unknown language"):
        rcd.resolve("rust", "2.0.0", tmp_path)


def test_cli_stdout_and_exit_codes(tmp_path, capsys):
    make_tree(tmp_path, python=["v2.0.0"])
    assert (
        rcd.main(["--lang", "python", "--version", "2.0.4", "--root", str(tmp_path)])
        == 0
    )
    assert capsys.readouterr().out == "python-client-generated/v2.0.0\n"
    assert (
        rcd.main(["--lang", "python", "--version", "2.1.0", "--root", str(tmp_path)])
        == 1
    )
    assert (
        rcd.main(["--lang", "python", "--version", "bad", "--root", str(tmp_path)]) == 1
    )
    assert (
        rcd.main(["--lang", "perl", "--version", "2.0.0", "--root", str(tmp_path)]) == 1
    )


def test_cli_github_output(tmp_path, monkeypatch):
    make_tree(tmp_path, go=["v2_0_0"])
    out = tmp_path / "gh_out"
    out.write_text("existing=1\n")
    monkeypatch.setenv("GITHUB_OUTPUT", str(out))
    assert (
        rcd.main(
            [
                "--lang",
                "go",
                "--version",
                "2.0.7",
                "--root",
                str(tmp_path),
                "--github-output",
            ]
        )
        == 0
    )
    assert out.read_text().splitlines() == [
        "existing=1",
        "pkg_dir=go-client-generated/v2_0_0",
        "version=2.0.7",
        "spec_version=2.0.0",
    ]


def test_cli_github_output_requires_env(tmp_path, monkeypatch):
    make_tree(tmp_path, go=["v2_0_0"])
    monkeypatch.delenv("GITHUB_OUTPUT", raising=False)
    assert (
        rcd.main(
            [
                "--lang",
                "go",
                "--version",
                "2.0.0",
                "--root",
                str(tmp_path),
                "--github-output",
            ]
        )
        == 1
    )


# --- Python stamping ---------------------------------------------------------

SITE_FILES = [rel for rel, _ in spv.SITES]


@pytest.fixture
def client(tmp_path):
    d = tmp_path / "client"
    for rel in SITE_FILES:
        (d / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(REAL_PY / rel, d / rel)
    return d


def snapshot(d: Path) -> dict[str, str]:
    return {rel: (d / rel).read_text() for rel in SITE_FILES}


def test_real_files_carry_expected_spec_version():
    # Guards the SITES patterns against drift when the generator templates change.
    for rel, pattern in spv.SITES:
        import re

        m = list(re.finditer(pattern, (REAL_PY / rel).read_text(), flags=re.MULTILINE))
        assert len(m) == 1, rel


def test_stamp_rewrites_only_package_version_sites(client):
    before = snapshot(client)
    changed = spv.stamp(client, SPEC_VER, "99.0.7")
    assert sorted(changed) == sorted(SITE_FILES)
    after = snapshot(client)
    for rel in SITE_FILES:
        old, new = before[rel].splitlines(), after[rel].splitlines()
        assert len(old) == len(new)
        diff = [(a, b) for a, b in zip(old, new) if a != b]
        assert len(diff) == 1, (rel, diff)
        assert "99.0.7" in diff[0][1]
    # API-version strings and OpenAPI-document headers are untouched.
    cfg = after["tmi_client/configuration.py"]
    assert f"Version of the API: {SPEC_VER}" in cfg
    assert "SDK Package Version: 99.0.7" in cfg
    assert f"The version of the OpenAPI document: {SPEC_VER}" in cfg
    assert "OpenAPI-Generator/99.0.7/python" in after["tmi_client/api_client.py"]
    assert '__version__ = "99.0.7"' in after["tmi_client/__init__.py"]
    assert 'version = "99.0.7"' in after["pyproject.toml"]
    assert 'VERSION = "99.0.7"' in after["setup.py"]


def test_stamp_noop_when_same(client):
    before = snapshot(client)
    assert spv.stamp(client, SPEC_VER, SPEC_VER) == []
    assert snapshot(client) == before


def test_stamp_second_run_with_same_target_fails_cleanly(client):
    spv.stamp(client, SPEC_VER, "2.0.1")
    with pytest.raises(ValueError, match=f"expected {SPEC_VER!r}"):
        spv.stamp(client, SPEC_VER, "2.0.1")


def test_stamp_missing_site_fails_without_partial_write(client):
    (client / "tmi_client/configuration.py").write_text("nothing here\n")
    before = snapshot(client)
    with pytest.raises(ValueError, match="configuration.py: expected exactly 1"):
        spv.stamp(client, SPEC_VER, "2.0.1")
    assert snapshot(client) == before


def test_stamp_missing_file_fails(client):
    (client / "setup.py").unlink()
    with pytest.raises(ValueError, match="missing"):
        spv.stamp(client, SPEC_VER, "2.0.1")


def test_stamp_wrong_from_fails(client):
    with pytest.raises(ValueError, match="expected '1.9.9'"):
        spv.stamp(client, "1.9.9", "2.0.1")


@pytest.mark.parametrize("bad", ["2.0", "2.0.1-rc1", "", "2.0.1\n", "2.0.01", "02.0.1"])
def test_stamp_rejects_bad_versions(client, bad):
    with pytest.raises(ValueError):
        spv.stamp(client, SPEC_VER, bad)
    with pytest.raises(ValueError):
        spv.stamp(client, bad, "2.0.1")


def test_stamp_cli(client, capsys):
    assert spv.main(["--dir", str(client), "--from", SPEC_VER, "--to", "2.0.2"]) == 0
    assert "stamped 2.0.2" in capsys.readouterr().out
    assert spv.main(["--dir", str(client), "--from", SPEC_VER, "--to", "2.0.3"]) == 1
