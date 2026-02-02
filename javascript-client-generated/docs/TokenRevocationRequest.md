# TmiJsClient.TokenRevocationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **String** | The token to be revoked (access token or refresh token) | 
**tokenTypeHint** | **String** | A hint about the type of the token. If omitted, the server will attempt to determine the token type. | [optional] 
**clientId** | **String** | Client identifier for client credentials authentication (alternative to Bearer token) | [optional] 
**clientSecret** | **String** | Client secret (required if client_id is provided) | [optional] 

<a name="TokenTypeHintEnum"></a>
## Enum: TokenTypeHintEnum

* `accessToken` (value: `"access_token"`)
* `refreshToken` (value: `"refresh_token"`)
* `_null` (value: `"null"`)

