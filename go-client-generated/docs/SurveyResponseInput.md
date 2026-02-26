# SurveyResponseInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Answers** | [**ModelMap**](interface{}.md) | Question answers keyed by question name. Values can be any JSON type to support all SurveyJS question types including dynamic panels (arrays of objects), matrix questions (objects of objects), and scalar values (strings, numbers, booleans). | [optional] [default to null]
**LinkedThreatModelId** | **string** | Optional link to existing threat model for re-reviews | [optional] [default to null]
**Authorization** | [**[]Authorization**](Authorization.md) | List of users and groups with access to this response | [optional] [default to null]
**UiState** | [**ModelMap**](interface{}.md) | Client-managed UI state for draft resumption (e.g., current page, scroll position). Cleared on submission. | [optional] [default to null]
**SurveyId** | **string** | ID of the survey this response is based on | [default to null]
**SurveyVersion** | **string** | Survey version captured at creation time - responses always complete on the original version | [optional] [default to null]
**ProjectId** | **string** | Optional reference to the project this survey response belongs to | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

