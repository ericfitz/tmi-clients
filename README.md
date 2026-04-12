# tmi-clients

REST clients for the TMI (Threat Modeling Improved) API, generated from the [TMI OpenAPI specification](https://github.com/ericfitz/tmi).

## Languages

- **Python** (`python-client-generated/`) - Package name: `tmi_client`
- **Go** (`go-client-generated/`)
- **TypeScript** (`typescript-client-generated/`) - Package name: `@tmiclient/client`

## Multi-Version Structure

This repository maintains multiple API versions simultaneously. Each language directory contains versioned subdirectories:

```
python-client-generated/
  scripts/           # Shared codegen config
  v1.2.1/            # Older release
  v1.3.0/            # Previous release
  v1.4.0/            # Latest
```

Versions are declared in `versions.json` at the repo root.

## Quick Start

```bash
# Python (latest version)
cd python-client-generated/v1.4.0
uv run python3 -c "import tmi_client; print('Success')"

# Go (latest version)
cd go-client-generated/v1.4.0
go build ./...

# TypeScript (latest version)
cd typescript-client-generated/v1.4.0
npm install && npm run build
```

## Regeneration

Regenerate all clients for all versions:

```bash
python3 regenerate_all.py
```

Filter by language or version:

```bash
python3 regenerate_all.py --language python
python3 regenerate_all.py --version 1.4.0
python3 regenerate_all.py --language go --version 1.3.0
```

See `CLAUDE.md` for full documentation on the regeneration workflow and repository structure.
