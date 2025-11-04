# coding: utf-8

"""
    TMI (Threat Modeling Improved) API - Template Tests

    Tests for pre-built component templates.
"""

import unittest

from tmi_client.helpers import DfdDiagramBuilder, templates


class TestTemplates(unittest.TestCase):
    """Template function tests"""

    def setUp(self):
        """Set up test fixtures"""
        self.builder = DfdDiagramBuilder(name="Test")

    def test_create_web_server(self):
        """Test web server template"""
        node_id = templates.create_web_server(self.builder, "Web Server")
        self.assertIsNotNone(node_id)
        self.assertEqual(len(self.builder.cells), 1)

    def test_create_database(self):
        """Test database template"""
        node_id = templates.create_database(self.builder, "PostgreSQL")
        self.assertIsNotNone(node_id)
        self.assertEqual(len(self.builder.cells), 1)

    def test_create_load_balancer(self):
        """Test load balancer template"""
        node_id = templates.create_load_balancer(self.builder, "ALB")
        self.assertIsNotNone(node_id)
        self.assertEqual(len(self.builder.cells), 1)

    def test_create_cache(self):
        """Test cache template"""
        node_id = templates.create_cache(self.builder, "Redis")
        self.assertIsNotNone(node_id)
        self.assertEqual(len(self.builder.cells), 1)

    def test_create_vpc_boundary(self):
        """Test VPC boundary template"""
        boundary_id = templates.create_vpc_boundary(self.builder, "Production VPC")
        self.assertIsNotNone(boundary_id)
        self.assertEqual(len(self.builder.cells), 1)

    def test_create_user_actor(self):
        """Test user actor template"""
        actor_id = templates.create_user_actor(self.builder)
        self.assertIsNotNone(actor_id)
        self.assertEqual(len(self.builder.cells), 1)

    def test_template_with_parent(self):
        """Test template with parent boundary"""
        vpc_id = templates.create_vpc_boundary(self.builder, "VPC")
        web_id = templates.create_web_server(self.builder, "Web", parent=vpc_id)

        self.assertEqual(len(self.builder.cells), 2)


if __name__ == '__main__':
    unittest.main()
