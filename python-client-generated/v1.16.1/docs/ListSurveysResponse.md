# ListSurveysResponse

Paginated list of surveys

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of surveys matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 
**surveys** | [**List[SurveyListItem]**](SurveyListItem.md) |  | 

## Example

```python
from tmi_client.models.list_surveys_response import ListSurveysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSurveysResponse from a JSON string
list_surveys_response_instance = ListSurveysResponse.from_json(json)
# print the JSON string representation of the object
print(ListSurveysResponse.to_json())

# convert the object into a dict
list_surveys_response_dict = list_surveys_response_instance.to_dict()
# create an instance of ListSurveysResponse from a dict
list_surveys_response_from_dict = ListSurveysResponse.from_dict(list_surveys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


