// Regression tests for the codegen patches in regenerate_go.py. Copied into
// each generated client root on regeneration; edit the copy in scripts/.
package tmiclient

import (
	"context"
	"encoding/json"
	"io"
	"net/http"
	"net/http/httptest"
	"strings"
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
