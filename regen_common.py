#!/usr/bin/env python3
"""Shared utilities for TMI client regeneration scripts."""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

DEFAULT_SPEC_URL = (
    "https://raw.githubusercontent.com/ericfitz/tmi/"
    "refs/heads/main/api-schema/tmi-openapi.json"
)

# ANSI color codes
_RED = "\033[0;31m"
_GREEN = "\033[0;32m"
_YELLOW = "\033[1;33m"
_NC = "\033[0m"


# ---------------------------------------------------------------------------
# Output functions
# ---------------------------------------------------------------------------


def print_banner(title: str, config: dict[str, str] | None = None) -> None:
    """Print a banner with a title and optional key-value configuration."""
    width = 60
    print("=" * width)
    print(f"  {title}")
    print("=" * width)
    if config:
        for key, value in config.items():
            print(f"  {key}: {value}")
        print("=" * width)


def print_step(n: int, msg: str) -> None:
    """Print a numbered step indicator."""
    print(f"\n{'=' * 40}")
    print(f"Step {n}: {msg}...")
    print("=" * 40)


def print_success(msg: str) -> None:
    """Print a green success message."""
    print(f"{_GREEN}✓ {msg}{_NC}")


def print_warning(msg: str) -> None:
    """Print a yellow warning message."""
    print(f"{_YELLOW}⚠ {msg}{_NC}")


def print_error(msg: str) -> None:
    """Print a red error message."""
    print(f"{_RED}✗ {msg}{_NC}")


def print_summary(results: dict[str, str]) -> None:
    """Print a summary banner with key-value results."""
    width = 60
    print("\n" + "=" * width)
    print("  SUMMARY")
    print("=" * width)
    for key, value in results.items():
        print(f"  {key}: {value}")
    print("=" * width)


# ---------------------------------------------------------------------------
# Prerequisite functions
# ---------------------------------------------------------------------------


def check_prerequisite(command: str, install_hint: str) -> None:
    """Verify that *command* is on PATH; exit with guidance if missing."""
    if shutil.which(command) is None:
        print_error(
            f"Required command '{command}' not found on PATH.\n"
            f"  Install it with: {install_hint}"
        )
        sys.exit(1)
    print_success(f"Found '{command}'")


def check_version(
    command: str,
    args: list[str],
    min_version: str,
    extract_pattern: str,
) -> None:
    """Check that *command* meets a minimum version requirement.

    *args* are passed to the command (e.g. ``["--version"]``).
    *extract_pattern* is a regex with a single capture group that extracts the
    version string from the command output.
    """
    try:
        result = subprocess.run(
            [command, *args],
            capture_output=True,
            text=True,
            timeout=30,
        )
        output = result.stdout + result.stderr
    except FileNotFoundError:
        print_error(
            f"Command '{command}' not found. "
            "Please install it before proceeding."
        )
        sys.exit(1)

    match = re.search(extract_pattern, output)
    if not match:
        print_warning(
            f"Could not determine version of '{command}' from output: "
            f"{output.strip()!r}. Proceeding anyway."
        )
        return

    version_str = match.group(1)

    def _version_tuple(v: str) -> tuple[int, ...]:
        return tuple(int(x) for x in re.findall(r"\d+", v))

    actual = _version_tuple(version_str)
    required = _version_tuple(min_version)

    if actual < required:
        print_error(
            f"'{command}' version {version_str} is below the minimum "
            f"required {min_version}. Please upgrade."
        )
        sys.exit(1)

    print_success(f"'{command}' version {version_str} meets minimum {min_version}")


# ---------------------------------------------------------------------------
# Spec management
# ---------------------------------------------------------------------------


def download_spec(url: str, dest: str | Path) -> None:
    """Download an OpenAPI spec from *url* to *dest*."""
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"  Downloading spec from {url}")
    try:
        urllib.request.urlretrieve(url, str(dest))
    except urllib.error.HTTPError as exc:
        print_error(
            f"HTTP {exc.code} when downloading spec from {url}.\n"
            f"  Reason: {exc.reason}\n"
            f"  Check that the URL is correct and the server is reachable."
        )
        sys.exit(1)
    except urllib.error.URLError as exc:
        print_error(
            f"Could not reach {url}.\n"
            f"  Reason: {exc.reason}\n"
            f"  Check your network connection and the URL."
        )
        sys.exit(1)
    print_success(f"Spec downloaded to {dest}")


def extract_spec_version(spec_path: str | Path) -> str:
    """Extract the API version from an OpenAPI spec file.

    Reads ``info.version`` from the JSON spec. Returns the version string
    (e.g. ``"1.3.0"``).  Exits with an error if the file cannot be parsed
    or the version field is missing.
    """
    spec_path = Path(spec_path)
    try:
        data = json.loads(spec_path.read_text(encoding="utf-8"))
        version = data["info"]["version"]
    except (json.JSONDecodeError, KeyError, FileNotFoundError) as exc:
        print_error(
            f"Could not extract version from spec: {spec_path}\n"
            f"  Error: {exc}"
        )
        sys.exit(1)
    print_success(f"Spec version: {version}")
    return version


def update_json_version(file_path: str | Path, key: str, version: str) -> None:
    """Update a version field in a JSON file.

    *key* is the top-level key to update (e.g. ``"packageVersion"``).
    """
    file_path = Path(file_path)
    data = json.loads(file_path.read_text(encoding="utf-8"))
    old = data.get(key)
    data[key] = version
    file_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    if old != version:
        print_success(f"Updated {file_path.name}: {key} {old} → {version}")
    else:
        print_success(f"{file_path.name}: {key} already {version}")


def copy_local_spec(src: str | Path, dest: str | Path) -> None:
    """Copy a local spec file from *src* to *dest*."""
    src = Path(src)
    dest = Path(dest)
    if not src.is_file():
        print_error(
            f"Local spec file not found: {src}\n"
            f"  Provide a valid path to the OpenAPI spec JSON file."
        )
        sys.exit(1)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    print_success(f"Spec copied from {src} to {dest}")


# ---------------------------------------------------------------------------
# Subprocess
# ---------------------------------------------------------------------------


def run_command(
    cmd: list[str],
    cwd: str | Path | None = None,
    capture: bool = False,
    env: dict[str, str] | None = None,
    error_context: str = "",
) -> subprocess.CompletedProcess[str]:
    """Run *cmd* via ``subprocess.run`` and return the result.

    Does **not** raise on non-zero exit codes — callers decide how to handle
    failures.  Exits immediately with an actionable message if the executable
    is not found.
    """
    merged_env = None
    if env is not None:
        merged_env = {**os.environ, **env}

    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=capture,
            text=True,
            env=merged_env,
        )
    except FileNotFoundError:
        label = error_context or cmd[0]
        print_error(
            f"Command not found: {cmd[0]}\n"
            f"  Context: {label}\n"
            f"  Ensure the program is installed and on your PATH."
        )
        sys.exit(1)

    return result


# ---------------------------------------------------------------------------
# Code generation
# ---------------------------------------------------------------------------


def run_codegen(
    spec_path: str | Path,
    language: str,
    output_dir: str | Path,
    config_file: str | Path | None = None,
    template_dir: str | Path | None = None,
) -> None:
    """Invoke swagger-codegen to generate a client.

    Exits with code 1 if code generation fails.
    """
    cmd: list[str] = [
        "swagger-codegen",
        "generate",
        "-i", str(spec_path),
        "-l", language,
        "-o", str(output_dir),
    ]
    if config_file is not None:
        cmd.extend(["-c", str(config_file)])
    if template_dir is not None:
        cmd.extend(["-t", str(template_dir)])

    print(f"  Running: {' '.join(cmd)}")
    result = run_command(cmd, error_context="swagger-codegen generate")
    if result.returncode != 0:
        print_error(
            "Code generation failed.\n"
            f"  Command: {' '.join(cmd)}\n"
            f"  Exit code: {result.returncode}\n"
            "  Check the swagger-codegen output above for details."
        )
        sys.exit(1)
    print_success(f"Code generation complete → {output_dir}")


def run_codegen_openapi_generator(
    spec_path: str | Path,
    generator: str,
    output_dir: str | Path,
    config_file: str | Path | None = None,
) -> None:
    """Invoke openapi-generator to generate a client.

    Exits with code 1 if code generation fails.
    """
    cmd: list[str] = [
        "openapi-generator",
        "generate",
        "-i", str(spec_path),
        "-g", generator,
        "-o", str(output_dir),
    ]
    if config_file is not None:
        cmd.extend(["-c", str(config_file)])

    print(f"  Running: {' '.join(cmd)}")
    result = run_command(cmd, error_context="openapi-generator generate")
    if result.returncode != 0:
        print_error(
            "Code generation failed.\n"
            f"  Command: {' '.join(cmd)}\n"
            f"  Exit code: {result.returncode}\n"
            "  Check the openapi-generator output above for details."
        )
        sys.exit(1)
    print_success(f"Code generation complete → {output_dir}")


# ---------------------------------------------------------------------------
# File patching
# ---------------------------------------------------------------------------


def patch_file_regex(
    file_path: str | Path,
    pattern: str,
    replacement: str,
    description: str = "",
) -> bool:
    """Apply a regex substitution to *file_path*.

    Returns ``True`` if at least one replacement was made.
    """
    file_path = Path(file_path)
    if not file_path.is_file():
        print_warning(
            f"Patch target not found: {file_path}"
            + (f" ({description})" if description else "")
        )
        return False

    text = file_path.read_text(encoding="utf-8")
    new_text, count = re.subn(pattern, replacement, text)

    if count == 0:
        print_warning(
            f"No matches for pattern in {file_path}"
            + (f" ({description})" if description else "")
        )
        return False

    file_path.write_text(new_text, encoding="utf-8")
    label = description or f"regex patch on {file_path.name}"
    print_success(f"{label}: {count} replacement(s)")
    return True


def patch_file_exact(
    file_path: str | Path,
    old_text: str,
    new_text: str,
    description: str = "",
) -> bool:
    """Replace an exact string in *file_path*.

    Returns ``True`` if the replacement was made.
    """
    file_path = Path(file_path)
    if not file_path.is_file():
        print_warning(
            f"Patch target not found: {file_path}"
            + (f" ({description})" if description else "")
        )
        return False

    content = file_path.read_text(encoding="utf-8")
    if old_text not in content:
        print_warning(
            f"Exact text not found in {file_path}"
            + (f" ({description})" if description else "")
        )
        return False

    content = content.replace(old_text, new_text)
    file_path.write_text(content, encoding="utf-8")
    label = description or f"exact patch on {file_path.name}"
    print_success(label)
    return True


# ---------------------------------------------------------------------------
# Backup / restore
# ---------------------------------------------------------------------------


def backup_files(
    files: list[str | Path],
    dirs: list[str | Path],
    backup_dir: str | Path,
) -> None:
    """Copy *files* and *dirs* into *backup_dir*, preserving relative names.

    Missing source items are silently skipped.
    """
    backup_dir = Path(backup_dir)
    backup_dir.mkdir(parents=True, exist_ok=True)

    for f in files:
        src = Path(f)
        if src.is_file():
            dest = backup_dir / src.name
            shutil.copy2(src, dest)
            print_success(f"Backed up {src.name}")
        else:
            print_warning(f"Skipping missing file: {src}")

    for d in dirs:
        src = Path(d)
        if src.is_dir():
            dest = backup_dir / src.name
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(src, dest)
            print_success(f"Backed up directory {src.name}/")
        else:
            print_warning(f"Skipping missing directory: {src}")


def restore_files(
    backup_dir: str | Path,
    dest_dir: str | Path,
    files: list[str],
    dirs: list[str],
) -> None:
    """Restore *files* and *dirs* from *backup_dir* into *dest_dir*.

    Missing backup items trigger a warning rather than an error.
    """
    backup_dir = Path(backup_dir)
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    for f in files:
        src = backup_dir / f
        if src.is_file():
            shutil.copy2(src, dest_dir / f)
            print_success(f"Restored {f}")
        else:
            print_warning(f"Backup file not found, skipping: {src}")

    for d in dirs:
        src = backup_dir / d
        if src.is_dir():
            dest = dest_dir / d
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(src, dest)
            print_success(f"Restored directory {d}/")
        else:
            print_warning(f"Backup directory not found, skipping: {src}")


# ---------------------------------------------------------------------------
# File utilities
# ---------------------------------------------------------------------------


def count_files(directory: str | Path, pattern: str = "*") -> int:
    """Return the number of files matching *pattern* under *directory*."""
    directory = Path(directory)
    if not directory.is_dir():
        return 0
    return sum(1 for _ in directory.rglob(pattern))


def write_file(path: str | Path, content: str) -> None:
    """Write *content* to *path*, creating parent directories as needed."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print_success(f"Wrote {path}")


def clean_paths(paths: list[Path]) -> None:
    """Remove files and directories in *paths*, skipping non-existent entries."""
    for p in paths:
        if p.is_file():
            p.unlink()
            print_success(f"Removed file {p}")
        elif p.is_dir():
            shutil.rmtree(p)
            print_success(f"Removed directory {p}")
        # silently skip non-existent paths


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------


def generate_report(
    title: str,
    sections: list[dict[str, str]],
) -> str:
    """Generate a Markdown report from *title* and *sections*.

    Each section dict must have ``"heading"`` and ``"content"`` keys.
    Returns the full Markdown text.
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines: list[str] = [
        f"# {title}",
        "",
        f"Generated: {now}",
        "",
    ]
    for section in sections:
        lines.append(f"## {section['heading']}")
        lines.append("")
        lines.append(section["content"])
        lines.append("")
    return "\n".join(lines)
