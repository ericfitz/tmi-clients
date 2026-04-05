# SAMLProviderInfo

SAML identity provider configuration and metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Provider identifier | 
**name** | **str** | Display name of the provider | 
**icon** | **str** | Icon identifier for the provider (Font Awesome class, URL, or path) | 
**auth_url** | **str** | TMI SAML login endpoint URL | 
**metadata_url** | **str** | SAML service provider metadata URL | 
**entity_id** | **str** | Service Provider entity ID | 
**acs_url** | **str** | Assertion Consumer Service URL | 
**slo_url** | **str** | Single Logout URL | [optional] 
**initialized** | **bool** | Whether the SAML provider was successfully initialized and is available for authentication | 

## Example

```python
from tmi_client.models.saml_provider_info import SAMLProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLProviderInfo from a JSON string
saml_provider_info_instance = SAMLProviderInfo.from_json(json)
# print the JSON string representation of the object
print(SAMLProviderInfo.to_json())

# convert the object into a dict
saml_provider_info_dict = saml_provider_info_instance.to_dict()
# create an instance of SAMLProviderInfo from a dict
saml_provider_info_from_dict = SAMLProviderInfo.from_dict(saml_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


