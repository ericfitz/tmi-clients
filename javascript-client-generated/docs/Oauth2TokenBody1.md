# TmiThreatModelingImprovedApi.Oauth2TokenBody1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grantType** | **String** | OAuth 2.0 grant type (RFC 6749) | 
**code** | **String** | Authorization code (required for authorization_code grant) | [optional] 
**clientId** | **String** | Client identifier (required for client_credentials grant) | [optional] 
**clientSecret** | **String** | Client secret (required for client_credentials grant) | [optional] 
**refreshToken** | **String** | Refresh token (required for refresh_token grant) | [optional] 
**redirectUri** | **String** | Redirect URI (required for authorization_code grant) | [optional] 
**codeVerifier** | **String** | PKCE code verifier (required for authorization_code grant) | [optional] 
**state** | **String** | State parameter for CSRF protection | [optional] 

<a name="GrantTypeEnum"></a>
## Enum: GrantTypeEnum

* `authorizationCode` (value: `"authorization_code"`)
* `clientCredentials` (value: `"client_credentials"`)
* `refreshToken` (value: `"refresh_token"`)

