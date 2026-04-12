# Team

A team representing an organizational unit

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
**status** | **str** | Team status (lifecycle, archival, deprecation, etc.) | [optional] 
**id** | **UUID** | Unique identifier for the team (UUID) | [optional] [readonly] 
**created_by** | **object** | User who created the team | [optional] [readonly] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] [readonly] 
**modified_by** | **object** | User who last modified the team | [optional] [readonly] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**reviewed_by** | **object** | User who last reviewed the team | [optional] 
**reviewed_at** | **datetime** | Last review timestamp (RFC3339) | [optional] 
**metadata** | [**List[Metadata]**](Metadata.md) | Optional metadata key-value pairs | [optional] 

## Example

```python
from tmi_client.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print(Team.to_json())

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_from_dict = Team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


