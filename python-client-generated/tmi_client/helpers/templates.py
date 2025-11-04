# coding: utf-8

"""
Pre-built Component Templates

Provides template functions for common infrastructure components with
appropriate styling and metadata.
"""

from typing import Dict, Optional, Any

from tmi_client.helpers.diagram_builder import DfdDiagramBuilder


def create_web_server(
    builder: DfdDiagramBuilder,
    name: str,
    position: tuple = (100, 100),
    parent: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> str:
    """
    Create a web server node with appropriate styling.

    Args:
        builder: DfdDiagramBuilder instance
        name: Server name
        position: (x, y) position
        parent: Optional parent boundary ID
        metadata: Additional metadata

    Returns:
        Node ID
    """
    default_metadata = {"component_type": "web_server", "layer": "presentation"}
    if metadata:
        default_metadata.update(metadata)

    return builder.add_node(
        name=name,
        shape="process",
        position=position,
        size=(140, 70),
        style={"fill": "#E3F2FD", "stroke": "#1976D2"},
        parent_id=parent,
        metadata=default_metadata
    )


def create_database(
    builder: DfdDiagramBuilder,
    name: str,
    position: tuple = (300, 100),
    parent: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> str:
    """
    Create a database node with appropriate styling.

    Args:
        builder: DfdDiagramBuilder instance
        name: Database name
        position: (x, y) position
        parent: Optional parent boundary ID
        metadata: Additional metadata

    Returns:
        Node ID
    """
    default_metadata = {"component_type": "database", "layer": "data"}
    if metadata:
        default_metadata.update(metadata)

    return builder.add_node(
        name=name,
        shape="store",
        position=position,
        size=(150, 70),
        style={"fill": "#FFF9C4", "stroke": "#F57C00"},
        parent_id=parent,
        metadata=default_metadata
    )


def create_load_balancer(
    builder: DfdDiagramBuilder,
    name: str,
    position: tuple = (100, 50),
    parent: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> str:
    """
    Create a load balancer node with appropriate styling.

    Args:
        builder: DfdDiagramBuilder instance
        name: Load balancer name
        position: (x, y) position
        parent: Optional parent boundary ID
        metadata: Additional metadata

    Returns:
        Node ID
    """
    default_metadata = {"component_type": "load_balancer", "layer": "network"}
    if metadata:
        default_metadata.update(metadata)

    return builder.add_node(
        name=name,
        shape="process",
        position=position,
        size=(140, 60),
        style={"fill": "#E8EAF6", "stroke": "#3F51B5"},
        parent_id=parent,
        metadata=default_metadata
    )


def create_cache(
    builder: DfdDiagramBuilder,
    name: str,
    position: tuple = (300, 200),
    parent: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> str:
    """
    Create a cache node with appropriate styling.

    Args:
        builder: DfdDiagramBuilder instance
        name: Cache name (e.g., "Redis", "Memcached")
        position: (x, y) position
        parent: Optional parent boundary ID
        metadata: Additional metadata

    Returns:
        Node ID
    """
    default_metadata = {"component_type": "cache", "layer": "data"}
    if metadata:
        default_metadata.update(metadata)

    return builder.add_node(
        name=name,
        shape="store",
        position=position,
        size=(130, 60),
        style={"fill": "#FCE4EC", "stroke": "#C2185B"},
        parent_id=parent,
        metadata=default_metadata
    )


def create_vpc_boundary(
    builder: DfdDiagramBuilder,
    name: str,
    region: str = "us-east-1",
    position: tuple = (50, 50),
    size: tuple = (700, 400)
) -> str:
    """
    Create a VPC security boundary with cloud metadata.

    Args:
        builder: DfdDiagramBuilder instance
        name: VPC name
        region: AWS region
        position: (x, y) position
        size: (width, height) dimensions

    Returns:
        Boundary ID
    """
    return builder.add_security_boundary(
        name=f"{name} ({region})",
        position=position,
        size=size,
        style={"fill": "#E8F5E9", "stroke": "#388E3C", "strokeDasharray": "5,5"}
    )


def create_user_actor(
    builder: DfdDiagramBuilder,
    name: str = "User",
    position: tuple = (50, 200),
    metadata: Optional[Dict[str, Any]] = None
) -> str:
    """
    Create a user actor node.

    Args:
        builder: DfdDiagramBuilder instance
        name: Actor name
        position: (x, y) position
        metadata: Additional metadata

    Returns:
        Node ID
    """
    default_metadata = {"actor_type": "user"}
    if metadata:
        default_metadata.update(metadata)

    return builder.add_node(
        name=name,
        shape="actor",
        position=position,
        size=(100, 100),
        style={"fill": "#FFEBEE", "stroke": "#D32F2F"},
        metadata=default_metadata
    )
