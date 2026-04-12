#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Orchestrate multi-version, multi-language TMI client regeneration."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from regen_common import (
    check_prerequisite,
    clean_paths,
    download_spec,
    extract_spec_version,
    print_banner,
    print_error,
    print_step,
    print_success,
    print_summary,
    print_warning,
    run_command,
    spec_url_for_branch,
    spec_url_for_tag,
)

REPO_ROOT = Path(__file__).resolve().parent
DEFAULT_CONFIG = REPO_ROOT / "versions.json"

LANGUAGES: dict[str, dict[str, Path]] = {
    "python": {
        "script": REPO_ROOT / "regenerate_python.py",
        "directory": REPO_ROOT / "python-client-generated",
    },
    "go": {
        "script": REPO_ROOT / "regenerate_go.py",
        "directory": REPO_ROOT / "go-client-generated",
    },
    "typescript": {
        "script": REPO_ROOT / "regenerate_ts.py",
        "directory": REPO_ROOT / "typescript-client-generated",
    },
}


class ConfigError(Exception):
    """Raised when versions.json is invalid."""


def load_versions_config(config_path: str | Path) -> dict:
    """Load and validate versions.json.

    The config must contain ``latest`` and ``versions`` keys.  There must be
    exactly 3 version entries, and ``latest`` must match one of them.  Each
    entry must have ``version`` and ``branch`` keys.

    Raises :class:`ConfigError` on any validation failure.
    """
    config_path = Path(config_path)
    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, FileNotFoundError) as exc:
        raise ConfigError(f"Cannot read config: {exc}") from exc

    if "latest" not in data:
        raise ConfigError("Config missing required key 'latest'")
    if "versions" not in data:
        raise ConfigError("Config missing required key 'versions'")

    versions = data["versions"]
    if len(versions) != 3:
        raise ConfigError(
            f"Config must contain exactly 3 versions, found {len(versions)}"
        )

    declared_versions: list[str] = []
    for i, entry in enumerate(versions):
        if "version" not in entry:
            raise ConfigError(f"Version entry {i} missing required key 'version'")
        if "branch" not in entry:
            raise ConfigError(f"Version entry {i} missing required key 'branch'")
        declared_versions.append(entry["version"])

    if data["latest"] not in declared_versions:
        raise ConfigError(
            f"'latest' value '{data['latest']}' is not one of the declared "
            f"versions: {declared_versions}"
        )

    return data


def resolve_spec_url_for_entry(entry: dict) -> str:
    """Return the spec URL for a version entry.

    Uses the ``tag`` field if present, otherwise falls back to ``branch``.
    """
    if "tag" in entry:
        return spec_url_for_tag(entry["tag"])
    return spec_url_for_branch(entry["branch"])


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for the orchestrator."""
    parser = argparse.ArgumentParser(
        description="Orchestrate multi-version TMI client regeneration",
    )
    parser.add_argument(
        "--config", "-c",
        default=str(DEFAULT_CONFIG),
        help="Path to versions.json (default: %(default)s)",
    )
    parser.add_argument(
        "--language", "-l",
        choices=["python", "go", "typescript"],
        default=None,
        help="Regenerate only this language (default: all)",
    )
    parser.add_argument(
        "--version", "-v",
        default=None,
        help="Regenerate only this version (default: all)",
    )
    parser.add_argument(
        "--no-prune",
        action="store_true",
        default=False,
        help="Skip pruning stale version directories",
    )
    return parser.parse_args()


def download_and_validate_spec(entry: dict, dest_dir: Path) -> Path | None:
    """Download the spec for *entry* and validate that its version matches.

    Returns the path to the downloaded spec, or ``None`` on failure.
    Catches ``SystemExit`` from ``download_spec``/``extract_spec_version``
    so the orchestrator can continue with other versions.
    """
    version = entry["version"]
    url = resolve_spec_url_for_entry(entry)
    spec_path = dest_dir / f"tmi-openapi-{version}.json"

    try:
        download_spec(url, spec_path)
    except SystemExit:
        print_error(f"Failed to download spec for version {version}")
        return None

    try:
        actual_version = extract_spec_version(spec_path)
    except SystemExit:
        print_error(f"Failed to extract version from spec for {version}")
        return None

    if actual_version != version:
        print_error(
            f"Spec version mismatch for {version}: "
            f"expected {version}, got {actual_version}"
        )
        return None

    return spec_path


def prune_stale_versions(lang_dir: Path, active_versions: list[str]) -> list[str]:
    """Remove versioned subdirectories not in *active_versions*.

    Only removes directories whose name starts with ``v`` followed by a digit
    (e.g. ``v1.2.0``).  Returns the list of pruned directory names.
    """
    pruned: list[str] = []
    if not lang_dir.is_dir():
        return pruned

    active_set = {f"v{v}" for v in active_versions}

    for child in sorted(lang_dir.iterdir()):
        if not child.is_dir():
            continue
        name = child.name
        if re.match(r"^v\d", name) and name not in active_set:
            shutil.rmtree(child)
            print_success(f"Pruned stale directory: {lang_dir.name}/{name}")
            pruned.append(name)

    return pruned


def regenerate_version_language(spec_path: Path, language: str) -> int:
    """Call the per-language regeneration script as a subprocess.

    Returns the subprocess exit code.
    """
    lang_info = LANGUAGES[language]
    script = lang_info["script"]
    cmd = [sys.executable, str(script), "--spec", str(spec_path)]
    print(f"  Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, text=True)
    return result.returncode


def main() -> int:
    """Orchestrate multi-version client regeneration."""
    args = parse_args()

    # Load config
    try:
        config = load_versions_config(args.config)
    except ConfigError as exc:
        print_error(f"Configuration error: {exc}")
        return 1

    all_versions = config["versions"]
    all_version_strings = [e["version"] for e in all_versions]

    # Apply version filter
    if args.version:
        versions = [e for e in all_versions if e["version"] == args.version]
        if not versions:
            print_error(
                f"Version '{args.version}' not found in config. "
                f"Available: {all_version_strings}"
            )
            return 1
    else:
        versions = all_versions

    # Apply language filter
    if args.language:
        languages = [args.language]
    else:
        languages = list(LANGUAGES.keys())

    print_banner("TMI Client Multi-Version Regeneration", {
        "Config": args.config,
        "Versions": ", ".join(e["version"] for e in versions),
        "Languages": ", ".join(languages),
        "Latest": config["latest"],
    })

    # Check prerequisites
    print_step(1, "Checking prerequisites")
    check_prerequisite("openapi-generator", "brew install openapi-generator")

    # Download and validate specs
    print_step(2, "Downloading and validating specs")
    tmp_dir = Path(tempfile.mkdtemp(prefix="tmi-specs-"))
    spec_paths: dict[str, Path] = {}
    for entry in versions:
        ver = entry["version"]
        spec = download_and_validate_spec(entry, tmp_dir)
        if spec is not None:
            spec_paths[ver] = spec

    if not spec_paths:
        print_error("No specs were successfully downloaded. Aborting.")
        clean_paths([tmp_dir])
        return 1

    # Regenerate each version/language combo
    print_step(3, "Regenerating clients")
    results: dict[str, str] = {}
    successes = 0
    failures = 0

    for entry in versions:
        ver = entry["version"]
        if ver not in spec_paths:
            for lang in languages:
                key = f"{lang}/{ver}"
                results[key] = "SKIPPED (spec download failed)"
                failures += 1
            continue

        spec = spec_paths[ver]
        for lang in languages:
            key = f"{lang}/{ver}"
            print(f"\n--- Regenerating {key} ---")
            exit_code = regenerate_version_language(spec, lang)
            if exit_code == 0:
                results[key] = "OK"
                successes += 1
            elif exit_code == 2:
                results[key] = "COMPLETED WITH ISSUES"
                successes += 1  # partial success still counts
            else:
                results[key] = f"FAILED (exit code {exit_code})"
                failures += 1

    # Prune stale version directories (use full config, not filtered)
    if not args.no_prune:
        print_step(4, "Pruning stale version directories")
        for lang in languages:
            lang_dir = LANGUAGES[lang]["directory"]
            pruned = prune_stale_versions(lang_dir, all_version_strings)
            if pruned:
                for d in pruned:
                    results[f"pruned:{lang}/{d}"] = "REMOVED"
            else:
                print_success(f"No stale directories in {lang_dir.name}")

    # Cleanup temp files
    clean_paths([tmp_dir])

    # Summary
    print_summary(results)

    if failures == 0:
        print_success("All regenerations completed successfully.")
        return 0
    elif successes > 0:
        print_warning("Some regenerations failed. See summary above.")
        return 2
    else:
        print_error("All regenerations failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
