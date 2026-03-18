# Project

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the project (UUID) | [optional] [default to null]
**Team** | [***interface{}**](interface{}.md) | The team this project belongs to (resolved) | [optional] [default to null]
**CreatedBy** | [***interface{}**](interface{}.md) | User who created the project | [optional] [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Creation timestamp (RFC3339) | [optional] [default to null]
**ModifiedBy** | [***interface{}**](interface{}.md) | User who last modified the project | [optional] [default to null]
**ModifiedAt** | [**time.Time**](time.Time.md) | Last modification timestamp (RFC3339) | [optional] [default to null]
**ReviewedBy** | [***interface{}**](interface{}.md) | User who last reviewed the project | [optional] [default to null]
**ReviewedAt** | [**time.Time**](time.Time.md) | Last review timestamp (RFC3339) | [optional] [default to null]
**Metadata** | [**[]Metadata**](Metadata.md) | Optional metadata key-value pairs | [optional] [default to null]
**Name** | **string** | Project name | [default to null]
**Description** | **string** | Project description | [optional] [default to null]
**TeamId** | **string** | UUID of the team this project belongs to | [default to null]
**ResponsibleParties** | [**[]ResponsibleParty**](ResponsibleParty.md) | Responsible parties for this project | [optional] [default to null]
**RelatedProjects** | [**[]RelatedProject**](RelatedProject.md) | Relationships to other projects | [optional] [default to null]
**Uri** | **string** | URL or reference to internal project page | [optional] [default to null]
**Status** | **string** | Project status (lifecycle, archival, deprecation, etc.) | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

