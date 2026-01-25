#!/usr/bin/env python3
"""
Integration test to verify all 6 OpenAPI fixes are working correctly.

This test validates:
1. DfdDiagram can be instantiated with type parameter
2. DfdDiagramInput can be instantiated with type parameter
3. Type parameter is preserved after construction
4. to_dict() serialization works correctly
5. Inheritance from Base classes works properly
"""

import sys

def test_dfd_diagram_instantiation():
    """Test 1: DfdDiagram can be instantiated with type parameter"""
    print("Test 1: DfdDiagram instantiation...")
    from tmi_client.models.dfd_diagram import DfdDiagram

    diagram = DfdDiagram(
        type="DFD-1.0.0",
        cells=[],
        name="Test Diagram",
        id="test-id",
        created_at="2025-01-01T00:00:00Z",
        modified_at="2025-01-01T00:00:00Z"
    )

    assert diagram is not None, "Failed to instantiate DfdDiagram"
    assert diagram.type == "DFD-1.0.0", f"Type not preserved: {diagram.type}"
    assert diagram.name == "Test Diagram", "Name not set correctly"
    print("✓ DfdDiagram instantiation successful")


def test_dfd_diagram_input_instantiation():
    """Test 2: DfdDiagramInput can be instantiated with type parameter"""
    print("\nTest 2: DfdDiagramInput instantiation...")
    from tmi_client.models.dfd_diagram_input import DfdDiagramInput

    diagram_input = DfdDiagramInput(
        type="DFD-1.0.0",
        cells=[],
        name="Test Diagram Input"
    )

    assert diagram_input is not None, "Failed to instantiate DfdDiagramInput"
    assert diagram_input.type == "DFD-1.0.0", f"Type not preserved: {diagram_input.type}"
    assert diagram_input.name == "Test Diagram Input", "Name not set correctly"
    print("✓ DfdDiagramInput instantiation successful")


def test_type_parameter_preservation():
    """Test 3: Type parameter is preserved after construction"""
    print("\nTest 3: Type parameter preservation...")
    from tmi_client.models.dfd_diagram import DfdDiagram
    from tmi_client.models.dfd_diagram_input import DfdDiagramInput

    # Test DfdDiagram - id, created_at, modified_at are required
    diagram = DfdDiagram(
        type="DFD-1.0.0",
        cells=[],
        name="Test",
        id="test-id",
        created_at="2025-01-01T00:00:00Z",
        modified_at="2025-01-01T00:00:00Z"
    )
    assert diagram.type == "DFD-1.0.0", "DfdDiagram type was overwritten"

    # Test DfdDiagramInput - no readOnly fields required
    diagram_input = DfdDiagramInput(type="DFD-1.0.0", cells=[], name="Test")
    assert diagram_input.type == "DFD-1.0.0", "DfdDiagramInput type was overwritten"

    print("✓ Type parameter preserved in both classes")


def test_serialization():
    """Test 4: to_dict() serialization works correctly"""
    print("\nTest 4: Serialization...")
    from tmi_client.models.dfd_diagram import DfdDiagram
    from tmi_client.models.dfd_diagram_input import DfdDiagramInput

    # Test DfdDiagram serialization
    diagram = DfdDiagram(
        type="DFD-1.0.0",
        cells=[{"id": "node1", "shape": "process"}],
        name="Serialization Test",
        id="test-id",
        created_at="2025-01-01T00:00:00Z",
        modified_at="2025-01-01T00:00:00Z"
    )

    diagram_dict = diagram.to_dict()
    assert diagram_dict['type'] == "DFD-1.0.0", "Type not in serialized dict"
    assert diagram_dict['name'] == "Serialization Test", "Name not in serialized dict"
    assert len(diagram_dict['cells']) == 1, "Cells not serialized correctly"

    # Test DfdDiagramInput serialization
    diagram_input = DfdDiagramInput(
        type="DFD-1.0.0",
        cells=[{"id": "node1", "shape": "process"}],
        name="Input Serialization Test"
    )

    input_dict = diagram_input.to_dict()
    assert input_dict['type'] == "DFD-1.0.0", "Type not in input serialized dict"
    assert input_dict['name'] == "Input Serialization Test", "Name not in input dict"

    print("✓ Serialization working correctly")


def test_inheritance():
    """Test 5: Inheritance from Base classes works properly"""
    print("\nTest 5: Inheritance...")
    from tmi_client.models.dfd_diagram import DfdDiagram
    from tmi_client.models.dfd_diagram_input import DfdDiagramInput
    from tmi_client.models.base_diagram import BaseDiagram
    from tmi_client.models.base_diagram_input import BaseDiagramInput

    # Test DfdDiagram inheritance - with required fields
    diagram = DfdDiagram(
        type="DFD-1.0.0",
        cells=[],
        name="Test",
        id="test-id",
        created_at="2025-01-01T00:00:00Z",
        modified_at="2025-01-01T00:00:00Z"
    )
    assert isinstance(diagram, BaseDiagram), "DfdDiagram not instance of BaseDiagram"
    assert isinstance(diagram, DfdDiagram), "DfdDiagram not instance of itself"

    # Test DfdDiagramInput inheritance
    diagram_input = DfdDiagramInput(type="DFD-1.0.0", cells=[], name="Test")
    assert isinstance(diagram_input, BaseDiagramInput), "DfdDiagramInput not instance of BaseDiagramInput"
    assert isinstance(diagram_input, DfdDiagramInput), "DfdDiagramInput not instance of itself"

    print("✓ Inheritance working correctly")


def test_cell_schemas():
    """Test 6: Cell schemas exist and can be imported"""
    print("\nTest 6: Cell schemas...")

    # Test that cell schema classes can be imported (proving they exist)
    try:
        from tmi_client.models.edge import Edge
        from tmi_client.models.node import Node
        from tmi_client.models.cell import Cell
        assert Edge is not None, "Edge class not found"
        assert Node is not None, "Node class not found"
        assert Cell is not None, "Cell class not found"
    except Exception as e:
        raise AssertionError(f"Failed to import cell classes: {e}")

    # Test Edge creation with required fields
    # Note: Edge shape must be "flow" per the OpenAPI spec
    edge = Edge(
        id="edge1",
        shape="flow",
        source={"cell": "node1"},
        target={"cell": "node2"}
    )
    assert edge.id == "edge1", "Edge id not set correctly"
    assert edge.shape == "flow", "Edge shape not set correctly"

    print("✓ Cell schemas exist and work correctly")


def test_webhooks():
    """Test 7: New webhook schemas exist and can be instantiated"""
    print("\nTest 7: Webhook schemas...")
    from tmi_client.models.webhook_subscription import WebhookSubscription
    from tmi_client.models.webhook_subscription_input import WebhookSubscriptionInput
    from tmi_client.models.webhook_delivery import WebhookDelivery

    # Test WebhookSubscriptionInput with all required fields
    webhook_input = WebhookSubscriptionInput(
        name="Test Webhook",
        url="https://example.com/webhook",
        events=["threat_model.created", "diagram.updated"]
    )
    assert webhook_input is not None, "Failed to create WebhookSubscriptionInput"
    assert webhook_input.url == "https://example.com/webhook", "Webhook URL not set"
    assert webhook_input.name == "Test Webhook", "Webhook name not set"

    print("✓ Webhook schemas working correctly")


def main():
    """Run all tests"""
    print("=" * 60)
    print("TMI Python Client Integration Tests")
    print("=" * 60)

    tests = [
        test_dfd_diagram_instantiation,
        test_dfd_diagram_input_instantiation,
        test_type_parameter_preservation,
        test_serialization,
        test_inheritance,
        test_cell_schemas,
        test_webhooks,
    ]

    failed = []

    for test in tests:
        try:
            test()
        except Exception as e:
            print(f"✗ {test.__name__} FAILED: {e}")
            failed.append((test.__name__, e))

    print("\n" + "=" * 60)
    if failed:
        print(f"FAILED: {len(failed)} out of {len(tests)} tests failed")
        for name, error in failed:
            print(f"  - {name}: {error}")
        sys.exit(1)
    else:
        print(f"SUCCESS: All {len(tests)} tests passed!")
        print("=" * 60)
        sys.exit(0)


if __name__ == "__main__":
    main()
