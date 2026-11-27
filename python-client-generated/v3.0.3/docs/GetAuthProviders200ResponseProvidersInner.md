# GetAuthProviders200ResponseProvidersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Provider identifier | 
**name** | **str** | Display name of the provider | 
**icon** | **str** | Icon identifier for the provider | 
**auth_url** | **str** | TMI authorization endpoint URL for this provider | 
**token_url** | **str** | TMI token exchange endpoint URL for this provider | 
**redirect_uri** | **str** | OAuth callback URI configured for this provider | 
**client_id** | **str** | OAuth client ID for this provider | 

## Example

```python
from tmi_client.models.get_auth_providers200_response_providers_inner import GetAuthProviders200ResponseProvidersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthProviders200ResponseProvidersInner from a JSON string
get_auth_providers200_response_providers_inner_instance = GetAuthProviders200ResponseProvidersInner.from_json(json)
# print the JSON string representation of the object
print(GetAuthProviders200ResponseProvidersInner.to_json())

# convert the object into a dict
get_auth_providers200_response_providers_inner_dict = get_auth_providers200_response_providers_inner_instance.to_dict()
# create an instance of GetAuthProviders200ResponseProvidersInner from a dict
get_auth_providers200_response_providers_inner_from_dict = GetAuthProviders200ResponseProvidersInner.from_dict(get_auth_providers200_response_providers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


