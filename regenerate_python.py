#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Regenerate the TMI Python client from the OpenAPI spec using openapi-generator."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from regen_common import (
    backup_files,
    check_prerequisite,
    clean_paths,
    copy_local_spec,
    count_files,
    extract_spec_version,
    generate_report,
    parse_regen_args,
    patch_file_regex,
    print_banner,
    print_step,
    print_success,
    print_summary,
    print_warning,
    restore_files,
    run_codegen_openapi_generator,
    run_command,
    update_json_version,
    write_file,
)

REPO_ROOT = Path(__file__).resolve().parent
LANG_DIR = REPO_ROOT / "python-client-generated"
CONFIG_FILE = LANG_DIR / "scripts" / "openapi-generator-config.json"

# ty (Astral type checker) config. The project's authoritative checker is mypy;
# ty is stricter about a few patterns openapi-generator emits in the generated
# package and that we do not hand-edit. Scope the rules to the generated
# package so ty still flags them in any hand-written code. See the inline
# comments for what each rule covers.
TY_TOML = """\
# ty (Astral type checker) configuration.
#
# The project's authoritative type checker is mypy (see [tool.mypy] in
# pyproject.toml). ty is stricter than mypy about a few patterns that
# openapi-generator emits in the generated tmi_client/ package and that we do
# not hand-edit:
#
#   - invalid-argument-type: rest.py builds a heterogeneous `pool_args` dict
#     (ssl.VerifyMode, str, bool, Mapping) and splats it as `**pool_args` into
#     urllib3's PoolManager/ProxyManager/SOCKSProxyManager; ty cannot narrow the
#     dict value type through the unpacking.
#   - invalid-return-type: api_client.py's response_deserialize returns an
#     ApiResponse whose type parameter ty widens to include None/Unknown.
#   - unresolved-import: models emit a self-referential `if TYPE_CHECKING:
#     from tmi_client.models.<self> import <Self>` forward-reference that ty
#     reports as unresolved even though the class is defined in the same module.
#
# These are generated-code limitations, not runtime bugs: mypy accepts them and
# the test suite passes. Scope the rules to the generated package only, so ty
# still flags them in any hand-written code.
[[overrides]]
include = ["tmi_client/**"]

[overrides.rules]
invalid-argument-type = "ignore"
invalid-return-type = "ignore"
unresolved-import = "ignore"
"""


# --- Patches ---


def patch_regex_validators(client_dir: Path, had_issues: bool) -> bool:
    """Fix openapi-generator bug: regex validators on non-string fields fail
    because Pydantic parses values to native types (UUID, datetime, etc.)
    before field validators run.

    The fix: insert a string conversion in each validator function that
    applies re.match() to a value that may not be a string.  Uses
    isoformat() for datetime objects and str() for everything else.

    For nullable optional fields the generator emits a None guard
    (``if value is None: return value``) before the re.match call.
    The conversion must be inserted *after* that guard so that
    ``str(None)`` doesn't defeat the check.
    """
    models_dir = client_dir / "tmi_client" / "models"
    if not models_dir.is_dir():
        print_warning("Models directory not found — skipping regex validator patch")
        return True

    patched_count = 0
    conversion_line = "        value = value.isoformat() if hasattr(value, 'isoformat') else str(value)\n"

    for model_file in sorted(models_dir.glob("*.py")):
        content = model_file.read_text(encoding="utf-8")
        if "re.match" not in content:
            continue

        new_content = content
        # Find all @field_validator functions that use re.match
        pattern = (
            r"(@field_validator\('\w+'\)\s*\n"
            r"    def \w+\(cls, value\):\s*\n)"
            r"(        \"\"\".*?\"\"\"\s*\n)"
        )
        matches = list(re.finditer(pattern, new_content))
        # Process in reverse order so insert offsets don't shift
        for m in reversed(matches):
            # Check if this validator uses re.match
            rest = new_content[m.end():m.end() + 500]
            if "re.match" not in rest:
                continue

            # Insert string conversion after the docstring — but if a
            # None guard is present (nullable field), insert after it
            # so that str(None) doesn't defeat the check.
            insert_point = m.end()
            none_guard = re.match(
                r"        if value is None:\s*\n            return value\s*\n",
                rest,
            )
            if none_guard:
                insert_point += none_guard.end()

            if conversion_line not in new_content[insert_point:insert_point + 200]:
                new_content = new_content[:insert_point] + conversion_line + new_content[insert_point:]
                patched_count += 1

        if new_content != content:
            model_file.write_text(new_content, encoding="utf-8")

    if patched_count > 0:
        print_success(f"Regex validator patch: {patched_count} validators fixed")
    else:
        print_warning("Regex validator patch: no validators needed fixing")

    return had_issues


def patch_urllib3_minimum_version(client_dir: Path, had_issues: bool) -> bool:
    """Bump urllib3 minimum version to >=2.6.3 across all dependency files.

    openapi-generator defaults to urllib3 >= 2.1.0, but versions before 2.6.3
    have HIGH-severity CVEs (decompression-bomb bypass, unbounded decompression
    chain).  This patch updates pyproject.toml, setup.py, and requirements.txt.
    """
    min_version = "2.6.3"
    files_patched = 0

    for rel_path in ["pyproject.toml", "setup.py", "requirements.txt"]:
        filepath = client_dir / rel_path
        if not filepath.is_file():
            continue
        content = filepath.read_text(encoding="utf-8")
        # Match urllib3 version specifier in all formats:
        #   pyproject.toml / setup.py: "urllib3 (>=1.25.3,<3.0.0)"
        #   requirements.txt:          urllib3 >= 1.25.3
        # Replace the lower bound while preserving upper bound and format.
        new_content = re.sub(
            r'(urllib3\s*)\(?>=?\s*[\d.]+(,\s*<\s*[\d.]+)?\)?',
            # rel_path is bound as a default argument: the lambda must see the
            # current iteration's value, not whatever the loop variable holds
            # whenever it happens to be called.
            lambda m, rel_path=rel_path: (
                f'{m.group(1)}(>={min_version}{m.group(2) or ""})'
                if '(' in m.group(0) or rel_path != "requirements.txt"
                else f'{m.group(1)}>= {min_version}'
            ),
            content,
        )
        if new_content != content:
            filepath.write_text(new_content, encoding="utf-8")
            files_patched += 1

    if files_patched > 0:
        print_success(f"urllib3 minimum version patch: {files_patched} files updated to >= {min_version}")
    else:
        print_success(f"urllib3 minimum version already >= {min_version}")

    return had_issues


def patch_python_minimum_version(client_dir: Path, had_issues: bool) -> bool:
    """Raise the minimum supported Python to >=3.10 in pyproject.toml and setup.py.

    openapi-generator defaults the floor to >=3.9, but urllib3 2.7.0 — which
    carries fixes for two HIGH-severity advisories (cross-origin header
    forwarding in proxied redirects, decompression-bomb bypass in the streaming
    API) — requires Python >=3.10.  Keeping a 3.9 floor forces the resolver to
    pin urllib3 2.6.3 for the 3.9 slice, leaving 3.9 users exposed with no
    backport available.  Raising the floor lets urllib3 resolve to 2.7.0 for
    every supported interpreter.  The ``tox = ">= 3.9.0"`` dev dependency is a
    tox *package* version and is intentionally left untouched.
    """
    min_python = "3.10"
    files_patched = 0

    # pyproject.toml: requires-python = ">=3.9"
    pyproject = client_dir / "pyproject.toml"
    if pyproject.is_file():
        content = pyproject.read_text(encoding="utf-8")
        new_content = re.sub(
            r'(^requires-python\s*=\s*")>=\s*[\d.]+(")',
            rf'\g<1>>={min_python}\g<2>',
            content,
            count=1,
            flags=re.MULTILINE,
        )
        if new_content != content:
            pyproject.write_text(new_content, encoding="utf-8")
            files_patched += 1

    # setup.py: PYTHON_REQUIRES = ">= 3.9"
    setup_py = client_dir / "setup.py"
    if setup_py.is_file():
        content = setup_py.read_text(encoding="utf-8")
        new_content = re.sub(
            r'(^PYTHON_REQUIRES\s*=\s*")>=\s*[\d.]+(")',
            rf'\g<1>>= {min_python}\g<2>',
            content,
            count=1,
            flags=re.MULTILINE,
        )
        if new_content != content:
            setup_py.write_text(new_content, encoding="utf-8")
            files_patched += 1

    if files_patched > 0:
        print_success(f"Python minimum version patch: {files_patched} files updated to >= {min_python}")
    else:
        print_success(f"Python minimum version already >= {min_python}")

    return had_issues


def patch_test_return_types(client_dir: Path, had_issues: bool) -> bool:
    """Fix openapi-generator bug: generated test stubs declare a return type
    on make_instance() but the body is commented out, so the function always
    returns None.  Change the annotation to ``-> None`` so type checkers
    (ty, mypy) don't report invalid-return-type errors.
    """
    test_dir = client_dir / "test"
    if not test_dir.is_dir():
        print_warning("Test directory not found — skipping test return-type patch")
        return True

    patched_count = 0
    pattern = re.compile(
        r"def make_instance\(self, include_optional\) -> [A-Za-z0-9_]+:"
    )
    replacement = "def make_instance(self, include_optional) -> None:"

    for test_file in sorted(test_dir.glob("*.py")):
        content = test_file.read_text(encoding="utf-8")
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            test_file.write_text(new_content, encoding="utf-8")
            patched_count += n

    if patched_count > 0:
        print_success(f"Test return-type patch: {patched_count} methods fixed")
    else:
        print_warning("Test return-type patch: no methods needed fixing")

    return had_issues


def patch_oneof_return_types(client_dir: Path, had_issues: bool) -> bool:
    """Fix type annotations in oneOf model ``to_json``/``to_dict`` methods.

    openapi-generator produces ``to_json`` and ``to_dict`` methods that
    call ``self.actual_instance.to_json()`` / ``.to_dict()`` behind a
    ``hasattr`` guard.  Type checkers cannot narrow the type through
    ``hasattr``, so the return value is inferred as ``object`` instead
    of the declared return type.

    Fixes:
    - ``to_json``: wrap with ``str()`` (to_json always returns str)
    - ``to_dict``: suppress with ``# type: ignore[return-value]``
    """
    models_dir = client_dir / "tmi_client" / "models"
    if not models_dir.is_dir():
        return had_issues

    patched_count = 0
    for model_file in sorted(models_dir.glob("*.py")):
        content = model_file.read_text(encoding="utf-8")
        if "actual_instance" not in content:
            continue

        new_content = re.sub(
            r"return self\.actual_instance\.to_json\(\)$",
            "return str(self.actual_instance.to_json())",
            content,
            flags=re.MULTILINE,
        )
        new_content = re.sub(
            r"return self\.actual_instance\.to_dict\(\)$",
            "return self.actual_instance.to_dict()  # type: ignore[return-value]",
            new_content,
            flags=re.MULTILINE,
        )

        if new_content != content:
            model_file.write_text(new_content, encoding="utf-8")
            patched_count += 1

    if patched_count > 0:
        print_success(f"OneOf return-type patch: {patched_count} files fixed")
    else:
        print_warning("OneOf return-type patch: no files needed fixing")

    return had_issues


def _oneof_wrapper_files(client_dir: Path) -> list[Path]:
    """Return the generated ``oneOf`` wrapper models (those with an
    ``actual_instance`` field holding the resolved variant)."""
    models_dir = client_dir / "tmi_client" / "models"
    if not models_dir.is_dir():
        return []
    return [
        f
        for f in sorted(models_dir.glob("*.py"))
        if "actual_instance: Optional[" in f.read_text(encoding="utf-8")
    ]


# Inserted into every oneOf wrapper immediately before its
# `actual_instance` field validator.
ONEOF_COERCION_VALIDATOR = '''    # Patched by regenerate_python.py: openapi-generator resolves the oneOf
    # only inside from_dict()/from_json().  A raw dict arriving through
    # ordinary Pydantic validation -- a constructor argument, or a parent
    # model's model_validate() -- matched none of this wrapper's fields, so
    # `actual_instance` stayed None and the value serialised away as null.
    # Route those payloads through from_dict() so the union is resolved and
    # a non-matching payload is rejected rather than silently discarded.
    @model_validator(mode='before')
    @classmethod
    def _resolve_oneof_payload(cls, data: Any) -> Any:
        if isinstance(data, dict) and data and not set(data) & set(cls.model_fields):
            return {"actual_instance": cls.from_dict(data).actual_instance}
        return data

'''


def patch_oneof_constructor_coercion(client_dir: Path, had_issues: bool) -> bool:
    """Make ``oneOf`` wrappers resolve raw dicts during normal validation.

    openapi-generator only resolves a ``oneOf`` union inside the wrapper's
    ``from_dict()``/``from_json()``.  Passing raw dicts anywhere Pydantic
    validates them instead — ``DfdDiagramInput(cells=[{...}])``, or any
    ``model_validate()`` on a parent model — matched no field on the wrapper,
    left ``actual_instance`` as ``None``, and serialised the request body as
    ``"cells": [null, null]``, silently discarding every cell.  Invalid cells
    were accepted the same way.

    The fix adds a ``mode='before'`` model validator that recognises a payload
    dict (one sharing no key with the wrapper's own fields) and routes it
    through ``from_dict()``.  Wrapper-shaped input and non-dict input are
    passed through untouched.
    """
    patched_count = 0

    for model_file in _oneof_wrapper_files(client_dir):
        content = model_file.read_text(encoding="utf-8")
        if "_resolve_oneof_payload" in content:
            continue

        anchor = "    @field_validator('actual_instance')\n"
        if anchor not in content:
            print_warning(
                f"OneOf coercion patch: no anchor in {model_file.name} — skipped"
            )
            had_issues = True
            continue

        new_content = content.replace(anchor, ONEOF_COERCION_VALIDATOR + anchor, 1)

        # `model_validator` and `Any` must be importable in the module.
        new_content = re.sub(
            r"^(from pydantic import .*?)(\n)",
            lambda m: (
                m.group(1) + ", model_validator" + m.group(2)
                if "model_validator" not in m.group(1)
                else m.group(0)
            ),
            new_content,
            count=1,
            flags=re.MULTILINE,
        )
        if not re.search(r"^from typing import .*\bAny\b", new_content, re.MULTILINE):
            new_content = re.sub(
                r"^(from typing import )",
                r"\1Any, ",
                new_content,
                count=1,
                flags=re.MULTILINE,
            )

        model_file.write_text(new_content, encoding="utf-8")
        patched_count += 1

    if patched_count > 0:
        print_success(f"OneOf coercion patch: {patched_count} wrappers fixed")
    else:
        print_warning("OneOf coercion patch: no wrappers needed fixing")

    return had_issues


def patch_oneof_json_safety(client_dir: Path, had_issues: bool) -> bool:
    """Let ``oneOf`` wrappers accept ``to_dict()`` output.

    The generated ``from_dict`` re-serialises its argument with
    ``json.dumps(obj)`` before handing it to ``from_json``.  ``to_dict()``
    leaves native ``UUID`` and ``datetime`` objects in place, so feeding a
    model's own output back in raised ``TypeError: Object of type UUID is not
    JSON serializable`` — the round trip a read-modify-write flow needs.

    ``to_jsonable_python`` is what the generator already uses in ``to_json``
    for exactly this reason; this applies it on the way back in.
    """
    patched_count = 0
    old_call = "return cls.from_json(json.dumps(obj))"
    new_call = "return cls.from_json(json.dumps(to_jsonable_python(obj)))"

    for model_file in _oneof_wrapper_files(client_dir):
        content = model_file.read_text(encoding="utf-8")
        if old_call not in content:
            continue

        new_content = content.replace(old_call, new_call)
        if "from pydantic_core import to_jsonable_python" not in new_content:
            new_content = re.sub(
                r"^(from pydantic import .*\n)",
                r"\1from pydantic_core import to_jsonable_python\n",
                new_content,
                count=1,
                flags=re.MULTILINE,
            )

        model_file.write_text(new_content, encoding="utf-8")
        patched_count += 1

    if patched_count > 0:
        print_success(f"OneOf JSON-safety patch: {patched_count} wrappers fixed")
    else:
        print_warning("OneOf JSON-safety patch: no wrappers needed fixing")

    return had_issues


def patch_self_referential_discriminator(client_dir: Path, had_issues: bool) -> bool:
    """Stop ``from_dict`` recursing when a discriminator maps a class to itself.

    When a schema is both a discriminator parent and one of its own mapping
    targets, openapi-generator emits a ``from_dict`` that is *only* a dispatch
    table — and one of its branches dispatches straight back into the same
    class.  ``DfdDiagram`` maps ``'DFD-1.0.0'`` to ``'DfdDiagram'``, so
    ``DfdDiagram.from_dict()`` recursed until it raised ``RecursionError``.
    ``ApiClient.__deserialize_model`` deserialises 200 responses through
    ``klass.from_dict()``, so every DFD diagram read failed.

    The fix replaces the self-dispatching branch with direct validation.
    Nested models — including ``oneOf`` wrappers, once
    ``patch_oneof_constructor_coercion`` has run — are resolved by Pydantic.
    """
    models_dir = client_dir / "tmi_client" / "models"
    if not models_dir.is_dir():
        print_warning("Models directory not found — skipping discriminator patch")
        return True

    patched_count = 0
    for model_file in sorted(models_dir.glob("*.py")):
        content = model_file.read_text(encoding="utf-8")
        if "return import_module" not in content:
            continue

        class_match = re.search(r"^class (\w+)\(", content, re.MULTILINE)
        if not class_match:
            continue
        cls_name = class_match.group(1)

        # Only the branch that dispatches back into this very class.
        self_branch = re.compile(
            rf"(^        if object_type ==\s+'[^']+':\n)"
            rf"            return import_module\([^)]*\)\.{cls_name}\.from_dict\(obj\)\n",
            re.MULTILINE,
        )
        replacement = (
            r"\1"
            "            # Patched by regenerate_python.py: the discriminator maps this\n"
            "            # value back to this same class, so dispatching would recurse\n"
            "            # forever.  Validate directly instead.\n"
            "            return cls.model_validate(obj)\n"
        )
        new_content, count = self_branch.subn(replacement, content)
        if count:
            model_file.write_text(new_content, encoding="utf-8")
            patched_count += count

    if patched_count > 0:
        print_success(
            f"Self-discriminator patch: {patched_count} recursive branches fixed"
        )
    else:
        print_warning("Self-discriminator patch: no branches needed fixing")

    return had_issues


def patch_api_client_types(client_dir: Path, had_issues: bool) -> bool:
    """Fix type annotation issues in the generated api_client.py.

    openapi-generator produces three type-checker issues:
    1. ``response_types_map.get()`` called without a None guard
       (parameter is ``Optional[Dict]``)
    2. ``response_type`` passed to ``deserialize()`` as a generic
       type var instead of ``str``
    3. ``param_serialize`` return tuple doesn't match
       ``RequestSerialized`` alias due to intermediate reassignments
    """
    api_client = client_dir / "tmi_client" / "api_client.py"
    if not api_client.is_file():
        return had_issues

    content = api_client.read_text(encoding="utf-8")
    new_content = content

    # Fix 1: add None guard to response_types_map.get() calls
    new_content = re.sub(
        r"response_type = response_types_map\.get\(str\(response_data\.status\), None\)$",
        "response_type = response_types_map.get(str(response_data.status), None) if response_types_map is not None else None",
        new_content,
        count=1,
        flags=re.MULTILINE,
    )
    new_content = re.sub(
        r'response_type = response_types_map\.get\(str\(response_data\.status\)\[0\] \+ "XX", None\)$',
        'response_type = response_types_map.get(str(response_data.status)[0] + "XX", None) if response_types_map is not None else None',
        new_content,
        count=1,
        flags=re.MULTILINE,
    )

    # Fix 2: coerce response_type to str for deserialize()
    new_content = new_content.replace(
        "return_data = self.deserialize(response_text, response_type, content_type)",
        "return_data = self.deserialize(response_text, str(response_type), content_type)",
    )

    # Fix 3: suppress return-type mismatch on param_serialize tuple
    new_content = re.sub(
        r"return method, url, header_params, body, post_params$",
        "return method, url, header_params, body, post_params  # type: ignore[return-value]",
        new_content,
        count=1,
        flags=re.MULTILINE,
    )

    if new_content != content:
        api_client.write_text(new_content, encoding="utf-8")
        print_success("API client type annotation patch applied")
    else:
        print_warning("API client type annotation patch: no changes needed")

    return had_issues


def patch_configuration_self_type(client_dir: Path, had_issues: bool) -> bool:
    """Fix ``Self`` type annotation issues in configuration.py.

    openapi-generator types the ``_default`` class variable as
    ``ClassVar[Optional[Self]]``.  Type checkers track ``Self``
    per-method, so ``Self@set_default`` != ``Self@get_default`` !=
    the class-level ``Self``, causing assignment and return-type errors.

    Fix: change the class variable type to ``Optional["Configuration"]``
    and suppress the remaining return-type mismatch in ``get_default``.
    """
    config_file = client_dir / "tmi_client" / "configuration.py"
    if not config_file.is_file():
        return had_issues

    content = config_file.read_text(encoding="utf-8")
    new_content = content

    # Fix the ClassVar type to avoid Self scoping issues
    new_content = new_content.replace(
        "_default: ClassVar[Optional[Self]] = None",
        '_default: ClassVar[Optional["Configuration"]] = None',
    )

    # get_default returns cls._default which is Optional["Configuration"],
    # but the return type is Self — suppress the unavoidable mismatch
    new_content = re.sub(
        r"return cls\._default$",
        "return cls._default  # type: ignore[return-value]",
        new_content,
        count=1,
        flags=re.MULTILINE,
    )

    if new_content != content:
        config_file.write_text(new_content, encoding="utf-8")
        print_success("Configuration Self type patch applied")
    else:
        print_warning("Configuration Self type patch: no changes needed")

    return had_issues


# --- Main ---


def main(spec_path: str, output_dir: str | None = None) -> int:
    had_issues = False

    # 1. Banner
    print_banner("TMI Python Client Regeneration (openapi-generator)", {
        "Package": "tmi_client",
        "Python": "3.10+",
        "Generator": "openapi-generator 7.x",
        "Models": "Pydantic v2",
        "Testing": "pytest",
    })

    # 2. Prerequisites
    print_step(1, "Checking prerequisites")
    check_prerequisite("openapi-generator", "brew install openapi-generator")
    check_prerequisite("uv", "brew install uv")
    print_success("All prerequisites met")

    # 3. Extract version from spec and compute output directory
    print_step(2, "Getting OpenAPI spec")
    spec_version = extract_spec_version(Path(spec_path))

    if output_dir:
        client_dir = Path(output_dir)
    else:
        client_dir = LANG_DIR / f"v{spec_version}"

    client_dir.mkdir(parents=True, exist_ok=True)
    spec_dest = client_dir / "tmi-openapi.json"
    backup_dir = client_dir / ".regeneration_backup"

    copy_local_spec(Path(spec_path), spec_dest)

    # 3b. Update codegen config with spec version
    update_json_version(CONFIG_FILE, "packageVersion", spec_version)

    # 4. Backup
    print_step(3, "Backing up custom files")
    backed_up = backup_files(
        files=[
            client_dir / "test_diagram_fixes.py",
            client_dir / ".openapi-generator-ignore",
        ],
        dirs=[],
        backup_dir=backup_dir,
    )
    print_success("Custom files backed up")

    # 5. Clean
    print_step(4, "Cleaning client directory")
    clean_paths([
        client_dir / "tmi_client",
        client_dir / "test",
        client_dir / ".openapi-generator",
    ])
    # Clean docs/*.md but not docs/developer/
    docs_dir = client_dir / "docs"
    if docs_dir.is_dir():
        for md in docs_dir.glob("*.md"):
            md.unlink()
    clean_paths([
        client_dir / ".gitignore",
        client_dir / ".travis.yml",
        client_dir / "git_push.sh",
        client_dir / "README.md",
    ])
    print_success("Client directory cleaned")

    # 6. Run codegen
    print_step(5, "Running openapi-generator")
    run_codegen_openapi_generator(
        spec_path=spec_dest,
        generator="python",
        output_dir=client_dir,
        config_file=CONFIG_FILE,
    )

    # --- Past this point, failures are exit code 2, not 1 ---

    # 6b. Stamp spec version into generated files
    print_step(6, "Stamping spec version into package files")
    patch_file_regex(
        client_dir / "pyproject.toml",
        r'^version = ".*"',
        f'version = "{spec_version}"',
        "pyproject.toml version",
    )
    patch_file_regex(
        client_dir / "setup.py",
        r'^VERSION = ".*"',
        f'VERSION = "{spec_version}"',
        "setup.py version",
    )

    # 7. Apply patches
    print_step(7, "Applying patches")
    had_issues = patch_regex_validators(client_dir, had_issues)
    had_issues = patch_test_return_types(client_dir, had_issues)
    had_issues = patch_urllib3_minimum_version(client_dir, had_issues)
    had_issues = patch_python_minimum_version(client_dir, had_issues)
    had_issues = patch_oneof_return_types(client_dir, had_issues)
    had_issues = patch_oneof_constructor_coercion(client_dir, had_issues)
    had_issues = patch_oneof_json_safety(client_dir, had_issues)
    had_issues = patch_self_referential_discriminator(client_dir, had_issues)
    had_issues = patch_api_client_types(client_dir, had_issues)
    had_issues = patch_configuration_self_type(client_dir, had_issues)
    print_success("Patches applied")

    # 7b. Write ty type-checker config (aligns ty with mypy on generated code)
    write_file(client_dir / "ty.toml", TY_TOML)
    print_success("Wrote ty.toml")

    # 8. Restore custom files
    print_step(8, "Restoring custom files")
    restore_files(
        backup_dir=backup_dir,
        dest_dir=client_dir,
        files=["test_diagram_fixes.py", ".openapi-generator-ignore"],
        dirs=[],
        backed_up=backed_up,
    )
    # Note: we do NOT restore pyproject.toml — openapi-generator produces
    # a good one with pydantic deps that we want to keep.

    # 9. Install deps
    print_step(9, "Installing dependencies")
    result = run_command(
        ["uv", "pip", "install", "-e", ".", "--quiet"],
        cwd=client_dir,
        error_context="Failed to install Python client dependencies.\n  Check that uv is working and pyproject.toml is valid.",
    )
    if result.returncode != 0:
        print_warning("Dependency installation had issues")
        had_issues = True

    # 10. Run tests
    print_step(10, "Running tests")
    result = run_command(
        ["uv", "run", "--with", "pytest", "python3", "-m", "pytest", "test/", "-v", "--tb=short"],
        cwd=client_dir,
        capture=True,
        error_context="Test execution failed.\n  Check test/ directory and dependencies.",
    )
    if result.returncode == 0:
        print_success("Auto-generated tests passed")
    else:
        print_warning("Some auto-generated tests failed — see test_output.log")
        had_issues = True
    (client_dir / "test_output.log").write_text(result.stdout + result.stderr)

    # Integration test
    integration_test = client_dir / "test_diagram_fixes.py"
    if integration_test.is_file():
        result = run_command(
            ["uv", "run", str(integration_test)],
            cwd=client_dir,
            capture=True,
            error_context="Integration test failed.",
        )
        if result.returncode == 0:
            print_success("Integration test passed")
        else:
            print_warning("Integration test failed — see integration_test_output.log")
            had_issues = True
        (client_dir / "integration_test_output.log").write_text(result.stdout + result.stderr)
    else:
        print_warning("Integration test file not found")

    # 11. Generate report
    print_step(11, "Generating summary report")
    api_count = count_files(client_dir / "tmi_client" / "api", "*.py")
    model_count = count_files(client_dir / "tmi_client" / "models", "*.py")
    test_count = count_files(client_dir / "test", "*.py")

    report = generate_report("Python Client Regeneration Report", [
        {"heading": "Changes Applied", "content": (
            "### Client Regenerated\n"
            f"- Source spec: `{spec_path}`\n"
            "- Generator: openapi-generator 7.x\n"
            f"- Package: tmi_client v{spec_version}\n"
            "- Models: Pydantic v2 with full type hints\n\n"
            "### Patches Applied\n"
            "- Regex validator fix (openapi-generator bug: "
            "regex validators on non-string fields like UUID and datetime fail "
            "because Pydantic parses the value before the validator runs)\n"
            "- Test return-type fix (openapi-generator bug: "
            "make_instance() stubs declare a model return type but body is "
            "commented out, causing type-checker errors)\n"
            "- urllib3 minimum version bump to >= 2.6.3 "
            "(CVE fixes for decompression-bomb and redirect vulnerabilities)\n"
            "- OneOf model return-type fix (type checkers can't narrow "
            "through hasattr guards on actual_instance)\n"
            "- OneOf constructor coercion (openapi-generator bug: raw dicts "
            "reaching Pydantic validation didn't resolve the oneOf, leaving "
            "actual_instance None and serialising the value away as null)\n"
            "- OneOf JSON-safety fix (openapi-generator bug: from_dict() did "
            "json.dumps() on to_dict() output, which still holds native UUID "
            "and datetime objects, breaking the read-modify-write round trip)\n"
            "- Self-referential discriminator fix (openapi-generator bug: a "
            "class listed in its own discriminator mapping dispatched from_dict() "
            "back into itself, so every DFD diagram read raised RecursionError)\n"
            "- API client type annotation fix (None guards, str coercion, "
            "return-type suppression)\n"
            "- Configuration Self type fix (ClassVar[Optional[Self]] causes "
            "per-method Self scope conflicts)\n\n"
            "### Generated Configuration\n"
            "- pyproject.toml with Pydantic v2 dependencies\n"
            "- Python 3.10+ requirement\n"
            "- pytest-based testing infrastructure\n"
            "- mypy configuration for type checking"
        )},
        {"heading": "Files Generated", "content": (
            f"- API classes: {api_count}\n"
            f"- Model classes: {model_count}\n"
            f"- Test files: {test_count}"
        )},
        {"heading": "Test Results", "content":
            "See test_output.log and integration_test_output.log for detailed test results."
        },
        {"heading": "Next Steps", "content": (
            "1. Review this report\n"
            "2. Check test_output.log for test failures\n"
            "3. Update documentation files\n"
            "4. Test against live API endpoints"
        )},
    ])
    write_file(client_dir / "REGENERATION_REPORT.md", report)
    print_success("Summary report generated: REGENERATION_REPORT.md")

    # 12. Cleanup
    print_step(12, "Cleaning up")
    clean_paths([backup_dir])
    print_success("Cleanup complete")

    # 13. Summary
    print_summary({
        "Client": "regenerated with openapi-generator",
        "Output": str(client_dir),
        "Models": "Pydantic v2 with type hints",
        "Patches": "regex validator fix" + (" (with warnings)" if had_issues else ""),
        "Tests": "see logs for results",
        "Report": "REGENERATION_REPORT.md",
    })

    return 2 if had_issues else 0


if __name__ == "__main__":
    args = parse_regen_args("Regenerate the TMI Python client from the OpenAPI spec.")
    sys.exit(main(spec_path=args.spec, output_dir=args.output_dir))
