# SurveyResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the response (UUID) | [optional] 
**status** | **str** | Current status of the survey response in the triage workflow | [optional] 
**is_confidential** | **bool** | Whether Security Reviewers group was excluded (set at creation, read-only after) | [optional] 
**revision_notes** | **str** | Notes from security reviewer when returning for revision | [optional] 
**created_threat_model_id** | **str** | ID of threat model created from this response | [optional] 
**owner** | **object** | User who created the response | [optional] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] 
**submitted_at** | **datetime** | When the response was submitted for review | [optional] 
**reviewed_at** | **datetime** | When the response was last reviewed | [optional] 
**reviewed_by** | **object** | Security engineer who last reviewed the response | [optional] 
**survey_json** | **dict(str, object)** | Snapshot of the survey survey_json at the time this response was created. Used to render historical responses against the correct survey version. | [optional] 
**metadata** | [**list[Metadata]**](Metadata.md) | Optional metadata key-value pairs | [optional] 
**created_by** | **object** | User who created the response | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

