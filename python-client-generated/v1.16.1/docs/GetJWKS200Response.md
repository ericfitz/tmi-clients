# GetJWKS200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[GetJWKS200ResponseKeysInner]**](GetJWKS200ResponseKeysInner.md) |  | 

## Example

```python
from tmi_client.models.get_jwks200_response import GetJWKS200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetJWKS200Response from a JSON string
get_jwks200_response_instance = GetJWKS200Response.from_json(json)
# print the JSON string representation of the object
print(GetJWKS200Response.to_json())

# convert the object into a dict
get_jwks200_response_dict = get_jwks200_response_instance.to_dict()
# create an instance of GetJWKS200Response from a dict
get_jwks200_response_from_dict = GetJWKS200Response.from_dict(get_jwks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


