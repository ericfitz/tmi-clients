# ListTeamNotesResponse

Paginated list of team notes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | [**List[TeamNoteListItem]**](TeamNoteListItem.md) |  | 
**total** | **int** | Total number of team notes matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_team_notes_response import ListTeamNotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTeamNotesResponse from a JSON string
list_team_notes_response_instance = ListTeamNotesResponse.from_json(json)
# print the JSON string representation of the object
print(ListTeamNotesResponse.to_json())

# convert the object into a dict
list_team_notes_response_dict = list_team_notes_response_instance.to_dict()
# create an instance of ListTeamNotesResponse from a dict
list_team_notes_response_from_dict = ListTeamNotesResponse.from_dict(list_team_notes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


