# Oauth2TokenBody1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | **str** | OAuth 2.0 grant type (RFC 6749) | 
**code** | **str** | Authorization code (required for authorization_code grant) | [optional] 
**client_id** | **str** | Client identifier (required for client_credentials grant) | [optional] 
**client_secret** | **str** | Client secret (required for client_credentials grant) | [optional] 
**refresh_token** | **str** | Refresh token (required for refresh_token grant) | [optional] 
**redirect_uri** | **str** | Redirect URI (required for authorization_code grant) | [optional] 
**code_verifier** | **str** | PKCE code verifier (required for authorization_code grant) | [optional] 
**state** | **str** | State parameter for CSRF protection | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

