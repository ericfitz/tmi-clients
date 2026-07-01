# TeamNote

Complete TeamNote schema with server-generated fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Note name | 
**content** | **str** | Note content in markdown format. Safe inline HTML (tables, SVG, formatting) is allowed and sanitized server-side; dangerous elements (script, iframe, event handlers) are stripped. | 
**description** | **str** | Description of note purpose or context | [optional] 
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**sharable** | **bool** | Controls note visibility. When true, visible to all team/project members. When false, only visible to admins and security reviewers. Only admins and security reviewers can set this field; regular users who include this field in requests will receive a 403 error. Default: true for regular users, false for admins/security reviewers. | [optional] 
**id** | **UUID** | Unique identifier for the team note | [readonly] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] [readonly] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] [readonly] 

## Example

```python
from tmi_client.models.team_note import TeamNote

# TODO update the JSON string below
json = "{}"
# create an instance of TeamNote from a JSON string
team_note_instance = TeamNote.from_json(json)
# print the JSON string representation of the object
print(TeamNote.to_json())

# convert the object into a dict
team_note_dict = team_note_instance.to_dict()
# create an instance of TeamNote from a dict
team_note_from_dict = TeamNote.from_dict(team_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


