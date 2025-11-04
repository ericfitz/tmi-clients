# coding: utf-8

"""
DFD Diagram Builder

Provides a simple, Pythonic API for building Data Flow Diagrams (DFD)
without needing to understand the underlying X6 format.
"""

from typing import Any, Dict, List, Optional, Tuple
import uuid

from tmi_client.models.dfd_diagram import DfdDiagram
from tmi_client.models.node import Node
from tmi_client.models.edge import Edge
from tmi_client.models.edge_label import EdgeLabel
from tmi_client.models.edge_label_attrs import EdgeLabelAttrs


class DfdDiagramBuilder:
    """
    Builder for creating DFD diagrams easily.

    This class provides a simple, intuitive API for creating Data Flow Diagrams
    without requiring knowledge of the underlying X6 format. It handles UUID
    generation, default styling, port configuration, and validation automatically.

    Example:
        >>> builder = DfdDiagramBuilder(name="My Architecture")
        >>> web_server = builder.add_node("Web Server", shape="process", position=(100, 100))
        >>> database = builder.add_node("Database", shape="store", position=(300, 100))
        >>> builder.add_edge(web_server, database, label="SQL Query", protocol="TCP", port=5432)
        >>> diagram = builder.build()
    """

    # Default styling per shape type
    DEFAULT_STYLES = {
        "process": {"fill": "#E1F5FE", "stroke": "#03A9F4"},
        "store": {"fill": "#FFF9C4", "stroke": "#FBC02D"},
        "actor": {"fill": "#FFEBEE", "stroke": "#F44336"},
        "security-boundary": {"fill": "#E3F2FD", "stroke": "#2196F3"},
        "text-box": {"fill": "#F5F5F5", "stroke": "#9E9E9E"}
    }

    # Default sizes per shape type
    DEFAULT_SIZES = {
        "process": (120, 60),
        "store": (140, 60),
        "actor": (100, 100),
        "security-boundary": (400, 300),
        "text-box": (120, 40)
    }

    def __init__(self, name: str = "Untitled Diagram"):
        """
        Initialize the diagram builder.

        Args:
            name: Name for the diagram
        """
        self.name = name
        self.cells: List[object] = []  # Will contain Node and Edge objects
        self._node_map: Dict[str, object] = {}  # Maps node ID to Node object

    def add_node(
        self,
        name: str,
        shape: str = "process",
        position: Tuple[float, float] = (0, 0),
        size: Optional[Tuple[float, float]] = None,
        style: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        parent_id: Optional[str] = None,
        node_id: Optional[str] = None,
        angle: float = 0,
        z_index: float = 10
    ) -> str:
        """
        Add a node to the diagram.

        Args:
            name: Node label text
            shape: Node shape - one of: "actor", "process", "store",
                   "security-boundary", "text-box"
            position: (x, y) coordinates in pixels
            size: (width, height) dimensions in pixels. If None, uses default
                  size for the shape type.
            style: Custom styling dict with "fill" and "stroke" colors.
                   If None, uses default colors for the shape type.
            metadata: Optional custom metadata dict. Will be converted to
                      _metadata format expected by the API.
            parent_id: Parent node ID for nesting (e.g., placing nodes inside
                       security boundaries)
            node_id: Custom node ID (UUID). If None, auto-generates a UUID.
            angle: Rotation angle in degrees (default: 0)
            z_index: Stacking order for overlapping elements (default: 10)

        Returns:
            Node ID (UUID string) for use in add_edge() calls

        Raises:
            ValueError: If shape is not a valid node shape type
        """
        # Generate or use provided ID
        node_id = node_id or str(uuid.uuid4())

        # Get position coordinates
        x, y = position

        # Use default size if not provided
        if size is None:
            size = self.DEFAULT_SIZES.get(shape, (120, 60))
        width, height = size

        # Use default styling if not provided
        if style is None:
            style = self.DEFAULT_STYLES.get(shape, {"fill": "#FFF", "stroke": "#333"})

        # Build attrs structure for X6
        attrs = {
            "body": style,
            "text": {"text": name}
        }

        # Create the node using flat format (x, y, width, height)
        # Note: id, shape, and z_index must be passed for Cell base class
        node = Node(
            id=node_id,
            shape=shape,
            x=x,
            y=y,
            width=width,
            height=height,
            angle=angle,
            parent=parent_id,
            attrs=attrs,
            z_index=z_index
        )

        # Add metadata if provided
        if metadata:
            from tmi_client.models.cell_data import CellData
            from tmi_client.models.metadata import Metadata

            metadata_items = [
                Metadata(key=k, value=str(v))
                for k, v in metadata.items()
            ]
            cell_data = CellData(metadata=metadata_items)
            node.data = cell_data

        # Add ports for process nodes
        if shape == "process":
            node.ports = {
                "groups": {
                    "in": {"position": "left"},
                    "out": {"position": "right"}
                },
                "items": [
                    {"id": "port-in", "group": "in"},
                    {"id": "port-out", "group": "out"}
                ]
            }

        self.cells.append(node)
        self._node_map[node_id] = node

        return node_id

    def add_edge(
        self,
        source: str,
        target: str,
        label: Optional[str] = None,
        protocol: Optional[str] = None,
        port: Optional[int] = None,
        bidirectional: bool = False,
        style: Optional[Dict[str, Any]] = None,
        edge_id: Optional[str] = None,
        z_index: float = 20
    ) -> str:
        """
        Add an edge (connection) between two nodes.

        Args:
            source: Source node ID (returned from add_node())
            target: Target node ID (returned from add_node())
            label: Optional edge label text
            protocol: Optional protocol name (e.g., "HTTP", "TCP", "HTTPS")
            port: Optional port number
            bidirectional: If True, adds arrows on both ends
            style: Custom line styling dict. If None, uses default styling.
            edge_id: Custom edge ID (UUID). If None, auto-generates a UUID.
            z_index: Stacking order (default: 20, above nodes)

        Returns:
            Edge ID (UUID string)

        Raises:
            ValueError: If source or target node ID is not found
        """
        # Generate or use provided ID
        edge_id = edge_id or str(uuid.uuid4())

        # Verify nodes exist
        source_node = self._node_map.get(source)
        target_node = self._node_map.get(target)

        if not source_node:
            raise ValueError(f"Source node '{source}' not found in diagram")
        if not target_node:
            raise ValueError(f"Target node '{target}' not found in diagram")

        # Build source and target connection objects
        source_obj = {"cell": source}
        target_obj = {"cell": target}

        # Add ports if available
        source_port = self._get_port(source_node, "out")
        if source_port:
            source_obj["port"] = source_port

        target_port = self._get_port(target_node, "in")
        if target_port:
            target_obj["port"] = target_port

        # Build label text
        label_parts = []
        if label:
            label_parts.append(label)
        if protocol:
            proto_str = f"({protocol}"
            if port:
                proto_str += f":{port}"
            proto_str += ")"
            label_parts.append(proto_str)

        label_text = " ".join(label_parts) if label_parts else None

        # Default styling for edges
        if style is None:
            style = {
                "stroke": "#333",
                "strokeWidth": 2,
                "targetMarker": {"name": "block", "width": 12, "height": 8}
            }
            if bidirectional:
                style["sourceMarker"] = {"name": "block", "width": 12, "height": 8}

        # Build attrs structure
        attrs = {"line": style}

        # Create the edge
        # Note: id, shape, and z_index must be passed for Cell base class
        edge = Edge(
            id=edge_id,
            shape="edge",
            source=source_obj,
            target=target_obj,
            attrs=attrs,
            router={"name": "manhattan"},
            connector={"name": "rounded"},
            z_index=z_index
        )

        # Add label if provided
        if label_text:
            label_attrs = EdgeLabelAttrs(text={"text": label_text})
            edge_label = EdgeLabel(attrs=label_attrs)
            edge.labels = [edge_label]

        self.cells.append(edge)
        return edge_id

    def add_security_boundary(
        self,
        name: str,
        position: Tuple[float, float] = (0, 0),
        size: Tuple[float, float] = (400, 300),
        style: Optional[Dict[str, str]] = None,
        boundary_id: Optional[str] = None
    ) -> str:
        """
        Add a security boundary (container for grouping components).

        This is a convenience method that creates a "security-boundary" node
        with appropriate styling. Child nodes can be nested inside by passing
        the returned boundary_id as the parent_id when adding nodes.

        Args:
            name: Boundary name/label
            position: (x, y) coordinates in pixels
            size: (width, height) dimensions in pixels
            style: Custom styling dict. If None, uses default boundary styling.
            boundary_id: Custom boundary ID (UUID). If None, auto-generates.

        Returns:
            Boundary ID (UUID string) - use as parent_id for child nodes
        """
        if style is None:
            style = {"fill": "#E3F2FD", "stroke": "#2196F3", "strokeDasharray": "5,5"}

        return self.add_node(
            name=name,
            shape="security-boundary",
            position=position,
            size=size,
            style=style,
            node_id=boundary_id,
            z_index=1  # Boundaries should be behind other elements
        )

    def build(self, validate: bool = True) -> DfdDiagram:
        """
        Build the final DfdDiagram object.

        Args:
            validate: If True (default), validates cells before building.
                     Set to False to skip validation.

        Returns:
            DfdDiagram object ready for API submission

        Raises:
            ValueError: If validation is enabled and cells are invalid
        """
        # Validate if requested
        if validate:
            from tmi_client.helpers.validators import validate_diagram_cells

            # Convert cells to dicts for validation
            cells_as_dicts = [cell.to_dict() for cell in self.cells]
            errors = validate_diagram_cells(cells_as_dicts)

            if errors:
                error_msg = "Diagram validation failed:\n"
                for cell_id, cell_errors in errors.items():
                    error_msg += f"  Cell {cell_id}:\n"
                    for error in cell_errors:
                        error_msg += f"    - {error}\n"
                raise ValueError(error_msg)

        # Create the DFD diagram
        # Note: Use __new__ workaround to bypass BaseDiagram.__init__ validation
        # that requires 'id' field. ID is set by the server, not the client.
        diagram = DfdDiagram.__new__(DfdDiagram)
        diagram._type = None
        diagram._cells = None
        diagram._id = None
        diagram._name = None
        diagram._created_at = None
        diagram._modified_at = None
        diagram._metadata = None
        diagram._update_vector = None
        diagram._image = None
        diagram._description = None
        diagram.discriminator = "type"

        # Set required fields
        diagram._type = "DFD-1.0.0"
        diagram.cells = self.cells
        diagram._name = self.name

        return diagram

    def _get_port(self, node, direction: str) -> Optional[str]:
        """
        Get port ID for a node in the given direction.

        Args:
            node: Node object
            direction: Port direction ("in" or "out")

        Returns:
            Port ID string if found, None otherwise
        """
        if not node.ports or not isinstance(node.ports, dict):
            return None

        items = node.ports.get("items", [])
        for item in items:
            if isinstance(item, dict) and item.get("group") == direction:
                return item.get("id")

        return None
