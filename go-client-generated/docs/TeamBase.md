# TeamBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Team name | [default to null]
**Description** | **string** | Team description | [optional] [default to null]
**Members** | [**[]TeamMember**](TeamMember.md) | List of team members with their roles | [optional] [default to null]
**ResponsibleParties** | [**[]ResponsibleParty**](ResponsibleParty.md) | Responsible parties for this team (in lieu of owner) | [optional] [default to null]
**RelatedTeams** | [**[]RelatedTeam**](RelatedTeam.md) | Relationships to other teams | [optional] [default to null]
**Uri** | **string** | URL or reference to internal team page | [optional] [default to null]
**EmailAddress** | **string** | Team email address | [optional] [default to null]
**Status** | **AllOfTeamBaseStatus** | Team lifecycle status. Defaults to &#x27;active&#x27; if not provided or set to null. | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

