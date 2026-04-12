# IntrospectToken500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message describing what went wrong | 
**request_id** | **str** | Unique request identifier for troubleshooting | [optional] 

## Example

```python
from tmi_client.models.introspect_token500_response import IntrospectToken500Response

# TODO update the JSON string below
json = "{}"
# create an instance of IntrospectToken500Response from a JSON string
introspect_token500_response_instance = IntrospectToken500Response.from_json(json)
# print the JSON string representation of the object
print(IntrospectToken500Response.to_json())

# convert the object into a dict
introspect_token500_response_dict = introspect_token500_response_instance.to_dict()
# create an instance of IntrospectToken500Response from a dict
introspect_token500_response_from_dict = IntrospectToken500Response.from_dict(introspect_token500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


