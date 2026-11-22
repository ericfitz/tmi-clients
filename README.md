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
cd python-client-generated/v3.0.0
uv run python3 -c "import tmi_client; print('Success')"

# Go (latest version)
cd go-client-generated/v3_0_0
go build ./...

# TypeScript (latest version)
cd typescript-client-generated/v3.0.0
npm install && npm run build
```

## Choosing a Client Version

When you build or deploy software that uses one of these clients, match the client to the TMI server it will talk to:

1. Get the server's API schema version, either from a running server (`GET /`, JSON path `.api.version`) or from `info.version` in [`api-schema/tmi-openapi.json`](https://github.com/ericfitz/tmi/blob/main/api-schema/tmi-openapi.json) in the TMI repository.
2. Use the client with the highest patch version whose major and minor versions match the schema's. For example, for schema `1.15.4` with clients `v1.15.0` and `v1.15.2` available, use `v1.15.2`.

Only the 3.0.0 clients are maintained (see [ADR 0006](docs/adr/0006-api-3.0.0-clients.md)). For a 2.x server, use the last 2.x release: `tmi-client` 2.2.0 on PyPI, `@tmi-dev/client` 2.2.0 on npm, or Go module `github.com/ericfitz/tmi-clients/go-client-generated/v2_2_0/v2` v2.2.0. For a 1.x server ([ADR 0002](docs/adr/0002-drop-1x-clients-at-api-2.md)), use the last 1.x release: `tmi-client` 1.16.1 on PyPI, `@tmi-dev/client` 1.16.1 on npm, or Go module `github.com/ericfitz/tmi-clients/go-client-generated/v1_16_1` v1.16.1.

Clients aren't regenerated for every patch release of the schema, because patch releases seldom change the API surface. An exact patch match may therefore not exist.

The Docker builds in [ericfitz/tmi-tf-wh](https://github.com/ericfitz/tmi-tf-wh) are a working example of this pattern.

## Content negotiation (Accept header)

Two operations return more than one representation, selected by the `Accept` header (the old `?format=` query parameter is gone):

| Operation | Media types |
|---|---|
| `getDiagramModel` | `application/json` (default), `application/yaml`, `application/graphml+xml` |
| `listSystemAuditEntries` | `application/json` (a page, default), `text/csv`, `application/x-ndjson` (an export) |

**Go** (`tmiclient.WithAccept`):

```go
ctx := tmiclient.WithAccept(context.Background(), "application/yaml")
_, resp, err := client.ThreatModelSubResourcesAPI.GetDiagramModel(ctx, tmID, diagramID).Execute()
if err != nil { /* ... */ }
defer resp.Body.Close()
body, _ := io.ReadAll(resp.Body) // raw YAML

ctx = tmiclient.WithAccept(context.Background(), "text/csv")
_, resp, err = client.AdministrationAPI.ListSystemAuditEntries(ctx).Execute()
```

**Python** (`_without_preload_content` plus `_headers`):

```python
resp = ThreatModelSubResourcesApi(api_client).get_diagram_model_without_preload_content(
    tm_id, diagram_id, _headers={"Accept": "application/yaml"})
yaml_text = resp.data.decode()

resp = AdministrationApi(api_client).list_system_audit_entries_without_preload_content(
    _headers={"Accept": "text/csv"})
csv_text = resp.data.decode()
```

**TypeScript** (`*Raw` plus a function-form `initOverrides`):

```ts
const withAccept = (mediaType: string) => async ({ init }: { init: RequestInit }) => ({
  headers: { ...(init.headers as Record<string, string>), Accept: mediaType },
});

const r = await new ThreatModelSubResourcesApi(config).getDiagramModelRaw(
  { threatModelId, diagramId }, withAccept("application/yaml"));
const yaml = await r.raw.text();

const csv = await (await new AdministrationApi(config).listSystemAuditEntriesRaw(
  {}, withAccept("text/csv"))).raw.text();
```

Notes:

- **Go:** with an override and a non-JSON response, `Execute()` returns a nil error and the model's zero value. Read the body from the returned `*http.Response`. JSON responses, including JSON error bodies, decode as usual. Without an override Go sends `application/json`.
- **Python:** the deserializing methods (`get_diagram_model()`, `list_system_audit_entries()`) raise for non-JSON responses, so use the `_without_preload_content` variants. Without `_headers`, Python sends `application/json`.
- **TypeScript:** pass a function as `initOverrides`. An object replaces all headers, including `Authorization`. TypeScript sends no `Accept` header unless you set one, and the server then returns JSON.

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
