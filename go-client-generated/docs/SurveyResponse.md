# SurveyResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the response (UUID) | [optional] [default to null]
**Status** | **string** | Current status of the survey response in the triage workflow | [optional] [default to null]
**IsConfidential** | **bool** | Whether Security Reviewers group was excluded (set at creation, read-only after) | [optional] [default to null]
**RevisionNotes** | **string** | Notes from security reviewer when returning for revision | [optional] [default to null]
**CreatedThreatModelId** | **string** | ID of threat model created from this response | [optional] [default to null]
**Owner** | [***interface{}**](interface{}.md) | User who created the response | [optional] [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Creation timestamp (RFC3339) | [optional] [default to null]
**ModifiedAt** | [**time.Time**](time.Time.md) | Last modification timestamp (RFC3339) | [optional] [default to null]
**SubmittedAt** | [**time.Time**](time.Time.md) | When the response was submitted for review | [optional] [default to null]
**ReviewedAt** | [**time.Time**](time.Time.md) | When the response was last reviewed | [optional] [default to null]
**ReviewedBy** | [***interface{}**](interface{}.md) | Security engineer who last reviewed the response | [optional] [default to null]
**SurveyJson** | [**ModelMap**](interface{}.md) | Snapshot of the survey survey_json at the time this response was created. Used to render historical responses against the correct survey version. | [optional] [default to null]
**Metadata** | [**[]Metadata**](Metadata.md) | Optional metadata key-value pairs | [optional] [default to null]
**CreatedBy** | [***interface{}**](interface{}.md) | User who created the response | [optional] [default to null]
**Answers** | [**ModelMap**](interface{}.md) | Question answers keyed by question name. Values can be any JSON type to support all SurveyJS question types including dynamic panels (arrays of objects), matrix questions (objects of objects), and scalar values (strings, numbers, booleans). | [optional] [default to null]
**LinkedThreatModelId** | **string** | Optional link to existing threat model for re-reviews | [optional] [default to null]
**Authorization** | [**[]Authorization**](Authorization.md) | List of users and groups with access to this response | [optional] [default to null]
**UiState** | [**ModelMap**](interface{}.md) | Client-managed UI state for draft resumption (e.g., current page, scroll position). Cleared on submission. | [optional] [default to null]
**SurveyId** | **string** | ID of the survey this response is based on | [default to null]
**SurveyVersion** | **string** | Survey version captured at creation time - responses always complete on the original version | [optional] [default to null]
**ProjectId** | **string** | Optional reference to the project this survey response belongs to | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

