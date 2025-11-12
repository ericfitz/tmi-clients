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
Automation scripts are in [`scripts/`](scripts/):

- **[regenerate_client.sh](scripts/regenerate_client.sh)** - Regenerate client from OpenAPI spec
- **[swagger-codegen-config.json](scripts/swagger-codegen-config.json)** - Code generator configuration

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
./scripts/regenerate_client.sh
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
├── scripts/                # Automation scripts
│   ├── regenerate_client.sh
│   └── swagger-codegen-config.json
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
