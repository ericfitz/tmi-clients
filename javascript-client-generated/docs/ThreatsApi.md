# TmiThreatModelingImprovedApi.ThreatsApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkDeleteThreatModelThreats**](ThreatsApi.md#bulkDeleteThreatModelThreats) | **DELETE** /threat_models/{threat_model_id}/threats/bulk | Bulk DELETE threats
[**bulkPatchThreatModelThreats**](ThreatsApi.md#bulkPatchThreatModelThreats) | **PATCH** /threat_models/{threat_model_id}/threats/bulk | Bulk PATCH threats

<a name="bulkDeleteThreatModelThreats"></a>
# **bulkDeleteThreatModelThreats**
> InlineResponse2008 bulkDeleteThreatModelThreats(threatModelId, threatIds)

Bulk DELETE threats

Delete multiple threats in a single request

### Example
```javascript
import {TmiThreatModelingImprovedApi} from 'tmi__threat_modeling_improved_api';
let defaultClient = TmiThreatModelingImprovedApi.ApiClient.instance;


let apiInstance = new TmiThreatModelingImprovedApi.ThreatsApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatIds = ["threatIds_example"]; // [String] | Comma-separated list of threat IDs to delete (UUID format)

apiInstance.bulkDeleteThreatModelThreats(threatModelId, threatIds, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **threatIds** | [**[String]**](String.md)| Comma-separated list of threat IDs to delete (UUID format) | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="bulkPatchThreatModelThreats"></a>
# **bulkPatchThreatModelThreats**
> [Threat] bulkPatchThreatModelThreats(body, threatModelId)

Bulk PATCH threats

Apply JSON Patch operations to multiple threats in a single request

### Example
```javascript
import {TmiThreatModelingImprovedApi} from 'tmi__threat_modeling_improved_api';
let defaultClient = TmiThreatModelingImprovedApi.ApiClient.instance;


let apiInstance = new TmiThreatModelingImprovedApi.ThreatsApi();
let body = new TmiThreatModelingImprovedApi.ThreatsBulkBody(); // ThreatsBulkBody | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.bulkPatchThreatModelThreats(body, threatModelId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThreatsBulkBody**](ThreatsBulkBody.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**[Threat]**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

