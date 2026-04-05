# SurveyListItem

Summary of a survey for list responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier for the survey (UUID) | [readonly] 
**name** | **str** | Name of the survey | 
**description** | **str** | Description of the survey | [optional] 
**version** | **str** | Version string | 
**status** | **str** | Survey status | 
**created_at** | **datetime** | Creation timestamp (RFC3339) | 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] 
**created_by** | [**User**](User.md) | Administrator who created the survey | [optional] 

## Example

```python
from tmi_client.models.survey_list_item import SurveyListItem

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyListItem from a JSON string
survey_list_item_instance = SurveyListItem.from_json(json)
# print the JSON string representation of the object
print(SurveyListItem.to_json())

# convert the object into a dict
survey_list_item_dict = survey_list_item_instance.to_dict()
# create an instance of SurveyListItem from a dict
survey_list_item_from_dict = SurveyListItem.from_dict(survey_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


