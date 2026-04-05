# TriageNoteBase

Base fields for TriageNote (user-writable only)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Triage note name | 
**content** | **str** | Triage note content in markdown format. Safe inline HTML (tables, SVG, formatting) is allowed and sanitized server-side; dangerous elements (script, iframe, event handlers) are stripped. | 

## Example

```python
from tmi_client.models.triage_note_base import TriageNoteBase

# TODO update the JSON string below
json = "{}"
# create an instance of TriageNoteBase from a JSON string
triage_note_base_instance = TriageNoteBase.from_json(json)
# print the JSON string representation of the object
print(TriageNoteBase.to_json())

# convert the object into a dict
triage_note_base_dict = triage_note_base_instance.to_dict()
# create an instance of TriageNoteBase from a dict
triage_note_base_from_dict = TriageNoteBase.from_dict(triage_note_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


