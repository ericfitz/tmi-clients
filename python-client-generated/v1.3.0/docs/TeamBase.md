# TeamBase

Client-writable fields for a team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Team name | 
**description** | **str** | Team description | [optional] 
**members** | [**List[TeamMember]**](TeamMember.md) | List of team members with their roles | [optional] 
**responsible_parties** | [**List[ResponsibleParty]**](ResponsibleParty.md) | Responsible parties for this team (in lieu of owner) | [optional] 
**related_teams** | [**List[RelatedTeam]**](RelatedTeam.md) | Relationships to other teams | [optional] 
**uri** | **str** | URL or reference to internal team page | [optional] 
**email_address** | **str** | Team email address | [optional] 
**status** | [**TeamStatus**](TeamStatus.md) | Team lifecycle status. Defaults to &#39;active&#39; if not provided or set to null. | [optional] 

## Example

```python
from tmi_client.models.team_base import TeamBase

# TODO update the JSON string below
json = "{}"
# create an instance of TeamBase from a JSON string
team_base_instance = TeamBase.from_json(json)
# print the JSON string representation of the object
print(TeamBase.to_json())

# convert the object into a dict
team_base_dict = team_base_instance.to_dict()
# create an instance of TeamBase from a dict
team_base_from_dict = TeamBase.from_dict(team_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


