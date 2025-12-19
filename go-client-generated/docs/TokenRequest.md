# TokenRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**GrantType** | **string** | OAuth 2.0 grant type (RFC 6749) | [default to null]
**Code** | **string** | Authorization code (required for authorization_code grant) | [optional] [default to null]
**ClientId** | **string** | Client identifier (required for client_credentials grant) | [optional] [default to null]
**ClientSecret** | **string** | Client secret (required for client_credentials grant) | [optional] [default to null]
**RefreshToken** | **string** | Refresh token (required for refresh_token grant) | [optional] [default to null]
**RedirectUri** | **string** | Redirect URI (required for authorization_code grant) | [optional] [default to null]
**CodeVerifier** | **string** | PKCE code verifier (required for authorization_code grant) | [optional] [default to null]
**State** | **string** | State parameter for CSRF protection | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

