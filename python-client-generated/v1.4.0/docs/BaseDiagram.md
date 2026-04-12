# BaseDiagram

Base diagram object with common properties - used for API responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier for the diagram (UUID) | [readonly] 
**name** | **str** | Name of the diagram | 
**type** | **str** | Type of diagram with version | 
**created_at** | **datetime** | Creation timestamp (ISO3339) | [readonly] 
**modified_at** | **datetime** | Last modification timestamp (ISO3339) | [readonly] 
**metadata** | [**List[Metadata]**](Metadata.md) | Key-value pairs for additional diagram metadata | [optional] 
**update_vector** | **int** | Server-managed monotonic version counter, incremented on each diagram update | [optional] [readonly] 
**image** | [**BaseDiagramImage**](BaseDiagramImage.md) |  | [optional] 
**description** | **str** | Optional description of the diagram | [optional] 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**deleted_at** | **datetime** | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] [readonly] 
**color_palette** | [**List[ColorPaletteEntry]**](ColorPaletteEntry.md) | Custom color palette for diagram elements, ordered by position | [optional] 

## Example

```python
from tmi_client.models.base_diagram import BaseDiagram

# TODO update the JSON string below
json = "{}"
# create an instance of BaseDiagram from a JSON string
base_diagram_instance = BaseDiagram.from_json(json)
# print the JSON string representation of the object
print(BaseDiagram.to_json())

# convert the object into a dict
base_diagram_dict = base_diagram_instance.to_dict()
# create an instance of BaseDiagram from a dict
base_diagram_from_dict = BaseDiagram.from_dict(base_diagram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


