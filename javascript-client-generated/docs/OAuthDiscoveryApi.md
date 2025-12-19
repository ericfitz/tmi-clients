# TmiJsClient.OAuthDiscoveryApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOAuthProtectedResourceMetadata**](OAuthDiscoveryApi.md#getOAuthProtectedResourceMetadata) | **GET** /.well-known/oauth-protected-resource | OAuth 2.0 Protected Resource Metadata

<a name="getOAuthProtectedResourceMetadata"></a>
# **getOAuthProtectedResourceMetadata**
> OAuthProtectedResourceMetadata getOAuthProtectedResourceMetadata()

OAuth 2.0 Protected Resource Metadata

Returns OAuth 2.0 protected resource metadata as per RFC 9728

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.OAuthDiscoveryApi();
apiInstance.getOAuthProtectedResourceMetadata().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OAuthProtectedResourceMetadata**](OAuthProtectedResourceMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

