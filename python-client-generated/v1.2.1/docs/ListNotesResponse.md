# ListNotesResponse

Paginated list of notes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | [**List[NoteListItem]**](NoteListItem.md) |  | 
**total** | **int** | Total number of notes matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_notes_response import ListNotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotesResponse from a JSON string
list_notes_response_instance = ListNotesResponse.from_json(json)
# print the JSON string representation of the object
print(ListNotesResponse.to_json())

# convert the object into a dict
list_notes_response_dict = list_notes_response_instance.to_dict()
# create an instance of ListNotesResponse from a dict
list_notes_response_from_dict = ListNotesResponse.from_dict(list_notes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


