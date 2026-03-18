# TeamBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Team name | 
**description** | **str** | Team description | [optional] 
**members** | [**list[TeamMember]**](TeamMember.md) | List of team members with their roles | [optional] 
**responsible_parties** | [**list[ResponsibleParty]**](ResponsibleParty.md) | Responsible parties for this team (in lieu of owner) | [optional] 
**related_teams** | [**list[RelatedTeam]**](RelatedTeam.md) | Relationships to other teams | [optional] 
**uri** | **str** | URL or reference to internal team page | [optional] 
**email_address** | **str** | Team email address | [optional] 
**status** | **AllOfTeamBaseStatus** | Team lifecycle status. Defaults to &#x27;active&#x27; if not provided or set to null. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

