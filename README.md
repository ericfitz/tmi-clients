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
  v1.3.0/            # Previous release
  v1.5.0/            # Latest
```

`versions.json` at the repo root lists the source branches to build from; each client's version is read from that branch's OpenAPI spec at build time and determines its directory. (Go uses underscores in directory names, e.g. `v1_5_0`.)

## Quick Start

```bash
# Python (latest version)
cd python-client-generated/v1.5.0
uv run python3 -c "import tmi_client; print('Success')"

# Go (latest version)
cd go-client-generated/v1_5_0
go build ./...

# TypeScript (latest version)
cd typescript-client-generated/v1.5.0
npm install && npm run build
```

## Regeneration

Regenerate all clients from all branches:

```bash
python3 regenerate_all.py
```

Filter by language or branch:

```bash
python3 regenerate_all.py --language python
python3 regenerate_all.py --branch main
python3 regenerate_all.py --language go --branch release/1.3.5
```

See `CLAUDE.md` for full documentation on the regeneration workflow and repository structure.
