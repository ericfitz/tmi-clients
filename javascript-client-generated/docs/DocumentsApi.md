# TmiJsClient.DocumentsApi

All URIs are relative to *https://api.tmi.dev*

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
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.DocumentsApi();
let body = [new TmiJsClient.JsonPatchDocumentInner()]; // [JsonPatchDocumentInner] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let documentId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Document identifier

apiInstance.patchThreatModelDocument(body, threatModelId, documentId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **documentId** | [**String**](.md)| Document identifier | 

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

