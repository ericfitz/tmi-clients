# TeamProjectNoteBase

Base fields for TeamProjectNote (user-writable only)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Note name | 
**content** | **str** | Note content in markdown format. Safe inline HTML (tables, SVG, formatting) is allowed and sanitized server-side; dangerous elements (script, iframe, event handlers) are stripped. | 
**description** | **str** | Description of note purpose or context | [optional] 
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**sharable** | **bool** | Controls note visibility. When true, visible to all team/project members. When false, only visible to admins and security reviewers. Only admins and security reviewers can set this field; regular users who include this field in requests will receive a 403 error. Default: true for regular users, false for admins/security reviewers. | [optional] 

## Example

```python
from tmi_client.models.team_project_note_base import TeamProjectNoteBase

# TODO update the JSON string below
json = "{}"
# create an instance of TeamProjectNoteBase from a JSON string
team_project_note_base_instance = TeamProjectNoteBase.from_json(json)
# print the JSON string representation of the object
print(TeamProjectNoteBase.to_json())

# convert the object into a dict
team_project_note_base_dict = team_project_note_base_instance.to_dict()
# create an instance of TeamProjectNoteBase from a dict
team_project_note_base_from_dict = TeamProjectNoteBase.from_dict(team_project_note_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


