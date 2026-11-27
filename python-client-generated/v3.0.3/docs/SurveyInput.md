# SurveyInput

Input schema for creating or updating Survey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the survey | 
**description** | **str** | Description of the survey and its purpose | [optional] 
**version** | **str** | Custom version string (e.g., &#39;2024-Q1&#39;, &#39;v2-pilot&#39;) | 
**status** | **str** | Survey status: active surveys appear in intake, inactive are hidden but editable, archived are read-only and preserved for historical reference | [optional] 
**settings** | [**SurveySettings**](SurveySettings.md) |  | [optional] 
**survey_json** | **Dict[str, object]** | Complete SurveyJS JSON definition. Opaque to the server; validated only for top-level structure (must contain a pages array). | 

## Example

```python
from tmi_client.models.survey_input import SurveyInput

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyInput from a JSON string
survey_input_instance = SurveyInput.from_json(json)
# print the JSON string representation of the object
print(SurveyInput.to_json())

# convert the object into a dict
survey_input_dict = survey_input_instance.to_dict()
# create an instance of SurveyInput from a dict
survey_input_from_dict = SurveyInput.from_dict(survey_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


