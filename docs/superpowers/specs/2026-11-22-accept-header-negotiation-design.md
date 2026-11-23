# Accept-header content negotiation in the clients (issue #24)

## Intent

The TMI server replaced the `?format=` query parameter with `Accept`-header content
negotiation. Two operations are affected:

- `getDiagramModel` returns `application/json` (the default), `application/yaml` or
  `application/graphml+xml`.
- `listSystemAuditEntries` returns `application/json` (a page, the default), `text/csv` or
  `application/x-ndjson` (an export).

Callers of every client need a supported way to request the non-JSON representations and
read the raw body.

## Current state (3.0.0 clients)

- No generated or hand-written code sends `format` (issue checklist items 1 and 2 are done).
- **Python:** `_headers={"Accept": ...}` overrides the generated Accept. The deserializing
  method then fails on YAML ("Unsupported content type") and on CSV (model parse).
  `*_without_preload_content(..., _headers=...)` returns the raw urllib3 response.
- **TypeScript:** `*Raw(params, initOverrideFn)` with a function that merges
  `init.headers` works, followed by `.raw.text()`. Passing an object as `initOverrides`
  replaces all headers, including `Authorization`. The generated TypeScript code sets no
  `Accept` by default (fetch then sends `*/*`), and the server returns JSON. (Found during implementation; this correction was approved by Eric Fitzgerald, a human decision.)
- **Go:** there is no per-request Accept. `Execute` always sends `application/json`;
  `AddDefaultHeader("Accept", ...)` appends a second value rather than replacing it. When the
  body is not JSON, `decode` errors on YAML/CSV/NDJSON and runs `xml.Unmarshal` into the model
  for GraphML.

## Goals / non-goals

- Goal: each client has a documented, tested way to select the representation and get the
  raw body.
- Non-goal: typed helper functions per operation (approach B, rejected).
- Anti-goal: changing behavior for callers who don't opt in; per-operation patches that break
  when the spec adds another negotiated operation.

## Approaches

- **A (chosen by Eric Fitzgerald, human decision):** a generic Go codegen patch, with Python
  and TypeScript using the existing generator hooks; recipes in the README; regression tests
  in each language.
- B: A plus hand-written helpers in each client that return the text. Rejected: three
  hand-written APIs that every regeneration must preserve.

## Design

**Go** (`regenerate_go.py` patch, asserted by `codegen_fixes_test.go`):

- Add an exported `WithAccept(ctx context.Context, mediaType string) context.Context` in
  `configuration.go`, backed by an unexported context key.
- In `prepareRequest`, after the header and default-header loops, if the context carries an
  override, call `localVarRequest.Header.Set("Accept", override)`.
- Replace each generated success-path call
  `a.client.decode(&localVarReturnValue, localVarBody, localVarHTTPResponse.Header.Get("Content-Type"))`
  with `a.client.decodeResponse(&localVarReturnValue, localVarBody, localVarHTTPResponse)`.
  `decodeResponse` skips decoding (returns nil, leaving the zero value) only when the request
  context carries an Accept override and the response Content-Type is not JSON. Otherwise it
  calls `decode` unchanged. The error-path calls (`decode(&v, ...)`) are left alone, so JSON
  error bodies still decode into `Error`. (Builder's call: limiting the patch to the
  success path, which is a separate call form, keeps error handling untouched.) The raw body
  stays readable from `*http.Response.Body`, which the generator already restores.
- The patch fails loudly (patch warning, exit 2) if no call sites match or if
  `prepareRequest` doesn't have the expected shape.

**Python / TypeScript:** no codegen change. The recipes are documented.

**Docs:** a "Content negotiation" section in the root `README.md` (the client READMEs are
regenerated), with one recipe per language for both operations, including the TypeScript
initOverrides gotcha.

**Tests** (copied into each client by regeneration and run by CI and the done gate), each
against a local HTTP test server:

- Go: `WithAccept` sends exactly one Accept with the override. `Execute` returns a nil
  error and the raw YAML/CSV body. Without the override, Accept is `application/json` and the
  JSON decodes. A JSON 4xx with the override still yields the decoded error.
- Python (`test_diagram_fixes.py`): `_headers` sends the override, and the
  `without_preload_content` body is the raw text.
- TypeScript (`codegen_fixes.test.ts`): the function-form initOverrides sends the override
  and keeps `Authorization`, `.raw.text()` is the raw body, and no Accept is set by default.
  It uses a stubbed `Configuration.fetchApi` rather than a socket server, because the
  client's tsconfig has no Node types (controller ruling, approved by Eric Fitzgerald after the design was approved: a human decision).

**Rollout:** commit the patch and tests to `scripts/` and `regenerate_go.py`, regenerate the
Go client only (API surface unchanged, so no spec change), and release `go-v3.0.1` as a
client-only fix release (ADR 0003). Python and TypeScript need no release (docs and tests
only).

## Left to the builder

The names of the unexported key and helper, the exact README wording, and the test-server
details.
