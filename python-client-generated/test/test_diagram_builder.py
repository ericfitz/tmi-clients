# coding: utf-8

"""
    TMI (Threat Modeling Improved) API - DfdDiagramBuilder Tests

    Tests for the DFD diagram builder helper class.
"""

import unittest
import uuid

from tmi_client.helpers import DfdDiagramBuilder
from tmi_client.models.dfd_diagram import DfdDiagram
from tmi_client.models.node import Node
from tmi_client.models.edge import Edge


class TestDfdDiagramBuilder(unittest.TestCase):
    """DfdDiagramBuilder unit tests"""

    def setUp(self):
        """Set up test fixtures"""
        self.builder = DfdDiagramBuilder(name="Test Diagram")

    def tearDown(self):
        """Clean up after tests"""
        pass

    def test_init(self):
        """Test DfdDiagramBuilder initialization"""
        builder = DfdDiagramBuilder(name="My Diagram")
        self.assertEqual(builder.name, "My Diagram")
        self.assertEqual(len(builder.cells), 0)
        self.assertEqual(len(builder._node_map), 0)

    def test_init_default_name(self):
        """Test DfdDiagramBuilder with default name"""
        builder = DfdDiagramBuilder()
        self.assertEqual(builder.name, "Untitled Diagram")

    def test_add_node_basic(self):
        """Test adding a basic node"""
        node_id = self.builder.add_node("Test Node", shape="process")

        # Check node ID is a valid UUID
        self.assertIsNotNone(node_id)
        uuid.UUID(node_id)  # Should not raise

        # Check node was added to cells
        self.assertEqual(len(self.builder.cells), 1)
        self.assertIsInstance(self.builder.cells[0], Node)

        # Check node properties
        node = self.builder.cells[0]
        self.assertEqual(node.id, node_id)
        self.assertEqual(node.shape, "process")
        self.assertEqual(node.x, 0)
        self.assertEqual(node.y, 0)
        self.assertEqual(node.width, 120)  # Default width for process
        self.assertEqual(node.height, 60)  # Default height for process

    def test_add_node_with_position(self):
        """Test adding a node with custom position"""
        node_id = self.builder.add_node(
            "Positioned Node",
            shape="process",
            position=(100, 200)
        )

        node = self.builder.cells[0]
        self.assertEqual(node.x, 100)
        self.assertEqual(node.y, 200)

    def test_add_node_with_size(self):
        """Test adding a node with custom size"""
        node_id = self.builder.add_node(
            "Sized Node",
            shape="process",
            size=(150, 80)
        )

        node = self.builder.cells[0]
        self.assertEqual(node.width, 150)
        self.assertEqual(node.height, 80)

    def test_add_node_with_custom_id(self):
        """Test adding a node with custom ID"""
        custom_id = str(uuid.uuid4())
        node_id = self.builder.add_node("Node", node_id=custom_id)

        self.assertEqual(node_id, custom_id)
        self.assertEqual(self.builder.cells[0].id, custom_id)

    def test_add_node_with_parent(self):
        """Test adding a child node with parent"""
        parent_id = self.builder.add_node("Parent", shape="security-boundary")
        child_id = self.builder.add_node("Child", shape="process", parent_id=parent_id)

        child = self.builder.cells[1]
        self.assertEqual(child.parent, parent_id)

    def test_add_node_with_metadata(self):
        """Test adding a node with metadata"""
        node_id = self.builder.add_node(
            "Node with Metadata",
            metadata={"env": "production", "region": "us-east-1"}
        )

        node = self.builder.cells[0]
        self.assertIsNotNone(node.data)
        self.assertIsNotNone(node.data.metadata)
        self.assertEqual(len(node.data.metadata), 2)

    def test_add_node_shapes(self):
        """Test adding nodes with different shapes"""
        shapes = ["actor", "process", "store", "security-boundary", "text-box"]

        for shape in shapes:
            builder = DfdDiagramBuilder()
            node_id = builder.add_node(f"{shape} node", shape=shape)
            node = builder.cells[0]
            self.assertEqual(node.shape, shape)

    def test_add_node_process_has_ports(self):
        """Test that process nodes get ports automatically"""
        node_id = self.builder.add_node("Process", shape="process")
        node = self.builder.cells[0]

        self.assertIsNotNone(node.ports)
        self.assertIn("items", node.ports)
        self.assertEqual(len(node.ports["items"]), 2)

    def test_add_node_styling(self):
        """Test node styling"""
        custom_style = {"fill": "#FF0000", "stroke": "#000000"}
        node_id = self.builder.add_node("Styled Node", style=custom_style)

        node = self.builder.cells[0]
        self.assertIsNotNone(node.attrs)
        self.assertEqual(node.attrs["body"]["fill"], "#FF0000")
        self.assertEqual(node.attrs["body"]["stroke"], "#000000")

    def test_add_edge_basic(self):
        """Test adding a basic edge"""
        source_id = self.builder.add_node("Source", shape="process")
        target_id = self.builder.add_node("Target", shape="process")
        edge_id = self.builder.add_edge(source_id, target_id)

        # Check edge was added
        self.assertEqual(len(self.builder.cells), 3)  # 2 nodes + 1 edge
        self.assertIsInstance(self.builder.cells[2], Edge)

        # Check edge properties
        edge = self.builder.cells[2]
        self.assertEqual(edge.shape, "edge")
        self.assertEqual(edge.source["cell"], source_id)
        self.assertEqual(edge.target["cell"], target_id)

    def test_add_edge_with_label(self):
        """Test adding an edge with label"""
        source_id = self.builder.add_node("Source", shape="process")
        target_id = self.builder.add_node("Target", shape="process")
        edge_id = self.builder.add_edge(source_id, target_id, label="HTTP Request")

        edge = self.builder.cells[2]
        self.assertIsNotNone(edge.labels)
        self.assertEqual(len(edge.labels), 1)

    def test_add_edge_with_protocol_and_port(self):
        """Test adding an edge with protocol and port"""
        source_id = self.builder.add_node("Source", shape="process")
        target_id = self.builder.add_node("Target", shape="process")
        edge_id = self.builder.add_edge(
            source_id, target_id,
            label="Database Query",
            protocol="TCP",
            port=5432
        )

        edge = self.builder.cells[2]
        self.assertIsNotNone(edge.labels)
        # Label should include text and protocol info

    def test_add_edge_bidirectional(self):
        """Test adding a bidirectional edge"""
        source_id = self.builder.add_node("Node1", shape="process")
        target_id = self.builder.add_node("Node2", shape="process")
        edge_id = self.builder.add_edge(source_id, target_id, bidirectional=True)

        edge = self.builder.cells[2]
        # Should have both source and target markers
        self.assertIn("sourceMarker", edge.attrs["line"])
        self.assertIn("targetMarker", edge.attrs["line"])

    def test_add_edge_invalid_source(self):
        """Test adding edge with invalid source node"""
        target_id = self.builder.add_node("Target", shape="process")

        with self.assertRaises(ValueError) as context:
            self.builder.add_edge("invalid-id", target_id)

        self.assertIn("Source node", str(context.exception))

    def test_add_edge_invalid_target(self):
        """Test adding edge with invalid target node"""
        source_id = self.builder.add_node("Source", shape="process")

        with self.assertRaises(ValueError) as context:
            self.builder.add_edge(source_id, "invalid-id")

        self.assertIn("Target node", str(context.exception))

    def test_add_security_boundary(self):
        """Test adding a security boundary"""
        boundary_id = self.builder.add_security_boundary(
            "Production VPC",
            position=(50, 50),
            size=(500, 400)
        )

        # Check boundary was added
        self.assertEqual(len(self.builder.cells), 1)
        boundary = self.builder.cells[0]

        # Check it's a security-boundary node
        self.assertEqual(boundary.shape, "security-boundary")
        self.assertEqual(boundary.x, 50)
        self.assertEqual(boundary.y, 50)
        self.assertEqual(boundary.width, 500)
        self.assertEqual(boundary.height, 400)

        # Should have lower z_index to appear behind other elements
        self.assertEqual(boundary.z_index, 1)

    def test_build_empty_diagram(self):
        """Test building an empty diagram"""
        diagram = self.builder.build(validate=False)

        self.assertIsInstance(diagram, DfdDiagram)
        self.assertEqual(diagram.type, "DFD-1.0.0")
        self.assertEqual(diagram.name, "Test Diagram")
        self.assertEqual(len(diagram.cells), 0)

    def test_build_diagram_with_nodes(self):
        """Test building a diagram with nodes"""
        self.builder.add_node("Node 1", shape="process")
        self.builder.add_node("Node 2", shape="store")

        diagram = self.builder.build(validate=False)

        self.assertIsInstance(diagram, DfdDiagram)
        self.assertEqual(len(diagram.cells), 2)

    def test_build_complete_diagram(self):
        """Test building a complete diagram with nodes and edges"""
        node1 = self.builder.add_node("Web Server", shape="process", position=(100, 100))
        node2 = self.builder.add_node("Database", shape="store", position=(300, 100))
        self.builder.add_edge(node1, node2, label="SQL", protocol="TCP", port=5432)

        diagram = self.builder.build(validate=False)

        self.assertIsInstance(diagram, DfdDiagram)
        self.assertEqual(len(diagram.cells), 3)  # 2 nodes + 1 edge

    def test_build_with_validation_valid(self):
        """Test building with validation on valid diagram"""
        node1 = self.builder.add_node("Node 1", shape="process", position=(100, 100))
        node2 = self.builder.add_node("Node 2", shape="store", position=(300, 100))
        self.builder.add_edge(node1, node2)

        # Should not raise
        diagram = self.builder.build(validate=True)
        self.assertIsInstance(diagram, DfdDiagram)

    def test_complex_diagram(self):
        """Test building a complex diagram with boundaries and nested nodes"""
        # Add a boundary
        vpc = self.builder.add_security_boundary(
            "VPC",
            position=(50, 50),
            size=(600, 400)
        )

        # Add nodes inside the boundary
        lb = self.builder.add_node(
            "Load Balancer",
            shape="process",
            position=(100, 100),
            parent_id=vpc
        )
        web = self.builder.add_node(
            "Web Server",
            shape="process",
            position=(300, 100),
            parent_id=vpc
        )
        db = self.builder.add_node(
            "Database",
            shape="store",
            position=(500, 100),
            parent_id=vpc
        )

        # Connect them
        self.builder.add_edge(lb, web, label="HTTP", port=80)
        self.builder.add_edge(web, db, label="SQL", port=5432)

        # Add external actor
        user = self.builder.add_node("User", shape="actor", position=(100, 500))
        self.builder.add_edge(user, lb, label="HTTPS", port=443)

        diagram = self.builder.build(validate=False)

        # Should have 4 nodes (1 boundary + 3 inside + 1 actor) + 3 edges
        self.assertEqual(len(diagram.cells), 8)


if __name__ == '__main__':
    unittest.main()
