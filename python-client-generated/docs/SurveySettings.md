# SurveySettings

Configuration settings for a survey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_threat_model_linking** | **bool** | Whether responses can link to existing threat models for re-reviews | [optional] [default to True]

## Example

```python
from tmi_client.models.survey_settings import SurveySettings

# TODO update the JSON string below
json = "{}"
# create an instance of SurveySettings from a JSON string
survey_settings_instance = SurveySettings.from_json(json)
# print the JSON string representation of the object
print(SurveySettings.to_json())

# convert the object into a dict
survey_settings_dict = survey_settings_instance.to_dict()
# create an instance of SurveySettings from a dict
survey_settings_from_dict = SurveySettings.from_dict(survey_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


