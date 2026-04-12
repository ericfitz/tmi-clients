# NoteInput

Input schema for creating or updating Note

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Note name | 
**content** | **str** | Note content in markdown format. Safe inline HTML (tables, SVG, formatting) is allowed and sanitized server-side; dangerous elements (script, iframe, event handlers) are stripped. | 
**description** | **str** | Description of note purpose or context | [optional] 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]

## Example

```python
from tmi_client.models.note_input import NoteInput

# TODO update the JSON string below
json = "{}"
# create an instance of NoteInput from a JSON string
note_input_instance = NoteInput.from_json(json)
# print the JSON string representation of the object
print(NoteInput.to_json())

# convert the object into a dict
note_input_dict = note_input_instance.to_dict()
# create an instance of NoteInput from a dict
note_input_from_dict = NoteInput.from_dict(note_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


