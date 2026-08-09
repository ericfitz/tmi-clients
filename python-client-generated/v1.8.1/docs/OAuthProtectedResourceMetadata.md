# OAuthProtectedResourceMetadata

OAuth 2.0 protected resource metadata as defined in RFC 9728

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | The protected resource&#39;s resource identifier URL | 
**scopes_supported** | **List[str]** | JSON array of OAuth scope values supported by this protected resource | [optional] 
**authorization_servers** | **List[str]** | List of authorization server issuer identifiers that can issue tokens for this resource | [optional] 
**jwks_uri** | **str** | URL of the protected resource&#39;s JSON Web Key Set (RFC 9728) | [optional] 
**bearer_methods_supported** | **List[str]** | Supported token presentation methods for bearer tokens | [optional] 
**resource_name** | **str** | Human-readable name of the protected resource | [optional] 
**resource_documentation** | **str** | URL with information for developers on how to use this protected resource | [optional] 
**tls_client_certificate_bound_access_tokens** | **bool** | Whether the protected resource supports TLS client certificate bound access tokens | [optional] 

## Example

```python
from tmi_client.models.o_auth_protected_resource_metadata import OAuthProtectedResourceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthProtectedResourceMetadata from a JSON string
o_auth_protected_resource_metadata_instance = OAuthProtectedResourceMetadata.from_json(json)
# print the JSON string representation of the object
print(OAuthProtectedResourceMetadata.to_json())

# convert the object into a dict
o_auth_protected_resource_metadata_dict = o_auth_protected_resource_metadata_instance.to_dict()
# create an instance of OAuthProtectedResourceMetadata from a dict
o_auth_protected_resource_metadata_from_dict = OAuthProtectedResourceMetadata.from_dict(o_auth_protected_resource_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


