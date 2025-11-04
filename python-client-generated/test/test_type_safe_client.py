# coding: utf-8

"""
    TMI (Threat Modeling Improved) API - TypeSafeTMIClient Tests

    Tests for the type-safe client wrapper.
"""

import unittest
from unittest.mock import Mock, MagicMock

from tmi_client.helpers import TypeSafeTMIClient
from tmi_client.models.dfd_diagram import DfdDiagram
from tmi_client.models.diagram_list_item import DiagramListItem


class TestTypeSafeTMIClient(unittest.TestCase):
    """TypeSafeTMIClient unit tests"""

    def setUp(self):
        """Set up test fixtures"""
        self.mock_api_client = Mock()
        self.client = TypeSafeTMIClient(self.mock_api_client)

    def tearDown(self):
        """Clean up after tests"""
        pass

    def test_init(self):
        """Test TypeSafeTMIClient initialization"""
        client = TypeSafeTMIClient(self.mock_api_client)
        self.assertIsNotNone(client.api)

    def test_list_diagrams_returns_list(self):
        """Test list_diagrams returns a list"""
        # Mock the API to return an empty list
        self.client.api.get_threat_model_diagrams = Mock(return_value=[])

        result = self.client.list_diagrams("tm-123")

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_list_diagrams_with_objects(self):
        """Test list_diagrams with DiagramListItem objects"""
        # Create mock diagram list items
        item1 = DiagramListItem(
            id="d1",
            name="Diagram 1",
            type="DFD-1.0.0"
        )
        item2 = DiagramListItem(
            id="d2",
            name="Diagram 2",
            type="DFD-1.0.0"
        )

        self.client.api.get_threat_model_diagrams = Mock(return_value=[item1, item2])

        result = self.client.list_diagrams("tm-123")

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], DiagramListItem)
        self.assertIsInstance(result[1], DiagramListItem)
        self.assertEqual(result[0].id, "d1")
        self.assertEqual(result[1].id, "d2")

    def test_list_diagrams_converts_dicts(self):
        """Test list_diagrams converts dicts to objects"""
        # Mock the API to return dicts (shouldn't happen but we handle it)
        dict_items = [
            {"id": "d1", "name": "Diagram 1", "type": "DFD-1.0.0"},
            {"id": "d2", "name": "Diagram 2", "type": "DFD-1.0.0"}
        ]

        self.client.api.get_threat_model_diagrams = Mock(return_value=dict_items)

        result = self.client.list_diagrams("tm-123")

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], DiagramListItem)
        self.assertIsInstance(result[1], DiagramListItem)

    def test_get_diagram_returns_object(self):
        """Test get_diagram returns a DfdDiagram object"""
        # Create a mock diagram using __new__ workaround
        mock_diagram = DfdDiagram.__new__(DfdDiagram)
        mock_diagram._id = "d1"
        mock_diagram._name = "Test Diagram"
        mock_diagram._type = "DFD-1.0.0"
        mock_diagram._cells = []

        self.client.api.get_threat_model_diagram = Mock(return_value=mock_diagram)

        result = self.client.get_diagram("tm-123", "d1")

        self.assertIsInstance(result, DfdDiagram)

    def test_get_diagram_converts_dict(self):
        """Test get_diagram converts dict to object"""
        # Mock the API to return a dict with all required fields
        dict_diagram = {
            "id": "d1",
            "name": "Test Diagram",
            "type": "DFD-1.0.0",
            "cells": [],
            "created_at": "2025-01-01T00:00:00Z",
            "modified_at": "2025-01-01T00:00:00Z"
        }

        self.client.api.get_threat_model_diagram = Mock(return_value=dict_diagram)

        result = self.client.get_diagram("tm-123", "d1")

        self.assertIsInstance(result, DfdDiagram)

    def test_create_diagram(self):
        """Test create_diagram"""
        # Create a mock diagram
        mock_diagram = DfdDiagram.__new__(DfdDiagram)
        mock_diagram._id = "d1"
        mock_diagram._name = "New Diagram"
        mock_diagram._type = "DFD-1.0.0"
        mock_diagram._cells = []

        self.client.api.create_threat_model_diagram = Mock(return_value=mock_diagram)

        result = self.client.create_diagram("tm-123", "New Diagram")

        self.assertIsInstance(result, DfdDiagram)
        self.client.api.create_threat_model_diagram.assert_called_once()

    def test_update_diagram(self):
        """Test update_diagram"""
        # Create mock diagrams
        input_diagram = DfdDiagram.__new__(DfdDiagram)
        input_diagram._type = "DFD-1.0.0"
        input_diagram._cells = []
        input_diagram._name = "Updated"

        output_diagram = DfdDiagram.__new__(DfdDiagram)
        output_diagram._id = "d1"
        output_diagram._name = "Updated"
        output_diagram._type = "DFD-1.0.0"
        output_diagram._cells = []

        self.client.api.update_threat_model_diagram = Mock(return_value=output_diagram)

        result = self.client.update_diagram("tm-123", "d1", input_diagram)

        self.assertIsInstance(result, DfdDiagram)
        self.client.api.update_threat_model_diagram.assert_called_once_with(
            input_diagram, "tm-123", "d1"
        )

    def test_delete_diagram(self):
        """Test delete_diagram"""
        self.client.api.delete_threat_model_diagram = Mock(return_value=None)

        # Should not raise
        self.client.delete_diagram("tm-123", "d1")

        self.client.api.delete_threat_model_diagram.assert_called_once_with("tm-123", "d1")


if __name__ == '__main__':
    unittest.main()
