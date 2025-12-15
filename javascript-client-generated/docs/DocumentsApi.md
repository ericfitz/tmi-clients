# TmiThreatModelingImprovedApi.DocumentsApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patchThreatModelDocument**](DocumentsApi.md#patchThreatModelDocument) | **PATCH** /threat_models/{threat_model_id}/documents/{document_id} | Partially update document

<a name="patchThreatModelDocument"></a>
# **patchThreatModelDocument**
> Document patchThreatModelDocument(body, threatModelId, documentId)

Partially update document

Apply JSON Patch operations to partially update a document

### Example
```javascript
import {TmiThreatModelingImprovedApi} from 'tmi__threat_modeling_improved_api';
let defaultClient = TmiThreatModelingImprovedApi.ApiClient.instance;


let apiInstance = new TmiThreatModelingImprovedApi.DocumentsApi();
let body = [new TmiThreatModelingImprovedApi.ThreatsThreatIdBody()]; // [ThreatsThreatIdBody] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let documentId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Document identifier

apiInstance.patchThreatModelDocument(body, threatModelId, documentId, (error, data, response) => {
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
 **body** | [**[ThreatsThreatIdBody]**](ThreatsThreatIdBody.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **documentId** | [**String**](.md)| Document identifier | 

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

