# GetJWKS200ResponseKeysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kty** | **str** |  | 
**use** | **str** |  | 
**alg** | **str** |  | 
**kid** | **str** |  | 

## Example

```python
from tmi_client.models.get_jwks200_response_keys_inner import GetJWKS200ResponseKeysInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetJWKS200ResponseKeysInner from a JSON string
get_jwks200_response_keys_inner_instance = GetJWKS200ResponseKeysInner.from_json(json)
# print the JSON string representation of the object
print(GetJWKS200ResponseKeysInner.to_json())

# convert the object into a dict
get_jwks200_response_keys_inner_dict = get_jwks200_response_keys_inner_instance.to_dict()
# create an instance of GetJWKS200ResponseKeysInner from a dict
get_jwks200_response_keys_inner_from_dict = GetJWKS200ResponseKeysInner.from_dict(get_jwks200_response_keys_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


