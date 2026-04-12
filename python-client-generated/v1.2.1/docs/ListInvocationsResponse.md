# ListInvocationsResponse

Paginated list of addon invocations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invocations** | [**List[InvocationResponse]**](InvocationResponse.md) |  | 
**total** | **int** | Total number of invocations | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_invocations_response import ListInvocationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListInvocationsResponse from a JSON string
list_invocations_response_instance = ListInvocationsResponse.from_json(json)
# print the JSON string representation of the object
print(ListInvocationsResponse.to_json())

# convert the object into a dict
list_invocations_response_dict = list_invocations_response_instance.to_dict()
# create an instance of ListInvocationsResponse from a dict
list_invocations_response_from_dict = ListInvocationsResponse.from_dict(list_invocations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


