# tmi-clients

REST clients for the TMI (Threat Modeling Improved) API, generated from the [TMI OpenAPI specification](https://github.com/ericfitz/tmi).

## Languages

- **Python** (`python-client-generated/`) - Package name: `tmi_client`
- **Go** (`go-client-generated/`)
- **TypeScript** (`typescript-client-generated/`) - Package name: `@tmi-dev/client`

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

## Choosing a Client Version

When you build or deploy software that uses one of these clients, match the client to the TMI server it will talk to:

1. Get the server's API schema version, either from a running server (`GET /`, JSON path `.api.version`) or from `info.version` in [`api-schema/tmi-openapi.json`](https://github.com/ericfitz/tmi/blob/main/api-schema/tmi-openapi.json) in the TMI repository.
2. Use the client with the highest patch version whose major and minor versions match the schema's. For example, for schema `1.15.4` with clients `v1.15.0` and `v1.15.2` available, use `v1.15.2`.

Clients aren't regenerated for every patch release of the schema, because patch releases seldom change the API surface. An exact patch match may therefore not exist.

The Docker builds in [ericfitz/tmi-tf-wh](https://github.com/ericfitz/tmi-tf-wh) are a working example of this pattern.

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
