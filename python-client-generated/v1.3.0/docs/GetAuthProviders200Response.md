# GetAuthProviders200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[GetAuthProviders200ResponseProvidersInner]**](GetAuthProviders200ResponseProvidersInner.md) |  | 

## Example

```python
from tmi_client.models.get_auth_providers200_response import GetAuthProviders200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthProviders200Response from a JSON string
get_auth_providers200_response_instance = GetAuthProviders200Response.from_json(json)
# print the JSON string representation of the object
print(GetAuthProviders200Response.to_json())

# convert the object into a dict
get_auth_providers200_response_dict = get_auth_providers200_response_instance.to_dict()
# create an instance of GetAuthProviders200Response from a dict
get_auth_providers200_response_from_dict = GetAuthProviders200Response.from_dict(get_auth_providers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


