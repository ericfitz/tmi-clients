# TmiJsClient.AuthenticationApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorizeOAuthProvider**](AuthenticationApi.md#authorizeOAuthProvider) | **GET** /oauth2/authorize | Initiate OAuth authorization flow
[**createClientCredential**](AuthenticationApi.md#createClientCredential) | **POST** /client-credentials | Create client credential
[**deleteClientCredential**](AuthenticationApi.md#deleteClientCredential) | **DELETE** /client-credentials/{id} | Delete client credential
[**exchangeOAuthCode**](AuthenticationApi.md#exchangeOAuthCode) | **POST** /oauth2/token | Exchange OAuth credentials for JWT tokens
[**getAuthProviders**](AuthenticationApi.md#getAuthProviders) | **GET** /oauth2/providers | List available OAuth providers
[**getCurrentUser**](AuthenticationApi.md#getCurrentUser) | **GET** /oauth2/userinfo | Get current user information
[**getCurrentUserProfile**](AuthenticationApi.md#getCurrentUserProfile) | **GET** /users/me | Get current user profile
[**getProviderGroups**](AuthenticationApi.md#getProviderGroups) | **GET** /oauth2/providers/{idp}/groups | Get groups for identity provider
[**getSAMLMetadata**](AuthenticationApi.md#getSAMLMetadata) | **GET** /saml/{provider}/metadata | Get SAML service provider metadata
[**getSAMLProviders**](AuthenticationApi.md#getSAMLProviders) | **GET** /saml/providers | List available SAML providers
[**handleOAuthCallback**](AuthenticationApi.md#handleOAuthCallback) | **GET** /oauth2/callback | Handle OAuth callback
[**initiateSAMLLogin**](AuthenticationApi.md#initiateSAMLLogin) | **GET** /saml/{provider}/login | Initiate SAML authentication
[**introspectToken**](AuthenticationApi.md#introspectToken) | **POST** /oauth2/introspect | Token Introspection
[**listClientCredentials**](AuthenticationApi.md#listClientCredentials) | **GET** /client-credentials | List client credentials
[**logoutUser**](AuthenticationApi.md#logoutUser) | **POST** /oauth2/revoke | Logout user
[**processSAMLLogout**](AuthenticationApi.md#processSAMLLogout) | **GET** /saml/slo | SAML Single Logout
[**processSAMLLogoutPost**](AuthenticationApi.md#processSAMLLogoutPost) | **POST** /saml/slo | SAML Single Logout (POST)
[**processSAMLResponse**](AuthenticationApi.md#processSAMLResponse) | **POST** /saml/acs | SAML Assertion Consumer Service
[**refreshToken**](AuthenticationApi.md#refreshToken) | **POST** /oauth2/refresh | Refresh JWT token

<a name="authorizeOAuthProvider"></a>
# **authorizeOAuthProvider**
> authorizeOAuthProvider(scope, codeChallenge, codeChallengeMethod, opts)

Initiate OAuth authorization flow

Redirects user to OAuth provider&#x27;s authorization page. Supports client callback URL for seamless client integration. Generates state parameter for CSRF protection.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.AuthenticationApi();
let scope = "scope_example"; // String | OAuth 2.0 scope parameter. For OpenID Connect, must include \"openid\". Supports \"profile\" and \"email\" scopes. Other scopes are silently ignored. Space-separated values.
let codeChallenge = "codeChallenge_example"; // String | PKCE code challenge (RFC 7636) - Base64url-encoded SHA256 hash of the code_verifier. Must be 43-128 characters using unreserved characters [A-Za-z0-9-._~]. The server associates this with the authorization code for later verification during token exchange.
let codeChallengeMethod = "codeChallengeMethod_example"; // String | PKCE code challenge method (RFC 7636) - Specifies the transformation applied to the code_verifier. Only \"S256\" (SHA256) is supported for security. The \"plain\" method is not supported.
let opts = { 
  'idp': "idp_example", // String | OAuth provider identifier. Defaults to 'test' provider in non-production builds if not specified.
  'clientCallback': "clientCallback_example", // String | Client callback URL where TMI should redirect after successful OAuth completion with tokens in URL fragment (#access_token=...). If not provided, tokens are returned as JSON response. Per OAuth 2.0 implicit flow spec, tokens are in fragments to prevent logging.
  'state': "state_example", // String | CSRF protection state parameter. Recommended for security. Will be included in the callback response.
  'loginHint': "loginHint_example" // String | User identity hint for test OAuth provider. Allows specifying a desired user identity for testing and automation. Only supported by the test provider (ignored by production providers like Google, GitHub, etc.). Must be 3-20 characters, alphanumeric and hyphens only.
};
apiInstance.authorizeOAuthProvider(scope, codeChallenge, codeChallengeMethod, opts).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **String**| OAuth 2.0 scope parameter. For OpenID Connect, must include \&quot;openid\&quot;. Supports \&quot;profile\&quot; and \&quot;email\&quot; scopes. Other scopes are silently ignored. Space-separated values. | 
 **codeChallenge** | **String**| PKCE code challenge (RFC 7636) - Base64url-encoded SHA256 hash of the code_verifier. Must be 43-128 characters using unreserved characters [A-Za-z0-9-._~]. The server associates this with the authorization code for later verification during token exchange. | 
 **codeChallengeMethod** | **String**| PKCE code challenge method (RFC 7636) - Specifies the transformation applied to the code_verifier. Only \&quot;S256\&quot; (SHA256) is supported for security. The \&quot;plain\&quot; method is not supported. | 
 **idp** | **String**| OAuth provider identifier. Defaults to &#x27;test&#x27; provider in non-production builds if not specified. | [optional] 
 **clientCallback** | **String**| Client callback URL where TMI should redirect after successful OAuth completion with tokens in URL fragment (#access_token&#x3D;...). If not provided, tokens are returned as JSON response. Per OAuth 2.0 implicit flow spec, tokens are in fragments to prevent logging. | [optional] 
 **state** | **String**| CSRF protection state parameter. Recommended for security. Will be included in the callback response. | [optional] 
 **loginHint** | **String**| User identity hint for test OAuth provider. Allows specifying a desired user identity for testing and automation. Only supported by the test provider (ignored by production providers like Google, GitHub, etc.). Must be 3-20 characters, alphanumeric and hyphens only. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="createClientCredential"></a>
# **createClientCredential**
> ClientCredentialResponse createClientCredential(body)

Create client credential

Creates a new OAuth 2.0 client credential for machine-to-machine authentication. The client_secret is ONLY returned once at creation and cannot be retrieved later.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuthenticationApi();
let body = new TmiJsClient.ClientcredentialsBody(); // ClientcredentialsBody | 

apiInstance.createClientCredential(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientcredentialsBody**](ClientcredentialsBody.md)|  | 

### Return type

[**ClientCredentialResponse**](ClientCredentialResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteClientCredential"></a>
# **deleteClientCredential**
> deleteClientCredential(id)

Delete client credential

Permanently deletes a client credential. All tokens issued with this credential will immediately become invalid.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuthenticationApi();
let id = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Client credential UUID

apiInstance.deleteClientCredential(id).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**String**](.md)| Client credential UUID | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="exchangeOAuthCode"></a>
# **exchangeOAuthCode**
> AuthTokenResponse exchangeOAuthCode(body, grantType, code, clientId, clientSecret, refreshToken, redirectUri, codeVerifier, state, opts)

Exchange OAuth credentials for JWT tokens

Provider-neutral endpoint to exchange OAuth credentials for TMI JWT tokens. Supports three grant types: (1) authorization_code for OAuth provider flows (Google, GitHub, Microsoft), (2) client_credentials for machine-to-machine authentication (RFC 6749 Section 4.4), and (3) refresh_token for token renewal. Accepts both application/json and application/x-www-form-urlencoded content types.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.AuthenticationApi();
let body = new TmiJsClient.Oauth2TokenBody(); // Oauth2TokenBody | 
let grantType = "grantType_example"; // String | 
let code = "code_example"; // String | 
let clientId = "clientId_example"; // String | 
let clientSecret = "clientSecret_example"; // String | 
let refreshToken = "refreshToken_example"; // String | 
let redirectUri = "redirectUri_example"; // String | 
let codeVerifier = "codeVerifier_example"; // String | 
let state = "state_example"; // String | 
let opts = { 
  'idp': "idp_example" // String | OAuth provider identifier. Defaults to 'test' provider in non-production builds if not specified.
};
apiInstance.exchangeOAuthCode(body, grantType, code, clientId, clientSecret, refreshToken, redirectUri, codeVerifier, state, opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Oauth2TokenBody**](Oauth2TokenBody.md)|  | 
 **grantType** | **String**|  | 
 **code** | **String**|  | 
 **clientId** | **String**|  | 
 **clientSecret** | **String**|  | 
 **refreshToken** | **String**|  | 
 **redirectUri** | **String**|  | 
 **codeVerifier** | **String**|  | 
 **state** | **String**|  | 
 **idp** | **String**| OAuth provider identifier. Defaults to &#x27;test&#x27; provider in non-production builds if not specified. | [optional] 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

<a name="getAuthProviders"></a>
# **getAuthProviders**
> InlineResponse2004 getAuthProviders()

List available OAuth providers

Returns a list of configured OAuth providers available for authentication

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.AuthenticationApi();
apiInstance.getAuthProviders().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getCurrentUser"></a>
# **getCurrentUser**
> InlineResponse2006 getCurrentUser()

Get current user information

Returns information about the currently authenticated user

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuthenticationApi();
apiInstance.getCurrentUser().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getCurrentUserProfile"></a>
# **getCurrentUserProfile**
> UserWithAdminStatus getCurrentUserProfile()

Get current user profile

Returns detailed information about the currently authenticated user including groups and identity provider

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuthenticationApi();
apiInstance.getCurrentUserProfile().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserWithAdminStatus**](UserWithAdminStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getProviderGroups"></a>
# **getProviderGroups**
> InlineResponse2005 getProviderGroups(idp)

Get groups for identity provider

Returns groups available from a specific identity provider for autocomplete and discovery

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuthenticationApi();
let idp = "idp_example"; // String | Identity provider ID (e.g., saml_okta, saml_azure)

apiInstance.getProviderGroups(idp).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp** | **String**| Identity provider ID (e.g., saml_okta, saml_azure) | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getSAMLMetadata"></a>
# **getSAMLMetadata**
> &#x27;String&#x27; getSAMLMetadata(provider)

Get SAML service provider metadata

Returns the SP metadata XML for SAML configuration

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.AuthenticationApi();
let provider = "provider_example"; // String | SAML provider identifier

apiInstance.getSAMLMetadata(provider).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **String**| SAML provider identifier | 

### Return type

**&#x27;String&#x27;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/samlmetadata+xml, application/json

<a name="getSAMLProviders"></a>
# **getSAMLProviders**
> InlineResponse20010 getSAMLProviders()

List available SAML providers

Returns a list of configured SAML providers available for authentication

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.AuthenticationApi();
apiInstance.getSAMLProviders().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="handleOAuthCallback"></a>
# **handleOAuthCallback**
> AuthTokenResponse handleOAuthCallback(code, opts)

Handle OAuth callback

Exchanges OAuth authorization code for JWT tokens. If client_callback was provided during authorization, redirects to client with tokens. Otherwise returns tokens as JSON response.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.AuthenticationApi();
let code = "code_example"; // String | Authorization code from the OAuth provider
let opts = { 
  'state': "state_example" // String | Optional state parameter for CSRF protection
};
apiInstance.handleOAuthCallback(code, opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **String**| Authorization code from the OAuth provider | 
 **state** | **String**| Optional state parameter for CSRF protection | [optional] 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="initiateSAMLLogin"></a>
# **initiateSAMLLogin**
> initiateSAMLLogin(provider, opts)

Initiate SAML authentication

Starts SAML authentication flow by redirecting to IdP

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.AuthenticationApi();
let provider = "provider_example"; // String | SAML provider identifier
let opts = { 
  'clientCallback': "clientCallback_example" // String | Client callback URL to redirect after authentication
};
apiInstance.initiateSAMLLogin(provider, opts).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **String**| SAML provider identifier | 
 **clientCallback** | **String**| Client callback URL to redirect after authentication | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="introspectToken"></a>
# **introspectToken**
> InlineResponse2003 introspectToken(token, tokenTypeHint)

Token Introspection

Introspects a JWT token to determine its validity and metadata as per RFC 7662

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.AuthenticationApi();
let token = "token_example"; // String | 
let tokenTypeHint = "tokenTypeHint_example"; // String | 

apiInstance.introspectToken(token, tokenTypeHint).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **String**|  | 
 **tokenTypeHint** | **String**|  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

<a name="listClientCredentials"></a>
# **listClientCredentials**
> [ClientCredentialInfo] listClientCredentials()

List client credentials

Retrieves all client credentials owned by the authenticated user. Secrets are never returned.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuthenticationApi();
apiInstance.listClientCredentials().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[ClientCredentialInfo]**](ClientCredentialInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="logoutUser"></a>
# **logoutUser**
> InlineResponse2007 logoutUser(opts)

Logout user

Invalidates the user&#x27;s JWT token by adding it to a blacklist, effectively ending the session. Once logged out, the token cannot be used for further authenticated requests until it naturally expires. The token blacklist is maintained in Redis with automatic cleanup based on token expiration times.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuthenticationApi();
let opts = { 
  'body': null // Object | Empty request body - token is provided via Authorization header
};
apiInstance.logoutUser(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)| Empty request body - token is provided via Authorization header | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="processSAMLLogout"></a>
# **processSAMLLogout**
> InlineResponse2009 processSAMLLogout(sAMLRequest)

SAML Single Logout

Handles SAML logout requests from IdP

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.AuthenticationApi();
let sAMLRequest = "sAMLRequest_example"; // String | Base64-encoded SAML logout request

apiInstance.processSAMLLogout(sAMLRequest).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sAMLRequest** | **String**| Base64-encoded SAML logout request | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="processSAMLLogoutPost"></a>
# **processSAMLLogoutPost**
> InlineResponse2009 processSAMLLogoutPost(opts)

SAML Single Logout (POST)

Handles SAML logout requests from IdP via POST

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.AuthenticationApi();
let opts = { 
  'sAMLRequest': "sAMLRequest_example" // String | 
};
apiInstance.processSAMLLogoutPost(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sAMLRequest** | **String**|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

<a name="processSAMLResponse"></a>
# **processSAMLResponse**
> AuthTokenResponse processSAMLResponse(opts)

SAML Assertion Consumer Service

Processes SAML responses from IdP after authentication

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.AuthenticationApi();
let opts = { 
  'sAMLResponse': "sAMLResponse_example", // String | 
  'relayState': "relayState_example" // String | 
};
apiInstance.processSAMLResponse(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sAMLResponse** | **String**|  | [optional] 
 **relayState** | **String**|  | [optional] 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

<a name="refreshToken"></a>
# **refreshToken**
> AuthTokenResponse refreshToken(opts)

Refresh JWT token

Exchanges a refresh token for a new JWT access token

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.AuthenticationApi();
let opts = { 
  'body': new TmiJsClient.Oauth2RefreshBody() // Oauth2RefreshBody | 
};
apiInstance.refreshToken(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Oauth2RefreshBody**](Oauth2RefreshBody.md)|  | [optional] 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

