# TmiJsClient.ConfigurationApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getClientConfig**](ConfigurationApi.md#getClientConfig) | **GET** /config | Get client configuration

<a name="getClientConfig"></a>
# **getClientConfig**
> ClientConfig getClientConfig()

Get client configuration

Returns configuration settings for client applications such as tmi-ux. This endpoint is public and cacheable.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.ConfigurationApi();
apiInstance.getClientConfig().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientConfig**](ClientConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

