# SurveyListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the survey (UUID) | [default to null]
**Name** | **string** | Name of the survey | [default to null]
**Description** | **string** | Description of the survey | [optional] [default to null]
**Version** | **string** | Version string | [default to null]
**Status** | **string** | Survey status | [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Creation timestamp (RFC3339) | [default to null]
**ModifiedAt** | [**time.Time**](time.Time.md) | Last modification timestamp (RFC3339) | [optional] [default to null]
**CreatedBy** | [***AllOfSurveyListItemCreatedBy**](AllOfSurveyListItemCreatedBy.md) | Administrator who created the survey | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

