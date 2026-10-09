# SurveyResponseListItem

Summary of a survey response for list endpoints

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier for the response (UUID) | [readonly] 
**status** | **str** | Current status of the survey response | 
**is_confidential** | **bool** | Whether this is a secret project (no auto Security Reviewers access) | [optional] 
**owner** | [**User**](User.md) | User who created the response | [optional] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | 
**submitted_at** | **datetime** | When the response was submitted | [optional] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] 
**survey_id** | **UUID** | ID of the survey | 
**survey_name** | **str** | Name of the survey | [optional] 
**survey_version** | **str** | Version of the survey | [optional] 

## Example

```python
from tmi_client.models.survey_response_list_item import SurveyResponseListItem

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyResponseListItem from a JSON string
survey_response_list_item_instance = SurveyResponseListItem.from_json(json)
# print the JSON string representation of the object
print(SurveyResponseListItem.to_json())

# convert the object into a dict
survey_response_list_item_dict = survey_response_list_item_instance.to_dict()
# create an instance of SurveyResponseListItem from a dict
survey_response_list_item_from_dict = SurveyResponseListItem.from_dict(survey_response_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


