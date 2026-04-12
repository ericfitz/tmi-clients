# NoteListItem

Summary information for Note in list responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Note name | 
**description** | **str** | Description of note purpose or context | [optional] 
**metadata** | [**List[Metadata]**](Metadata.md) | Key-value pairs for additional note metadata | [optional] 
**id** | **UUID** | Unique identifier for the note | [readonly] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] [readonly] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]

## Example

```python
from tmi_client.models.note_list_item import NoteListItem

# TODO update the JSON string below
json = "{}"
# create an instance of NoteListItem from a JSON string
note_list_item_instance = NoteListItem.from_json(json)
# print the JSON string representation of the object
print(NoteListItem.to_json())

# convert the object into a dict
note_list_item_dict = note_list_item_instance.to_dict()
# create an instance of NoteListItem from a dict
note_list_item_from_dict = NoteListItem.from_dict(note_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


