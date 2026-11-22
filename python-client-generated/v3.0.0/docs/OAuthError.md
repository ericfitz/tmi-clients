# OAuthError

Error response for OAuth, SAML and discovery routes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error code for OAuth, SAML and discovery routes: the RFC 6749, 7009 and 9470 codes, the documented TMI extensions (identity_mismatch, account_conflict, email_not_verified, provider_unreachable, provider_response_invalid, invalid_provider), and the transport codes that route-agnostic middleware can emit (unauthorized, not_found, method_not_allowed, not_acceptable, payload_too_large, unsupported_media_type, rate_limit_exceeded, server_error). SAML routes also use the TMI extension codes saml_error, saml_not_enabled, saml_unavailable, saml_provider_not_found, saml_metadata_error, saml_init_error, saml_invalid_logout_request and saml_logout_error. | 
**error_description** | **str** | Human-readable error description | 
**error_uri** | **str** | URI to documentation about the error | [optional] 
**details** | [**ErrorDetails**](ErrorDetails.md) |  | [optional] 

## Example

```python
from tmi_client.models.o_auth_error import OAuthError

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthError from a JSON string
o_auth_error_instance = OAuthError.from_json(json)
# print the JSON string representation of the object
print(OAuthError.to_json())

# convert the object into a dict
o_auth_error_dict = o_auth_error_instance.to_dict()
# create an instance of OAuthError from a dict
o_auth_error_from_dict = OAuthError.from_dict(o_auth_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


