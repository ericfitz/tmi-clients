# Accept-Header Content Negotiation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let callers of the Go, Python and TypeScript 3.0.0 clients request the non-JSON representations of `getDiagramModel` and `listSystemAuditEntries` with the `Accept` header and read the raw body (issue #24).

**Architecture:** Go gets an opt-in, generic codegen patch: `WithAccept(ctx, mediaType)`. With it, `prepareRequest` sets the header, and the success-path decode is skipped for non-JSON responses. Python and TypeScript keep their generator hooks. Regression tests in each language's `scripts/` dir are copied into the clients. The root README documents a recipe per language.

**Tech Stack:** openapi-generator 7.27.0 output; Go `net/http/httptest`; Python stdlib `http.server` with `tmi_client`; TypeScript vitest with a `fetchApi` stub and the typescript-fetch runtime.

**Spec:** `docs/superpowers/specs/2026-11-22-accept-header-negotiation-design.md`

## Global Constraints

- Opt-in only: a request without `WithAccept` behaves exactly as before (Accept `application/json`, normal decoding).
- `WithAccept(ctx, "")` is no override (the default Accept is sent).
- The override replaces Accept: the request carries exactly one Accept value, even if `cfg.DefaultHeader` also has one.
- Error-path decoding (`a.client.decode(&v, ...)`) is not modified.
- Patches must fail loudly (`print_warning`, return `True` so the script exits 2) if an anchor is not found exactly as expected. On an already-patched tree the patch is a no-op success.
- Do not touch `python-client-generated/v3.0.0` or `typescript-client-generated/v3.0.0` beyond copying in the updated regression test file. No regeneration or release for Python and TypeScript.
- Environment facts for implementers: Node/npm come from nvm only (`export NVM_DIR=~/.nvm; . "$NVM_DIR/nvm.sh"`); Python always via `uv run`; use `rg`, not grep, with an explicit path; the Bash tool runs zsh.

## Review Focus

- GraphML responses: `application/graphml+xml` matches the generated `XmlCheck`, so without the skip it would be `xml.Unmarshal`ed into the model. The test must use this exact content type and expect a nil error plus the raw body.
- A JSON error status (406, 401) with an override set must still return a `*GenericOpenAPIError` whose `Model()` is an `Error`.
- An override of `application/json` with a JSON response must still decode the model (the skip applies only to non-JSON responses).
- In TypeScript, the object form of `initOverrides` drops `Authorization`. The test must prove the function form keeps it, and the README must warn about the object form.
- A `*http.Response` without a `Request` (as in hand-built tests or a custom transport) must not panic in `decodeResponse`.

---

### Task 1: Go `WithAccept` codegen patch

**Files:**
- Modify: `regenerate_go.py`: add `patch_accept_override(client_dir: Path, had_issues: bool) -> bool` after `patch_shape_enum_checks`, and call it in the patch sequence after line ~509 (`had_issues = patch_shape_enum_checks(...)`).
- Modify: `go-client-generated/scripts/codegen_fixes_test.go`: add the tests below.
- Regenerated: `go-client-generated/v3_0_0/` (only `configuration.go`, `client.go`, `api_*.go`, `codegen_fixes_test.go` and the README build date should change).

**Interfaces:**
- Produces (Go, package `tmiclient`, in `configuration.go`):
  - `func WithAccept(ctx context.Context, mediaType string) context.Context`
  - unexported `func acceptOverride(ctx context.Context) (string, bool)`: false when absent or empty. The key is an unexported struct type.
- Produces (in `client.go`):
  - In `prepareRequest`, immediately after the `for header, value := range c.cfg.DefaultHeader { localVarRequest.Header.Add(header, value) }` loop and before `return localVarRequest, nil`: if `acceptOverride(ctx)` is true, call `localVarRequest.Header.Set("Accept", mediaType)`.
  - `func (c *APIClient) decodeResponse(v interface{}, b []byte, resp *http.Response) error`: when `resp.Request != nil`, `acceptOverride(resp.Request.Context())` is set, and `!JsonCheck.MatchString(resp.Header.Get("Content-Type"))`, return nil. Otherwise return `c.decode(v, b, resp.Header.Get("Content-Type"))`.
- Produces (in `api_*.go`): every `a.client.decode(&localVarReturnValue, localVarBody, localVarHTTPResponse.Header.Get("Content-Type"))` becomes `a.client.decodeResponse(&localVarReturnValue, localVarBody, localVarHTTPResponse)`. The 3.0.0 tree has 289 sites. Warn if 0 are replaced on an unpatched tree, or if any remain afterwards.
- Idempotency: if `func WithAccept(` is already in `configuration.go`, print success ("already applied") and return `had_issues` unchanged.

- [ ] **Step 1: Write the failing tests** in `go-client-generated/scripts/codegen_fixes_test.go`. Use one helper, `acceptServer(t, status int, contentType, body string) (*httptest.Server, *[]string)`, which records `r.Header.Values("Accept")`. Use the client built as in `TestRevokeTokenSendsFormBody`. Path IDs are valid UUIDs (`"123e4567-e89b-41d4-a716-446655440000"`). Tests:
  - `TestAcceptOverrideYAMLReturnsRawBody`: 200 `application/yaml`, body `"name: x\n"`. `GetDiagramModel(WithAccept(ctx, "application/yaml"), tm, d).Execute()` gives err nil, Accept values `["application/yaml"]`, and `io.ReadAll(resp.Body) == "name: x\n"`.
  - `TestAcceptOverrideGraphMLReturnsRawBody`: 200 `application/graphml+xml`, body `<graphml xmlns="http://graphml.graphdrawing.org/xmlns"><graph id="g"/></graphml>`. Gives err nil and the raw body equal.
  - `TestAcceptOverrideCSVAuditExport`: `AdministrationAPI.ListSystemAuditEntries(WithAccept(ctx, "text/csv")).Execute()` with 200 `text/csv`, body `"id,actor\n1,a\n"`. Gives err nil, Accept `["text/csv"]`, and the raw body equal.
  - `TestAcceptOverrideReplacesDefaultHeader`: `cfg.AddDefaultHeader("Accept", "application/json")` plus `WithAccept(ctx, "application/x-ndjson")` on ListSystemAuditEntries gives Accept values exactly `["application/x-ndjson"]`.
  - `TestAcceptDefaultIsJSONAndDecodes`: no override, 200 `application/json`, a minimal valid `MinimalDiagramModel` JSON (build it from the fields `model_minimal_diagram_model.go` requires). Accept is `["application/json"]` and the returned model has the sent id.
  - `TestAcceptEmptyOverrideIgnored`: `WithAccept(ctx, "")` gives Accept `["application/json"]`.
  - `TestAcceptOverrideJSONStillDecodes`: `WithAccept(ctx, "application/json")` with a JSON 200 decodes the model as in the default test.
  - `TestAcceptOverrideErrorStillDecodes`: `WithAccept(ctx, "application/yaml")` with 406 `application/json`, body `{"error":"not_acceptable","error_description":"x"}`. err is a `*GenericOpenAPIError` whose `Model()` is an `Error` with `Error == "not_acceptable"`.
  - `TestDecodeResponseNilRequest`: `(&APIClient{cfg: NewConfiguration()}).decodeResponse(&m, []byte("{...}"), &http.Response{Header: http.Header{"Content-Type": {"application/json"}}})` does not panic and decodes.

- [ ] **Step 2: Run the tests to verify they fail.** Copy the test file into the client and run:
  `cp go-client-generated/scripts/codegen_fixes_test.go go-client-generated/v3_0_0/ && (cd go-client-generated/v3_0_0 && go test ./... 2>&1 | tail -5)`
  Expected: build failure `undefined: WithAccept`.

- [ ] **Step 3: Implement `patch_accept_override`** in `regenerate_go.py`, following `patch_lenient_decoding`'s style (exact-string anchors, `print_success`/`print_warning`, return `had_issues`). It inserts the Go code described in Interfaces. Doc comment on `WithAccept`: it selects the representation for content-negotiated operations (getDiagramModel, listSystemAuditEntries); for a non-JSON response the returned model is the zero value and the raw body is on `*http.Response.Body`.

- [ ] **Step 4: Regenerate the Go client and run the tests.**
  `python3 regenerate_go.py --spec python-client-generated/v3.0.0/tmi-openapi.json --output-dir go-client-generated/v3_0_0; echo "exit $?"`
  Expected: exit 0. The output includes `Accept override patch: 289 decode sites`. Then `(cd go-client-generated/v3_0_0 && go build ./... && go test ./...)` shows `ok` for both packages. `git status --short go-client-generated/v3_0_0` lists only `configuration.go`, `client.go`, `api_*.go`, `codegen_fixes_test.go`, `README.md` (and `build_output.log` if it changed).

- [ ] **Step 5: Second run is a no-op.** Run `python3 -c` to import `regenerate_go` and call `patch_accept_override(Path("go-client-generated/v3_0_0"), False)`. It returns False and prints "already applied", and `git diff --stat` is unchanged from Step 4.

- [ ] **Step 6: Commit**
  ```bash
  git add regenerate_go.py go-client-generated/scripts/codegen_fixes_test.go go-client-generated/v3_0_0
  git commit -m "feat(go): WithAccept selects the response representation (issue #24)"
  ```

### Task 2: Python and TypeScript regression tests, README recipes

**Files:**
- Modify: `python-client-generated/scripts/test_diagram_fixes.py`: add `@check` functions. Copy to `python-client-generated/v3.0.0/test_diagram_fixes.py`.
- Modify: `typescript-client-generated/scripts/codegen_fixes.test.ts`: add a `describe` block. Copy to `typescript-client-generated/v3.0.0/test/codegen_fixes.test.ts`.
- Modify: `README.md`: add a `## Content negotiation (Accept header)` section after `## Choosing a Client Version`.

**Interfaces:**
- Consumes: Go `tmiclient.WithAccept(ctx, mediaType)` from Task 1 (README only).
- Python: `ThreatModelSubResourcesApi.get_diagram_model_without_preload_content(threat_model_id, diagram_id, _headers=...)`, `AdministrationApi.list_system_audit_entries_without_preload_content(_headers=...)`. Both return a urllib3 response; read `.data`.
- TypeScript: `ThreatModelSubResourcesApi.getDiagramModelRaw(params, initOverrideFn)`, `AdministrationApi.listSystemAuditEntriesRaw(params, initOverrideFn)`, where `initOverrideFn = async ({ init }) => ({ headers: { ...init.headers, Accept: mediaType } })`; read `(await r).raw.text()`.

- [ ] **Step 1: Write the Python checks**, each against a `ThreadingHTTPServer` on `127.0.0.1:0` in a daemon thread. Its handler records the `Accept` and `Authorization` headers and replies with a per-test status, Content-Type and body. Shut it down in `finally`. The client uses `Configuration(host=f"http://127.0.0.1:{port}", access_token="tok")`.
  - `_accept_override_yaml_raw_body`: `_headers={"Accept": "application/yaml"}` sends Accept `application/yaml`, `.data == b"name: x\n"`, and Authorization is `Bearer tok`.
  - `_accept_override_csv_raw_body`: list_system_audit_entries with `text/csv` gives `.data == b"id,actor\n1,a\n"`.
  - `_accept_default_json`: plain `get_diagram_model(tm, d)` without `_headers` sends Accept `application/json`. Reply with the same minimal MinimalDiagramModel JSON as the Go test and assert the decoded id.

- [ ] **Step 2: Write the TypeScript tests** in a `describe("Accept-header content negotiation", ...)` using a stub `fetchApi` in the `Configuration` (no sockets; the generated TypeScript client sets no default Accept), with `new Configuration({ basePath, accessToken: "tok" })`:
  - `"function-form initOverrides selects YAML and keeps Authorization"`: Accept is `application/yaml`, Authorization is `Bearer tok`, and `raw.text()` is `"name: x\n"`.
  - `"audit export as CSV returns the raw body"`: `text/csv` round trip.
  - `"no default Accept"`: no overrides sends no Accept header (the server picks JSON).

- [ ] **Step 3: Copy both test files into their clients and run them.** They should pass without code changes, because these hooks already exist. If one fails, the spec's statement of current behavior is wrong: stop and report.
  - `cp python-client-generated/scripts/test_diagram_fixes.py python-client-generated/v3.0.0/ && (cd python-client-generated/v3.0.0 && uv run python3 test_diagram_fixes.py | tail -2)` should show `N/N checks passed`.
  - `cp typescript-client-generated/scripts/codegen_fixes.test.ts typescript-client-generated/v3.0.0/test/ && (export NVM_DIR=~/.nvm; . "$NVM_DIR/nvm.sh"; cd typescript-client-generated/v3.0.0 && npm run test --silent 2>&1 | tail -4)` should show all tests passed.

- [ ] **Step 4: Check the tests detect a broken hook.** Temporarily change the Python check's expected Accept to `application/json` and confirm it fails. Do the same for one TS assertion. Revert both.

- [ ] **Step 5: Write the README section.** It has one recipe per language for both operations (the shapes in the spec), a table of the media types per operation (from the spec's Intent), and three notes. First, in Go, a non-JSON response leaves the returned model at its zero value and the body is read from `resp.Body`. Second, in Python, the deserializing `get_diagram_model()` raises for non-JSON, so use `_without_preload_content`. Third, in TypeScript, pass a function as `initOverrides`, because an object replaces all headers including `Authorization`. Check every name against the generated code: `rg -n 'func WithAccept|def get_diagram_model_without_preload_content|async listSystemAuditEntriesRaw' go-client-generated/v3_0_0 python-client-generated/v3.0.0/tmi_client typescript-client-generated/v3.0.0/src`.

- [ ] **Step 6: Run the done gate.** `export NVM_DIR=~/.nvm; . "$NVM_DIR/nvm.sh"; bash done_gate.sh > "$SCRATCH/gate.log" 2>&1; tail -1 "$SCRATCH/gate.log"` (SCRATCH = any temp dir outside the repo)` should print `done_gate: all checks passed`.

- [ ] **Step 7: Commit**
  ```bash
  git add python-client-generated/scripts/test_diagram_fixes.py python-client-generated/v3.0.0/test_diagram_fixes.py \
    typescript-client-generated/scripts/codegen_fixes.test.ts typescript-client-generated/v3.0.0/test/codegen_fixes.test.ts README.md
  git commit -m "test,docs: Accept-header recipes and regression tests for Python and TypeScript (issue #24)"
  ```
