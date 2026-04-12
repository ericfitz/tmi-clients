# DiagramListItem

Summary diagram object for GET /diagrams list endpoints. Excludes large fields (cells) for performance. Includes image for thumbnail rendering and description for display. Full diagram details available via GET /diagrams/{id} which returns DfdDiagram.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the diagram (UUID) | [readonly] 
**name** | **str** | Name of the diagram | 
**type** | **str** | Type of the diagram | 
**description** | **str** | Optional description of the diagram | [optional] 
**created_at** | **datetime** | Creation timestamp (ISO3339) | [readonly] 
**modified_at** | **datetime** | Last modification timestamp (ISO3339) | [readonly] 
**image** | [**DiagramListItemImage**](DiagramListItemImage.md) |  | [optional] 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**deleted_at** | **datetime** | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] [readonly] 

## Example

```python
from tmi_client.models.diagram_list_item import DiagramListItem

# TODO update the JSON string below
json = "{}"
# create an instance of DiagramListItem from a JSON string
diagram_list_item_instance = DiagramListItem.from_json(json)
# print the JSON string representation of the object
print(DiagramListItem.to_json())

# convert the object into a dict
diagram_list_item_dict = diagram_list_item_instance.to_dict()
# create an instance of DiagramListItem from a dict
diagram_list_item_from_dict = DiagramListItem.from_dict(diagram_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


