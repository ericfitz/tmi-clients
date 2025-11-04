# TMI Python Client - Improvement Recommendations

This document outlines recommended improvements to make the TMI Python client easier and more intuitive to use.

## Current Pain Points

### 1. Manual Object Construction Required

**Problem**: Users must manually construct `DfdDiagram` objects bypassing `__init__`:

```python
# Current workaround (16 lines!)
dfd_diagram = DfdDiagram.__new__(DfdDiagram)
dfd_diagram._type = None
dfd_diagram._cells = None
dfd_diagram._id = None
dfd_diagram._name = None
dfd_diagram._created_at = None
dfd_diagram._modified_at = None
dfd_diagram._metadata = None
dfd_diagram._update_vector = None
dfd_diagram._image = None
dfd_diagram._description = None
dfd_diagram.discriminator = "type"
dfd_diagram._type = "DFD-1.0.0"
dfd_diagram.cells = cells
dfd_diagram._name = "My Diagram"
```

**Impact**: Error-prone, verbose, requires knowledge of internals

---

### 2. No Helper Methods for Cell Manipulation

**Problem**: Users work directly with raw cell dictionaries (X6 format):

```python
# Creating cells is manual and verbose
cell = {
    "id": str(uuid.uuid4()),
    "shape": "process",
    "x": 100,
    "y": 100,
    "width": 120,
    "height": 60,
    "zIndex": 10,
    "attrs": {
        "body": {"fill": "#E1F5FE", "stroke": "#03A9F4"},
        "text": {"text": "My Component"}
    },
    "data": {
        "_metadata": [
            {"key": "component_id", "value": "comp-123"},
            {"key": "component_type", "value": "compute"}
        ]
    }
}
```

**Impact**: Steep learning curve, easy to make mistakes, no validation

---

### 3. Inconsistent Type Handling

**Problem**: API returns mix of dicts and objects:

```python
# Defensive coding required everywhere
diagram_id = diagram["id"] if isinstance(diagram, dict) else diagram.id
```

**Impact**: Type uncertainty, verbose code, potential runtime errors

---

### 4. No Validation or Schema Helpers

**Problem**: No way to validate cells before sending to API:

```python
# Users can create invalid cells
cell = {"id": "123"}  # Missing required fields
# Error only discovered when API rejects it
```

**Impact**: Late error detection, poor developer experience

---

### 5. Complex X6 Format Knowledge Required

**Problem**: Users must understand AntV X6 v2 format:

```python
# What are ports? What's a router? What's a connector?
edge = {
    "shape": "edge",
    "source": {"cell": "source-id", "port": "port-out"},
    "target": {"cell": "target-id", "port": "port-in"},
    "router": {"name": "manhattan"},
    "connector": {"name": "rounded"},
    "attrs": {
        "line": {
            "stroke": "#333",
            "strokeWidth": 2,
            "targetMarker": {"name": "block", "width": 12, "height": 8}
        }
    }
}
```

**Impact**: High barrier to entry, documentation burden

---

## Recommended Improvements

### Priority 1: Helper Classes for Diagram Creation ⭐⭐⭐

Create builder classes to simplify diagram construction:

```python
# New: Simple builder API
from tmi_client.helpers import DfdDiagramBuilder

builder = DfdDiagramBuilder(name="Infrastructure Diagram")

# Add nodes with simple API
node1 = builder.add_node(
    name="Web Server",
    shape="process",
    position=(100, 100),
    metadata={"type": "compute", "subtype": "vm"}
)

node2 = builder.add_node(
    name="Database",
    shape="store",
    position=(300, 100)
)

# Add edges
builder.add_edge(
    source=node1,
    target=node2,
    label="SQL Query",
    protocol="TCP",
    port=3306
)

# Build the diagram (handles all the manual construction)
diagram = builder.build()  # Returns properly constructed DfdDiagram

# Use directly with API
api.update_threat_model_diagram(diagram, tm_id, diagram_id)
```

**Implementation**:

```python
# tmi_client/helpers/dfd_builder.py

from typing import Any, Dict, List, Optional, Tuple
import uuid
from ..models import DfdDiagram

class DfdDiagramBuilder:
    """Builder for creating DFD diagrams easily."""

    def __init__(self, name: str = "Untitled Diagram"):
        """Initialize builder."""
        self.name = name
        self.cells: List[Dict[str, Any]] = []
        self._node_map: Dict[str, Dict[str, Any]] = {}

    def add_node(
        self,
        name: str,
        shape: str = "process",
        position: Tuple[int, int] = (0, 0),
        size: Tuple[int, int] = (120, 60),
        style: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        parent_id: Optional[str] = None,
        node_id: Optional[str] = None
    ) -> str:
        """
        Add a node to the diagram.

        Args:
            name: Node label
            shape: Node shape (process, store, actor, security-boundary)
            position: (x, y) coordinates
            size: (width, height) dimensions
            style: Custom styling (fill, stroke colors)
            metadata: Custom metadata dict
            parent_id: Parent node ID (for nesting)
            node_id: Custom node ID (auto-generated if None)

        Returns:
            Node ID (for use in add_edge)
        """
        node_id = node_id or str(uuid.uuid4())
        x, y = position
        width, height = size

        # Default styling by shape
        default_styles = {
            "process": {"fill": "#E1F5FE", "stroke": "#03A9F4"},
            "store": {"fill": "#FFF9C4", "stroke": "#FBC02D"},
            "actor": {"fill": "#FFEBEE", "stroke": "#F44336"},
            "security-boundary": {"fill": "#E3F2FD", "stroke": "#2196F3"}
        }

        body_style = style or default_styles.get(shape, {"fill": "#FFF", "stroke": "#333"})

        cell = {
            "id": node_id,
            "shape": shape,
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "zIndex": 10,
            "attrs": {
                "body": body_style,
                "text": {"text": name}
            }
        }

        # Add metadata if provided
        if metadata:
            cell["data"] = {
                "_metadata": [{"key": k, "value": v} for k, v in metadata.items()]
            }

        # Add parent if provided
        if parent_id:
            cell["parent"] = parent_id

        # Add ports for certain shapes
        if shape in ["process"]:
            cell["ports"] = {
                "groups": {
                    "in": {"position": "left"},
                    "out": {"position": "right"}
                },
                "items": [
                    {"id": "port-in", "group": "in"},
                    {"id": "port-out", "group": "out"}
                ]
            }

        self.cells.append(cell)
        self._node_map[node_id] = cell
        return node_id

    def add_edge(
        self,
        source: str,
        target: str,
        label: Optional[str] = None,
        protocol: Optional[str] = None,
        port: Optional[int] = None,
        bidirectional: bool = False,
        style: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Add an edge between nodes.

        Args:
            source: Source node ID
            target: Target node ID
            label: Edge label
            protocol: Protocol name (e.g., "HTTP", "TCP")
            port: Port number
            bidirectional: Whether flow is bidirectional
            style: Custom line styling

        Returns:
            Edge ID
        """
        edge_id = str(uuid.uuid4())

        # Build label
        label_parts = []
        if label:
            label_parts.append(label)
        if protocol:
            proto_str = f"({protocol}"
            if port:
                proto_str += f":{port}"
            proto_str += ")"
            label_parts.append(proto_str)

        label_text = " ".join(label_parts) if label_parts else ""

        # Get source/target cells
        source_cell = self._node_map.get(source)
        target_cell = self._node_map.get(target)

        if not source_cell or not target_cell:
            raise ValueError(f"Source ({source}) or target ({target}) node not found")

        # Determine ports
        source_port = self._get_port(source_cell, "out")
        target_port = self._get_port(target_cell, "in")

        # Default styling
        default_style = {
            "stroke": "#333",
            "strokeWidth": 2,
            "targetMarker": {"name": "block", "width": 12, "height": 8}
        }
        if bidirectional:
            default_style["sourceMarker"] = {"name": "block", "width": 12, "height": 8}

        line_style = style or default_style

        edge = {
            "id": edge_id,
            "shape": "edge",
            "source": {"cell": source},
            "target": {"cell": target},
            "zIndex": 20,
            "attrs": {"line": line_style},
            "router": {"name": "manhattan"},
            "connector": {"name": "rounded"}
        }

        # Add ports if available
        if source_port:
            edge["source"]["port"] = source_port
        if target_port:
            edge["target"]["port"] = target_port

        # Add label if provided
        if label_text:
            edge["labels"] = [{
                "attrs": {"text": {"text": label_text}}
            }]

        self.cells.append(edge)
        return edge_id

    def add_security_boundary(
        self,
        name: str,
        position: Tuple[int, int] = (0, 0),
        size: Tuple[int, int] = (400, 300),
        style: Optional[Dict[str, str]] = None,
        boundary_id: Optional[str] = None
    ) -> str:
        """
        Add a security boundary (for grouping components).

        Args:
            name: Boundary name
            position: (x, y) coordinates
            size: (width, height) dimensions
            style: Custom styling
            boundary_id: Custom boundary ID

        Returns:
            Boundary ID (use as parent_id for child nodes)
        """
        return self.add_node(
            name=name,
            shape="security-boundary",
            position=position,
            size=size,
            style=style or {"fill": "#E3F2FD", "stroke": "#2196F3"},
            node_id=boundary_id
        )

    def build(self) -> DfdDiagram:
        """
        Build the final DfdDiagram object.

        Returns:
            Properly constructed DfdDiagram ready for API submission
        """
        # Use manual construction workaround until spec is fixed
        dfd_diagram = DfdDiagram.__new__(DfdDiagram)
        dfd_diagram._type = None
        dfd_diagram._cells = None
        dfd_diagram._id = None
        dfd_diagram._name = None
        dfd_diagram._created_at = None
        dfd_diagram._modified_at = None
        dfd_diagram._metadata = None
        dfd_diagram._update_vector = None
        dfd_diagram._image = None
        dfd_diagram._description = None
        dfd_diagram.discriminator = "type"

        # Set fields
        dfd_diagram._type = "DFD-1.0.0"
        dfd_diagram.cells = self.cells
        dfd_diagram._name = self.name

        return dfd_diagram

    def _get_port(self, cell: Dict[str, Any], direction: str) -> Optional[str]:
        """Get port ID for cell in given direction."""
        if "ports" not in cell:
            return None

        items = cell.get("ports", {}).get("items", [])
        for item in items:
            if item.get("group") == direction:
                return item.get("id")
        return None
```

---

### Priority 2: Cell Validation Helpers ⭐⭐

Add validation before sending to API:

```python
# New: Validation helpers
from tmi_client.helpers import validate_cell, validate_diagram

# Validate individual cells
cell = {"id": "123", "shape": "process"}
errors = validate_cell(cell)
if errors:
    print(f"Invalid cell: {errors}")
    # ['Missing required field: x', 'Missing required field: y', ...]

# Validate entire diagram
diagram = builder.build()
if diagram.validate():
    api.update_diagram(diagram, tm_id, d_id)
else:
    print(f"Diagram validation errors: {diagram.validation_errors()}")
```

**Implementation**:

```python
# tmi_client/helpers/validators.py

from typing import Any, Dict, List

def validate_cell(cell: Dict[str, Any]) -> List[str]:
    """
    Validate a cell object against X6 v2 format requirements.

    Args:
        cell: Cell dictionary

    Returns:
        List of error messages (empty if valid)
    """
    errors = []

    # Required fields
    if "id" not in cell:
        errors.append("Missing required field: id")
    if "shape" not in cell:
        errors.append("Missing required field: shape")

    # Shape-specific validation
    shape = cell.get("shape")
    if shape == "edge":
        if "source" not in cell:
            errors.append("Edge missing required field: source")
        if "target" not in cell:
            errors.append("Edge missing required field: target")
    else:
        # Node validation
        if "x" not in cell:
            errors.append("Node missing required field: x")
        if "y" not in cell:
            errors.append("Node missing required field: y")
        if "width" not in cell:
            errors.append("Node missing required field: width")
        if "height" not in cell:
            errors.append("Node missing required field: height")

        # Dimension constraints
        if cell.get("width", 0) < 40:
            errors.append("Node width must be at least 40px")
        if cell.get("height", 0) < 30:
            errors.append("Node height must be at least 30px")

    return errors

def validate_diagram_cells(cells: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    """
    Validate all cells in a diagram.

    Args:
        cells: List of cell dictionaries

    Returns:
        Dict mapping cell IDs to error lists (empty dict if all valid)
    """
    errors_by_cell = {}

    for cell in cells:
        cell_errors = validate_cell(cell)
        if cell_errors:
            cell_id = cell.get("id", "unknown")
            errors_by_cell[cell_id] = cell_errors

    return errors_by_cell
```

---

### Priority 3: Type-Safe Wrappers ⭐⭐

Create wrapper classes that ensure consistent typing:

```python
# New: Type-safe API wrapper
from tmi_client.helpers import TypeSafeTMIClient

client = TypeSafeTMIClient(api_key="...")

# Always returns typed objects, never dicts
diagram: DfdDiagram = client.create_diagram(tm_id, name="My Diagram")
diagrams: List[DiagramListItem] = client.list_diagrams(tm_id)

# No more isinstance checks needed!
diagram_id = diagram.id  # Always works
```

**Implementation**:

```python
# tmi_client/helpers/type_safe_client.py

from typing import List
from ..api import ThreatModelSubResourcesApi
from ..models import DfdDiagram, DiagramListItem, CreateDiagramRequest

class TypeSafeTMIClient:
    """
    Type-safe wrapper around TMI API client.

    Ensures all responses are properly deserialized to model objects.
    """

    def __init__(self, api_client):
        """Initialize with configured API client."""
        self.api = ThreatModelSubResourcesApi(api_client)

    def list_diagrams(self, threat_model_id: str) -> List[DiagramListItem]:
        """
        List all diagrams for a threat model.

        Args:
            threat_model_id: Threat model UUID

        Returns:
            List of DiagramListItem objects (never dicts)
        """
        result = self.api.get_threat_model_diagrams(threat_model_id)

        # Ensure proper typing
        if not isinstance(result, list):
            raise TypeError(f"Expected list, got {type(result)}")

        typed_result = []
        for item in result:
            if isinstance(item, dict):
                # Convert dict to DiagramListItem
                typed_result.append(DiagramListItem(**item))
            else:
                typed_result.append(item)

        return typed_result

    def create_diagram(
        self,
        threat_model_id: str,
        name: str
    ) -> DfdDiagram:
        """
        Create a new diagram.

        Args:
            threat_model_id: Threat model UUID
            name: Diagram name

        Returns:
            DfdDiagram object (never dict)
        """
        request = CreateDiagramRequest(name=name, type="DFD-1.0.0")
        result = self.api.create_threat_model_diagram(request, threat_model_id)

        # Ensure proper typing
        if isinstance(result, dict):
            return DfdDiagram(**result)
        return result

    def update_diagram(
        self,
        threat_model_id: str,
        diagram_id: str,
        diagram: DfdDiagram
    ) -> DfdDiagram:
        """
        Update an existing diagram.

        Args:
            threat_model_id: Threat model UUID
            diagram_id: Diagram UUID
            diagram: DfdDiagram object

        Returns:
            Updated DfdDiagram object (never dict)
        """
        result = self.api.update_threat_model_diagram(
            diagram, threat_model_id, diagram_id
        )

        # Ensure proper typing
        if isinstance(result, dict):
            return DfdDiagram(**result)
        return result
```

---

### Priority 4: Pre-built Shape Templates ⭐

Provide common component templates:

```python
# New: Pre-built templates
from tmi_client.helpers.templates import (
    create_web_server,
    create_database,
    create_load_balancer,
    create_vpc_boundary
)

builder = DfdDiagramBuilder()

# Use templates for common components
vpc_id = create_vpc_boundary(builder, name="Production VPC", region="us-east-1")
lb_id = create_load_balancer(builder, name="ALB", parent=vpc_id)
web_id = create_web_server(builder, name="Web Server", parent=vpc_id)
db_id = create_database(builder, name="PostgreSQL", parent=vpc_id)

# Connect them
builder.add_edge(lb_id, web_id, label="HTTP Traffic", port=80)
builder.add_edge(web_id, db_id, label="SQL Queries", port=5432)
```

---

### Priority 5: Documentation & Examples ⭐

Create comprehensive examples:

```python
# examples/simple_diagram.py
"""Example: Create a simple 3-tier architecture diagram."""

from tmi_client.helpers import DfdDiagramBuilder, TypeSafeTMIClient
from tmi_client import ApiClient, Configuration

# Configure client
config = Configuration()
config.api_key["bearerAuth"] = "your-token"
client = TypeSafeTMIClient(ApiClient(config))

# Build diagram
builder = DfdDiagramBuilder(name="3-Tier Architecture")

# Add security boundary
vpc = builder.add_security_boundary("VPC", position=(50, 50), size=(700, 400))

# Add components
lb = builder.add_node("Load Balancer", shape="process", position=(100, 100), parent_id=vpc)
web = builder.add_node("Web Server", shape="process", position=(300, 100), parent_id=vpc)
db = builder.add_node("Database", shape="store", position=(500, 100), parent_id=vpc)

# Add connections
builder.add_edge(lb, web, label="HTTP", port=80)
builder.add_edge(web, db, label="SQL", port=5432)

# Create diagram
diagram = builder.build()
result = client.update_diagram("threat-model-id", "diagram-id", diagram)
print(f"Diagram updated: {result.id}")
```

---

## Implementation Plan

### Phase 1: Core Helpers (2 weeks)
1. Implement `DfdDiagramBuilder` class
2. Add basic validation functions
3. Write unit tests
4. Document API

### Phase 2: Type Safety (1 week)
1. Implement `TypeSafeTMIClient` wrapper
2. Add type stubs
3. Test with mypy/pyright

### Phase 3: Templates & Examples (1 week)
1. Create common component templates
2. Write example scripts
3. Add to documentation

### Phase 4: Documentation (1 week)
1. Write comprehensive guide
2. Add inline examples
3. Create tutorial video/walkthrough

---

## File Structure

```
tmi_client/
├── helpers/
│   ├── __init__.py
│   ├── dfd_builder.py          # DfdDiagramBuilder class
│   ├── validators.py            # Validation functions
│   ├── type_safe_client.py     # TypeSafeTMIClient wrapper
│   └── templates.py             # Pre-built component templates
├── models/                       # Existing generated models
└── api/                          # Existing generated API

examples/
├── simple_diagram.py
├── aws_infrastructure.py
├── kubernetes_cluster.py
└── microservices.py

docs/
├── helpers_guide.md
├── cell_format.md
└── examples.md
```

---

## Benefits

1. **Lower Barrier to Entry**: No need to learn X6 format
2. **Faster Development**: Pre-built helpers and templates
3. **Fewer Errors**: Validation catches issues early
4. **Better Type Safety**: Consistent object types
5. **Improved DX**: Intuitive, Pythonic API
6. **Easier Maintenance**: Abstracts away manual construction workarounds

---

## Breaking Changes?

**No!** All helpers are additions. Existing code continues to work:

```python
# Old way still works
cells = [{"id": "123", "shape": "process", ...}]
diagram = DfdDiagram.__new__(DfdDiagram)
# ... manual construction ...

# New way is just easier
builder = DfdDiagramBuilder()
builder.add_node(...)
diagram = builder.build()
```

---

## Questions?

- **Do we need backwards compatibility?** Yes - helpers are optional additions
- **What about other diagram types?** Start with DFD, extend pattern later
- **Performance impact?** Minimal - just wrapper classes
- **Testing strategy?** Unit tests for helpers, integration tests for API

See `DFD_DIAGRAM_FIX.md` for technical issues that motivated these improvements.
