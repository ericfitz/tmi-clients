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
from datetime import datetime
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


def load_branches_config(config_path: str | Path) -> list[str]:
    """Load and validate versions.json.

    The config declares only the source branches to build clients from::

        {"branches": ["release/1.3.5", "main"]}

    The client version is not declared here — it is read from each spec's
    ``info.version`` at build time (see :func:`download_spec_for_branch`), so
    the directory a client lands in (``v1.5.0`` / ``v1_5_0``) always matches
    the spec it was generated from.

    Must contain a ``branches`` key holding at least one non-empty string.
    Returns the list of branches.  Raises :class:`ConfigError` on any
    validation failure.
    """
    config_path = Path(config_path)
    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, FileNotFoundError) as exc:
        raise ConfigError(f"Cannot read config: {exc}") from exc

    if "branches" not in data:
        raise ConfigError("Config missing required key 'branches'")

    branches = data["branches"]
    if not isinstance(branches, list) or len(branches) < 1:
        raise ConfigError("Config 'branches' must be a non-empty list")

    for i, branch in enumerate(branches):
        if not isinstance(branch, str) or not branch.strip():
            raise ConfigError(f"Branch entry {i} must be a non-empty string")

    return branches


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
        "--branch", "-b",
        default=None,
        help="Regenerate only from this branch (default: all branches in config)",
    )
    parser.add_argument(
        "--no-prune",
        action="store_true",
        default=False,
        help="Skip pruning stale version directories",
    )
    parser.add_argument(
        "--no-pr",
        action="store_true",
        default=False,
        help="Skip creating a git branch, commit, and pull request for the regenerated clients",
    )
    return parser.parse_args()


def download_spec_for_branch(branch: str, dest_dir: Path) -> tuple[str, Path] | None:
    """Download the spec for *branch* and read its declared version.

    The client version is whatever the branch's spec declares in
    ``info.version`` — there is no expected value to validate against.
    Returns ``(version, spec_path)``, or ``None`` on failure.  Catches
    ``SystemExit`` from ``download_spec``/``extract_spec_version`` so the
    orchestrator can continue with other branches.
    """
    safe_name = branch.replace("/", "-")
    url = spec_url_for_branch(branch)
    spec_path = dest_dir / f"tmi-openapi-{safe_name}.json"

    try:
        download_spec(url, spec_path)
    except SystemExit:
        print_error(f"Failed to download spec for branch {branch}")
        return None

    try:
        version = extract_spec_version(spec_path)
    except SystemExit:
        print_error(f"Failed to extract version from spec for branch {branch}")
        return None

    print_success(f"Branch {branch} -> version {version}")
    return version, spec_path


def prune_stale_versions(
    lang_dir: Path,
    active_versions: list[str],
    is_go: bool = False,
) -> list[str]:
    """Remove versioned subdirectories not in *active_versions*.

    Only removes directories whose name starts with ``v`` followed by a digit
    (e.g. ``v1.2.0`` or ``v1_2_0``).  Returns the list of pruned directory
    names.

    For Go clients (*is_go=True*), active directories use underscores instead
    of dots (``v1_4_0``) because Go's module system rejects dotted version
    path elements.  Old dotted directories are also pruned.
    """
    pruned: list[str] = []
    if not lang_dir.is_dir():
        return pruned

    # Build the set of directory names that should be kept.
    active_set: set[str] = set()
    for v in active_versions:
        active_set.add(f"v{v}")                     # dotted (Python/TS)
        if is_go:
            active_set.add(f"v{v.replace('.', '_')}") # underscored (Go)

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


def _run_git(cmd: list[str], capture: bool = False) -> "subprocess.CompletedProcess[str]":
    """Run a git/gh *cmd* from the repo root."""
    return run_command(cmd, cwd=REPO_ROOT, capture=capture, error_context=" ".join(cmd[:2]))


def create_regeneration_pr(versions: list[str], languages: list[str]) -> dict[str, str]:
    """Create a branch, commit regenerated clients, push, and open a PR.

    Returns a results dict to merge into the run summary.  Reports errors and
    returns a failure/skip marker rather than raising.  Never attempts to work
    around a failed push (no alternate transport, no credential tricks): if the
    push fails the commit is left on a local branch and the user is told.
    """
    check_prerequisite("git", "https://git-scm.com/downloads")
    check_prerequisite("gh", "brew install gh")

    # Determine the base branch (the branch we are currently on).
    head = _run_git(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture=True)
    if head.returncode != 0:
        print_error("Could not determine the current git branch.")
        return {"pr": "FAILED (git rev-parse)"}
    base_branch = head.stdout.strip()
    if base_branch == "HEAD":
        print_error("Detached HEAD — check out a branch before creating a PR.")
        return {"pr": "SKIPPED (detached HEAD)"}

    # Bail out early if there is nothing to commit.
    status = _run_git(["git", "status", "--porcelain"], capture=True)
    if status.returncode != 0:
        print_error("Could not read git status.")
        return {"pr": "FAILED (git status)"}
    if not status.stdout.strip():
        print_warning("No changes to commit — skipping PR creation.")
        return {"pr": "SKIPPED (no changes)"}

    # Create a uniquely named branch off the current branch.
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    branch = f"chore/regenerate-clients-{timestamp}"
    if _run_git(["git", "switch", "-c", branch]).returncode != 0:
        print_error(f"Failed to create branch {branch}.")
        return {"pr": "FAILED (git switch -c)"}
    print_success(f"Created branch {branch}")

    # Stage and commit everything.
    if _run_git(["git", "add", "-A"]).returncode != 0:
        print_error("Failed to stage changes.")
        return {"pr": "FAILED (git add)"}

    ver_list = ", ".join(versions)
    lang_list = ", ".join(languages)
    commit_msg = (
        "Regenerated clients\n\n"
        f"Versions: {ver_list}\n"
        f"Languages: {lang_list}\n"
    )
    if _run_git(["git", "commit", "-m", commit_msg]).returncode != 0:
        print_error("Failed to commit changes.")
        return {"pr": "FAILED (git commit)"}
    print_success("Committed regenerated clients")

    # Push the branch.  If this fails, report and stop — do NOT work around it.
    if _run_git(["git", "push", "-u", "origin", branch]).returncode != 0:
        print_error(
            f"Failed to push branch {branch}. The commit is saved locally; "
            "push it and open the PR yourself when ready."
        )
        return {"pr": f"FAILED (git push) — local branch {branch}"}
    print_success(f"Pushed {branch} to origin")

    # Open the PR; gh prints the PR URL on stdout.
    pr_body = (
        "Automated client regeneration.\n\n"
        f"- Versions: {ver_list}\n"
        f"- Languages: {lang_list}\n\n"
        "Routed through a PR because the `main` branch ruleset requires CodeQL "
        "code-scanning results, which a direct push of the large regenerated "
        "diff cannot satisfy. Review the checks and merge when green."
    )
    pr = _run_git(
        [
            "gh", "pr", "create",
            "--base", base_branch,
            "--head", branch,
            "--title", "Regenerated clients",
            "--body", pr_body,
        ],
        capture=True,
    )
    if pr.returncode != 0:
        print_error("Failed to create the PR via gh:\n" + (pr.stderr or "").strip())
        return {"pr": f"FAILED (gh pr create) — branch {branch} pushed"}

    pr_url = pr.stdout.strip()
    print_success("Pull request created:")
    print(f"\n  {pr_url}\n")
    return {"pr": f"CREATED {pr_url}"}


def main() -> int:
    """Orchestrate multi-version client regeneration."""
    args = parse_args()

    # Load config
    try:
        all_branches = load_branches_config(args.config)
    except ConfigError as exc:
        print_error(f"Configuration error: {exc}")
        return 1

    # Apply branch filter
    if args.branch:
        branches = [b for b in all_branches if b == args.branch]
        if not branches:
            print_error(
                f"Branch '{args.branch}' not found in config. "
                f"Available: {all_branches}"
            )
            return 1
    else:
        branches = all_branches

    # Apply language filter
    if args.language:
        languages = [args.language]
    else:
        languages = list(LANGUAGES.keys())

    print_banner("TMI Client Multi-Version Regeneration", {
        "Config": args.config,
        "Branches": ", ".join(branches),
        "Languages": ", ".join(languages),
    })

    # Check prerequisites
    print_step(1, "Checking prerequisites")
    check_prerequisite("openapi-generator", "brew install openapi-generator")

    # Download each branch's spec and read its declared version.
    print_step(2, "Downloading specs and reading versions")
    tmp_dir = Path(tempfile.mkdtemp(prefix="tmi-specs-"))
    # branch -> (version, spec_path) for branches that downloaded successfully
    resolved: dict[str, tuple[str, Path]] = {}
    for branch in branches:
        result = download_spec_for_branch(branch, tmp_dir)
        if result is not None:
            version, spec = result
            resolved[branch] = (version, spec)

    if not resolved:
        print_error("No specs were successfully downloaded. Aborting.")
        clean_paths([tmp_dir])
        return 1

    # Two branches declaring the same version would build into the same
    # directory and clobber each other — warn rather than silently overwrite.
    seen_versions: dict[str, str] = {}
    for branch, (version, _spec) in resolved.items():
        if version in seen_versions:
            print_warning(
                f"Branches '{seen_versions[version]}' and '{branch}' both "
                f"declare version {version}; the later build wins its directory."
            )
        else:
            seen_versions[version] = branch

    # Versions successfully resolved from the (possibly filtered) branch set.
    resolved_versions = sorted({v for v, _ in resolved.values()})

    # Regenerate each branch/language combo
    print_step(3, "Regenerating clients")
    results: dict[str, str] = {}
    successes = 0
    failures = 0

    for branch in branches:
        if branch not in resolved:
            for lang in languages:
                results[f"{lang}/{branch}"] = "SKIPPED (spec download failed)"
                failures += 1
            continue

        version, spec = resolved[branch]
        for lang in languages:
            key = f"{lang}/{version} ({branch})"
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

    # Prune stale version directories.  Only prune when building the full,
    # unfiltered branch set — a filtered run doesn't know about the versions it
    # skipped and would wrongly delete their directories.
    if args.no_prune:
        pass
    elif args.branch:
        print_step(4, "Pruning stale version directories")
        print_warning("Skipping prune: --branch filters the build to one branch.")
    elif len(resolved) != len(branches):
        print_step(4, "Pruning stale version directories")
        print_warning(
            "Skipping prune: a branch spec failed to download, so its version "
            "is unknown and its directory must not be treated as stale."
        )
    else:
        print_step(4, "Pruning stale version directories")
        for lang in languages:
            lang_dir = LANGUAGES[lang]["directory"]
            pruned = prune_stale_versions(
                lang_dir, resolved_versions, is_go=(lang == "go"),
            )
            if pruned:
                for d in pruned:
                    results[f"pruned:{lang}/{d}"] = "REMOVED"
            else:
                print_success(f"No stale directories in {lang_dir.name}")

    # Cleanup temp files
    clean_paths([tmp_dir])

    # Optionally create a pull request with the regenerated clients
    if args.no_pr:
        print_success("Skipping PR creation (--no-pr).")
    elif failures > 0:
        print_warning("Skipping PR creation because some regenerations failed.")
        results["pr"] = "SKIPPED (regeneration failures)"
    else:
        print_step(5, "Creating pull request")
        results.update(create_regeneration_pr(resolved_versions, languages))

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
