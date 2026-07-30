# GetSAMLProviders200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[SAMLProviderInfo]**](SAMLProviderInfo.md) |  | 

## Example

```python
from tmi_client.models.get_saml_providers200_response import GetSAMLProviders200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSAMLProviders200Response from a JSON string
get_saml_providers200_response_instance = GetSAMLProviders200Response.from_json(json)
# print the JSON string representation of the object
print(GetSAMLProviders200Response.to_json())

# convert the object into a dict
get_saml_providers200_response_dict = get_saml_providers200_response_instance.to_dict()
# create an instance of GetSAMLProviders200Response from a dict
get_saml_providers200_response_from_dict = GetSAMLProviders200Response.from_dict(get_saml_providers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


