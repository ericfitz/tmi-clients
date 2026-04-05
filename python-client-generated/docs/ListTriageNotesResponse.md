# ListTriageNotesResponse

Paginated list of triage notes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**triage_notes** | [**List[TriageNoteListItem]**](TriageNoteListItem.md) |  | 
**total** | **int** | Total number of triage notes | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_triage_notes_response import ListTriageNotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTriageNotesResponse from a JSON string
list_triage_notes_response_instance = ListTriageNotesResponse.from_json(json)
# print the JSON string representation of the object
print(ListTriageNotesResponse.to_json())

# convert the object into a dict
list_triage_notes_response_dict = list_triage_notes_response_instance.to_dict()
# create an instance of ListTriageNotesResponse from a dict
list_triage_notes_response_from_dict = ListTriageNotesResponse.from_dict(list_triage_notes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


