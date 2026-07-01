# ListProjectNotesResponse

Paginated list of project notes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | [**List[ProjectNoteListItem]**](ProjectNoteListItem.md) |  | 
**total** | **int** | Total number of project notes matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_project_notes_response import ListProjectNotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListProjectNotesResponse from a JSON string
list_project_notes_response_instance = ListProjectNotesResponse.from_json(json)
# print the JSON string representation of the object
print(ListProjectNotesResponse.to_json())

# convert the object into a dict
list_project_notes_response_dict = list_project_notes_response_instance.to_dict()
# create an instance of ListProjectNotesResponse from a dict
list_project_notes_response_from_dict = ListProjectNotesResponse.from_dict(list_project_notes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


