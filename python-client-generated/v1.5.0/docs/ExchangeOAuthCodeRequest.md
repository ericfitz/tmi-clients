# ExchangeOAuthCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | **str** | OAuth 2.0 grant type (RFC 6749) | 
**code** | **str** | Authorization code received from OAuth provider. Per RFC 6749, can contain any visible ASCII characters (VSCHAR: 0x20-0x7E). | [optional] 
**state** | **str** | State parameter for CSRF protection (optional but recommended) | [optional] 
**redirect_uri** | **str** | Redirect URI used in the authorization request (must match exactly) | [optional] 
**code_verifier** | **str** | PKCE code verifier (RFC 7636) - High-entropy cryptographic random string used to mitigate authorization code interception attacks. Must be 43-128 characters using [A-Za-z0-9-._~] characters. | [optional] 
**client_id** | **str** | Client identifier (required for client_credentials grant) | [optional] 
**client_secret** | **str** | Client secret (required for client_credentials grant) | [optional] 
**refresh_token** | **str** | Refresh token (required for refresh_token grant) | [optional] 

## Example

```python
from tmi_client.models.exchange_o_auth_code_request import ExchangeOAuthCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeOAuthCodeRequest from a JSON string
exchange_o_auth_code_request_instance = ExchangeOAuthCodeRequest.from_json(json)
# print the JSON string representation of the object
print(ExchangeOAuthCodeRequest.to_json())

# convert the object into a dict
exchange_o_auth_code_request_dict = exchange_o_auth_code_request_instance.to_dict()
# create an instance of ExchangeOAuthCodeRequest from a dict
exchange_o_auth_code_request_from_dict = ExchangeOAuthCodeRequest.from_dict(exchange_o_auth_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


