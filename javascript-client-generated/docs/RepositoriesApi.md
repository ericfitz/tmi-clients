# TmiThreatModelingImprovedApi.RepositoriesApi

All URIs are relative to *http://localhost:{port}*

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
import {TmiThreatModelingImprovedApi} from 'tmi__threat_modeling_improved_api';
let defaultClient = TmiThreatModelingImprovedApi.ApiClient.instance;


let apiInstance = new TmiThreatModelingImprovedApi.RepositoriesApi();
let body = [new TmiThreatModelingImprovedApi.ThreatsThreatIdBody()]; // [ThreatsThreatIdBody] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let repositoryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Repository identifier

apiInstance.patchThreatModelRepository(body, threatModelId, repositoryId, (error, data, response) => {
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
 **repositoryId** | [**String**](.md)| Repository identifier | 

### Return type

[**Repository**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

