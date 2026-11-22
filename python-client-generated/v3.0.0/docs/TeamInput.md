# TeamInput

Client-writable fields for Team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Team name | 
**description** | **str** | Team description | [optional] 
**related_teams** | [**List[RelatedTeam]**](RelatedTeam.md) | Relationships to other teams | [optional] 
**uri** | **str** | URL or reference to internal team page | [optional] 
**email_address** | **str** | Team email address | [optional] 
**status** | [**TeamStatus**](TeamStatus.md) | Team lifecycle status. Defaults to &#39;active&#39; if not provided or set to null. | [optional] 
**members** | [**List[TeamMemberInput]**](TeamMemberInput.md) | List of team members with their roles | [optional] 
**responsible_parties** | [**List[ResponsiblePartyInput]**](ResponsiblePartyInput.md) | Responsible parties for this team (in lieu of owner) | [optional] 

## Example

```python
from tmi_client.models.team_input import TeamInput

# TODO update the JSON string below
json = "{}"
# create an instance of TeamInput from a JSON string
team_input_instance = TeamInput.from_json(json)
# print the JSON string representation of the object
print(TeamInput.to_json())

# convert the object into a dict
team_input_dict = team_input_instance.to_dict()
# create an instance of TeamInput from a dict
team_input_from_dict = TeamInput.from_dict(team_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


