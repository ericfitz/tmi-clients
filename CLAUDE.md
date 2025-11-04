# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains auto-generated API clients for the TMI (Threat Modeling Improved) API in multiple languages:
- **Python** (`python-client-generated/`) - Package name: `tmi_client`
- **Go** (`go-client-generated/`)
- **Java** (`java-client-generated/`)
- **JavaScript** (`javascript-client-generated/`)

All clients are generated from the TMI OpenAPI specification using swagger-codegen 3.0.75.

## Python Client Development

The Python client is the primary focus. It uses modern Python packaging with both `pyproject.toml` and `setup.py`.

### Running Commands

**CRITICAL**: Always use `uv run` for executing Python scripts, never use the `python` executable directly. When you need to call the Python interpreter, use `python3`.

**Python Script Requirements**: Always add uv inline script metadata to standalone Python scripts. Use this format at the top of the file:

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "tmi-client",
#     "six",
#     "certifi",
# ]
# ///
```

This allows uv to automatically manage dependencies when running the script with `uv run script.py`.

### Testing

Run tests with pytest via uv:

```bash
cd python-client-generated

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
cd python-client-generated

# Import the package (uv handles dependencies automatically)
uv run python3 -c "import tmi_client; print('Success')"
```

### Legacy Testing

The repository also includes tox configuration for multi-version Python testing:

```bash
cd python-client-generated
tox  # Tests against Python 3.8-3.14
```

## Critical OpenAPI Issues (RESOLVED)

The Python client has been patched to fix 6 critical OpenAPI specification issues. See `MIGRATION_GUIDE.md` for full details.

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

# ✓ CORRECT - DfdDiagramInput for updates (no readOnly fields)
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

Each language client follows the swagger-codegen structure:
```
<lang>-client-generated/
├── api/               # API endpoint classes
├── models/            # Data models matching OpenAPI schemas
├── docs/              # Auto-generated API documentation
├── test/              # Generated unit tests
└── README.md          # Client-specific usage guide
```

### Python Client Package Layout

```
python-client-generated/
├── tmi_client/                    # Main package
│   ├── api/                       # API classes (17 API endpoint classes)
│   │   └── threat_model_sub_resources_api.py  # Primary API for threat models
│   ├── models/                    # 106+ model classes
│   │   ├── dfd_diagram.py         # Output schema (with readOnly fields)
│   │   ├── dfd_diagram_input.py   # Input schema (no readOnly fields)
│   │   ├── base_diagram.py        # Base class for diagrams
│   │   └── ...
│   ├── configuration.py           # Client configuration
│   ├── api_client.py              # Base API client
│   └── rest.py                    # REST utilities
├── test/                          # 120+ generated test files
├── pyproject.toml                 # Modern Python packaging (uv compatible)
├── setup.py                       # Legacy setuptools config
└── requirements.txt               # Runtime dependencies
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

## Known Issues and Workarounds

See `CLIENT_IMPROVEMENTS.md` for recommended improvements and `OPENAPI_ISSUES_SUMMARY.md` for technical details on resolved issues.

## Documentation Files

- `MIGRATION_GUIDE.md` - Migration guide for the fixed OpenAPI issues
- `OPENAPI_FIX_SUMMARY.md` - Summary of OpenAPI specification fixes
- `OPENAPI_ISSUES_SUMMARY.md` - Detailed analysis of the 6 resolved issues
- `DFD_DIAGRAM_FIX.md` - Deep dive into the DfdDiagram inheritance bug fix
- `CLIENT_IMPROVEMENTS.md` - Recommendations for future client improvements
- `test_diagram_fixes.py` - Integration test verifying all fixes work correctly

## Multi-Language Support

While this repository contains clients for Go, Java, and JavaScript, they are currently auto-generated without custom patches. The Python client is the most mature and has been enhanced with bug fixes and modern tooling.

Each client directory contains:
- Language-specific README with usage examples
- Auto-generated documentation in `docs/`
- Build configuration (e.g., `go.mod`, `pom.xml`, `package.json`)

## Generation Notes

Clients were generated using swagger-codegen 3.0.75. When regenerating:
1. The Python package name should be `tmi_client` (not `swagger_client`)
2. Important patches in Python client may be overwritten - review `MIGRATION_GUIDE.md`
3. The `pyproject.toml` file is custom-added for uv support
