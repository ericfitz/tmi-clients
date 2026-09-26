# CLAUDE.md

Auto-generated API clients for the TMI (Threat Modeling Improved) API, built with openapi-generator 7.x:

- **Python** (`python-client-generated/`) — package `tmi_client`; the primary, most mature client (Pydantic v2 models, bug-fix patches, modern tooling)
- **Go** (`go-client-generated/`) — auto-generated with minimal codegen-bug patches
- **TypeScript** (`typescript-client-generated/`) — package `@tmiclient/client`; likewise

## Versioned layout

Each language directory holds `scripts/` (shared codegen config, `openapi-generator-config.json`) plus one subdirectory per API version:

```
python-client-generated/
  scripts/
  v1.2.1/            # from release/1.2.0
  v1.3.0/            # from main
  v1.4.0/            # from dev/1.4.0
```

**Go uses underscores** (`v1_4_0`) because Go's module system rejects dotted version path elements other than major-version suffixes (`/v2`). Go module paths are `github.com/ericfitz/tmi-clients/go-client-generated/v<major>_<minor>_<patch>`.

Each version directory contains the generated package (`api/`, `models/`), `docs/`, `test/`, a README, build config (`pyproject.toml`, `go.mod`, `package.json`), and a `REGENERATION_REPORT.md` from its last regeneration.

`versions.json` at the repo root lists **only source branches**; each client's version is read from that branch's spec (`info.version`) at build time and determines its directory. To add or drop a maintained client, add or remove a branch. Two branches declaring the same version resolve to the same directory and the later build wins (the orchestrator warns). CI derives its test matrix from the committed client directories, not from this file.

```json
{ "branches": ["release/1.3.5", "main"] }
```

Specs are downloaded from `https://raw.githubusercontent.com/ericfitz/tmi/<branch>/api-schema/tmi-openapi.json`.

## Python client

**Always use `uv run`**, never the `python` executable directly; when you need the interpreter, use `python3`. Standalone scripts get uv inline metadata:

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["tmi-client", "six", "certifi"]
# ///
```

```bash
cd python-client-generated/v1.4.0
uv run --with pytest python3 -m pytest test/ -v                       # all tests
uv run --with pytest python3 -m pytest test/test_dfd_diagram.py -v    # one file
uv run --with pytest --with pytest-cov python3 -m pytest test/ --cov=tmi_client --cov-report=term
uv run python3 -c "import tmi_client; print('Success')"               # import check
tox                        # all supported Pythons (3.9–3.14); `tox -e py311`; `tox -- -k test_dfd_diagram`
```

### Key API classes

- `ThreatModelSubResourcesApi` — primary API for threat models, diagrams, assets, threats
- `ThreatModelsApi` — threat model CRUD; `AuthenticationApi` — OAuth2/SAML
- `AssetsApi`, `ThreatsApi`, `DocumentsApi`, etc. — resource-specific

### Input vs output schemas

`*Input` classes are for POST/PUT and exclude readOnly fields; base classes are returned from GET and include everything (`id`, `created_at`, `modified_at`). Diagrams: `BaseDiagram → DfdDiagram` (output) and `BaseDiagramInput → DfdDiagramInput` (input); the `type` discriminator is currently only `"DFD-1.0.0"`.

```python
from tmi_client.models.create_diagram_request import CreateDiagramRequest
from tmi_client.models.dfd_diagram_input import DfdDiagramInput

diagram = api.create_threat_model_diagram(CreateDiagramRequest(name="My Diagram", type="DFD-1.0.0"), tm_id)
diagram = api.get_threat_model_diagram(tm_id, diagram_id)          # DfdDiagram

# Update with DfdDiagramInput, NOT DfdDiagram. from_dict() and the constructor both resolve the
# cells oneOf and reject cells that match neither Node nor Edge.
update = DfdDiagramInput.from_dict(diagram.to_dict())              # read-modify-write round trip
update.name = "Renamed"
api.update_threat_model_diagram(update, tm_id, diagram_id)
```

> The three `oneOf`/discriminator defects tracked in issue #41 — cells silently discarded by the constructor, `to_dict()` not round-tripping through `from_dict()`, and `DfdDiagram.from_dict()` recursing forever — are generator bugs fixed by `patch_oneof_constructor_coercion`, `patch_oneof_json_safety`, and `patch_self_referential_discriminator` in `regenerate_python.py`. The patches must survive every regeneration; `test_diagram_fixes.py` asserts all three. The older swagger-codegen-era spec patches are gone (see `MIGRATION_GUIDE.md`); what remains is listed in each version's `REGENERATION_REPORT.md`.

### Cells (AntV X6 format)

Each entry in `cells` is a `oneOf` over `Node` and `Edge` and must match exactly one. A cell violating these constraints is rejected however the diagram is built:

| Field | Constraint |
|---|---|
| `Node.shape` | one of `actor`, `process`, `store`, `security-boundary`, `text-box` |
| `Edge.shape` | `flow` — **not** `edge` |
| `Node.width` / `Node.height` | `>= 40` / `>= 30` |

```python
{"id": "uuid", "shape": "process", "x": 100, "y": 100, "width": 120, "height": 60,
 "attrs": {"body": {"fill": "#E1F5FE"}, "text": {"text": "Component"}}}          # node
{"id": "uuid", "shape": "flow", "source": {"cell": "src-id"}, "target": {"cell": "dst-id"},
 "attrs": {"line": {"stroke": "#333"}}}                                           # edge
```

## Regeneration

Scripts at the repo root: `regenerate_all.py` (orchestrator), `regenerate_python.py`, `regenerate_go.py`, `regenerate_ts.py`, `regen_common.py` (shared utilities). Analysis helpers for Python: `python-client-generated/scripts/analyze_spec_changes.py` and `validate_regeneration.py`.

**Requirements:** `openapi-generator` (`brew install openapi-generator`), plus `uv` (Python), `go`, or `node` as applicable; `git` and `gh` for the PR step.

```bash
python3 regenerate_all.py                                  # all languages, all branches; then branch + commit + push + PR
python3 regenerate_all.py --language python                # one language
python3 regenerate_all.py --branch main                    # one branch (all languages)
python3 regenerate_all.py --language go --branch release/1.3.5
python3 regenerate_all.py --no-prune                       # keep stale version directories
python3 regenerate_all.py --no-pr                          # leave changes in the working tree

# per-language scripts directly
python3 regenerate_python.py --spec path/to/tmi-openapi.json --output-dir python-client-generated/v1.4.0
python3 regenerate_go.py     --spec path/to/tmi-openapi.json --output-dir go-client-generated/v1_4_0
python3 regenerate_ts.py     --spec path/to/tmi-openapi.json --output-dir typescript-client-generated/v1.4.0
```

Each per-language script runs openapi-generator, applies codegen bug-fix patches (UUID/datetime regex validator and the `oneOf` fixes for Python; optional-extends and TokenRequest for TypeScript; constructor fixes and auth settings for Go), writes modern config files, backs up and restores custom files, runs tests, and writes `REGENERATION_REPORT.md`. Exit codes: 0 success, 1 fatal (codegen failed), 2 completed with issues (test failures or patch warnings).

Pruning of stale version directories is skipped automatically under `--branch` (a single-branch run doesn't know the full version set) or when any spec fails to download (its version is unknown, so its directory must not be treated as stale).

### Landing regenerated clients (PR required)

A ruleset on `main` requires CodeQL results, and a direct push of the large regenerated diff is rejected (`GH013`: "Code scanning is waiting for results from CodeQL") because the size-limited push-time scan never produces them. Regenerated clients land via PR, where CodeQL runs against the full tree. `regenerate_all.py` does this automatically when a run produces changes: it branches off the current branch (`chore/regenerate-clients-<timestamp>`), commits, pushes, opens a PR via `gh`, and prints the URL to review and merge. The PR step is skipped if there are no changes, any regeneration hard-failed, or HEAD is detached. If `git push` fails, the script reports it and leaves the commit on a local branch; it never works around the failure.

By hand:

```bash
git switch -c chore/regenerate-clients
git add -A && git commit -m "Regenerated clients"
git push -u origin chore/regenerate-clients
gh pr create --base main --head chore/regenerate-clients --title "Regenerated clients"
```

The ruleset also blocks force-pushes and deletion of `main`.
