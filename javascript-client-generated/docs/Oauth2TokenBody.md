# TmiThreatModelingImprovedApi.Oauth2TokenBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grantType** | **String** | OAuth 2.0 grant type (RFC 6749) | 
**code** | **String** | Authorization code received from OAuth provider. Per RFC 6749, can contain any visible ASCII characters (VSCHAR: 0x20-0x7E). | [optional] 
**state** | **String** | State parameter for CSRF protection (optional but recommended) | [optional] 
**redirectUri** | **String** | Redirect URI used in the authorization request (must match exactly) | [optional] 
**codeVerifier** | **String** | PKCE code verifier (RFC 7636) - High-entropy cryptographic random string used to mitigate authorization code interception attacks. Must be 43-128 characters using [A-Za-z0-9-._~] characters. | [optional] 
**clientId** | **String** | Client identifier (required for client_credentials grant) | [optional] 
**clientSecret** | **String** | Client secret (required for client_credentials grant) | [optional] 
**refreshToken** | **String** | Refresh token (required for refresh_token grant) | [optional] 

<a name="GrantTypeEnum"></a>
## Enum: GrantTypeEnum

* `authorizationCode` (value: `"authorization_code"`)
* `clientCredentials` (value: `"client_credentials"`)
* `refreshToken` (value: `"refresh_token"`)

