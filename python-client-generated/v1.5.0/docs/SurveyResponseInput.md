# SurveyResponseInput

Input schema for updating a SurveyResponse

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

## Example

```python
from tmi_client.models.survey_response_input import SurveyResponseInput

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyResponseInput from a JSON string
survey_response_input_instance = SurveyResponseInput.from_json(json)
# print the JSON string representation of the object
print(SurveyResponseInput.to_json())

# convert the object into a dict
survey_response_input_dict = survey_response_input_instance.to_dict()
# create an instance of SurveyResponseInput from a dict
survey_response_input_from_dict = SurveyResponseInput.from_dict(survey_response_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


