# TeamNoteListItem

Summary information for TeamNote in list responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier for the team note | [readonly] 
**name** | **str** | Note name | 
**description** | **str** | Description of note purpose or context | [optional] 
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**sharable** | **bool** | Controls note visibility | [optional] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] [readonly] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] [readonly] 

## Example

```python
from tmi_client.models.team_note_list_item import TeamNoteListItem

# TODO update the JSON string below
json = "{}"
# create an instance of TeamNoteListItem from a JSON string
team_note_list_item_instance = TeamNoteListItem.from_json(json)
# print the JSON string representation of the object
print(TeamNoteListItem.to_json())

# convert the object into a dict
team_note_list_item_dict = team_note_list_item_instance.to_dict()
# create an instance of TeamNoteListItem from a dict
team_note_list_item_from_dict = TeamNoteListItem.from_dict(team_note_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


