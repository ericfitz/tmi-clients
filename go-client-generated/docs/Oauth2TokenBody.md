# Oauth2TokenBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**GrantType** | **string** | OAuth 2.0 grant type (RFC 6749) | [default to null]
**Code** | **string** | Authorization code received from OAuth provider. Per RFC 6749, can contain any visible ASCII characters (VSCHAR: 0x20-0x7E). | [optional] [default to null]
**State** | **string** | State parameter for CSRF protection (optional but recommended) | [optional] [default to null]
**RedirectUri** | **string** | Redirect URI used in the authorization request (must match exactly) | [optional] [default to null]
**CodeVerifier** | **string** | PKCE code verifier (RFC 7636) - High-entropy cryptographic random string used to mitigate authorization code interception attacks. Must be 43-128 characters using [A-Za-z0-9-._~] characters. | [optional] [default to null]
**ClientId** | **string** | Client identifier (required for client_credentials grant) | [optional] [default to null]
**ClientSecret** | **string** | Client secret (required for client_credentials grant) | [optional] [default to null]
**RefreshToken** | **string** | Refresh token (required for refresh_token grant) | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

