# TimmyUsageResponse

Response containing Timmy usage records

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | [**List[TimmyUsageRecord]**](TimmyUsageRecord.md) |  | 
**total** | **int** | Total number of usage records | 

## Example

```python
from tmi_client.models.timmy_usage_response import TimmyUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TimmyUsageResponse from a JSON string
timmy_usage_response_instance = TimmyUsageResponse.from_json(json)
# print the JSON string representation of the object
print(TimmyUsageResponse.to_json())

# convert the object into a dict
timmy_usage_response_dict = timmy_usage_response_instance.to_dict()
# create an instance of TimmyUsageResponse from a dict
timmy_usage_response_from_dict = TimmyUsageResponse.from_dict(timmy_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


