# coding: utf-8

"""
    TMI (Threat Modeling Improved) API - Validator Tests

    Tests for cell and diagram validation functions.
"""

import unittest

from tmi_client.helpers import validate_cell, validate_diagram_cells


class TestValidators(unittest.TestCase):
    """Validator function unit tests"""

    def setUp(self):
        """Set up test fixtures"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        pass

    def test_validate_cell_valid_node(self):
        """Test validating a valid node"""
        cell = {
            "id": "node-1",
            "shape": "process",
            "x": 100,
            "y": 200,
            "width": 120,
            "height": 60
        }

        errors = validate_cell(cell)
        self.assertEqual(len(errors), 0)

    def test_validate_cell_valid_edge(self):
        """Test validating a valid edge"""
        cell = {
            "id": "edge-1",
            "shape": "edge",
            "source": {"cell": "node-1"},
            "target": {"cell": "node-2"}
        }

        errors = validate_cell(cell)
        self.assertEqual(len(errors), 0)

    def test_validate_cell_missing_id(self):
        """Test validating a cell with missing ID"""
        cell = {
            "shape": "process",
            "x": 100,
            "y": 200,
            "width": 120,
            "height": 60
        }

        errors = validate_cell(cell)
        self.assertGreater(len(errors), 0)
        self.assertTrue(any("id" in error.lower() for error in errors))

    def test_validate_cell_missing_shape(self):
        """Test validating a cell with missing shape"""
        cell = {
            "id": "node-1",
            "x": 100,
            "y": 200,
            "width": 120,
            "height": 60
        }

        errors = validate_cell(cell)
        self.assertGreater(len(errors), 0)
        self.assertTrue(any("shape" in error.lower() for error in errors))

    def test_validate_cell_node_missing_position(self):
        """Test validating a node with missing position"""
        cell = {
            "id": "node-1",
            "shape": "process",
            "width": 120,
            "height": 60
        }

        errors = validate_cell(cell)
        self.assertGreater(len(errors), 0)
        # Should complain about missing x/y or position

    def test_validate_cell_node_missing_size(self):
        """Test validating a node with missing size"""
        cell = {
            "id": "node-1",
            "shape": "process",
            "x": 100,
            "y": 200
        }

        errors = validate_cell(cell)
        self.assertGreater(len(errors), 0)
        # Should complain about missing width/height or size

    def test_validate_cell_node_too_small(self):
        """Test validating a node that's too small"""
        cell = {
            "id": "node-1",
            "shape": "process",
            "x": 100,
            "y": 200,
            "width": 20,  # Too small
            "height": 10   # Too small
        }

        errors = validate_cell(cell)
        self.assertGreater(len(errors), 0)
        self.assertTrue(any("width" in error.lower() for error in errors))
        self.assertTrue(any("height" in error.lower() for error in errors))

    def test_validate_cell_edge_missing_source(self):
        """Test validating an edge with missing source"""
        cell = {
            "id": "edge-1",
            "shape": "edge",
            "target": {"cell": "node-2"}
        }

        errors = validate_cell(cell)
        self.assertGreater(len(errors), 0)
        self.assertTrue(any("source" in error.lower() for error in errors))

    def test_validate_cell_edge_missing_target(self):
        """Test validating an edge with missing target"""
        cell = {
            "id": "edge-1",
            "shape": "edge",
            "source": {"cell": "node-1"}
        }

        errors = validate_cell(cell)
        self.assertGreater(len(errors), 0)
        self.assertTrue(any("target" in error.lower() for error in errors))

    def test_validate_cell_edge_invalid_source(self):
        """Test validating an edge with invalid source structure"""
        cell = {
            "id": "edge-1",
            "shape": "edge",
            "source": {"port": "out"},  # Missing 'cell'
            "target": {"cell": "node-2"}
        }

        errors = validate_cell(cell)
        self.assertGreater(len(errors), 0)
        self.assertTrue(any("source" in error.lower() for error in errors))

    def test_validate_cell_edge_invalid_target(self):
        """Test validating an edge with invalid target structure"""
        cell = {
            "id": "edge-1",
            "shape": "edge",
            "source": {"cell": "node-1"},
            "target": {"port": "in"}  # Missing 'cell'
        }

        errors = validate_cell(cell)
        self.assertGreater(len(errors), 0)
        self.assertTrue(any("target" in error.lower() for error in errors))

    def test_validate_cell_invalid_shape(self):
        """Test validating a node with invalid shape"""
        cell = {
            "id": "node-1",
            "shape": "invalid-shape",
            "x": 100,
            "y": 200,
            "width": 120,
            "height": 60
        }

        errors = validate_cell(cell)
        self.assertGreater(len(errors), 0)
        self.assertTrue(any("shape" in error.lower() for error in errors))

    def test_validate_cell_with_position_object(self):
        """Test validating a node with position/size objects"""
        cell = {
            "id": "node-1",
            "shape": "process",
            "position": {"x": 100, "y": 200},
            "size": {"width": 120, "height": 60}
        }

        errors = validate_cell(cell)
        self.assertEqual(len(errors), 0)

    def test_validate_cell_all_shapes(self):
        """Test validating all valid node shapes"""
        shapes = ["actor", "process", "store", "security-boundary", "text-box"]

        for shape in shapes:
            cell = {
                "id": f"{shape}-1",
                "shape": shape,
                "x": 100,
                "y": 200,
                "width": 120,
                "height": 60
            }

            errors = validate_cell(cell)
            self.assertEqual(len(errors), 0, f"Shape {shape} should be valid")

    def test_validate_diagram_cells_empty(self):
        """Test validating an empty diagram"""
        cells = []

        errors = validate_diagram_cells(cells)
        self.assertEqual(len(errors), 0)

    def test_validate_diagram_cells_valid(self):
        """Test validating a valid diagram"""
        cells = [
            {
                "id": "node-1",
                "shape": "process",
                "x": 100,
                "y": 200,
                "width": 120,
                "height": 60
            },
            {
                "id": "node-2",
                "shape": "store",
                "x": 300,
                "y": 200,
                "width": 140,
                "height": 60
            },
            {
                "id": "edge-1",
                "shape": "edge",
                "source": {"cell": "node-1"},
                "target": {"cell": "node-2"}
            }
        ]

        errors = validate_diagram_cells(cells)
        self.assertEqual(len(errors), 0)

    def test_validate_diagram_cells_with_errors(self):
        """Test validating a diagram with errors"""
        cells = [
            {
                "id": "node-1",
                "shape": "process",
                # Missing position and size
            },
            {
                "id": "node-2",
                "shape": "store",
                "x": 300,
                "y": 200,
                "width": 140,
                "height": 60
            }
        ]

        errors = validate_diagram_cells(cells)
        self.assertGreater(len(errors), 0)
        self.assertIn("node-1", errors)

    def test_validate_diagram_cells_duplicate_ids(self):
        """Test validating a diagram with duplicate IDs"""
        cells = [
            {
                "id": "node-1",
                "shape": "process",
                "x": 100,
                "y": 200,
                "width": 120,
                "height": 60
            },
            {
                "id": "node-1",  # Duplicate ID
                "shape": "store",
                "x": 300,
                "y": 200,
                "width": 140,
                "height": 60
            }
        ]

        errors = validate_diagram_cells(cells)
        self.assertGreater(len(errors), 0)
        self.assertIn("node-1", errors)
        self.assertTrue(any("duplicate" in error.lower() for error in errors["node-1"]))

    def test_validate_diagram_cells_invalid_edge_reference(self):
        """Test validating a diagram with invalid edge references"""
        cells = [
            {
                "id": "node-1",
                "shape": "process",
                "x": 100,
                "y": 200,
                "width": 120,
                "height": 60
            },
            {
                "id": "edge-1",
                "shape": "edge",
                "source": {"cell": "node-1"},
                "target": {"cell": "node-999"}  # Non-existent node
            }
        ]

        errors = validate_diagram_cells(cells)
        self.assertGreater(len(errors), 0)
        self.assertIn("edge-1", errors)
        self.assertTrue(any("non-existent" in error.lower() for error in errors["edge-1"]))

    def test_validate_diagram_cells_multiple_errors(self):
        """Test validating a diagram with multiple errors across cells"""
        cells = [
            {
                "id": "node-1",
                "shape": "process",
                "x": 100,
                "y": 200,
                "width": 20,  # Too small
                "height": 60
            },
            {
                "id": "node-2",
                "shape": "invalid-shape",  # Invalid shape
                "x": 300,
                "y": 200,
                "width": 140,
                "height": 60
            },
            {
                "id": "edge-1",
                "shape": "edge",
                "source": {"cell": "node-999"},  # Non-existent
                "target": {"cell": "node-2"}
            }
        ]

        errors = validate_diagram_cells(cells)
        self.assertEqual(len(errors), 3)  # All three cells have errors
        self.assertIn("node-1", errors)
        self.assertIn("node-2", errors)
        self.assertIn("edge-1", errors)


if __name__ == '__main__':
    unittest.main()
