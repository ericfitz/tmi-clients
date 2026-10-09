# ListDiagramsResponse

Paginated list of diagrams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diagrams** | [**List[DiagramListItem]**](DiagramListItem.md) |  | 
**total** | **int** | Total number of diagrams matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_diagrams_response import ListDiagramsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDiagramsResponse from a JSON string
list_diagrams_response_instance = ListDiagramsResponse.from_json(json)
# print the JSON string representation of the object
print(ListDiagramsResponse.to_json())

# convert the object into a dict
list_diagrams_response_dict = list_diagrams_response_instance.to_dict()
# create an instance of ListDiagramsResponse from a dict
list_diagrams_response_from_dict = ListDiagramsResponse.from_dict(list_diagrams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


