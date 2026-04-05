# Survey

A survey defining questions for security review intake

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the survey | 
**description** | **str** | Description of the survey and its purpose | [optional] 
**version** | **str** | Custom version string (e.g., &#39;2024-Q1&#39;, &#39;v2-pilot&#39;) | 
**status** | **str** | Survey status: active surveys appear in intake, inactive are hidden but editable, archived are read-only and preserved for historical reference | [optional] 
**settings** | [**SurveySettings**](SurveySettings.md) |  | [optional] 
**survey_json** | **Dict[str, object]** | Complete SurveyJS JSON definition. Opaque to the server; validated only for top-level structure (must contain a pages array). | 
**id** | **UUID** | Unique identifier for the survey (UUID) | [optional] [readonly] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] [readonly] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**created_by** | [**User**](User.md) | Administrator who created the survey | [optional] [readonly] 
**metadata** | [**List[Metadata]**](Metadata.md) | Optional metadata key-value pairs | [optional] 

## Example

```python
from tmi_client.models.survey import Survey

# TODO update the JSON string below
json = "{}"
# create an instance of Survey from a JSON string
survey_instance = Survey.from_json(json)
# print the JSON string representation of the object
print(Survey.to_json())

# convert the object into a dict
survey_dict = survey_instance.to_dict()
# create an instance of Survey from a dict
survey_from_dict = Survey.from_dict(survey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


