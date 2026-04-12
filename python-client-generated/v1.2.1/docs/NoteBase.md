# NoteBase

Base fields for Note (user-writable only)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Note name | 
**content** | **str** | Note content in markdown format. Safe inline HTML (tables, SVG, formatting) is allowed and sanitized server-side; dangerous elements (script, iframe, event handlers) are stripped. | 
**description** | **str** | Description of note purpose or context | [optional] 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]

## Example

```python
from tmi_client.models.note_base import NoteBase

# TODO update the JSON string below
json = "{}"
# create an instance of NoteBase from a JSON string
note_base_instance = NoteBase.from_json(json)
# print the JSON string representation of the object
print(NoteBase.to_json())

# convert the object into a dict
note_base_dict = note_base_instance.to_dict()
# create an instance of NoteBase from a dict
note_base_from_dict = NoteBase.from_dict(note_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


