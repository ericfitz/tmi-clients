# CreateThreatModelFromSurveyResponse

Response after creating a threat model from a survey response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threat_model_id** | **UUID** | ID of the newly created threat model | 
**survey_response_id** | **UUID** | ID of the source survey response | 

## Example

```python
from tmi_client.models.create_threat_model_from_survey_response import CreateThreatModelFromSurveyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateThreatModelFromSurveyResponse from a JSON string
create_threat_model_from_survey_response_instance = CreateThreatModelFromSurveyResponse.from_json(json)
# print the JSON string representation of the object
print(CreateThreatModelFromSurveyResponse.to_json())

# convert the object into a dict
create_threat_model_from_survey_response_dict = create_threat_model_from_survey_response_instance.to_dict()
# create an instance of CreateThreatModelFromSurveyResponse from a dict
create_threat_model_from_survey_response_from_dict = CreateThreatModelFromSurveyResponse.from_dict(create_threat_model_from_survey_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


