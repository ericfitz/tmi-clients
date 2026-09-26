# TriageNoteInput

Input schema for creating a TriageNote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Triage note name | 
**content** | **str** | Triage note content in markdown format. Safe inline HTML (tables, SVG, formatting) is allowed and sanitized server-side; dangerous elements (script, iframe, event handlers) are stripped. | 

## Example

```python
from tmi_client.models.triage_note_input import TriageNoteInput

# TODO update the JSON string below
json = "{}"
# create an instance of TriageNoteInput from a JSON string
triage_note_input_instance = TriageNoteInput.from_json(json)
# print the JSON string representation of the object
print(TriageNoteInput.to_json())

# convert the object into a dict
triage_note_input_dict = triage_note_input_instance.to_dict()
# create an instance of TriageNoteInput from a dict
triage_note_input_from_dict = TriageNoteInput.from_dict(triage_note_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


