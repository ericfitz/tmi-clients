# TmiJsClient.GeneralApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getApiInfo**](GeneralApi.md#getApiInfo) | **GET** / | Get API information

<a name="getApiInfo"></a>
# **getApiInfo**
> ApiInfo getApiInfo()

Get API information

Returns service, API, and operator information without authentication

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';

let apiInstance = new TmiJsClient.GeneralApi();
apiInstance.getApiInfo().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiInfo**](ApiInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

