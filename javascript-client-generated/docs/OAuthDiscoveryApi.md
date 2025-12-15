# TmiThreatModelingImprovedApi.OAuthDiscoveryApi

All URIs are relative to *http://localhost:{port}*

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
import {TmiThreatModelingImprovedApi} from 'tmi__threat_modeling_improved_api';

let apiInstance = new TmiThreatModelingImprovedApi.OAuthDiscoveryApi();
apiInstance.getOAuthProtectedResourceMetadata((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
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

