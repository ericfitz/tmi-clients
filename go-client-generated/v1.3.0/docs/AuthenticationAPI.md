# \AuthenticationAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AuthorizeOAuthProvider**](AuthenticationAPI.md#AuthorizeOAuthProvider) | **Get** /oauth2/authorize | Initiate OAuth authorization flow
[**CreateCurrentUserClientCredential**](AuthenticationAPI.md#CreateCurrentUserClientCredential) | **Post** /me/client_credentials | Create client credential
[**DeleteCurrentUserClientCredential**](AuthenticationAPI.md#DeleteCurrentUserClientCredential) | **Delete** /me/client_credentials/{credential_id} | Delete client credential
[**ExchangeOAuthCode**](AuthenticationAPI.md#ExchangeOAuthCode) | **Post** /oauth2/token | Exchange OAuth credentials for JWT tokens
[**GetAuthProviders**](AuthenticationAPI.md#GetAuthProviders) | **Get** /oauth2/providers | List available OAuth providers
[**GetCurrentUser**](AuthenticationAPI.md#GetCurrentUser) | **Get** /oauth2/userinfo | Get current user information
[**GetCurrentUserProfile**](AuthenticationAPI.md#GetCurrentUserProfile) | **Get** /me | Get current user profile
[**GetProviderGroups**](AuthenticationAPI.md#GetProviderGroups) | **Get** /oauth2/providers/{idp}/groups | Get groups for identity provider
[**GetSAMLMetadata**](AuthenticationAPI.md#GetSAMLMetadata) | **Get** /saml/{provider}/metadata | Get SAML service provider metadata
[**GetSAMLProviders**](AuthenticationAPI.md#GetSAMLProviders) | **Get** /saml/providers | List available SAML providers
[**HandleOAuthCallback**](AuthenticationAPI.md#HandleOAuthCallback) | **Get** /oauth2/callback | Handle OAuth callback
[**InitiateSAMLLogin**](AuthenticationAPI.md#InitiateSAMLLogin) | **Get** /saml/{provider}/login | Initiate SAML authentication
[**IntrospectToken**](AuthenticationAPI.md#IntrospectToken) | **Post** /oauth2/introspect | Token Introspection
[**ListCurrentUserClientCredentials**](AuthenticationAPI.md#ListCurrentUserClientCredentials) | **Get** /me/client_credentials | List client credentials
[**ListMyGroupMembers**](AuthenticationAPI.md#ListMyGroupMembers) | **Get** /me/groups/{internal_uuid}/members | List members of my group
[**ListMyGroups**](AuthenticationAPI.md#ListMyGroups) | **Get** /me/groups | List my groups
[**ProcessSAMLLogout**](AuthenticationAPI.md#ProcessSAMLLogout) | **Get** /saml/slo | SAML Single Logout
[**ProcessSAMLLogoutPost**](AuthenticationAPI.md#ProcessSAMLLogoutPost) | **Post** /saml/slo | SAML Single Logout (POST)
[**ProcessSAMLResponse**](AuthenticationAPI.md#ProcessSAMLResponse) | **Post** /saml/acs | SAML Assertion Consumer Service
[**RefreshToken**](AuthenticationAPI.md#RefreshToken) | **Post** /oauth2/refresh | Refresh JWT token
[**RevokeToken**](AuthenticationAPI.md#RevokeToken) | **Post** /oauth2/revoke | Revoke token



## AuthorizeOAuthProvider

> AuthorizeOAuthProvider(ctx).Scope(scope).CodeChallenge(codeChallenge).CodeChallengeMethod(codeChallengeMethod).Idp(idp).ClientCallback(clientCallback).State(state).LoginHint(loginHint).Execute()

Initiate OAuth authorization flow



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	scope := "openid profile email" // string | OAuth 2.0 scope parameter. For OpenID Connect, must include \"openid\". Supports \"profile\" and \"email\" scopes. Other scopes are silently ignored. Space-separated values.
	codeChallenge := "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM" // string | PKCE code challenge (RFC 7636) - Base64url-encoded SHA256 hash of the code_verifier. Must be 43-128 characters using unreserved characters [A-Za-z0-9-._~]. The server associates this with the authorization code for later verification during token exchange.
	codeChallengeMethod := "S256" // string | PKCE code challenge method (RFC 7636) - Specifies the transformation applied to the code_verifier. Only \"S256\" (SHA256) is supported for security. The \"plain\" method is not supported.
	idp := "idp_example" // string | OAuth provider identifier. Defaults to 'tmi' provider in non-production builds if not specified. (optional)
	clientCallback := "http://localhost:4200/oauth2/callback" // string | Client callback URL where TMI should redirect after successful OAuth completion with tokens in URL fragment (#access_token=...). If not provided, tokens are returned as JSON response. Per OAuth 2.0 implicit flow spec, tokens are in fragments to prevent logging. (optional)
	state := "random_state_abc123" // string | CSRF protection state parameter. Recommended for security. Will be included in the callback response. (optional)
	loginHint := "alice" // string | User identity hint for TMI OAuth provider. Allows specifying a desired user identity for testing and automation. Only supported by the TMI provider (ignored by production providers like Google, GitHub, etc.). Must be 3-20 characters, alphanumeric and hyphens only. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AuthenticationAPI.AuthorizeOAuthProvider(context.Background()).Scope(scope).CodeChallenge(codeChallenge).CodeChallengeMethod(codeChallengeMethod).Idp(idp).ClientCallback(clientCallback).State(state).LoginHint(loginHint).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.AuthorizeOAuthProvider``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAuthorizeOAuthProviderRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **string** | OAuth 2.0 scope parameter. For OpenID Connect, must include \&quot;openid\&quot;. Supports \&quot;profile\&quot; and \&quot;email\&quot; scopes. Other scopes are silently ignored. Space-separated values. | 
 **codeChallenge** | **string** | PKCE code challenge (RFC 7636) - Base64url-encoded SHA256 hash of the code_verifier. Must be 43-128 characters using unreserved characters [A-Za-z0-9-._~]. The server associates this with the authorization code for later verification during token exchange. | 
 **codeChallengeMethod** | **string** | PKCE code challenge method (RFC 7636) - Specifies the transformation applied to the code_verifier. Only \&quot;S256\&quot; (SHA256) is supported for security. The \&quot;plain\&quot; method is not supported. | 
 **idp** | **string** | OAuth provider identifier. Defaults to &#39;tmi&#39; provider in non-production builds if not specified. | 
 **clientCallback** | **string** | Client callback URL where TMI should redirect after successful OAuth completion with tokens in URL fragment (#access_token&#x3D;...). If not provided, tokens are returned as JSON response. Per OAuth 2.0 implicit flow spec, tokens are in fragments to prevent logging. | 
 **state** | **string** | CSRF protection state parameter. Recommended for security. Will be included in the callback response. | 
 **loginHint** | **string** | User identity hint for TMI OAuth provider. Allows specifying a desired user identity for testing and automation. Only supported by the TMI provider (ignored by production providers like Google, GitHub, etc.). Must be 3-20 characters, alphanumeric and hyphens only. | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateCurrentUserClientCredential

> ClientCredentialResponse CreateCurrentUserClientCredential(ctx).CreateCurrentUserClientCredentialRequest(createCurrentUserClientCredentialRequest).Execute()

Create client credential



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	createCurrentUserClientCredentialRequest := *openapiclient.NewCreateCurrentUserClientCredentialRequest("CI/CD Pipeline") // CreateCurrentUserClientCredentialRequest | Client credential creation request

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.CreateCurrentUserClientCredential(context.Background()).CreateCurrentUserClientCredentialRequest(createCurrentUserClientCredentialRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.CreateCurrentUserClientCredential``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateCurrentUserClientCredential`: ClientCredentialResponse
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.CreateCurrentUserClientCredential`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateCurrentUserClientCredentialRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createCurrentUserClientCredentialRequest** | [**CreateCurrentUserClientCredentialRequest**](CreateCurrentUserClientCredentialRequest.md) | Client credential creation request | 

### Return type

[**ClientCredentialResponse**](ClientCredentialResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteCurrentUserClientCredential

> DeleteCurrentUserClientCredential(ctx, credentialId).Execute()

Delete client credential



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	credentialId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal UUID of the client credential (the \"id\" field from the list response, not the \"client_id\")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AuthenticationAPI.DeleteCurrentUserClientCredential(context.Background(), credentialId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.DeleteCurrentUserClientCredential``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**credentialId** | **string** | Internal UUID of the client credential (the \&quot;id\&quot; field from the list response, not the \&quot;client_id\&quot;) | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteCurrentUserClientCredentialRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ExchangeOAuthCode

> AuthTokenResponse ExchangeOAuthCode(ctx).ExchangeOAuthCodeRequest(exchangeOAuthCodeRequest).Idp(idp).Execute()

Exchange OAuth credentials for JWT tokens



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	exchangeOAuthCodeRequest := *openapiclient.NewExchangeOAuthCodeRequest("authorization_code") // ExchangeOAuthCodeRequest | OAuth 2.0 token exchange request parameters
	idp := "idp_example" // string | OAuth provider identifier. Defaults to 'tmi' provider in non-production builds if not specified. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.ExchangeOAuthCode(context.Background()).ExchangeOAuthCodeRequest(exchangeOAuthCodeRequest).Idp(idp).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.ExchangeOAuthCode``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExchangeOAuthCode`: AuthTokenResponse
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.ExchangeOAuthCode`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiExchangeOAuthCodeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchangeOAuthCodeRequest** | [**ExchangeOAuthCodeRequest**](ExchangeOAuthCodeRequest.md) | OAuth 2.0 token exchange request parameters | 
 **idp** | **string** | OAuth provider identifier. Defaults to &#39;tmi&#39; provider in non-production builds if not specified. | 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAuthProviders

> GetAuthProviders200Response GetAuthProviders(ctx).Execute()

List available OAuth providers



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.GetAuthProviders(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.GetAuthProviders``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAuthProviders`: GetAuthProviders200Response
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.GetAuthProviders`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetAuthProvidersRequest struct via the builder pattern


### Return type

[**GetAuthProviders200Response**](GetAuthProviders200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCurrentUser

> GetCurrentUser200Response GetCurrentUser(ctx).Execute()

Get current user information



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.GetCurrentUser(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.GetCurrentUser``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCurrentUser`: GetCurrentUser200Response
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.GetCurrentUser`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetCurrentUserRequest struct via the builder pattern


### Return type

[**GetCurrentUser200Response**](GetCurrentUser200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCurrentUserProfile

> UserWithAdminStatus GetCurrentUserProfile(ctx).Execute()

Get current user profile



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.GetCurrentUserProfile(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.GetCurrentUserProfile``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCurrentUserProfile`: UserWithAdminStatus
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.GetCurrentUserProfile`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetCurrentUserProfileRequest struct via the builder pattern


### Return type

[**UserWithAdminStatus**](UserWithAdminStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProviderGroups

> GetProviderGroups200Response GetProviderGroups(ctx, idp).Execute()

Get groups for identity provider



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	idp := "idp_example" // string | Identity provider ID (e.g., saml_okta, saml_azure)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.GetProviderGroups(context.Background(), idp).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.GetProviderGroups``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetProviderGroups`: GetProviderGroups200Response
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.GetProviderGroups`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**idp** | **string** | Identity provider ID (e.g., saml_okta, saml_azure) | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetProviderGroupsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GetProviderGroups200Response**](GetProviderGroups200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSAMLMetadata

> string GetSAMLMetadata(ctx, provider).Execute()

Get SAML service provider metadata



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	provider := "provider_example" // string | SAML provider identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.GetSAMLMetadata(context.Background(), provider).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.GetSAMLMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSAMLMetadata`: string
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.GetSAMLMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**provider** | **string** | SAML provider identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSAMLMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/samlmetadata+xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSAMLProviders

> GetSAMLProviders200Response GetSAMLProviders(ctx).Execute()

List available SAML providers



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.GetSAMLProviders(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.GetSAMLProviders``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSAMLProviders`: GetSAMLProviders200Response
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.GetSAMLProviders`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetSAMLProvidersRequest struct via the builder pattern


### Return type

[**GetSAMLProviders200Response**](GetSAMLProviders200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## HandleOAuthCallback

> AuthTokenResponse HandleOAuthCallback(ctx).Code(code).State(state).Execute()

Handle OAuth callback



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	code := "code_example" // string | Authorization code from the OAuth provider
	state := "random_state_abc123" // string | CSRF protection state parameter. Recommended for security. Will be included in the callback response. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.HandleOAuthCallback(context.Background()).Code(code).State(state).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.HandleOAuthCallback``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `HandleOAuthCallback`: AuthTokenResponse
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.HandleOAuthCallback`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiHandleOAuthCallbackRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **string** | Authorization code from the OAuth provider | 
 **state** | **string** | CSRF protection state parameter. Recommended for security. Will be included in the callback response. | 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## InitiateSAMLLogin

> InitiateSAMLLogin(ctx, provider).ClientCallback(clientCallback).Execute()

Initiate SAML authentication



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	provider := "provider_example" // string | SAML provider identifier
	clientCallback := "http://localhost:4200/oauth2/callback" // string | Client callback URL where TMI should redirect after successful OAuth completion with tokens in URL fragment (#access_token=...). If not provided, tokens are returned as JSON response. Per OAuth 2.0 implicit flow spec, tokens are in fragments to prevent logging. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AuthenticationAPI.InitiateSAMLLogin(context.Background(), provider).ClientCallback(clientCallback).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.InitiateSAMLLogin``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**provider** | **string** | SAML provider identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiInitiateSAMLLoginRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **clientCallback** | **string** | Client callback URL where TMI should redirect after successful OAuth completion with tokens in URL fragment (#access_token&#x3D;...). If not provided, tokens are returned as JSON response. Per OAuth 2.0 implicit flow spec, tokens are in fragments to prevent logging. | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IntrospectToken

> IntrospectToken200Response IntrospectToken(ctx).Token(token).TokenTypeHint(tokenTypeHint).Execute()

Token Introspection



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	token := "token_example" // string | The JWT token to introspect
	tokenTypeHint := "tokenTypeHint_example" // string | Optional hint about the type of token being introspected (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.IntrospectToken(context.Background()).Token(token).TokenTypeHint(tokenTypeHint).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.IntrospectToken``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `IntrospectToken`: IntrospectToken200Response
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.IntrospectToken`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiIntrospectTokenRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **string** | The JWT token to introspect | 
 **tokenTypeHint** | **string** | Optional hint about the type of token being introspected | 

### Return type

[**IntrospectToken200Response**](IntrospectToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListCurrentUserClientCredentials

> ListClientCredentialsResponse ListCurrentUserClientCredentials(ctx).Limit(limit).Offset(offset).Execute()

List client credentials



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.ListCurrentUserClientCredentials(context.Background()).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.ListCurrentUserClientCredentials``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListCurrentUserClientCredentials`: ListClientCredentialsResponse
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.ListCurrentUserClientCredentials`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListCurrentUserClientCredentialsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListClientCredentialsResponse**](ListClientCredentialsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListMyGroupMembers

> GroupMemberListResponse ListMyGroupMembers(ctx, internalUuid).Limit(limit).Offset(offset).Execute()

List members of my group



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 50)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.ListMyGroupMembers(context.Background(), internalUuid).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.ListMyGroupMembers``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListMyGroupMembers`: GroupMemberListResponse
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.ListMyGroupMembers`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 

### Other Parameters

Other parameters are passed through a pointer to a apiListMyGroupMembersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** | Maximum number of results to return | [default to 50]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**GroupMemberListResponse**](GroupMemberListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListMyGroups

> MyGroupListResponse ListMyGroups(ctx).Execute()

List my groups



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.ListMyGroups(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.ListMyGroups``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListMyGroups`: MyGroupListResponse
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.ListMyGroups`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiListMyGroupsRequest struct via the builder pattern


### Return type

[**MyGroupListResponse**](MyGroupListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ProcessSAMLLogout

> ProcessSAMLLogout200Response ProcessSAMLLogout(ctx).SAMLRequest(sAMLRequest).Execute()

SAML Single Logout



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	sAMLRequest := "sAMLRequest_example" // string | Base64-encoded SAML logout request

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.ProcessSAMLLogout(context.Background()).SAMLRequest(sAMLRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.ProcessSAMLLogout``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ProcessSAMLLogout`: ProcessSAMLLogout200Response
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.ProcessSAMLLogout`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiProcessSAMLLogoutRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sAMLRequest** | **string** | Base64-encoded SAML logout request | 

### Return type

[**ProcessSAMLLogout200Response**](ProcessSAMLLogout200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ProcessSAMLLogoutPost

> ProcessSAMLLogout200Response ProcessSAMLLogoutPost(ctx).SAMLRequest(sAMLRequest).Execute()

SAML Single Logout (POST)



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	sAMLRequest := "sAMLRequest_example" // string | Base64-encoded SAML logout request

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.ProcessSAMLLogoutPost(context.Background()).SAMLRequest(sAMLRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.ProcessSAMLLogoutPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ProcessSAMLLogoutPost`: ProcessSAMLLogout200Response
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.ProcessSAMLLogoutPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiProcessSAMLLogoutPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sAMLRequest** | **string** | Base64-encoded SAML logout request | 

### Return type

[**ProcessSAMLLogout200Response**](ProcessSAMLLogout200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ProcessSAMLResponse

> AuthTokenResponse ProcessSAMLResponse(ctx).SAMLResponse(sAMLResponse).RelayState(relayState).Execute()

SAML Assertion Consumer Service



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	sAMLResponse := "sAMLResponse_example" // string | Base64-encoded SAML response
	relayState := "relayState_example" // string | State parameter for CSRF protection (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.ProcessSAMLResponse(context.Background()).SAMLResponse(sAMLResponse).RelayState(relayState).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.ProcessSAMLResponse``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ProcessSAMLResponse`: AuthTokenResponse
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.ProcessSAMLResponse`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiProcessSAMLResponseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sAMLResponse** | **string** | Base64-encoded SAML response | 
 **relayState** | **string** | State parameter for CSRF protection | 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RefreshToken

> AuthTokenResponse RefreshToken(ctx).TokenRefreshRequest(tokenRefreshRequest).Execute()

Refresh JWT token



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	tokenRefreshRequest := *openapiclient.NewTokenRefreshRequest("8xLOxBtZp8_example_refresh_token") // TokenRefreshRequest | OAuth 2.0 token refresh request parameters (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.RefreshToken(context.Background()).TokenRefreshRequest(tokenRefreshRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.RefreshToken``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RefreshToken`: AuthTokenResponse
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.RefreshToken`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRefreshTokenRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenRefreshRequest** | [**TokenRefreshRequest**](TokenRefreshRequest.md) | OAuth 2.0 token refresh request parameters | 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RevokeToken

> map[string]interface{} RevokeToken(ctx).Token(token).TokenTypeHint(tokenTypeHint).ClientId(clientId).ClientSecret(clientSecret).Execute()

Revoke token



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	token := "token_example" // string | The token to be revoked (access token or refresh token)
	tokenTypeHint := "tokenTypeHint_example" // string | A hint about the type of the token. If omitted, the server will attempt to determine the token type. (optional)
	clientId := "clientId_example" // string | Client identifier for client credentials authentication (alternative to Bearer token) (optional)
	clientSecret := "clientSecret_example" // string | Client secret (required if client_id is provided) (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.RevokeToken(context.Background()).Token(token).TokenTypeHint(tokenTypeHint).ClientId(clientId).ClientSecret(clientSecret).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.RevokeToken``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RevokeToken`: map[string]interface{}
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.RevokeToken`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRevokeTokenRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **string** | The token to be revoked (access token or refresh token) | 
 **tokenTypeHint** | **string** | A hint about the type of the token. If omitted, the server will attempt to determine the token type. | 
 **clientId** | **string** | Client identifier for client credentials authentication (alternative to Bearer token) | 
 **clientSecret** | **string** | Client secret (required if client_id is provided) | 

### Return type

**map[string]interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded, application/json
- **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

