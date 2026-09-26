// Regression tests for the codegen patches in regenerate_go.py. Copied into
// each generated client root on regeneration; edit the copy in scripts/.
package tmiclient

import (
	"context"
	"encoding/json"
	"io"
	"net/http"
	"net/http/httptest"
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

// patch_embedded_model_unmarshal: models embedding another model must decode.
func TestEmbeddedModelsUnmarshal(t *testing.T) {
	cases := map[string]struct {
		v    interface{}
		data string
	}{
		"DfdDiagram":      {&DfdDiagram{}, diagramJSON},
		"Diagram":         {&Diagram{}, diagramJSON},
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
	// patch_non_string_regex_validators + shadowed-field tags: cells resolve through oneOf
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
