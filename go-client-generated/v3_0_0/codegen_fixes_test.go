// Regression tests for the codegen patches in regenerate_go.py. Copied into
// each generated client root on regeneration; edit the copy in scripts/.
package tmiclient

import (
	"context"
	"encoding/json"
	"go/ast"
	"go/parser"
	"go/token"
	"io"
	"net/http"
	"net/http/httptest"
	"os"
	"reflect"
	"strconv"
	"strings"
	"sync"
	"testing"
)

const nodeID = "11111111-1111-4111-8111-111111111111"
const edgeID = "22222222-2222-4222-8222-222222222222"

const nodeJSON = `{"id":"` + nodeID + `","shape":"process","x":100,"y":100,"width":120,"height":60}`
const edgeJSON = `{"id":"` + edgeID + `","shape":"flow","source":{"cell":"` + nodeID + `"},"target":{"cell":"` + nodeID + `"}}`
const cellsJSON = `"cells":[` + nodeJSON + `,` + edgeJSON + `]`
const diagramJSON = `{"id":"33333333-3333-4333-8333-333333333333","name":"d","type":"DFD-1.0.0",` +
	`"created_at":"2026-01-01T00:00:00Z","modified_at":"2026-01-01T00:00:00Z",` + cellsJSON + `}`

// patch_form_content_type: RevokeToken must send its form params as a form body.
func TestRevokeTokenSendsFormBody(t *testing.T) {
	var gotType, gotBody string
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		gotType = r.Header.Get("Content-Type")
		b, _ := io.ReadAll(r.Body)
		gotBody = string(b)
		w.Header().Set("Content-Type", "application/json")
		_, _ = w.Write([]byte(`{}`))
	}))
	defer srv.Close()

	cfg := NewConfiguration()
	cfg.Servers = ServerConfigurations{{URL: srv.URL}}
	if _, _, err := NewAPIClient(cfg).AuthenticationAPI.RevokeToken(context.Background()).Token("tok").Execute(); err != nil {
		t.Fatalf("RevokeToken: %v", err)
	}
	if gotType != "application/x-www-form-urlencoded" || gotBody != "token=tok" {
		t.Fatalf("got Content-Type %q body %q", gotType, gotBody)
	}
}

// Diagram and cell models must decode. Before API 2.0.0 these embedded other
// models and needed patch_embedded_model_unmarshal; the check stays as a guard.
func TestEmbeddedModelsUnmarshal(t *testing.T) {
	cases := map[string]struct {
		v    interface{}
		data string
	}{
		"DfdDiagram":      {&DfdDiagram{}, diagramJSON},
		"DfdDiagramInput": {&DfdDiagramInput{}, `{"name":"d","type":"DFD-1.0.0",` + cellsJSON + `}`},
		"Node":            {&Node{}, nodeJSON},
		"Edge":            {&Edge{}, edgeJSON},
	}
	for name, c := range cases {
		if err := json.Unmarshal([]byte(c.data), c.v); err != nil {
			t.Errorf("%s: %v", name, err)
		}
	}

	var d DfdDiagram
	if err := json.Unmarshal([]byte(diagramJSON), &d); err != nil {
		t.Fatal(err)
	}
	if d.GetType() != "DFD-1.0.0" || d.Name != "d" || len(d.Cells) != 2 {
		t.Fatalf("decoded wrong: type=%q name=%q cells=%d", d.GetType(), d.Name, len(d.Cells))
	}
	// patch_non_string_regex_validators: cells resolve through oneOf
	if d.Cells[0].Node == nil || d.Cells[1].Edge == nil {
		t.Fatalf("cells not resolved to Node/Edge: %+v", d.Cells)
	}
	out, err := json.Marshal(d)
	if err != nil {
		t.Fatal(err)
	}
	var back DfdDiagram
	if err := json.Unmarshal(out, &back); err != nil {
		t.Fatalf("round trip: %v\n%s", err, out)
	}
}

const minimalNodeJSON = `{"id":"` + nodeID + `","shape":"process","children":[],"labels":[],"metadata":{},"security_boundary":false}`
const minimalEdgeJSON = `{"id":"` + edgeID + `","shape":"flow","source":{"cell":"` + nodeID + `"},"target":{"cell":"` + nodeID + `"},"labels":[],"metadata":{}}`

// withExtra adds an unknown top-level property to a JSON object.
func withExtra(obj string) string {
	return obj[:len(obj)-1] + `,"unknown_future_field":{"a":1}}`
}

// patch_lenient_decoding: unknown response fields must not fail decoding, but
// required fields must still be enforced.
func TestUnknownFieldsTolerated(t *testing.T) {
	var team Team
	if err := json.Unmarshal([]byte(`{"name":"t","unknown_future_field":1}`), &team); err != nil {
		t.Fatalf("Team with unknown field: %v", err)
	}
	if team.Name != "t" {
		t.Fatalf("Team name = %q", team.Name)
	}
	if err := json.Unmarshal([]byte(`{"unknown_future_field":1}`), &team); err == nil {
		t.Fatal("Team without required name decoded without error")
	}
}

// patch_lenient_decoding + patch_shape_enum_checks: with unknown fields allowed,
// a cell must still resolve to exactly one of Node/Edge.
func TestCellOneOfWithUnknownFields(t *testing.T) {
	cases := map[string]struct {
		data     string
		wantNode bool
	}{
		"node":       {nodeJSON, true},
		"node+extra": {withExtra(nodeJSON), true},
		"edge":       {edgeJSON, false},
		"edge+extra": {withExtra(edgeJSON), false},
	}
	for name, c := range cases {
		var cell DfdDiagramCellsInner
		if err := json.Unmarshal([]byte(c.data), &cell); err != nil {
			t.Errorf("%s: %v", name, err)
			continue
		}
		if (cell.Node != nil) != c.wantNode || (cell.Edge != nil) == c.wantNode {
			t.Errorf("%s: resolved node=%v edge=%v", name, cell.Node != nil, cell.Edge != nil)
		}
	}
}

func TestMinimalCellOneOfWithUnknownFields(t *testing.T) {
	cases := map[string]struct {
		data     string
		wantNode bool
	}{
		"node":       {minimalNodeJSON, true},
		"node+extra": {withExtra(minimalNodeJSON), true},
		"edge":       {minimalEdgeJSON, false},
		"edge+extra": {withExtra(minimalEdgeJSON), false},
	}
	for name, c := range cases {
		var cell MinimalCell
		if err := json.Unmarshal([]byte(c.data), &cell); err != nil {
			t.Errorf("%s: %v", name, err)
			continue
		}
		if (cell.MinimalNode != nil) != c.wantNode || (cell.MinimalEdge != nil) == c.wantNode {
			t.Errorf("%s: resolved node=%v edge=%v", name, cell.MinimalNode != nil, cell.MinimalEdge != nil)
		}
	}
}

// patch_shape_enum_checks: a shape outside the spec enum is rejected, which is
// what keeps the Node/Edge oneOf disjoint once unknown fields are allowed.
func TestShapeEnumRejected(t *testing.T) {
	swap := func(obj, from, to string) string {
		return strings.Replace(obj, `"shape":"`+from+`"`, `"shape":"`+to+`"`, 1)
	}
	var n Node
	if err := json.Unmarshal([]byte(swap(nodeJSON, "process", "flow")), &n); err == nil {
		t.Error("Node accepted shape flow")
	}
	var e Edge
	if err := json.Unmarshal([]byte(swap(edgeJSON, "flow", "process")), &e); err == nil {
		t.Error("Edge accepted shape process")
	}
	var mn MinimalNode
	if err := json.Unmarshal([]byte(swap(minimalNodeJSON, "process", "flow")), &mn); err == nil {
		t.Error("MinimalNode accepted shape flow")
	}
	var me MinimalEdge
	if err := json.Unmarshal([]byte(swap(minimalEdgeJSON, "flow", "process")), &me); err == nil {
		t.Error("MinimalEdge accepted shape process")
	}
}

// A full diagram response with unknown fields at the top level and on cells.
func TestDiagramWithUnknownFields(t *testing.T) {
	data := `{"id":"33333333-3333-4333-8333-333333333333","name":"d","type":"DFD-1.0.0",` +
		`"created_at":"2026-01-01T00:00:00Z","modified_at":"2026-01-01T00:00:00Z",` +
		`"unknown_future_field":true,"cells":[` + withExtra(nodeJSON) + `,` + withExtra(edgeJSON) + `]}`
	var d DfdDiagram
	if err := json.Unmarshal([]byte(data), &d); err != nil {
		t.Fatal(err)
	}
	if len(d.Cells) != 2 || d.Cells[0].Node == nil || d.Cells[1].Edge == nil {
		t.Fatalf("cells not resolved: %+v", d.Cells)
	}
}

// wellFormedTag reports whether tag is a space-separated list of key:"value"
// pairs, the format reflect.StructTag.Get and go vet's structtag check expect.
func wellFormedTag(tag string) bool {
	for tag != "" {
		tag = strings.TrimLeft(tag, " ")
		if tag == "" {
			break
		}
		i := 0
		for i < len(tag) && tag[i] > ' ' && tag[i] != ':' && tag[i] != '"' && tag[i] != 0x7f {
			i++
		}
		if i == 0 || i+1 >= len(tag) || tag[i] != ':' || tag[i+1] != '"' {
			return false
		}
		tag = tag[i+1:]
		i = 1
		for i < len(tag) && tag[i] != '"' {
			if tag[i] == '\\' {
				i++
			}
			i++
		}
		if i >= len(tag) {
			return false
		}
		if _, err := strconv.Unquote(tag[:i+1]); err != nil {
			return false
		}
		tag = tag[i+1:]
		if tag != "" && tag[0] != ' ' {
			return false
		}
	}
	return true
}

func TestWellFormedTag(t *testing.T) {
	for tag, want := range map[string]bool{
		`json:"name,omitempty"`:                      true,
		`json:"name" validate:"regexp=^[^<>\"'&]*$"`: true,
		`json:"name,omitempty"'&]*$"`:                false,
		`json:"name"validate:"x"`:                    false,
		`json:"unterminated`:                         false,
		``:                                           true,
	} {
		if got := wellFormedTag(tag); got != want {
			t.Errorf("wellFormedTag(%q) = %v, want %v", tag, got, want)
		}
	}
}

// patch_non_string_regex_validators: stripping a validate tag must not leave
// a malformed struct tag behind when the pattern contains an escaped quote
// (RepositoryBase.name: ^[^<>\"'&]*$). go vet's structtag check flags these.
func TestStructTagsWellFormed(t *testing.T) {
	fset := token.NewFileSet()
	pkgs, err := parser.ParseDir(fset, ".", func(fi os.FileInfo) bool {
		return !strings.HasSuffix(fi.Name(), "_test.go")
	}, 0)
	if err != nil {
		t.Fatal(err)
	}
	tags := 0
	for _, pkg := range pkgs {
		for _, f := range pkg.Files {
			ast.Inspect(f, func(n ast.Node) bool {
				field, ok := n.(*ast.Field)
				if !ok || field.Tag == nil {
					return true
				}
				tags++
				tag, err := strconv.Unquote(field.Tag.Value)
				if err != nil || !wellFormedTag(tag) {
					t.Errorf("%s: malformed struct tag %s", fset.Position(field.Pos()), field.Tag.Value)
				}
				return true
			})
		}
	}
	if tags < 100 {
		t.Fatalf("only %d struct tags found; is the test running in the client root?", tags)
	}
	f, _ := reflect.TypeOf(Repository{}).FieldByName("Name")
	if f.Tag != `json:"name,omitempty"` {
		t.Errorf("Repository.Name tag = %q", f.Tag)
	}
}

// ADR 0005: Error.error and OAuthError.error list the server's codes, but the
// server may add codes; an unknown one must still decode.
func TestUnknownErrorCodeDecodes(t *testing.T) {
	data := []byte(`{"error":"some_future_code","error_description":"d"}`)
	var e Error
	if err := json.Unmarshal(data, &e); err != nil || e.Error != "some_future_code" {
		t.Errorf("Error: %v (%q)", err, e.Error)
	}
	var o OAuthError
	if err := json.Unmarshal(data, &o); err != nil || o.Error != "some_future_code" {
		t.Errorf("OAuthError: %v (%q)", err, o.Error)
	}
}

// --- Accept override (WithAccept) ---

const acceptTM = "123e4567-e89b-41d4-a716-446655440000"
const acceptDiagram = "223e4567-e89b-41d4-a716-446655440000"
const minimalModelJSON = `{"id":"` + acceptDiagram + `","name":"n","description":"d","metadata":{},"cells":[],"assets":[]}`

// acceptLog collects Accept header values; the server handler runs on another
// goroutine, so access is locked to keep go test -race clean.
type acceptLog struct {
	mu     sync.Mutex
	values []string
}

func (l *acceptLog) add(v []string) {
	l.mu.Lock()
	defer l.mu.Unlock()
	l.values = append(l.values, v...)
}

func (l *acceptLog) get() []string {
	l.mu.Lock()
	defer l.mu.Unlock()
	return append([]string(nil), l.values...)
}

// acceptServer answers every request with the given status, Content-Type and
// body, and records the Accept header values of each request.
func acceptServer(t *testing.T, status int, contentType, body string) (*httptest.Server, *acceptLog) {
	t.Helper()
	accepts := &acceptLog{}
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		accepts.add(r.Header.Values("Accept"))
		w.Header().Set("Content-Type", contentType)
		w.WriteHeader(status)
		_, _ = w.Write([]byte(body))
	}))
	t.Cleanup(srv.Close)
	return srv, accepts
}

func acceptClient(srvURL string) (*APIClient, *Configuration) {
	cfg := NewConfiguration()
	cfg.Servers = ServerConfigurations{{URL: srvURL}}
	return NewAPIClient(cfg), cfg
}

func checkAccept(t *testing.T, log *acceptLog, want ...string) {
	t.Helper()
	if got := log.get(); !reflect.DeepEqual(got, want) {
		t.Fatalf("Accept values = %q, want %q", got, want)
	}
}

func checkRawBody(t *testing.T, resp *http.Response, want string) {
	t.Helper()
	b, err := io.ReadAll(resp.Body)
	if err != nil {
		t.Fatalf("read body: %v", err)
	}
	if string(b) != want {
		t.Fatalf("body = %q, want %q", b, want)
	}
}

func TestAcceptOverrideYAMLReturnsRawBody(t *testing.T) {
	srv, accepts := acceptServer(t, 200, "application/yaml", "name: x\n")
	client, _ := acceptClient(srv.URL)
	ctx := WithAccept(context.Background(), "application/yaml")
	_, resp, err := client.ThreatModelSubResourcesAPI.GetDiagramModel(ctx, acceptTM, acceptDiagram).Execute()
	if err != nil {
		t.Fatalf("GetDiagramModel: %v", err)
	}
	checkAccept(t, accepts, "application/yaml")
	checkRawBody(t, resp, "name: x\n")
}

func TestAcceptOverrideGraphMLReturnsRawBody(t *testing.T) {
	// XML-decoding this body would allocate the model and set its Id from <Id>,
	// so a nil model proves the decode was skipped.
	body := `<graphml xmlns="http://graphml.graphdrawing.org/xmlns"><Id>from-xml</Id><graph id="g"/></graphml>`
	srv, accepts := acceptServer(t, 200, "application/graphml+xml", body)
	client, _ := acceptClient(srv.URL)
	ctx := WithAccept(context.Background(), "application/graphml+xml")
	m, resp, err := client.ThreatModelSubResourcesAPI.GetDiagramModel(ctx, acceptTM, acceptDiagram).Execute()
	if err != nil {
		t.Fatalf("GetDiagramModel: %v", err)
	}
	if m != nil {
		t.Fatalf("model was decoded from the raw body: %+v", m)
	}
	checkAccept(t, accepts, "application/graphml+xml")
	checkRawBody(t, resp, body)
}

func TestAcceptOverrideCSVAuditExport(t *testing.T) {
	srv, accepts := acceptServer(t, 200, "text/csv", "id,actor\n1,a\n")
	client, _ := acceptClient(srv.URL)
	ctx := WithAccept(context.Background(), "text/csv")
	_, resp, err := client.AdministrationAPI.ListSystemAuditEntries(ctx).Execute()
	if err != nil {
		t.Fatalf("ListSystemAuditEntries: %v", err)
	}
	checkAccept(t, accepts, "text/csv")
	checkRawBody(t, resp, "id,actor\n1,a\n")
}

func TestAcceptOverrideReplacesDefaultHeader(t *testing.T) {
	srv, accepts := acceptServer(t, 200, "application/x-ndjson", "{}\n")
	client, cfg := acceptClient(srv.URL)
	cfg.AddDefaultHeader("Accept", "application/json")
	ctx := WithAccept(context.Background(), "application/x-ndjson")
	if _, _, err := client.AdministrationAPI.ListSystemAuditEntries(ctx).Execute(); err != nil {
		t.Fatalf("ListSystemAuditEntries: %v", err)
	}
	checkAccept(t, accepts, "application/x-ndjson")
}

func TestAcceptDefaultIsJSONAndDecodes(t *testing.T) {
	srv, accepts := acceptServer(t, 200, "application/json", minimalModelJSON)
	client, _ := acceptClient(srv.URL)
	m, _, err := client.ThreatModelSubResourcesAPI.GetDiagramModel(context.Background(), acceptTM, acceptDiagram).Execute()
	if err != nil {
		t.Fatalf("GetDiagramModel: %v", err)
	}
	checkAccept(t, accepts, "application/json")
	if m.Id != acceptDiagram {
		t.Fatalf("Id = %q, want %q", m.Id, acceptDiagram)
	}
}

func TestAcceptEmptyOverrideIgnored(t *testing.T) {
	srv, accepts := acceptServer(t, 200, "application/json", minimalModelJSON)
	client, _ := acceptClient(srv.URL)
	ctx := WithAccept(context.Background(), "")
	if _, _, err := client.ThreatModelSubResourcesAPI.GetDiagramModel(ctx, acceptTM, acceptDiagram).Execute(); err != nil {
		t.Fatalf("GetDiagramModel: %v", err)
	}
	checkAccept(t, accepts, "application/json")
}

func TestAcceptOverrideJSONStillDecodes(t *testing.T) {
	srv, accepts := acceptServer(t, 200, "application/json", minimalModelJSON)
	client, _ := acceptClient(srv.URL)
	ctx := WithAccept(context.Background(), "application/json")
	m, _, err := client.ThreatModelSubResourcesAPI.GetDiagramModel(ctx, acceptTM, acceptDiagram).Execute()
	if err != nil {
		t.Fatalf("GetDiagramModel: %v", err)
	}
	checkAccept(t, accepts, "application/json")
	if m.Id != acceptDiagram {
		t.Fatalf("Id = %q, want %q", m.Id, acceptDiagram)
	}
}

func TestAcceptOverrideErrorStillDecodes(t *testing.T) {
	srv, _ := acceptServer(t, 406, "application/json", `{"error":"not_acceptable","error_description":"x"}`)
	client, _ := acceptClient(srv.URL)
	ctx := WithAccept(context.Background(), "application/yaml")
	_, _, err := client.ThreatModelSubResourcesAPI.GetDiagramModel(ctx, acceptTM, acceptDiagram).Execute()
	gerr, ok := err.(*GenericOpenAPIError)
	if !ok {
		t.Fatalf("err = %T %v, want *GenericOpenAPIError", err, err)
	}
	model, ok := gerr.Model().(Error)
	if !ok || model.Error != "not_acceptable" {
		t.Fatalf("Model() = %#v, want Error{Error: not_acceptable}", gerr.Model())
	}
}

func TestDecodeResponseNilRequest(t *testing.T) {
	var m MinimalDiagramModel
	resp := &http.Response{Header: http.Header{"Content-Type": {"application/json"}}}
	if err := (&APIClient{cfg: NewConfiguration()}).decodeResponse(&m, []byte(minimalModelJSON), resp); err != nil {
		t.Fatalf("decodeResponse: %v", err)
	}
	if m.Id != acceptDiagram {
		t.Fatalf("Id = %q, want %q", m.Id, acceptDiagram)
	}
}

// Without an override a non-JSON 2xx still goes through decode and fails as
// it always did; only WithAccept opts in to skipping the decode.
func TestNonJSONWithoutOverrideStillErrors(t *testing.T) {
	srv, _ := acceptServer(t, 200, "application/yaml", "name: x\n")
	client, _ := acceptClient(srv.URL)
	_, _, err := client.ThreatModelSubResourcesAPI.GetDiagramModel(context.Background(), acceptTM, acceptDiagram).Execute()
	if err == nil {
		t.Fatal("non-JSON response without WithAccept returned a nil error")
	}
}

// A nil context must behave as before the patch: no override, no panic.
func TestNilContextNoOverride(t *testing.T) {
	srv, accepts := acceptServer(t, 200, "application/json", minimalModelJSON)
	client, _ := acceptClient(srv.URL)
	//nolint:staticcheck // a nil context is deliberate
	m, _, err := client.ThreatModelSubResourcesAPI.GetDiagramModel(nil, acceptTM, acceptDiagram).Execute()
	if err != nil {
		t.Fatalf("GetDiagramModel(nil ctx): %v", err)
	}
	checkAccept(t, accepts, "application/json")
	if m.Id != acceptDiagram {
		t.Fatalf("Id = %q, want %q", m.Id, acceptDiagram)
	}
}
