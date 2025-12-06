# Oauth2TokenBody

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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

