# SurveyResponseListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the response (UUID) | [default to null]
**Status** | **string** | Current status of the survey response | [default to null]
**IsConfidential** | **bool** | Whether this is a secret project (no auto Security Reviewers access) | [optional] [default to null]
**Owner** | [***AllOfSurveyResponseListItemOwner**](AllOfSurveyResponseListItemOwner.md) | User who created the response | [optional] [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Creation timestamp (RFC3339) | [default to null]
**SubmittedAt** | [**time.Time**](time.Time.md) | When the response was submitted | [optional] [default to null]
**ModifiedAt** | [**time.Time**](time.Time.md) | Last modification timestamp (RFC3339) | [optional] [default to null]
**SurveyId** | **string** | ID of the survey | [default to null]
**SurveyName** | **string** | Name of the survey | [optional] [default to null]
**SurveyVersion** | **string** | Version of the survey | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

