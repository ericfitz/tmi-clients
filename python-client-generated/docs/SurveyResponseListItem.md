# SurveyResponseListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the response (UUID) | 
**status** | **str** | Current status of the survey response | 
**is_confidential** | **bool** | Whether this is a secret project (no auto Security Reviewers access) | [optional] 
**owner** | **AllOfSurveyResponseListItemOwner** | User who created the response | [optional] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | 
**submitted_at** | **datetime** | When the response was submitted | [optional] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] 
**survey_id** | **str** | ID of the survey | 
**survey_name** | **str** | Name of the survey | [optional] 
**survey_version** | **str** | Version of the survey | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

