# TeamMemberInput

Client-writable fields of TeamMember (excludes the server-resolved user).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** | UUID of the team member user | 
**role** | [**TeamMemberRole**](TeamMemberRole.md) |  | [optional] 
**custom_role** | **str** | Custom role description when role is &#39;other&#39; | [optional] 

## Example

```python
from tmi_client.models.team_member_input import TeamMemberInput

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMemberInput from a JSON string
team_member_input_instance = TeamMemberInput.from_json(json)
# print the JSON string representation of the object
print(TeamMemberInput.to_json())

# convert the object into a dict
team_member_input_dict = team_member_input_instance.to_dict()
# create an instance of TeamMemberInput from a dict
team_member_input_from_dict = TeamMemberInput.from_dict(team_member_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


