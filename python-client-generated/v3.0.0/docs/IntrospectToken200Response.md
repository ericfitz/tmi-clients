# IntrospectToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the token is active/valid | 
**sub** | **str** | Subject (user identifier) | [optional] 
**email** | **str** | User email address | [optional] 
**name** | **str** | User&#39;s full name | [optional] 
**exp** | **int** | Token expiration time (Unix timestamp) | [optional] 
**iat** | **int** | Token issued at time (Unix timestamp) | [optional] 
**iss** | **str** | Token issuer | [optional] 
**token_type** | **str** | Type of the token (RFC 7662) | [optional] 
**scope** | **str** | Space-separated list of scopes (RFC 7662) | [optional] 

## Example

```python
from tmi_client.models.introspect_token200_response import IntrospectToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of IntrospectToken200Response from a JSON string
introspect_token200_response_instance = IntrospectToken200Response.from_json(json)
# print the JSON string representation of the object
print(IntrospectToken200Response.to_json())

# convert the object into a dict
introspect_token200_response_dict = introspect_token200_response_instance.to_dict()
# create an instance of IntrospectToken200Response from a dict
introspect_token200_response_from_dict = IntrospectToken200Response.from_dict(introspect_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


