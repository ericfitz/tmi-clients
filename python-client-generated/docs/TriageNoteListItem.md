# TriageNoteListItem

Summary information for TriageNote in list responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Sequential identifier for the triage note within its survey response | [readonly] 
**name** | **str** | Triage note name | 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] [readonly] 
**created_by** | [**User**](User.md) | User who created this triage note | [optional] [readonly] 

## Example

```python
from tmi_client.models.triage_note_list_item import TriageNoteListItem

# TODO update the JSON string below
json = "{}"
# create an instance of TriageNoteListItem from a JSON string
triage_note_list_item_instance = TriageNoteListItem.from_json(json)
# print the JSON string representation of the object
print(TriageNoteListItem.to_json())

# convert the object into a dict
triage_note_list_item_dict = triage_note_list_item_instance.to_dict()
# create an instance of TriageNoteListItem from a dict
triage_note_list_item_from_dict = TriageNoteListItem.from_dict(triage_note_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


