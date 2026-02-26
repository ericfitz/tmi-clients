# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AuthorizeOAuthProvider**](AuthenticationApi.md#AuthorizeOAuthProvider) | **Get** /oauth2/authorize | Initiate OAuth authorization flow
[**CreateCurrentUserClientCredential**](AuthenticationApi.md#CreateCurrentUserClientCredential) | **Post** /me/client_credentials | Create client credential
[**DeleteCurrentUserClientCredential**](AuthenticationApi.md#DeleteCurrentUserClientCredential) | **Delete** /me/client_credentials/{id} | Delete client credential
[**ExchangeOAuthCode**](AuthenticationApi.md#ExchangeOAuthCode) | **Post** /oauth2/token | Exchange OAuth credentials for JWT tokens
[**GetAuthProviders**](AuthenticationApi.md#GetAuthProviders) | **Get** /oauth2/providers | List available OAuth providers
[**GetCurrentUser**](AuthenticationApi.md#GetCurrentUser) | **Get** /oauth2/userinfo | Get current user information
[**GetCurrentUserProfile**](AuthenticationApi.md#GetCurrentUserProfile) | **Get** /me | Get current user profile
[**GetProviderGroups**](AuthenticationApi.md#GetProviderGroups) | **Get** /oauth2/providers/{idp}/groups | Get groups for identity provider
[**GetSAMLMetadata**](AuthenticationApi.md#GetSAMLMetadata) | **Get** /saml/{provider}/metadata | Get SAML service provider metadata
[**GetSAMLProviders**](AuthenticationApi.md#GetSAMLProviders) | **Get** /saml/providers | List available SAML providers
[**HandleOAuthCallback**](AuthenticationApi.md#HandleOAuthCallback) | **Get** /oauth2/callback | Handle OAuth callback
[**InitiateSAMLLogin**](AuthenticationApi.md#InitiateSAMLLogin) | **Get** /saml/{provider}/login | Initiate SAML authentication
[**IntrospectToken**](AuthenticationApi.md#IntrospectToken) | **Post** /oauth2/introspect | Token Introspection
[**ListCurrentUserClientCredentials**](AuthenticationApi.md#ListCurrentUserClientCredentials) | **Get** /me/client_credentials | List client credentials
[**ListMyGroupMembers**](AuthenticationApi.md#ListMyGroupMembers) | **Get** /me/groups/{internal_uuid}/members | List members of my group
[**ListMyGroups**](AuthenticationApi.md#ListMyGroups) | **Get** /me/groups | List my groups
[**ProcessSAMLLogout**](AuthenticationApi.md#ProcessSAMLLogout) | **Get** /saml/slo | SAML Single Logout
[**ProcessSAMLLogoutPost**](AuthenticationApi.md#ProcessSAMLLogoutPost) | **Post** /saml/slo | SAML Single Logout (POST)
[**ProcessSAMLResponse**](AuthenticationApi.md#ProcessSAMLResponse) | **Post** /saml/acs | SAML Assertion Consumer Service
[**RefreshToken**](AuthenticationApi.md#RefreshToken) | **Post** /oauth2/refresh | Refresh JWT token
[**RevokeToken**](AuthenticationApi.md#RevokeToken) | **Post** /oauth2/revoke | Revoke token

# **AuthorizeOAuthProvider**
> AuthorizeOAuthProvider(ctx, scope, codeChallenge, codeChallengeMethod, optional)
Initiate OAuth authorization flow

Redirects user to OAuth provider's authorization page. Supports client callback URL for seamless client integration. Generates state parameter for CSRF protection.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **scope** | **string**| OAuth 2.0 scope parameter. For OpenID Connect, must include \&quot;openid\&quot;. Supports \&quot;profile\&quot; and \&quot;email\&quot; scopes. Other scopes are silently ignored. Space-separated values. | 
  **codeChallenge** | **string**| PKCE code challenge (RFC 7636) - Base64url-encoded SHA256 hash of the code_verifier. Must be 43-128 characters using unreserved characters [A-Za-z0-9-._~]. The server associates this with the authorization code for later verification during token exchange. | 
  **codeChallengeMethod** | **string**| PKCE code challenge method (RFC 7636) - Specifies the transformation applied to the code_verifier. Only \&quot;S256\&quot; (SHA256) is supported for security. The \&quot;plain\&quot; method is not supported. | 
 **optional** | ***AuthenticationApiAuthorizeOAuthProviderOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuthenticationApiAuthorizeOAuthProviderOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idp** | **optional.String**| OAuth provider identifier. Defaults to &#x27;tmi&#x27; provider in non-production builds if not specified. | 
 **clientCallback** | **optional.String**| Client callback URL where TMI should redirect after successful OAuth completion with tokens in URL fragment (#access_token&#x3D;...). If not provided, tokens are returned as JSON response. Per OAuth 2.0 implicit flow spec, tokens are in fragments to prevent logging. | 
 **state** | **optional.String**| CSRF protection state parameter. Recommended for security. Will be included in the callback response. | 
 **loginHint** | **optional.String**| User identity hint for TMI OAuth provider. Allows specifying a desired user identity for testing and automation. Only supported by the TMI provider (ignored by production providers like Google, GitHub, etc.). Must be 3-20 characters, alphanumeric and hyphens only. | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateCurrentUserClientCredential**
> ClientCredentialResponse CreateCurrentUserClientCredential(ctx, body)
Create client credential

Creates a new OAuth 2.0 client credential for machine-to-machine authentication. The client_secret is ONLY returned once at creation and cannot be retrieved later.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**MeClientCredentialsBody**](MeClientCredentialsBody.md)| Client credential creation request | 

### Return type

[**ClientCredentialResponse**](ClientCredentialResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteCurrentUserClientCredential**
> DeleteCurrentUserClientCredential(ctx, id)
Delete client credential

Permanently deletes a client credential. All tokens issued with this credential will immediately become invalid.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | [**string**](.md)| Administrator grant ID | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ExchangeOAuthCode**
> AuthTokenResponse ExchangeOAuthCode(ctx, body, grantType, code, clientId, clientSecret, refreshToken, redirectUri, codeVerifier, state, optional)
Exchange OAuth credentials for JWT tokens

Provider-neutral endpoint to exchange OAuth credentials for TMI JWT tokens. Supports three grant types: (1) authorization_code for OAuth provider flows (Google, GitHub, Microsoft), (2) client_credentials for machine-to-machine authentication (RFC 6749 Section 4.4), and (3) refresh_token for token renewal. Accepts both application/json and application/x-www-form-urlencoded content types.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**Oauth2TokenBody**](Oauth2TokenBody.md)| OAuth 2.0 token exchange request parameters | 
  **grantType** | **string**|  | 
  **code** | **string**|  | 
  **clientId** | **string**|  | 
  **clientSecret** | **string**|  | 
  **refreshToken** | **string**|  | 
  **redirectUri** | **string**|  | 
  **codeVerifier** | **string**|  | 
  **state** | **string**|  | 
 **optional** | ***AuthenticationApiExchangeOAuthCodeOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuthenticationApiExchangeOAuthCodeOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------









 **idp** | **optional.**| OAuth provider identifier. Defaults to &#x27;tmi&#x27; provider in non-production builds if not specified. | 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAuthProviders**
> InlineResponse2004 GetAuthProviders(ctx, )
List available OAuth providers

Returns a list of configured OAuth providers available for authentication

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](inline_response_200_4.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCurrentUser**
> InlineResponse2006 GetCurrentUser(ctx, )
Get current user information

Returns information about the currently authenticated user

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](inline_response_200_6.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCurrentUserProfile**
> UserWithAdminStatus GetCurrentUserProfile(ctx, )
Get current user profile

Returns detailed information about the currently authenticated user including groups and identity provider

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**UserWithAdminStatus**](UserWithAdminStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetProviderGroups**
> InlineResponse2005 GetProviderGroups(ctx, idp)
Get groups for identity provider

Returns groups available from a specific identity provider for autocomplete and discovery

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **idp** | **string**| Identity provider ID (e.g., saml_okta, saml_azure) | 

### Return type

[**InlineResponse2005**](inline_response_200_5.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetSAMLMetadata**
> string GetSAMLMetadata(ctx, provider)
Get SAML service provider metadata

Returns the SP metadata XML for SAML configuration

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **provider** | **string**| SAML provider identifier | 

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/samlmetadata+xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetSAMLProviders**
> InlineResponse2009 GetSAMLProviders(ctx, )
List available SAML providers

Returns a list of configured SAML providers available for authentication

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](inline_response_200_9.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **HandleOAuthCallback**
> AuthTokenResponse HandleOAuthCallback(ctx, code, optional)
Handle OAuth callback

Exchanges OAuth authorization code for JWT tokens. If client_callback was provided during authorization, redirects to client with tokens. Otherwise returns tokens as JSON response.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **code** | **string**| Authorization code from the OAuth provider | 
 **optional** | ***AuthenticationApiHandleOAuthCallbackOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuthenticationApiHandleOAuthCallbackOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **state** | **optional.String**| CSRF protection state parameter. Recommended for security. Will be included in the callback response. | 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **InitiateSAMLLogin**
> InitiateSAMLLogin(ctx, provider, optional)
Initiate SAML authentication

Starts SAML authentication flow by redirecting to IdP

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **provider** | **string**| SAML provider identifier | 
 **optional** | ***AuthenticationApiInitiateSAMLLoginOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuthenticationApiInitiateSAMLLoginOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **clientCallback** | **optional.String**| Client callback URL where TMI should redirect after successful OAuth completion with tokens in URL fragment (#access_token&#x3D;...). If not provided, tokens are returned as JSON response. Per OAuth 2.0 implicit flow spec, tokens are in fragments to prevent logging. | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **IntrospectToken**
> InlineResponse2003 IntrospectToken(ctx, token, tokenTypeHint)
Token Introspection

Introspects a JWT token to determine its validity and metadata as per RFC 7662

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **token** | **string**|  | 
  **tokenTypeHint** | **string**|  | 

### Return type

[**InlineResponse2003**](inline_response_200_3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListCurrentUserClientCredentials**
> ListClientCredentialsResponse ListCurrentUserClientCredentials(ctx, optional)
List client credentials

Retrieves all client credentials owned by the authenticated user. Secrets are never returned.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***AuthenticationApiListCurrentUserClientCredentialsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuthenticationApiListCurrentUserClientCredentialsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**ListClientCredentialsResponse**](ListClientCredentialsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListMyGroupMembers**
> GroupMemberListResponse ListMyGroupMembers(ctx, internalUuid, optional)
List members of my group

Returns a paginated list of members for a group that the authenticated user belongs to. Only effective members (direct or via nested group membership) can list a group's members. Admin audit fields (added_by, notes) are redacted from the response.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 
 **optional** | ***AuthenticationApiListMyGroupMembersOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuthenticationApiListMyGroupMembersOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **optional.Int32**| Maximum number of results to return | [default to 50]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**GroupMemberListResponse**](GroupMemberListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListMyGroups**
> MyGroupListResponse ListMyGroups(ctx, )
List my groups

Returns the TMI-managed groups that the authenticated user belongs to. Returns direct memberships only (excludes the implicit everyone pseudo-group). Each group includes its internal_uuid which can be used to query group members via GET /me/groups/{internal_uuid}/members.

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**MyGroupListResponse**](MyGroupListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ProcessSAMLLogout**
> InlineResponse2008 ProcessSAMLLogout(ctx, sAMLRequest)
SAML Single Logout

Handles SAML logout requests from IdP

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **sAMLRequest** | **string**| Base64-encoded SAML logout request | 

### Return type

[**InlineResponse2008**](inline_response_200_8.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ProcessSAMLLogoutPost**
> InlineResponse2008 ProcessSAMLLogoutPost(ctx, optional)
SAML Single Logout (POST)

Handles SAML logout requests from IdP via POST

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***AuthenticationApiProcessSAMLLogoutPostOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuthenticationApiProcessSAMLLogoutPostOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sAMLRequest** | **optional.**|  | 

### Return type

[**InlineResponse2008**](inline_response_200_8.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ProcessSAMLResponse**
> AuthTokenResponse ProcessSAMLResponse(ctx, optional)
SAML Assertion Consumer Service

Processes SAML responses from IdP after authentication

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***AuthenticationApiProcessSAMLResponseOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuthenticationApiProcessSAMLResponseOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sAMLResponse** | **optional.**|  | 
 **relayState** | **optional.**|  | 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **RefreshToken**
> AuthTokenResponse RefreshToken(ctx, optional)
Refresh JWT token

Exchanges a refresh token for a new JWT access token

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***AuthenticationApiRefreshTokenOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuthenticationApiRefreshTokenOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**optional.Interface of TokenRefreshRequest**](TokenRefreshRequest.md)| OAuth 2.0 token refresh request parameters | 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **RevokeToken**
> interface{} RevokeToken(ctx, token, tokenTypeHint, clientId, clientSecret, body)
Revoke token

Revokes an OAuth 2.0 token per RFC 7009. The token to revoke is passed in the request body. Supports both access tokens and refresh tokens. Authentication is required via Bearer token in the Authorization header OR client credentials (client_id/client_secret) in the request body. Per RFC 7009, the response is always 200 OK regardless of whether the token was valid, to prevent token existence disclosure.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **token** | **string**|  | 
  **tokenTypeHint** | **string**|  | 
  **clientId** | **string**|  | 
  **clientSecret** | **string**|  | 
  **body** | [**TokenRevocationRequest**](TokenRevocationRequest.md)| Token revocation request per RFC 7009 | 

### Return type

[**interface{}**](interface{}.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

