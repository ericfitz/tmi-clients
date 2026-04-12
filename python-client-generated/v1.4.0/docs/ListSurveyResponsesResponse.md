# ListSurveyResponsesResponse

Paginated list of survey responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**survey_responses** | [**List[SurveyResponseListItem]**](SurveyResponseListItem.md) |  | 
**total** | **int** | Total number of responses matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_survey_responses_response import ListSurveyResponsesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSurveyResponsesResponse from a JSON string
list_survey_responses_response_instance = ListSurveyResponsesResponse.from_json(json)
# print the JSON string representation of the object
print(ListSurveyResponsesResponse.to_json())

# convert the object into a dict
list_survey_responses_response_dict = list_survey_responses_response_instance.to_dict()
# create an instance of ListSurveyResponsesResponse from a dict
list_survey_responses_response_from_dict = ListSurveyResponsesResponse.from_dict(list_survey_responses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


