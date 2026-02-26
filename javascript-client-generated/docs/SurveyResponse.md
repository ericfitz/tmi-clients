# TmiJsClient.SurveyResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique identifier for the response (UUID) | [optional] 
**status** | **String** | Current status of the survey response in the triage workflow | [optional] 
**isConfidential** | **Boolean** | Whether Security Reviewers group was excluded (set at creation, read-only after) | [optional] 
**revisionNotes** | **String** | Notes from security reviewer when returning for revision | [optional] 
**createdThreatModelId** | **String** | ID of threat model created from this response | [optional] 
**owner** | **Object** | User who created the response | [optional] 
**createdAt** | **Date** | Creation timestamp (RFC3339) | [optional] 
**modifiedAt** | **Date** | Last modification timestamp (RFC3339) | [optional] 
**submittedAt** | **Date** | When the response was submitted for review | [optional] 
**reviewedAt** | **Date** | When the response was last reviewed | [optional] 
**reviewedBy** | **Object** | Security engineer who last reviewed the response | [optional] 
**surveyJson** | **{String: Object}** | Snapshot of the survey survey_json at the time this response was created. Used to render historical responses against the correct survey version. | [optional] 
**metadata** | [**[Metadata]**](Metadata.md) | Optional metadata key-value pairs | [optional] 
**createdBy** | **Object** | User who created the response | [optional] 
