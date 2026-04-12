# InvocationResponse

Status and result of an addon invocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Invocation identifier | 
**addon_id** | **UUID** | Add-on that was invoked | 
**threat_model_id** | **UUID** | Threat model context | 
**object_type** | **str** | Object type (if specified) | [optional] 
**object_id** | **UUID** | Object ID (if specified) | [optional] 
**invoked_by** | [**User**](User.md) | User who triggered the invocation | 
**status** | **str** | Current status | 
**status_percent** | **int** | Progress percentage (0-100) | 
**status_message** | **str** | Optional status description | [optional] 
**created_at** | **datetime** | Creation timestamp | 
**status_updated_at** | **datetime** | Last status update timestamp | 
**data** | **str** | JSON-encoded data | [optional] 

## Example

```python
from tmi_client.models.invocation_response import InvocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvocationResponse from a JSON string
invocation_response_instance = InvocationResponse.from_json(json)
# print the JSON string representation of the object
print(InvocationResponse.to_json())

# convert the object into a dict
invocation_response_dict = invocation_response_instance.to_dict()
# create an instance of InvocationResponse from a dict
invocation_response_from_dict = InvocationResponse.from_dict(invocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


