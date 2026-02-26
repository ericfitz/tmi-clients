#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///

"""
Analyze changes between the current OpenAPI spec and what was previously used.

This script examines the OpenAPI specification to identify:
- New endpoints/paths
- New schemas/models
- Changed schemas
- New operations
- Tag changes (API groupings)

Usage:
    uv run scripts/analyze_spec_changes.py
"""

import json
import os
import urllib.request
import tempfile
from pathlib import Path
from typing import Dict, List, Set, Any
from collections import defaultdict

# Paths
SCRIPT_DIR = Path(__file__).parent
CLIENT_DIR = SCRIPT_DIR.parent
OPENAPI_SPEC_URL = "https://raw.githubusercontent.com/ericfitz/tmi/refs/heads/main/api-schema/tmi-openapi.json"
OPENAPI_SPEC_PATH = CLIENT_DIR / "tmi-openapi.json"


def load_spec() -> Dict[str, Any]:
    """Load the OpenAPI specification."""
    with open(OPENAPI_SPEC_PATH) as f:
        return json.load(f)


def get_current_apis() -> Set[str]:
    """Get list of currently generated API classes."""
    api_dir = CLIENT_DIR / "tmi_client" / "api"
    if not api_dir.exists():
        return set()

    apis = set()
    for file in api_dir.glob("*.py"):
        if file.stem not in ["__init__", "__pycache__"]:
            apis.add(file.stem)
    return apis


def get_current_models() -> Set[str]:
    """Get list of currently generated model classes."""
    models_dir = CLIENT_DIR / "tmi_client" / "models"
    if not models_dir.exists():
        return set()

    models = set()
    for file in models_dir.glob("*.py"):
        if file.stem not in ["__init__", "__pycache__"]:
            models.add(file.stem)
    return models


def analyze_paths(spec: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze API paths and operations."""
    paths = spec.get("paths", {})

    paths_by_tag: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    operations_by_method: Dict[str, int] = defaultdict(int)

    for path, operations in paths.items():
        for method, operation in operations.items():
            if method in ["get", "post", "put", "patch", "delete"]:
                operations_by_method[method.upper()] += 1

                # Group by tags
                tags = operation.get("tags", ["untagged"])
                for tag in tags:
                    paths_by_tag[tag].append({
                        "path": path,
                        "method": method.upper(),
                        "operationId": operation.get("operationId", ""),
                        "summary": operation.get("summary", ""),
                    })

    return {
        "total_paths": len(paths),
        "paths_by_tag": paths_by_tag,
        "operations_by_method": operations_by_method,
        "all_paths": sorted(paths.keys()),
    }


def analyze_schemas(spec: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze component schemas."""
    schemas = spec.get("components", {}).get("schemas", {})

    schemas_with_discriminator: List[Dict[str, Any]] = []
    schemas_with_readonly: List[Dict[str, Any]] = []
    schemas_with_required: List[Dict[str, Any]] = []

    for schema_name, schema_def in schemas.items():
        # Check for discriminator
        if "discriminator" in schema_def:
            schemas_with_discriminator.append({
                "name": schema_name,
                "discriminator": schema_def["discriminator"],
            })

        # Check for readOnly fields
        properties = schema_def.get("properties", {})
        readonly_fields = [
            prop_name for prop_name, prop_def in properties.items()
            if prop_def.get("readOnly", False)
        ]
        if readonly_fields:
            schemas_with_readonly.append({
                "name": schema_name,
                "readonly_fields": readonly_fields,
            })

        # Check for required fields
        if schema_def.get("required"):
            schemas_with_required.append({
                "name": schema_name,
                "required_fields": schema_def["required"],
            })

    return {
        "total_schemas": len(schemas),
        "schema_names": sorted(schemas.keys()),
        "schemas_with_discriminator": schemas_with_discriminator,
        "schemas_with_readonly": schemas_with_readonly,
        "schemas_with_required": schemas_with_required,
    }


def compare_with_current(spec: Dict[str, Any]) -> Dict[str, Any]:
    """Compare spec with currently generated client."""
    current_apis = get_current_apis()
    current_models = get_current_models()

    # Expected APIs from spec (based on tags)
    spec_tags = {tag["name"] for tag in spec.get("tags", [])}

    # Expected models from spec
    spec_schemas = set(spec.get("components", {}).get("schemas", {}).keys())

    # Convert schema names to Python module names (snake_case)
    def to_snake_case(name: str) -> str:
        """Convert PascalCase to snake_case."""
        result = []
        for i, char in enumerate(name):
            if char.isupper() and i > 0:
                result.append('_')
            result.append(char.lower())
        return ''.join(result)

    expected_models = {to_snake_case(schema) for schema in spec_schemas}

    comparison = {
        "current_apis": sorted(current_apis),
        "current_models": sorted(current_models),
        "spec_tags": sorted(spec_tags),
        "spec_schemas": sorted(spec_schemas),
        "new_models_expected": sorted(expected_models - current_models),
        "removed_models_expected": sorted(current_models - expected_models),
        "api_count_change": len(spec_tags) - len(current_apis),
        "model_count_change": len(expected_models) - len(current_models),
    }

    return comparison


def generate_report(spec: Dict[str, Any]) -> str:
    """Generate a comprehensive analysis report."""
    info = spec.get("info", {})

    lines = [
        "=" * 80,
        "OpenAPI Specification Analysis Report",
        "=" * 80,
        "",
        f"Spec Version: {info.get('version', 'unknown')}",
        f"Title: {info.get('title', 'unknown')}",
        f"Spec Location: {OPENAPI_SPEC_PATH}",
        "",
        "=" * 80,
        "1. PATHS ANALYSIS",
        "=" * 80,
        "",
    ]

    paths_analysis = analyze_paths(spec)
    lines.append(f"Total API Paths: {paths_analysis['total_paths']}")
    lines.append("")
    lines.append("Operations by HTTP Method:")
    for method, count in sorted(paths_analysis["operations_by_method"].items()):
        lines.append(f"  {method}: {count}")
    lines.append("")

    lines.append("Paths by Tag (API Group):")
    for tag, operations in sorted(paths_analysis["paths_by_tag"].items()):
        lines.append(f"\n  {tag} ({len(operations)} operations):")
        for op in operations[:5]:  # Show first 5
            lines.append(f"    {op['method']} {op['path']}")
            if op['summary']:
                lines.append(f"      Summary: {op['summary']}")
        if len(operations) > 5:
            lines.append(f"    ... and {len(operations) - 5} more")

    lines.append("")
    lines.append("=" * 80)
    lines.append("2. SCHEMAS ANALYSIS")
    lines.append("=" * 80)
    lines.append("")

    schemas_analysis = analyze_schemas(spec)
    lines.append(f"Total Schemas: {schemas_analysis['total_schemas']}")
    lines.append("")

    lines.append(f"Schemas with Discriminator: {len(schemas_analysis['schemas_with_discriminator'])}")
    for schema in schemas_analysis['schemas_with_discriminator']:
        lines.append(f"  - {schema['name']}: {schema['discriminator']}")
    lines.append("")

    lines.append(f"Schemas with ReadOnly Fields: {len(schemas_analysis['schemas_with_readonly'])}")
    for schema in schemas_analysis['schemas_with_readonly'][:10]:  # Show first 10
        lines.append(f"  - {schema['name']}: {', '.join(schema['readonly_fields'])}")
    if len(schemas_analysis['schemas_with_readonly']) > 10:
        lines.append(f"  ... and {len(schemas_analysis['schemas_with_readonly']) - 10} more")
    lines.append("")

    lines.append("=" * 80)
    lines.append("3. COMPARISON WITH CURRENT CLIENT")
    lines.append("=" * 80)
    lines.append("")

    comparison = compare_with_current(spec)
    lines.append(f"Current API modules: {len(comparison['current_apis'])}")
    lines.append(f"Expected API tags: {len(comparison['spec_tags'])}")
    lines.append(f"API count change: {comparison['api_count_change']:+d}")
    lines.append("")

    lines.append(f"Current model classes: {len(comparison['current_models'])}")
    lines.append(f"Expected schemas: {len(comparison['spec_schemas'])}")
    lines.append(f"Model count change: {comparison['model_count_change']:+d}")
    lines.append("")

    if comparison['new_models_expected']:
        lines.append(f"New Models Expected ({len(comparison['new_models_expected'])}):")
        for model in comparison['new_models_expected'][:20]:
            lines.append(f"  + {model}")
        if len(comparison['new_models_expected']) > 20:
            lines.append(f"  ... and {len(comparison['new_models_expected']) - 20} more")
        lines.append("")

    if comparison['removed_models_expected']:
        lines.append(f"Models to be Removed ({len(comparison['removed_models_expected'])}):")
        for model in comparison['removed_models_expected'][:20]:
            lines.append(f"  - {model}")
        if len(comparison['removed_models_expected']) > 20:
            lines.append(f"  ... and {len(comparison['removed_models_expected']) - 20} more")
        lines.append("")

    lines.append("=" * 80)
    lines.append("4. SUMMARY")
    lines.append("=" * 80)
    lines.append("")
    lines.append("Key Findings:")
    lines.append(f"  - {paths_analysis['total_paths']} API endpoints")
    lines.append(f"  - {schemas_analysis['total_schemas']} data models")
    lines.append(f"  - {len(paths_analysis['paths_by_tag'])} API groups/tags")
    lines.append(f"  - {sum(paths_analysis['operations_by_method'].values())} total operations")
    lines.append("")

    if comparison['new_models_expected']:
        lines.append(f"⚠ IMPORTANT: {len(comparison['new_models_expected'])} new models will be generated")
    if comparison['removed_models_expected']:
        lines.append(f"⚠ IMPORTANT: {len(comparison['removed_models_expected'])} models will be removed (BREAKING CHANGE)")

    lines.append("")
    lines.append("Next Steps:")
    lines.append("  1. Review the changes above")
    lines.append("  2. Run: ./scripts/regenerate_client.sh")
    lines.append("  3. Review generated migration guide")
    lines.append("  4. Test the regenerated client")
    lines.append("")
    lines.append("=" * 80)

    return "\n".join(lines)


def save_json_analysis(spec: Dict[str, Any], output_path: Path) -> None:
    """Save detailed JSON analysis for programmatic use."""
    analysis = {
        "spec_info": spec.get("info", {}),
        "paths": analyze_paths(spec),
        "schemas": analyze_schemas(spec),
        "comparison": compare_with_current(spec),
    }

    with open(output_path, "w") as f:
        json.dump(analysis, f, indent=2)


def download_spec() -> None:
    """Download the OpenAPI spec from GitHub."""
    print(f"Downloading OpenAPI spec from {OPENAPI_SPEC_URL}...")
    urllib.request.urlretrieve(OPENAPI_SPEC_URL, OPENAPI_SPEC_PATH)
    print(f"✓ Downloaded to {OPENAPI_SPEC_PATH}")


def main():
    """Main execution."""
    print("Loading OpenAPI specification...")

    # Download the spec if not present or force download
    download_spec()

    spec = load_spec()

    print("Analyzing specification...")
    report = generate_report(spec)

    # Print to console
    print("\n")
    print(report)

    # Save to file
    docs_dir = CLIENT_DIR / "docs" / "developer"
    docs_dir.mkdir(parents=True, exist_ok=True)

    report_path = docs_dir / "SPEC_ANALYSIS.md"
    with open(report_path, "w") as f:
        f.write(report)

    print(f"\nReport saved to: {report_path}")

    # Save JSON analysis
    json_path = docs_dir / "spec_analysis.json"
    save_json_analysis(spec, json_path)
    print(f"JSON analysis saved to: {json_path}")

    return 0


if __name__ == "__main__":
    exit(main())
