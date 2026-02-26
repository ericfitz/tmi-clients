# SurveyResponseBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answers** | **dict(str, object)** | Question answers keyed by question name. Values can be any JSON type to support all SurveyJS question types including dynamic panels (arrays of objects), matrix questions (objects of objects), and scalar values (strings, numbers, booleans). | [optional] 
**linked_threat_model_id** | **str** | Optional link to existing threat model for re-reviews | [optional] 
**authorization** | [**list[Authorization]**](Authorization.md) | List of users and groups with access to this response | [optional] 
**ui_state** | **dict(str, object)** | Client-managed UI state for draft resumption (e.g., current page, scroll position). Cleared on submission. | [optional] 
**survey_id** | **str** | ID of the survey this response is based on | 
**survey_version** | **str** | Survey version captured at creation time - responses always complete on the original version | [optional] 
**project_id** | **str** | Optional reference to the project this survey response belongs to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

