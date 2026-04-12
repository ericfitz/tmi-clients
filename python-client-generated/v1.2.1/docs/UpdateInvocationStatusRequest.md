# UpdateInvocationStatusRequest

Request to update the status of an async addon invocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | New status (cannot transition back to pending) | 
**status_percent** | **int** | Progress percentage | [optional] 
**status_message** | **str** | Optional status description | [optional] 

## Example

```python
from tmi_client.models.update_invocation_status_request import UpdateInvocationStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInvocationStatusRequest from a JSON string
update_invocation_status_request_instance = UpdateInvocationStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInvocationStatusRequest.to_json())

# convert the object into a dict
update_invocation_status_request_dict = update_invocation_status_request_instance.to_dict()
# create an instance of UpdateInvocationStatusRequest from a dict
update_invocation_status_request_from_dict = UpdateInvocationStatusRequest.from_dict(update_invocation_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


