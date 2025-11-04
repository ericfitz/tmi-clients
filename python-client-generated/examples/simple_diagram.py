#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "tmi-client",
# ]
# ///
"""
Simple 3-Tier Architecture Diagram Example

This example demonstrates how to use the TMI Client helpers to easily build
a diagram of a simple 3-tier web application architecture.
"""

from tmi_client.helpers import DfdDiagramBuilder, templates

def main():
    """Create a simple 3-tier architecture diagram."""

    # Create a diagram builder
    builder = DfdDiagramBuilder(name="3-Tier Web Application")

    # Add a VPC security boundary
    vpc_id = templates.create_vpc_boundary(
        builder,
        name="Production VPC",
        region="us-east-1",
        position=(50, 50),
        size=(700, 450)
    )

    # Add load balancer
    lb_id = templates.create_load_balancer(
        builder,
        name="Application Load Balancer",
        position=(350, 100),
        parent=vpc_id
    )

    # Add web servers
    web1_id = templates.create_web_server(
        builder,
        name="Web Server 1",
        position=(250, 200),
        parent=vpc_id
    )

    web2_id = templates.create_web_server(
        builder,
        name="Web Server 2",
        position=(450, 200),
        parent=vpc_id
    )

    # Add database
    db_id = templates.create_database(
        builder,
        name="PostgreSQL",
        position=(350, 350),
        parent=vpc_id,
        metadata={"version": "15", "encrypted": "true"}
    )

    # Add external user
    user_id = templates.create_user_actor(
        builder,
        name="End User",
        position=(350, 550)
    )

    # Connect components
    builder.add_edge(user_id, lb_id, label="HTTPS", protocol="TLS", port=443)
    builder.add_edge(lb_id, web1_id, label="HTTP", port=8080)
    builder.add_edge(lb_id, web2_id, label="HTTP", port=8080)
    builder.add_edge(web1_id, db_id, label="SQL", protocol="TCP", port=5432)
    builder.add_edge(web2_id, db_id, label="SQL", protocol="TCP", port=5432)

    # Build the diagram (with validation)
    diagram = builder.build()

    print(f"Created diagram: {diagram.name}")
    print(f"  Type: {diagram.type}")
    print(f"  Cells: {len(diagram.cells)} (nodes + edges)")

    # The diagram object is now ready to be submitted to the TMI API:
    # from tmi_client import ApiClient, Configuration
    # from tmi_client.helpers import TypeSafeTMIClient
    #
    # config = Configuration()
    # config.api_key['bearerAuth'] = 'your-api-token'
    # client = TypeSafeTMIClient(ApiClient(config))
    #
    # result = client.update_diagram(threat_model_id, diagram_id, diagram)
    # print(f"Diagram updated: {result.id}")

    return diagram


if __name__ == "__main__":
    diagram = main()
