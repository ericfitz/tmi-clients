# UpdateInvocationStatusResponse

Response confirming invocation status update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Invocation identifier | 
**status** | **str** | Current status | 
**status_percent** | **int** | Progress percentage | 
**status_updated_at** | **datetime** | Status update timestamp | 

## Example

```python
from tmi_client.models.update_invocation_status_response import UpdateInvocationStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInvocationStatusResponse from a JSON string
update_invocation_status_response_instance = UpdateInvocationStatusResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateInvocationStatusResponse.to_json())

# convert the object into a dict
update_invocation_status_response_dict = update_invocation_status_response_instance.to_dict()
# create an instance of UpdateInvocationStatusResponse from a dict
update_invocation_status_response_from_dict = UpdateInvocationStatusResponse.from_dict(update_invocation_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


