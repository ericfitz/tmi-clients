# TmiJsClient.SurveyResponseBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answers** | **{String: Object}** | Question answers keyed by question name. Values can be any JSON type to support all SurveyJS question types including dynamic panels (arrays of objects), matrix questions (objects of objects), and scalar values (strings, numbers, booleans). | [optional] 
**linkedThreatModelId** | **String** | Optional link to existing threat model for re-reviews | [optional] 
**authorization** | [**[Authorization]**](Authorization.md) | List of users and groups with access to this response | [optional] 
**uiState** | **{String: Object}** | Client-managed UI state for draft resumption (e.g., current page, scroll position). Cleared on submission. | [optional] 
**surveyId** | **String** | ID of the survey this response is based on | 
**surveyVersion** | **String** | Survey version captured at creation time - responses always complete on the original version | [optional] 
**projectId** | **String** | Optional reference to the project this survey response belongs to | [optional] 
