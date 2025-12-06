# TmiJsClient.OIDCDiscoveryApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJWKS**](OIDCDiscoveryApi.md#getJWKS) | **GET** /.well-known/jwks.json | JSON Web Key Set
[**getOAuthAuthorizationServerMetadata**](OIDCDiscoveryApi.md#getOAuthAuthorizationServerMetadata) | **GET** /.well-known/oauth-authorization-server | OAuth 2.0 Authorization Server Metadata
[**getOpenIDConfiguration**](OIDCDiscoveryApi.md#getOpenIDConfiguration) | **GET** /.well-known/openid-configuration | OpenID Connect Discovery Configuration

<a name="getJWKS"></a>
# **getJWKS**
> InlineResponse2002 getJWKS()

JSON Web Key Set

Returns the JSON Web Key Set (JWKS) for JWT signature verification

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.OIDCDiscoveryApi();
apiInstance.getJWKS().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getOAuthAuthorizationServerMetadata"></a>
# **getOAuthAuthorizationServerMetadata**
> InlineResponse2001 getOAuthAuthorizationServerMetadata()

OAuth 2.0 Authorization Server Metadata

Returns OAuth 2.0 authorization server metadata as per RFC 8414

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.OIDCDiscoveryApi();
apiInstance.getOAuthAuthorizationServerMetadata().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getOpenIDConfiguration"></a>
# **getOpenIDConfiguration**
> InlineResponse200 getOpenIDConfiguration()

OpenID Connect Discovery Configuration

Returns OpenID Connect provider configuration metadata as per RFC 8414

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.OIDCDiscoveryApi();
apiInstance.getOpenIDConfiguration().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

