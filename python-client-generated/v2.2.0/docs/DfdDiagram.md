# DfdDiagram

Data Flow Diagram with cells, edges, and visual styling for JointJS rendering

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier for the diagram (UUID) | [readonly] 
**name** | **str** | Name of the diagram | 
**type** | **str** | DFD diagram type with version | 
**created_at** | **datetime** | Creation timestamp (ISO3339) | [readonly] 
**modified_at** | **datetime** | Last modification timestamp (ISO3339) | [readonly] 
**metadata** | [**List[Metadata]**](Metadata.md) | Key-value pairs for additional diagram metadata | [optional] 
**update_vector** | **int** | Server-managed monotonic version counter, incremented on each diagram update | [optional] [readonly] 
**image** | [**DfdDiagramImage**](DfdDiagramImage.md) |  | [optional] 
**description** | **str** | Optional description of the diagram | [optional] 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**deleted_at** | **datetime** | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] [readonly] 
**color_palette** | [**List[ColorPaletteEntry]**](ColorPaletteEntry.md) | Custom color palette for diagram elements, ordered by position | [optional] 
**auto_generated** | **bool** | True when the diagram was created by an automation/service-account principal. Sticky from creation. | [optional] [readonly] 
**alias** | **int** | Server-assigned monotonically-increasing integer alias, unique within the parent threat model. Immutable after creation. | [optional] [readonly] 
**cells** | [**List[DfdDiagramCellsInner]**](DfdDiagramCellsInner.md) | List of diagram cells (nodes and edges) following X6 structure | 
**version** | **int** | Server-managed monotonically-increasing optimistic-locking version. Returned on reads and bumped by every successful PUT/PATCH. Clients echo this back via the If-Match request header (preferred) or the body &#39;version&#39; field on the next mutation. A mismatch returns 409 Conflict. See issue #385. | [optional] [readonly] 

## Example

```python
from tmi_client.models.dfd_diagram import DfdDiagram

# TODO update the JSON string below
json = "{}"
# create an instance of DfdDiagram from a JSON string
dfd_diagram_instance = DfdDiagram.from_json(json)
# print the JSON string representation of the object
print(DfdDiagram.to_json())

# convert the object into a dict
dfd_diagram_dict = dfd_diagram_instance.to_dict()
# create an instance of DfdDiagram from a dict
dfd_diagram_from_dict = DfdDiagram.from_dict(dfd_diagram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


