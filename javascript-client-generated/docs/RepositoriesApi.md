# TmiJsClient.RepositoriesApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patchThreatModelRepository**](RepositoriesApi.md#patchThreatModelRepository) | **PATCH** /threat_models/{threat_model_id}/repositories/{repository_id} | Partially update repository

<a name="patchThreatModelRepository"></a>
# **patchThreatModelRepository**
> Repository patchThreatModelRepository(body, threatModelId, repositoryId)

Partially update repository

Apply JSON Patch operations to partially update a repository

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.RepositoriesApi();
let body = [new TmiJsClient.JsonPatchDocumentInner()]; // [JsonPatchDocumentInner] | JSON Patch operations to apply to the repository
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let repositoryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Repository identifier

apiInstance.patchThreatModelRepository(body, threatModelId, repositoryId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| JSON Patch operations to apply to the repository | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **repositoryId** | [**String**](.md)| Repository identifier | 

### Return type

[**Repository**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

