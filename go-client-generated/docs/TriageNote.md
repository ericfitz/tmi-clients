# TriageNote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** | Sequential identifier for the triage note within its survey response | [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Creation timestamp (RFC3339) | [optional] [default to null]
**CreatedBy** | [***interface{}**](interface{}.md) | User who created this triage note | [optional] [default to null]
**ModifiedAt** | [**time.Time**](time.Time.md) | Last modification timestamp (RFC3339) | [optional] [default to null]
**ModifiedBy** | [***interface{}**](interface{}.md) | User who last modified this triage note | [optional] [default to null]
**Name** | **string** | Triage note name | [default to null]
**Content** | **string** | Triage note content in markdown format. Safe inline HTML (tables, SVG, formatting) is allowed and sanitized server-side; dangerous elements (script, iframe, event handlers) are stripped. | [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

