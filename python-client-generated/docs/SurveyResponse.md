# SurveyResponse

A survey response containing answers to survey questions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answers** | **Dict[str, object]** | Question answers keyed by question name. Values can be any JSON type to support all SurveyJS question types including dynamic panels (arrays of objects), matrix questions (objects of objects), and scalar values (strings, numbers, booleans). | [optional] 
**linked_threat_model_id** | **UUID** | Optional link to existing threat model for re-reviews | [optional] 
**authorization** | [**List[Authorization]**](Authorization.md) | List of users and groups with access to this response | [optional] 
**ui_state** | **Dict[str, object]** | Client-managed UI state for draft resumption (e.g., current page, scroll position). Cleared on submission. | [optional] 
**survey_id** | **UUID** | ID of the survey this response is based on | 
**survey_version** | **str** | Survey version captured at creation time - responses always complete on the original version | [optional] [readonly] 
**project_id** | **UUID** | Optional reference to the project this survey response belongs to | [optional] 
**id** | **UUID** | Unique identifier for the response (UUID) | [optional] [readonly] 
**status** | **str** | Current status of the survey response in the triage workflow | [optional] 
**is_confidential** | **bool** | Whether Security Reviewers group was excluded (set at creation, read-only after) | [optional] [readonly] 
**revision_notes** | **str** | Notes from security reviewer when returning for revision | [optional] [readonly] 
**created_threat_model_id** | **UUID** | ID of threat model created from this response | [optional] [readonly] 
**owner** | **object** | User who created the response | [optional] [readonly] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] [readonly] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**submitted_at** | **datetime** | When the response was submitted for review | [optional] [readonly] 
**reviewed_at** | **datetime** | When the response was last reviewed | [optional] [readonly] 
**reviewed_by** | **object** | Security engineer who last reviewed the response | [optional] [readonly] 
**survey_json** | **Dict[str, object]** | Snapshot of the survey survey_json at the time this response was created. Used to render historical responses against the correct survey version. | [optional] [readonly] 
**metadata** | [**List[Metadata]**](Metadata.md) | Optional metadata key-value pairs | [optional] 
**created_by** | **object** | User who created the response | [optional] [readonly] 

## Example

```python
from tmi_client.models.survey_response import SurveyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyResponse from a JSON string
survey_response_instance = SurveyResponse.from_json(json)
# print the JSON string representation of the object
print(SurveyResponse.to_json())

# convert the object into a dict
survey_response_dict = survey_response_instance.to_dict()
# create an instance of SurveyResponse from a dict
survey_response_from_dict = SurveyResponse.from_dict(survey_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


