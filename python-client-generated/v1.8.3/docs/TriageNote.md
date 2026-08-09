# TriageNote

Complete TriageNote schema with server-generated fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Triage note name | 
**content** | **str** | Triage note content in markdown format. Safe inline HTML (tables, SVG, formatting) is allowed and sanitized server-side; dangerous elements (script, iframe, event handlers) are stripped. | 
**id** | **int** | Sequential identifier for the triage note within its survey response | [readonly] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] [readonly] 
**created_by** | **object** | User who created this triage note | [optional] [readonly] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**modified_by** | **object** | User who last modified this triage note | [optional] [readonly] 

## Example

```python
from tmi_client.models.triage_note import TriageNote

# TODO update the JSON string below
json = "{}"
# create an instance of TriageNote from a JSON string
triage_note_instance = TriageNote.from_json(json)
# print the JSON string representation of the object
print(TriageNote.to_json())

# convert the object into a dict
triage_note_dict = triage_note_instance.to_dict()
# create an instance of TriageNote from a dict
triage_note_from_dict = TriageNote.from_dict(triage_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


