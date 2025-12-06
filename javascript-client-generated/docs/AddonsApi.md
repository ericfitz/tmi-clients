# TmiJsClient.AddonsApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAddon**](AddonsApi.md#createAddon) | **POST** /addons | Create add-on
[**deleteAddon**](AddonsApi.md#deleteAddon) | **DELETE** /addons/{id} | Delete add-on
[**getAddon**](AddonsApi.md#getAddon) | **GET** /addons/{id} | Get add-on
[**getInvocation**](AddonsApi.md#getInvocation) | **GET** /invocations/{id} | Get invocation
[**invokeAddon**](AddonsApi.md#invokeAddon) | **POST** /addons/{id}/invoke | Invoke add-on
[**listAddons**](AddonsApi.md#listAddons) | **GET** /addons | List add-ons
[**listInvocations**](AddonsApi.md#listInvocations) | **GET** /invocations | List invocations
[**updateInvocationStatus**](AddonsApi.md#updateInvocationStatus) | **POST** /invocations/{id}/status | Update invocation status

<a name="createAddon"></a>
# **createAddon**
> AddonResponse createAddon(body)

Create add-on

Create a new add-on (administrators only)

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AddonsApi();
let body = new TmiJsClient.CreateAddonRequest(); // CreateAddonRequest | 

apiInstance.createAddon(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAddonRequest**](CreateAddonRequest.md)|  | 

### Return type

[**AddonResponse**](AddonResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteAddon"></a>
# **deleteAddon**
> deleteAddon(id)

Delete add-on

Delete an add-on (administrators only)

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AddonsApi();
let id = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Resource identifier

apiInstance.deleteAddon(id).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**String**](.md)| Resource identifier | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getAddon"></a>
# **getAddon**
> AddonResponse getAddon(id)

Get add-on

Get a single add-on by ID

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AddonsApi();
let id = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Resource identifier

apiInstance.getAddon(id).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**String**](.md)| Resource identifier | 

### Return type

[**AddonResponse**](AddonResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getInvocation"></a>
# **getInvocation**
> InvocationResponse getInvocation(id)

Get invocation

Get a single invocation by ID (own invocations or admin)

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AddonsApi();
let id = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Resource identifier

apiInstance.getInvocation(id).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**String**](.md)| Resource identifier | 

### Return type

[**InvocationResponse**](InvocationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="invokeAddon"></a>
# **invokeAddon**
> InvokeAddonResponse invokeAddon(body, id)

Invoke add-on

Trigger an add-on invocation (authenticated users)

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AddonsApi();
let body = new TmiJsClient.InvokeAddonRequest(); // InvokeAddonRequest | 
let id = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Resource identifier

apiInstance.invokeAddon(body, id).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvokeAddonRequest**](InvokeAddonRequest.md)|  | 
 **id** | [**String**](.md)| Resource identifier | 

### Return type

[**InvokeAddonResponse**](InvokeAddonResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="listAddons"></a>
# **listAddons**
> Object listAddons(opts)

List add-ons

List all add-ons (authenticated users)

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AddonsApi();
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0, // Number | Number of results to skip
  'threatModelId': "38400000-8cf0-11bd-b23e-10b96e4ef00d" // String | Filter by threat model
};
apiInstance.listAddons(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]
 **threatModelId** | [**String**](.md)| Filter by threat model | [optional] 

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listInvocations"></a>
# **listInvocations**
> Object listInvocations(opts)

List invocations

List add-on invocations (users see own, admins see all)

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AddonsApi();
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0, // Number | Number of results to skip
  'status': "status_example", // String | Filter by status
  'addonId': "38400000-8cf0-11bd-b23e-10b96e4ef00d" // String | Filter by add-on
};
apiInstance.listInvocations(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]
 **status** | **String**| Filter by status | [optional] 
 **addonId** | [**String**](.md)| Filter by add-on | [optional] 

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="updateInvocationStatus"></a>
# **updateInvocationStatus**
> UpdateInvocationStatusResponse updateInvocationStatus(body, id, xWebhookSignature)

Update invocation status

Update invocation status (webhook callback with HMAC authentication)

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AddonsApi();
let body = new TmiJsClient.UpdateInvocationStatusRequest(); // UpdateInvocationStatusRequest | 
let id = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Resource identifier
let xWebhookSignature = "xWebhookSignature_example"; // String | HMAC-SHA256 signature (format: sha256={hex_signature})

apiInstance.updateInvocationStatus(body, id, xWebhookSignature).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateInvocationStatusRequest**](UpdateInvocationStatusRequest.md)|  | 
 **id** | [**String**](.md)| Resource identifier | 
 **xWebhookSignature** | **String**| HMAC-SHA256 signature (format: sha256&#x3D;{hex_signature}) | 

### Return type

[**UpdateInvocationStatusResponse**](UpdateInvocationStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

