# TmiJsClient.ThreatsApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkDeleteThreatModelThreats**](ThreatsApi.md#bulkDeleteThreatModelThreats) | **DELETE** /threat_models/{threat_model_id}/threats/bulk | Bulk DELETE threats
[**bulkPatchThreatModelThreats**](ThreatsApi.md#bulkPatchThreatModelThreats) | **PATCH** /threat_models/{threat_model_id}/threats/bulk | Bulk PATCH threats

<a name="bulkDeleteThreatModelThreats"></a>
# **bulkDeleteThreatModelThreats**
> InlineResponse2007 bulkDeleteThreatModelThreats(threatModelId, threatIds)

Bulk DELETE threats

Delete multiple threats in a single request

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatsApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatIds = ["threatIds_example"]; // [String] | Comma-separated list of threat IDs to delete (UUID format)

apiInstance.bulkDeleteThreatModelThreats(threatModelId, threatIds).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **threatIds** | [**[String]**](String.md)| Comma-separated list of threat IDs to delete (UUID format) | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="bulkPatchThreatModelThreats"></a>
# **bulkPatchThreatModelThreats**
> [Threat] bulkPatchThreatModelThreats(body, threatModelId)

Bulk PATCH threats

Apply JSON Patch operations to multiple threats. Each patch specifies a threat ID and an array of RFC 6902 operations to apply.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatsApi();
let body = new TmiJsClient.BulkPatchRequest(); // BulkPatchRequest | JSON Patch operations to apply to multiple threats
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.bulkPatchThreatModelThreats(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkPatchRequest**](BulkPatchRequest.md)| JSON Patch operations to apply to multiple threats | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**[Threat]**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

