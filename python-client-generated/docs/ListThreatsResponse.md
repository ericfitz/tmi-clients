# ListThreatsResponse

Paginated list of threats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threats** | [**List[Threat]**](Threat.md) |  | 
**total** | **int** | Total number of threats matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_threats_response import ListThreatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListThreatsResponse from a JSON string
list_threats_response_instance = ListThreatsResponse.from_json(json)
# print the JSON string representation of the object
print(ListThreatsResponse.to_json())

# convert the object into a dict
list_threats_response_dict = list_threats_response_instance.to_dict()
# create an instance of ListThreatsResponse from a dict
list_threats_response_from_dict = ListThreatsResponse.from_dict(list_threats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


