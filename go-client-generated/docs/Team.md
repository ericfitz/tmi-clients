# Team

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the team (UUID) | [optional] [default to null]
**CreatedBy** | [***interface{}**](interface{}.md) | User who created the team | [optional] [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Creation timestamp (RFC3339) | [optional] [default to null]
**ModifiedBy** | [***interface{}**](interface{}.md) | User who last modified the team | [optional] [default to null]
**ModifiedAt** | [**time.Time**](time.Time.md) | Last modification timestamp (RFC3339) | [optional] [default to null]
**ReviewedBy** | [***interface{}**](interface{}.md) | User who last reviewed the team | [optional] [default to null]
**ReviewedAt** | [**time.Time**](time.Time.md) | Last review timestamp (RFC3339) | [optional] [default to null]
**Metadata** | [**[]Metadata**](Metadata.md) | Optional metadata key-value pairs | [optional] [default to null]
**Name** | **string** | Team name | [default to null]
**Description** | **string** | Team description | [optional] [default to null]
**Members** | [**[]TeamMember**](TeamMember.md) | List of team members with their roles | [optional] [default to null]
**ResponsibleParties** | [**[]ResponsibleParty**](ResponsibleParty.md) | Responsible parties for this team (in lieu of owner) | [optional] [default to null]
**RelatedTeams** | [**[]RelatedTeam**](RelatedTeam.md) | Relationships to other teams | [optional] [default to null]
**Uri** | **string** | URL or reference to internal team page | [optional] [default to null]
**EmailAddress** | **string** | Team email address | [optional] [default to null]
**Status** | **string** | Team status (lifecycle, archival, deprecation, etc.) | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

