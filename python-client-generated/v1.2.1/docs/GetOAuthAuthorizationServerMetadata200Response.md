# GetOAuthAuthorizationServerMetadata200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** |  | 
**authorization_endpoint** | **str** |  | 
**token_endpoint** | **str** |  | 
**introspection_endpoint** | **str** |  | [optional] 
**response_types_supported** | **List[str]** |  | 
**grant_types_supported** | **List[str]** |  | [optional] 
**token_endpoint_auth_methods_supported** | **List[str]** |  | [optional] 

## Example

```python
from tmi_client.models.get_o_auth_authorization_server_metadata200_response import GetOAuthAuthorizationServerMetadata200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOAuthAuthorizationServerMetadata200Response from a JSON string
get_o_auth_authorization_server_metadata200_response_instance = GetOAuthAuthorizationServerMetadata200Response.from_json(json)
# print the JSON string representation of the object
print(GetOAuthAuthorizationServerMetadata200Response.to_json())

# convert the object into a dict
get_o_auth_authorization_server_metadata200_response_dict = get_o_auth_authorization_server_metadata200_response_instance.to_dict()
# create an instance of GetOAuthAuthorizationServerMetadata200Response from a dict
get_o_auth_authorization_server_metadata200_response_from_dict = GetOAuthAuthorizationServerMetadata200Response.from_dict(get_o_auth_authorization_server_metadata200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


