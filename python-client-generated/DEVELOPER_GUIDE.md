# TMI Python Client - Developer Guide

Welcome to the TMI Python Client development documentation.

## Quick Links

### Documentation
All developer documentation is organized in [`docs/developer/`](docs/developer/):

- **[MIGRATION_GUIDE.md](docs/developer/MIGRATION_GUIDE.md)** - Migration guide for upgrading to v1.0.0
- **[CHANGELOG.md](docs/developer/CHANGELOG.md)** - Complete changelog
- **[REGENERATION_README.md](docs/developer/REGENERATION_README.md)** - How to regenerate the client
- **[REGENERATION_REPORT.md](docs/developer/REGENERATION_REPORT.md)** - Latest regeneration details

### Scripts
Analysis and validation scripts are in [`scripts/`](scripts/):

- **[openapi-generator-config.json](scripts/openapi-generator-config.json)** - Code generator configuration
- **[analyze_spec_changes.py](scripts/analyze_spec_changes.py)** - Analyze OpenAPI spec changes
- **[validate_regeneration.py](scripts/validate_regeneration.py)** - Validate regeneration output

Regeneration is done via [`regenerate_python.py`](../regenerate_python.py) at the repo root.

### Tests
- **[test_diagram_fixes.py](test_diagram_fixes.py)** - Integration tests for critical fixes

## Quick Start

### Running Tests
```bash
# All auto-generated tests
uv run --with pytest python3 -m pytest test/ -v

# Integration tests
uv run --with six --with certifi python3 test_diagram_fixes.py
```

### Regenerating the Client
```bash
cd /Users/efitz/Projects/tmi-clients
python3 regenerate_python.py
```

See [REGENERATION_README.md](docs/developer/REGENERATION_README.md) for detailed instructions.

### Installing the Package
```bash
# From the python-client-generated directory
uv pip install -e .

# Or with pip
pip install -e .
```

## Repository Structure

```
python-client-generated/
├── docs/
│   └── developer/          # Developer documentation
│       ├── CHANGELOG.md
│       ├── MIGRATION_GUIDE.md
│       ├── REGENERATION_README.md
│       └── REGENERATION_REPORT.md
├── scripts/                # Analysis, validation, and config
│   ├── analyze_spec_changes.py
│   ├── validate_regeneration.py
│   └── openapi-generator-config.json
├── tmi_client/             # Main package
│   ├── api/                # API classes
│   └── models/             # Data models
├── test/                   # Auto-generated tests
├── test_diagram_fixes.py   # Integration tests
├── pyproject.toml          # Modern Python packaging
├── setup.py                # Traditional setup
└── requirements.txt        # Dependencies
```

## Support

- For migration help, see [MIGRATION_GUIDE.md](docs/developer/MIGRATION_GUIDE.md)
- For regeneration, see [REGENERATION_README.md](docs/developer/REGENERATION_README.md)
- For changes, see [CHANGELOG.md](docs/developer/CHANGELOG.md)
- For repository guidance, see [../CLAUDE.md](../CLAUDE.md)
