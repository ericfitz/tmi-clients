# TmiJsClient.SurveyResponseListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique identifier for the response (UUID) | 
**status** | **String** | Current status of the survey response | 
**isConfidential** | **Boolean** | Whether this is a secret project (no auto Security Reviewers access) | [optional] 
**owner** | **AllOfSurveyResponseListItemOwner** | User who created the response | [optional] 
**createdAt** | **Date** | Creation timestamp (RFC3339) | 
**submittedAt** | **Date** | When the response was submitted | [optional] 
**modifiedAt** | **Date** | Last modification timestamp (RFC3339) | [optional] 
**surveyId** | **String** | ID of the survey | 
**surveyName** | **String** | Name of the survey | [optional] 
**surveyVersion** | **String** | Version of the survey | [optional] 
