# SurveyResponseCreateRequest

Request to create a new survey response, combining base fields with creation-specific options

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
**is_confidential** | **bool** | If true, Security Reviewers group is NOT auto-added. Can only be set at creation. | [optional] [default to False]

## Example

```python
from tmi_client.models.survey_response_create_request import SurveyResponseCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyResponseCreateRequest from a JSON string
survey_response_create_request_instance = SurveyResponseCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SurveyResponseCreateRequest.to_json())

# convert the object into a dict
survey_response_create_request_dict = survey_response_create_request_instance.to_dict()
# create an instance of SurveyResponseCreateRequest from a dict
survey_response_create_request_from_dict = SurveyResponseCreateRequest.from_dict(survey_response_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


