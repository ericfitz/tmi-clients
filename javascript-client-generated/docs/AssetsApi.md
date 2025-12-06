# TmiJsClient.AssetsApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patchThreatModelAsset**](AssetsApi.md#patchThreatModelAsset) | **PATCH** /threat_models/{threat_model_id}/assets/{asset_id} | Partially update asset

<a name="patchThreatModelAsset"></a>
# **patchThreatModelAsset**
> Asset patchThreatModelAsset(body, threatModelId, assetId)

Partially update asset

Apply JSON Patch operations to partially update a asset

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AssetsApi();
let body = [new TmiJsClient.ThreatsThreatIdBody()]; // [ThreatsThreatIdBody] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let assetId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Asset identifier

apiInstance.patchThreatModelAsset(body, threatModelId, assetId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[ThreatsThreatIdBody]**](ThreatsThreatIdBody.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **assetId** | [**String**](.md)| Asset identifier | 

### Return type

[**Asset**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

