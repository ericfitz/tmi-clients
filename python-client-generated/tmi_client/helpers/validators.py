# coding: utf-8

"""
Cell and Diagram Validation

Provides validation functions for diagram cells (nodes and edges) to catch
errors early before submitting to the API.
"""

from typing import Any, Dict, List


def validate_cell(cell: Dict[str, Any]) -> List[str]:
    """
    Validate a cell object against X6 v2 format requirements.

    Args:
        cell: Cell dictionary (node or edge)

    Returns:
        List of error messages (empty list if valid)
    """
    errors = []

    # Required fields for all cells
    if "id" not in cell or cell["id"] is None:
        errors.append("Missing required field: id")
    if "shape" not in cell or cell["shape"] is None:
        errors.append("Missing required field: shape")

    shape = cell.get("shape")

    # Shape-specific validation
    if shape == "edge":
        # Edge validation
        if "source" not in cell or cell["source"] is None:
            errors.append("Edge missing required field: source")
        else:
            # Validate source structure
            source = cell["source"]
            if isinstance(source, dict) and "cell" not in source:
                errors.append("Edge source missing required field: cell")

        if "target" not in cell or cell["target"] is None:
            errors.append("Edge missing required field: target")
        else:
            # Validate target structure
            target = cell["target"]
            if isinstance(target, dict) and "cell" not in target:
                errors.append("Edge target missing required field: cell")

    elif shape in ["actor", "process", "store", "security-boundary", "text-box"]:
        # Node validation - must have position and size information
        # Can use either flat format (x, y, width, height) or object format (position, size)

        has_flat_format = all(k in cell for k in ["x", "y", "width", "height"])
        has_object_format = "position" in cell and "size" in cell

        if not has_flat_format and not has_object_format:
            errors.append(
                "Node missing position/size. Must have either (x, y, width, height) "
                "or (position, size)"
            )

        # Check flat format if present
        if has_flat_format:
            x = cell.get("x")
            y = cell.get("y")
            width = cell.get("width")
            height = cell.get("height")

            if x is None:
                errors.append("Node missing required field: x")
            if y is None:
                errors.append("Node missing required field: y")
            if width is None:
                errors.append("Node missing required field: width")
            elif width < 40:
                errors.append("Node width must be at least 40px")
            if height is None:
                errors.append("Node missing required field: height")
            elif height < 30:
                errors.append("Node height must be at least 30px")

        # Check object format if present
        if has_object_format:
            position = cell.get("position")
            size = cell.get("size")

            if position is not None:
                if not isinstance(position, dict):
                    errors.append("Node position must be an object")
                elif "x" not in position or "y" not in position:
                    errors.append("Node position missing x or y coordinate")

            if size is not None:
                if not isinstance(size, dict):
                    errors.append("Node size must be an object")
                elif "width" not in size or "height" not in size:
                    errors.append("Node size missing width or height")
                else:
                    if size.get("width", 0) < 40:
                        errors.append("Node width must be at least 40px")
                    if size.get("height", 0) < 30:
                        errors.append("Node height must be at least 30px")

        # Validate shape value
        valid_shapes = ["actor", "process", "store", "security-boundary", "text-box"]
        if shape not in valid_shapes:
            errors.append(
                f"Invalid node shape '{shape}'. Must be one of: {', '.join(valid_shapes)}"
            )

    elif shape is not None:
        # Unknown shape
        errors.append(f"Unknown shape type: '{shape}'")

    return errors


def validate_diagram_cells(cells: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    """
    Validate all cells in a diagram.

    Args:
        cells: List of cell dictionaries (nodes and edges)

    Returns:
        Dict mapping cell IDs to lists of error messages.
        Returns empty dict if all cells are valid.
    """
    errors_by_cell = {}

    if not cells:
        return errors_by_cell

    # Collect all cell IDs
    cell_ids = set()
    for cell in cells:
        cell_id = cell.get("id", "unknown")
        if cell_id in cell_ids:
            if cell_id not in errors_by_cell:
                errors_by_cell[cell_id] = []
            errors_by_cell[cell_id].append(f"Duplicate cell ID: {cell_id}")
        cell_ids.add(cell_id)

    # Validate each cell
    for cell in cells:
        cell_errors = validate_cell(cell)
        if cell_errors:
            cell_id = cell.get("id", "unknown")
            if cell_id not in errors_by_cell:
                errors_by_cell[cell_id] = []
            errors_by_cell[cell_id].extend(cell_errors)

    # Validate edge references
    for cell in cells:
        if cell.get("shape") == "edge":
            cell_id = cell.get("id", "unknown")

            # Check if source cell exists
            source = cell.get("source", {})
            if isinstance(source, dict):
                source_cell_id = source.get("cell")
                if source_cell_id and source_cell_id not in cell_ids:
                    if cell_id not in errors_by_cell:
                        errors_by_cell[cell_id] = []
                    errors_by_cell[cell_id].append(
                        f"Edge references non-existent source cell: {source_cell_id}"
                    )

            # Check if target cell exists
            target = cell.get("target", {})
            if isinstance(target, dict):
                target_cell_id = target.get("cell")
                if target_cell_id and target_cell_id not in cell_ids:
                    if cell_id not in errors_by_cell:
                        errors_by_cell[cell_id] = []
                    errors_by_cell[cell_id].append(
                        f"Edge references non-existent target cell: {target_cell_id}"
                    )

    return errors_by_cell
