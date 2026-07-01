# Multi-Version Client Generation

## Problem

The TMI client repo generates Python, Go, and TypeScript API clients from the upstream TMI OpenAPI specification. Currently, regenerating from a different upstream branch overwrites the clients in-place. There is no way to maintain multiple API versions simultaneously (e.g., 1.2.0, 1.3.0, and 1.4.0 clients coexisting in the repo).

Consumers need versioned clients published to package registries (PyPI, npm) and available via Go modules, with up to three versions maintained at any time.

## Decisions

- **Directory-based versioning** over branch-based: all versions coexist on `main`, no parallel branches in the clients repo.
- **Language-first, version-nested** directory layout: `{language}-client-generated/v{version}/`.
- **Three-version retention policy**: n, n-1, n-2. Older versions are pruned on regeneration.
- **Config-driven**: a `versions.json` file declares which versions to generate, not auto-discovered from upstream.
- **Regeneration is separate from release**: regen scripts update code on disk; tagging and publishing are separate steps.
- **Go module path breaking change accepted**: moving from `go-client-generated/` to `go-client-generated/v{version}/` is an intentional clean break. Old git tags remain valid for pinned consumers.
- **Delete and regenerate for migration**: no incremental migration of existing flat structure; delete generated code and regenerate all versions fresh.

## Directory Structure

After regeneration with three versions:

```
tmi-clients/
├── versions.json
├── regen_common.py
├── regenerate_python.py
├── regenerate_go.py
├── regenerate_ts.py
├── regenerate_all.py                      # NEW orchestrator
├── python-client-generated/
│   ├── scripts/                           # codegen config, shared across versions
│   │   └── openapi-generator-config.json
│   ├── v1.2.0/
│   │   ├── tmi_client/
│   │   ├── pyproject.toml
│   │   ├── test/
│   │   ├── tmi-openapi.json               # copy of spec for traceability
│   │   └── ...
│   ├── v1.3.0/
│   │   └── ...
│   └── v1.4.0/
│       └── ...
├── go-client-generated/
│   ├── scripts/
│   │   └── openapi-generator-config.json
│   ├── v1.2.0/
│   │   ├── go.mod                         # module: .../go-client-generated/v1.2.0
│   │   └── ...
│   ├── v1.3.0/
│   │   └── ...
│   └── v1.4.0/
│       └── ...
└── typescript-client-generated/
    ├── scripts/
    │   └── openapi-generator-config.json
    ├── v1.2.0/
    │   ├── package.json                   # @tmiclient/client version 1.2.0
    │   └── ...
    ├── v1.3.0/
    │   └── ...
    └── v1.4.0/
        └── ...
```

- `scripts/` stays at the language root, shared across versions.
- Each `v{version}/` directory is a complete, self-contained client.
- Go module paths include the version directory for correct `go get` resolution.

## `versions.json` Schema

```json
{
  "latest": "1.4.0",
  "versions": [
    {
      "version": "1.2.0",
      "branch": "release/1.2.0"
    },
    {
      "version": "1.3.0",
      "branch": "main",
      "tag": "v1.3.0"
    },
    {
      "version": "1.4.0",
      "branch": "dev/1.4.0"
    }
  ]
}
```

### Fields

- **`latest`** — the version considered current; used by consumers and docs to determine the default version.
- **`versions`** — exactly 3 entries (enforced by the orchestrator). Each entry:
  - **`version`** — the expected API version string (e.g., `"1.4.0"`).
  - **`branch`** — upstream `ericfitz/tmi` branch to fetch the OpenAPI spec from.
  - **`tag`** (optional) — if present, fetch the spec from this git tag instead of branch HEAD. Takes precedence over `branch` for download. `branch` is retained for documentation.

### Validation

After downloading a spec, the orchestrator extracts `info.version` and confirms it matches the declared `version` field. A mismatch skips that version entry (logged as a failure, same as a codegen failure) and continues with the remaining versions. This prevents silent version drift while not aborting the entire run.

### Spec Resolution Order

1. If `tag` is set: fetch from `refs/tags/{tag}`
2. Otherwise: fetch from `refs/heads/{branch}`

### Pruning

Any `v*` directory under a language root that is not declared in `versions.json` is removed during regeneration.

## Per-Language Script Changes

### New CLI Interface

The three per-language scripts (`regenerate_python.py`, `regenerate_go.py`, `regenerate_ts.py`) change from:

```bash
# Old
python3 regenerate_python.py [spec_path] [--branch <branch>]
```

To:

```bash
# New
python3 regenerate_python.py --spec <path-to-local-spec-file> [--output-dir <path>]
```

- **`--spec`** (required) — path to a local OpenAPI spec JSON file. The script extracts the version from `info.version` and uses it to compute the output directory.
- **`--output-dir`** (optional) — override the default output directory. For experimentation only (e.g., `--output-dir /tmp/test-client`).

### Behavioral Changes

- `CLIENT_DIR` constant is removed entirely. The output directory is always derived from the spec version: `{REPO_ROOT}/{language}-client-generated/v{version}/`, unless overridden by `--output-dir`.
- The `scripts/` directory (codegen configs) remains referenced at the language root, not inside version dirs.
- The `tmi-openapi.json` spec file is copied into the version output dir for traceability.
- Backup/restore logic operates within the version output dir.
- Per-language scripts no longer handle spec downloading or branch resolution — the orchestrator does that.

### What Doesn't Change

- All patch logic (regex validators for Python, constructor fixes for Go, TokenRequest fixes for TypeScript).
- Prerequisite checks, codegen invocations, report generation.
- The scripts remain independently runnable for single-version generation (given a local spec file).

## `regen_common.py` Changes

- **`parse_regen_args()`** updated: `--spec` (required), `--output-dir` (optional). The old `spec_path` positional arg and `--branch` flag are removed.
- **New helper**: `spec_url_for_tag(tag: str) -> str` — returns the raw GitHub URL for the spec at a given git tag (URL template uses `refs/tags/{tag}` instead of `refs/heads/{branch}`).

## Orchestrator: `regenerate_all.py`

### Workflow

1. **Read `versions.json`** — validate schema: exactly 3 versions, `latest` is one of them.
2. **Check prerequisites** — verify `openapi-generator` and `swagger-codegen` are installed (once, not per-version).
3. **For each version entry**:
   - Resolve spec URL (tag takes precedence over branch).
   - Download spec to a temp location.
   - Extract `info.version`, validate it matches the declared version. Fatal error on mismatch.
4. **For each version, for each language** (filtered by CLI flags):
   - Call the per-language script as a subprocess: `python3 regenerate_python.py --spec <downloaded-spec>`.
   - Track success/failure.
5. **Prune** — for each language directory, list `v*` subdirectories, remove any not in `versions.json`.
6. **Report** — print summary of generated versions, pruned directories, and any failures.

### CLI Interface

```bash
# Regenerate everything
python3 regenerate_all.py

# Regenerate only one language
python3 regenerate_all.py --language python

# Regenerate only one version (across all languages)
python3 regenerate_all.py --version 1.4.0

# Combine: one language, one version
python3 regenerate_all.py --language python --version 1.4.0

# Skip pruning (development use)
python3 regenerate_all.py --no-prune

# Use a different config file
python3 regenerate_all.py --config my-versions.json
```

### Failure Handling

- If a single version/language combination fails, the orchestrator logs the error and continues with the rest.
- Exit codes: 0 = all succeeded, 1 = fatal error (can't read config, missing codegen tools), 2 = partial success (some combinations failed).
- Failed versions are NOT pruned — if `v1.3.0/` exists from a prior successful run but regeneration fails this time, the old output is preserved.

### Subprocess Invocation

The orchestrator calls per-language scripts as subprocesses, not by importing their functions. This keeps each script independently runnable and avoids shared mutable state.

## Migration

1. Delete the contents of `python-client-generated/`, `go-client-generated/`, `typescript-client-generated/` (keeping `scripts/` in each).
2. Create `versions.json` at the repo root.
3. Run `python3 regenerate_all.py`.
4. Update `CLAUDE.md`, `README.md`, and docs that reference old flat paths.
5. Commit and tag.

No incremental migration needed — all generated code is reproducible from the regen scripts.

## Impact on Existing Consumers

### PyPI (Python)

No impact. Publishing is a separate step (`release_python.sh`). Existing published versions on PyPI are immutable and unaffected by regeneration. New versions are published explicitly.

### npm (TypeScript)

No impact. `npm publish` is separate. Existing published versions cannot be overwritten after 72 hours.

### Go Modules

**Breaking change.** The Go module path changes from:

```
github.com/ericfitz/tmi-clients/go-client-generated
```

To:

```
github.com/ericfitz/tmi-clients/go-client-generated/v1.4.0
```

This is effectively a new module. Existing consumers must update their import paths. Old git tags remain valid for consumers pinned to them. This is an accepted, documented breaking change.

## Out of Scope

- Tagging workflow (to be designed separately).
- Registry publishing automation (to be designed separately).
- CI/CD pipeline changes.
