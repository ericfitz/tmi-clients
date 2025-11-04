# coding: utf-8

"""
Type-Safe TMI API Client

Provides a wrapper around the TMI API client that ensures all responses
are properly typed model objects, never dicts. This eliminates the need
for isinstance() checks and provides a more predictable API.
"""

from typing import List, Optional

from tmi_client.api.threat_model_sub_resources_api import ThreatModelSubResourcesApi
from tmi_client.models.dfd_diagram import DfdDiagram
from tmi_client.models.diagram_list_item import DiagramListItem
from tmi_client.models.create_diagram_request import CreateDiagramRequest


class TypeSafeTMIClient:
    """
    Type-safe wrapper around TMI API client.

    Ensures all responses are properly deserialized to model objects, providing
    consistent typing and eliminating the need for runtime type checks.

    Example:
        >>> from tmi_client import ApiClient, Configuration
        >>> config = Configuration()
        >>> config.api_key['bearerAuth'] = 'your-token'
        >>> client = TypeSafeTMIClient(ApiClient(config))
        >>>
        >>> # All methods return properly typed objects
        >>> diagrams = client.list_diagrams(threat_model_id)
        >>> for diagram in diagrams:
        ...     print(diagram.id)  # Always works, no isinstance check needed
    """

    def __init__(self, api_client):
        """
        Initialize the type-safe client.

        Args:
            api_client: Configured ApiClient instance with authentication
        """
        self.api = ThreatModelSubResourcesApi(api_client)

    def list_diagrams(self, threat_model_id: str) -> List[DiagramListItem]:
        """
        List all diagrams for a threat model.

        Args:
            threat_model_id: Threat model UUID

        Returns:
            List of DiagramListItem objects (never dicts)

        Raises:
            ApiException: If the API request fails
        """
        result = self.api.get_threat_model_diagrams(threat_model_id)

        # Ensure proper typing
        if not isinstance(result, list):
            # If single item returned, wrap in list
            result = [result] if result else []

        typed_result = []
        for item in result:
            if isinstance(item, dict):
                # Convert dict to DiagramListItem
                typed_result.append(DiagramListItem(**item))
            elif isinstance(item, DiagramListItem):
                typed_result.append(item)
            else:
                # Unknown type, try to convert
                typed_result.append(DiagramListItem(**item.to_dict()))

        return typed_result

    def get_diagram(
        self,
        threat_model_id: str,
        diagram_id: str
    ) -> DfdDiagram:
        """
        Get a specific diagram.

        Args:
            threat_model_id: Threat model UUID
            diagram_id: Diagram UUID

        Returns:
            DfdDiagram object (never dict)

        Raises:
            ApiException: If the API request fails
        """
        result = self.api.get_threat_model_diagram(threat_model_id, diagram_id)

        # Ensure proper typing
        if isinstance(result, dict):
            return DfdDiagram(**result)
        elif isinstance(result, DfdDiagram):
            return result
        else:
            # Unknown type, try to convert
            return DfdDiagram(**result.to_dict())

    def create_diagram(
        self,
        threat_model_id: str,
        name: str,
        diagram_type: str = "DFD-1.0.0"
    ) -> DfdDiagram:
        """
        Create a new diagram.

        Args:
            threat_model_id: Threat model UUID
            name: Diagram name
            diagram_type: Diagram type (default: "DFD-1.0.0")

        Returns:
            DfdDiagram object (never dict)

        Raises:
            ApiException: If the API request fails
        """
        request = CreateDiagramRequest(name=name, type=diagram_type)
        result = self.api.create_threat_model_diagram(request, threat_model_id)

        # Ensure proper typing
        if isinstance(result, dict):
            return DfdDiagram(**result)
        elif isinstance(result, DfdDiagram):
            return result
        else:
            # Unknown type, try to convert
            return DfdDiagram(**result.to_dict())

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
            diagram: DfdDiagram object with updated content

        Returns:
            Updated DfdDiagram object (never dict)

        Raises:
            ApiException: If the API request fails
        """
        result = self.api.update_threat_model_diagram(
            diagram, threat_model_id, diagram_id
        )

        # Ensure proper typing
        if isinstance(result, dict):
            return DfdDiagram(**result)
        elif isinstance(result, DfdDiagram):
            return result
        else:
            # Unknown type, try to convert
            return DfdDiagram(**result.to_dict())

    def delete_diagram(
        self,
        threat_model_id: str,
        diagram_id: str
    ) -> None:
        """
        Delete a diagram.

        Args:
            threat_model_id: Threat model UUID
            diagram_id: Diagram UUID

        Raises:
            ApiException: If the API request fails
        """
        self.api.delete_threat_model_diagram(threat_model_id, diagram_id)
