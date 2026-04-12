# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains auto-generated API clients for the TMI (Threat Modeling Improved) API in multiple languages:
- **Python** (`python-client-generated/`) - Package name: `tmi_client`
- **Go** (`go-client-generated/`)
- **TypeScript** (`typescript-client-generated/`) - Package name: `@tmiclient/client`

Clients are generated from the TMI OpenAPI specification using openapi-generator 7.x (Python, TypeScript) and swagger-codegen 3.0.75 (Go).

### Multi-Version Directory Structure

The repository maintains multiple API versions simultaneously. Each language client directory contains versioned subdirectories rather than a flat layout:

```
python-client-generated/
  scripts/           # Shared codegen config (openapi-generator-config.json)
  v1.2.1/            # Client generated from release/1.2.0 branch
  v1.3.0/            # Client generated from main branch
  v1.4.0/            # Client generated from dev/1.4.0 branch
```

The same structure applies to `typescript-client-generated/`.

**Go uses underscores instead of dots** in version directory names (e.g. `v1_4_0` instead of `v1.4.0`) because Go's module system rejects path elements matching a dotted version pattern unless they are a major-version suffix (`/v2`, `/v3`, etc.):

```
go-client-generated/
  scripts/           # Shared codegen config
  v1_2_1/            # Client generated from release/1.2.0 branch
  v1_3_0/            # Client generated from main branch
  v1_4_0/            # Client generated from dev/1.4.0 branch
```

Version definitions live in `versions.json` at the repo root, which declares each version, its source branch, and which version is the latest.

## Python Client Development

The Python client is the primary focus. It uses modern Python packaging with both `pyproject.toml` and `setup.py`.

### Running Commands

**CRITICAL**: Always use `uv run` for executing Python scripts, never use the `python` executable directly. When you need to call the Python interpreter, use `python3`.

**Python Script Requirements**: Always add uv inline script metadata to standalone Python scripts. Use this format at the top of the file:

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "tmi-client",
#     "six",
#     "certifi",
# ]
# ///
```

This allows uv to automatically manage dependencies when running the script with `uv run script.py`.

### Testing

Run tests with pytest via uv. Navigate to the specific version directory first:

```bash
cd python-client-generated/v1.4.0

# Run all tests
uv run --with pytest python3 -m pytest test/ -v

# Run specific test file
uv run --with pytest python3 -m pytest test/test_dfd_diagram.py -v

# Run with coverage
uv run --with pytest --with pytest-cov python3 -m pytest test/ --cov=tmi_client --cov-report=term
```

### Package Installation

The package uses `pyproject.toml` for dependency management with uv:

```bash
cd python-client-generated/v1.4.0

# Import the package (uv handles dependencies automatically)
uv run python3 -c "import tmi_client; print('Success')"
```

### Multi-version Testing

Use tox to test the client against all supported Python versions (3.9-3.14):

```bash
cd python-client-generated/v1.4.0
tox  # Tests against Python 3.9-3.14

# Test specific Python version
tox -e py311

# Run with additional pytest arguments
tox -- -k test_dfd_diagram
```

## Critical OpenAPI Issues (RESOLVED)

The Python client was previously patched to fix 6 critical OpenAPI specification issues. With the migration from swagger-codegen to openapi-generator, most of these patches are no longer needed. The only remaining patch is the UUID/datetime regex validator fix. See `MIGRATION_GUIDE.md` for full details.

### Key API Patterns

**Creating Diagrams:**
```python
from tmi_client.models.create_diagram_request import CreateDiagramRequest
request = CreateDiagramRequest(name="My Diagram", type="DFD-1.0.0")
diagram = api.create_threat_model_diagram(request, tm_id)
```

**Updating Diagrams (use DfdDiagramInput, NOT DfdDiagram):**
```python
from tmi_client.models.dfd_diagram_input import DfdDiagramInput

# CORRECT - DfdDiagramInput for updates (no readOnly fields)
update = DfdDiagramInput(
    type="DFD-1.0.0",
    name="Updated Name",
    cells=[...]
)
updated_diagram = api.update_threat_model_diagram(update, tm_id, diagram_id)
```

**Reading Diagrams:**
```python
# Returns DfdDiagram (with readOnly fields: id, created_at, modified_at)
diagram = api.get_threat_model_diagram(tm_id, diagram_id)
```

### Input vs Output Schemas

The API uses separate schemas for input and output:
- **Input schemas** (`*Input` classes): Used for POST/PUT operations, exclude readOnly fields
- **Output schemas** (base classes): Returned from GET operations, include all fields including readOnly

## Architecture

### Client Structure

Each language client follows the codegen structure (openapi-generator for Python and TypeScript, swagger-codegen for Go), with versioned subdirectories:
```
<lang>-client-generated/
├── scripts/                # Shared codegen config
└── v<version>/             # One per version in versions.json
    ├── <package>/          # Generated package (tmi_client, swagger, etc.)
    │   ├── api/            # API endpoint classes
    │   └── models/         # Data models matching OpenAPI schemas
    ├── docs/               # Auto-generated API documentation
    ├── test/               # Generated unit tests
    └── README.md           # Client-specific usage guide
```

### Python Client Package Layout

```
python-client-generated/
├── scripts/                           # Shared codegen config
│   └── openapi-generator-config.json
├── v1.4.0/                            # Latest version
│   ├── tmi_client/                    # Main package
│   │   ├── api/                       # API classes (17 API endpoint classes)
│   │   │   └── threat_model_sub_resources_api.py  # Primary API for threat models
│   │   ├── models/                    # 106+ model classes (Pydantic v2 BaseModel subclasses)
│   │   │   ├── dfd_diagram.py         # Output schema (with readOnly fields)
│   │   │   ├── dfd_diagram_input.py   # Input schema (no readOnly fields)
│   │   │   ├── base_diagram.py        # Base class for diagrams
│   │   │   └── ...
│   │   ├── configuration.py           # Client configuration
│   │   ├── api_client.py              # Base API client
│   │   └── rest.py                    # REST utilities
│   ├── test/                          # 120+ generated test files
│   ├── pyproject.toml                 # Modern Python packaging (uv compatible)
│   └── requirements.txt               # Runtime dependencies
├── v1.3.0/                            # Previous version
└── v1.2.1/                            # Older version
```

### Key API Classes

- `ThreatModelSubResourcesApi` - Primary API for working with threat models, diagrams, assets, threats
- `ThreatModelsApi` - Threat model CRUD operations
- `AuthenticationApi` - OAuth2/SAML authentication
- `AssetsApi`, `ThreatsApi`, `DocumentsApi`, etc. - Resource-specific operations

### Diagram Models Hierarchy

```
BaseDiagram (abstract)
├── DfdDiagram (output - has id, created_at, modified_at)

BaseDiagramInput (abstract)
├── DfdDiagramInput (input - no readOnly fields)
```

The discriminator field `type` determines the diagram type (currently only "DFD-1.0.0" is supported).

## Cell Structure (AntV X6 Compatibility)

Diagrams use the AntV X6 graph library format for cells (nodes and edges). Cells are represented as dictionaries with X6-compatible structure:

```python
# Node example
{
    "id": "uuid",
    "shape": "process",
    "x": 100, "y": 100,
    "width": 120, "height": 60,
    "attrs": {
        "body": {"fill": "#E1F5FE"},
        "text": {"text": "Component"}
    }
}

# Edge example
{
    "id": "uuid",
    "shape": "edge",
    "source": {"cell": "source-node-id"},
    "target": {"cell": "target-node-id"},
    "attrs": {"line": {"stroke": "#333"}}
}
```

## Documentation Structure

Regeneration scripts are at the repo root:
- `regenerate_all.py` - Orchestrator that reads `versions.json` and calls per-language scripts for each version
- `regenerate_python.py` - Python client regeneration
- `regenerate_go.py` - Go client regeneration
- `regenerate_ts.py` - TypeScript client regeneration
- `regen_common.py` - Shared utilities for all regeneration scripts
- `versions.json` - Declares all maintained versions, their source branches, and the latest version

Codegen config files are in each client's `scripts/` directory:
- `python-client-generated/scripts/openapi-generator-config.json` (openapi-generator)
- `go-client-generated/scripts/openapi-generator-config.json` and `swagger-codegen-config.json` (swagger-codegen)
- `typescript-client-generated/scripts/openapi-generator-config.json` (openapi-generator)

Analysis and validation scripts (Python client only):
- `python-client-generated/scripts/analyze_spec_changes.py`
- `python-client-generated/scripts/validate_regeneration.py`

Each version directory contains its own `REGENERATION_REPORT.md` with details of its last regeneration.

## Multi-Language Support

While this repository contains clients for Go and TypeScript, they are currently auto-generated with minimal patches for codegen bugs. The Python client is the most mature and has been enhanced with bug fixes and modern tooling.

Each client version directory contains:
- Language-specific README with usage examples
- Auto-generated documentation in `docs/`
- Build configuration (e.g., `go.mod`, `package.json`, `pyproject.toml`)

### Go Module Path

Go module paths include the version directory with underscores (not dots):
```
github.com/ericfitz/tmi-clients/go-client-generated/v<major>_<minor>_<patch>
```

For example: `github.com/ericfitz/tmi-clients/go-client-generated/v1_4_0`

## OpenAPI Specification

The clients are generated from the TMI OpenAPI specification. Each version in `versions.json` specifies a branch, and the regeneration scripts download the spec from that branch:
```
https://raw.githubusercontent.com/ericfitz/tmi/<branch>/api-schema/tmi-openapi.json
```

## Regeneration

### Orchestrator (regenerate_all.py)

The primary entry point for regeneration is `regenerate_all.py`, which reads `versions.json` and calls the per-language scripts for each version:

```bash
# Regenerate all clients for all versions
python3 regenerate_all.py

# Regenerate only Python clients (all versions)
python3 regenerate_all.py --language python

# Regenerate only a specific version (all languages)
python3 regenerate_all.py --version 1.4.0

# Regenerate a specific language and version
python3 regenerate_all.py --language go --version 1.3.0

# Skip pruning of stale version directories
python3 regenerate_all.py --no-prune
```

### Per-Language Scripts

The per-language scripts can also be called directly. They require `--spec` to point at a local OpenAPI spec file and optionally `--output-dir` to control where the generated client is written:

```bash
python3 regenerate_python.py --spec path/to/tmi-openapi.json --output-dir python-client-generated/v1.4.0
python3 regenerate_go.py --spec path/to/tmi-openapi.json --output-dir go-client-generated/v1_4_0
python3 regenerate_ts.py --spec path/to/tmi-openapi.json --output-dir typescript-client-generated/v1.4.0
```

### versions.json

The `versions.json` file at the repo root defines which versions to maintain:

```json
{
  "latest": "1.4.0",
  "versions": [
    { "version": "1.2.1", "branch": "release/1.2.0" },
    { "version": "1.3.0", "branch": "main" },
    { "version": "1.4.0", "branch": "dev/1.4.0" }
  ]
}
```

### What Each Script Does

Each per-language script automatically:
- Runs openapi-generator (Python, TypeScript) or swagger-codegen (Go) with language-specific configuration
- Applies codegen bug fix patches (UUID/datetime regex validator for Python; optional-extends and TokenRequest for TypeScript; constructor fixes, auth settings, etc. for Go)
- Writes modern config files (pyproject.toml, go.mod, package.json, etc.)
- Backs up and restores custom files
- Runs tests and generates a `REGENERATION_REPORT.md` in the output directory

The Python client generates Pydantic v2 models with full type hints.

**Exit codes:** 0 = success, 1 = fatal error (codegen failed), 2 = completed with issues (test failures or patch warnings).

**Requirements:** `openapi-generator` (brew install openapi-generator) for Python and TypeScript; `swagger-codegen` (brew install swagger-codegen) for Go; plus `uv` for Python, `go` for Go, or `node` for TypeScript.
