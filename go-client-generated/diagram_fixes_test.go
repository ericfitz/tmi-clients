package tmiclient

import (
	"testing"
)

// TestDiagramInputSchemas verifies that input schemas exist for diagram operations
func TestDiagramInputSchemas(t *testing.T) {
	t.Run("DfdDiagramInput exists", func(t *testing.T) {
		// After regeneration, this type should exist
		var input DfdDiagramInput
		input.Type = stringPtr("DFD-1.0.0")
		input.Name = stringPtr("Test Diagram")
		
		if input.Type == nil || *input.Type != "DFD-1.0.0" {
			t.Error("DfdDiagramInput.Type should be set")
		}
	})
	
	t.Run("BaseDiagramInput exists", func(t *testing.T) {
		// After regeneration, this type should exist
		var input BaseDiagramInput
		input.Type = stringPtr("DFD-1.0.0")
		input.Name = stringPtr("Test")
		
		if input.Type == nil {
			t.Error("BaseDiagramInput.Type should be settable")
		}
	})
}

// TestWebhookModels verifies that webhook models exist
func TestWebhookModels(t *testing.T) {
	t.Run("WebhookSubscription exists", func(t *testing.T) {
		var sub WebhookSubscription
		sub.Url = stringPtr("https://example.com/webhook")
		sub.Events = []string{"threat_model.created"}
		
		if sub.Url == nil {
			t.Error("WebhookSubscription.Url should be settable")
		}
	})
	
	t.Run("WebhookSubscriptionInput exists", func(t *testing.T) {
		var input WebhookSubscriptionInput
		input.Url = stringPtr("https://example.com/webhook")
		input.Events = []string{"threat_model.created"}
		input.Active = boolPtr(true)
		
		if input.Url == nil || *input.Url != "https://example.com/webhook" {
			t.Error("WebhookSubscriptionInput should work")
		}
	})
}

// TestDiagramCellTypes verifies cell types work correctly
func TestDiagramCellTypes(t *testing.T) {
	t.Run("Node cell creation", func(t *testing.T) {
		node := Node{
			Id:     stringPtr("node-1"),
			Shape:  stringPtr("process"),
			X:      float64Ptr(100),
			Y:      float64Ptr(100),
			Width:  float64Ptr(120),
			Height: float64Ptr(60),
		}
		
		if node.Id == nil || *node.Id != "node-1" {
			t.Error("Node ID should be set")
		}
		if node.Shape == nil || *node.Shape != "process" {
			t.Error("Node shape should be set")
		}
	})
	
	t.Run("Edge cell creation", func(t *testing.T) {
		edge := Edge{
			Id:    stringPtr("edge-1"),
			Shape: stringPtr("edge"),
			Source: &EdgeTerminal{
				Cell: stringPtr("node-1"),
			},
			Target: &EdgeTerminal{
				Cell: stringPtr("node-2"),
			},
		}
		
		if edge.Source == nil || edge.Source.Cell == nil {
			t.Error("Edge source should be set")
		}
		if edge.Target == nil || edge.Target.Cell == nil {
			t.Error("Edge target should be set")
		}
	})
}

// Helper functions for tests
func stringPtr(s string) *string {
	return &s
}

func boolPtr(b bool) *bool {
	return &b
}

func float64Ptr(f float64) *float64 {
	return &f
}
