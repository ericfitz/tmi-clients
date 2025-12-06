#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///

"""
Validation script for Python client regeneration.

This script validates that:
1. All expected models are present
2. Constructor patches were applied
3. Configuration files are correct
4. No Python 2.x code remains
5. Critical APIs are accessible

Usage:
    uv run scripts/validate_regeneration.py [--backup-dir PATH]
"""

import argparse
import ast
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Paths
SCRIPT_DIR = Path(__file__).parent
CLIENT_DIR = SCRIPT_DIR.parent
SPEC_ANALYSIS_PATH = CLIENT_DIR / "docs" / "developer" / "spec_analysis.json"


class ValidationError(Exception):
    """Validation failed."""
    pass


class Validator:
    def __init__(self, backup_dir: Path = None):
        self.backup_dir = backup_dir
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.passed: List[str] = []

    def error(self, msg: str):
        """Record an error."""
        self.errors.append(f"❌ {msg}")

    def warning(self, msg: str):
        """Record a warning."""
        self.warnings.append(f"⚠️  {msg}")

    def success(self, msg: str):
        """Record a success."""
        self.passed.append(f"✓ {msg}")

    def validate_constructor_patches(self) -> bool:
        """Verify constructor patches were applied correctly."""
        print("\n" + "=" * 80)
        print("Validating Constructor Patches")
        print("=" * 80)

        # Check DfdDiagram
        dfd_diagram_file = CLIENT_DIR / "tmi_client" / "models" / "dfd_diagram.py"
        if not dfd_diagram_file.exists():
            self.error("DfdDiagram model file not found")
            return False

        content = dfd_diagram_file.read_text()
        if "kwargs['type'] = type" in content or 'kwargs["type"] = type' in content:
            self.success("DfdDiagram constructor patch applied")
        else:
            self.error("DfdDiagram constructor patch NOT applied")

        # Check DfdDiagramInput
        dfd_diagram_input_file = CLIENT_DIR / "tmi_client" / "models" / "dfd_diagram_input.py"
        if not dfd_diagram_input_file.exists():
            self.error("DfdDiagramInput model file not found")
            return False

        content = dfd_diagram_input_file.read_text()
        if "kwargs['type'] = type" in content or 'kwargs["type"] = type' in content:
            self.success("DfdDiagramInput constructor patch applied")
        else:
            self.error("DfdDiagramInput constructor patch NOT applied")

        return len(self.errors) == 0

    def validate_python_version(self) -> bool:
        """Verify Python 3.8+ requirements."""
        print("\n" + "=" * 80)
        print("Validating Python Version Requirements")
        print("=" * 80)

        # Check pyproject.toml
        pyproject_file = CLIENT_DIR / "pyproject.toml"
        if pyproject_file.exists():
            content = pyproject_file.read_text()
            if 'requires-python = ">=3.8"' in content:
                self.success("pyproject.toml requires Python 3.8+")
            else:
                self.error("pyproject.toml does not require Python 3.8+")
        else:
            self.warning("pyproject.toml not found")

        # Check setup.py
        setup_file = CLIENT_DIR / "setup.py"
        if setup_file.exists():
            content = setup_file.read_text()
            if 'python_requires=">=3.8"' in content or "python_requires='>=3.8'" in content:
                self.success("setup.py requires Python 3.8+")
            else:
                self.error("setup.py does not require Python 3.8+")
        else:
            self.warning("setup.py not found")

        return len(self.errors) == 0

    def validate_dependencies(self) -> bool:
        """Verify modern dependencies are present."""
        print("\n" + "=" * 80)
        print("Validating Dependencies")
        print("=" * 80)

        requirements_file = CLIENT_DIR / "requirements.txt"
        if not requirements_file.exists():
            self.error("requirements.txt not found")
            return False

        content = requirements_file.read_text()

        expected_deps = {
            "certifi": "2024.2.2",
            "six": "1.16.0",
            "python-dateutil": "2.9.0",
            "setuptools": "70.0.0",
            "urllib3": "2.0.0",
        }

        for dep, min_version in expected_deps.items():
            pattern = rf"{dep}\s*>=\s*{re.escape(min_version)}"
            if re.search(pattern, content):
                self.success(f"{dep} >= {min_version}")
            else:
                self.error(f"{dep} >= {min_version} not found in requirements.txt")

        return len(self.errors) == 0

    def validate_no_python2(self) -> bool:
        """Check for Python 2.x code patterns."""
        print("\n" + "=" * 80)
        print("Validating No Python 2.x Code")
        print("=" * 80)

        python2_patterns = [
            (r'\bprint\s+[^(]', "print statement (not function)"),
            (r'\bunicode\s*\(', "unicode() builtin"),
            (r'\.has_key\s*\(', ".has_key() method"),
            (r'<>\s*', "<> operator"),
            (r'`.*`', "backtick repr"),
        ]

        found_python2 = False

        for py_file in (CLIENT_DIR / "tmi_client").rglob("*.py"):
            content = py_file.read_text()
            for pattern, description in python2_patterns:
                matches = re.findall(pattern, content)
                if matches:
                    self.error(f"Python 2.x code in {py_file.name}: {description}")
                    found_python2 = True

        if not found_python2:
            self.success("No Python 2.x code patterns found")

        return not found_python2

    def validate_expected_models(self) -> bool:
        """Verify expected new models are present."""
        print("\n" + "=" * 80)
        print("Validating Expected Models")
        print("=" * 80)

        if not SPEC_ANALYSIS_PATH.exists():
            self.warning("Spec analysis not found, skipping model validation")
            return True

        with open(SPEC_ANALYSIS_PATH) as f:
            analysis = json.load(f)

        expected_new = set(analysis["comparison"]["new_models_expected"])

        models_dir = CLIENT_DIR / "tmi_client" / "models"
        if not models_dir.exists():
            self.error("Models directory not found")
            return False

        actual_models = {
            f.stem for f in models_dir.glob("*.py")
            if f.stem not in ["__init__", "__pycache__"]
        }

        # Check for new models
        found_new = expected_new & actual_models
        missing_new = expected_new - actual_models

        if found_new:
            self.success(f"Found {len(found_new)} new models")
            # Show some examples
            for model in sorted(list(found_new))[:5]:
                print(f"    + {model}")
            if len(found_new) > 5:
                print(f"    ... and {len(found_new) - 5} more")

        if missing_new:
            self.warning(f"{len(missing_new)} expected new models not found")
            for model in sorted(list(missing_new))[:5]:
                print(f"    - {model}")

        # Critical new models that MUST be present
        critical_models = {
            "addon_response",
            "administrator",
            "admin_user",
            "webhook_event_type",
        }

        missing_critical = critical_models - actual_models
        if missing_critical:
            for model in missing_critical:
                self.error(f"Critical model missing: {model}")
        else:
            self.success("All critical new models present")

        return len(self.errors) == 0

    def validate_api_modules(self) -> bool:
        """Verify expected API modules are present."""
        print("\n" + "=" * 80)
        print("Validating API Modules")
        print("=" * 80)

        api_dir = CLIENT_DIR / "tmi_client" / "api"
        if not api_dir.exists():
            self.error("API directory not found")
            return False

        api_modules = {
            f.stem for f in api_dir.glob("*.py")
            if f.stem not in ["__init__", "__pycache__"]
        }

        # Expected new APIs
        expected_apis = {
            # Should exist after regeneration - but naming may vary based on swagger-codegen
            # We can't predict exact names, so we check for critical ones
        }

        # Just check we have APIs
        if len(api_modules) >= 14:  # Original had 14
            self.success(f"Found {len(api_modules)} API modules")
        else:
            self.warning(f"Only {len(api_modules)} API modules (expected >= 14)")

        # Check critical APIs still exist
        critical_apis = {
            "threat_model_sub_resources_api",
            "threat_models_api",
            "webhooks_api",
            "authentication_api",
        }

        missing_critical = critical_apis - api_modules
        if missing_critical:
            for api in missing_critical:
                self.error(f"Critical API missing: {api}")
        else:
            self.success("All critical APIs present")

        return len(self.errors) == 0

    def validate_custom_files(self) -> bool:
        """Verify custom files are preserved."""
        print("\n" + "=" * 80)
        print("Validating Custom Files")
        print("=" * 80)

        custom_files = [
            "test_diagram_fixes.py",
            "scripts/regenerate_client.sh",
            "scripts/swagger-codegen-config.json",
            "scripts/analyze_spec_changes.py",
            "scripts/backup_before_regen.sh",
            "scripts/validate_regeneration.py",
        ]

        for file_path in custom_files:
            full_path = CLIENT_DIR / file_path
            if full_path.exists():
                self.success(f"{file_path} present")
            else:
                self.error(f"{file_path} missing")

        # Check for docs
        docs_dir = CLIENT_DIR / "docs" / "developer"
        if docs_dir.exists():
            self.success("docs/developer/ directory present")
        else:
            self.warning("docs/developer/ directory missing")

        return len(self.errors) == 0

    def run_all_validations(self) -> bool:
        """Run all validation checks."""
        print("=" * 80)
        print("Python Client Regeneration Validation")
        print("=" * 80)
        print(f"Client directory: {CLIENT_DIR}")
        print("")

        validations = [
            self.validate_constructor_patches,
            self.validate_python_version,
            self.validate_dependencies,
            self.validate_no_python2,
            self.validate_expected_models,
            self.validate_api_modules,
            self.validate_custom_files,
        ]

        for validation in validations:
            try:
                validation()
            except Exception as e:
                self.error(f"Validation failed with exception: {e}")

        # Print summary
        print("\n" + "=" * 80)
        print("Validation Summary")
        print("=" * 80)
        print("")

        if self.passed:
            print(f"✓ Passed: {len(self.passed)}")
            for msg in self.passed:
                print(f"  {msg}")
            print("")

        if self.warnings:
            print(f"⚠️  Warnings: {len(self.warnings)}")
            for msg in self.warnings:
                print(f"  {msg}")
            print("")

        if self.errors:
            print(f"❌ Errors: {len(self.errors)}")
            for msg in self.errors:
                print(f"  {msg}")
            print("")
            print("=" * 80)
            print("VALIDATION FAILED")
            print("=" * 80)
            return False
        else:
            print("=" * 80)
            print("✓ ALL VALIDATIONS PASSED")
            print("=" * 80)
            return True


def main():
    """Main execution."""
    parser = argparse.ArgumentParser(
        description="Validate Python client regeneration"
    )
    parser.add_argument(
        "--backup-dir",
        type=Path,
        help="Path to backup directory for comparison"
    )

    args = parser.parse_args()

    validator = Validator(backup_dir=args.backup_dir)
    success = validator.run_all_validations()

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
