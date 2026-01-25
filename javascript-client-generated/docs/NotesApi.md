# TmiJsClient.NotesApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patchThreatModelNote**](NotesApi.md#patchThreatModelNote) | **PATCH** /threat_models/{threat_model_id}/notes/{note_id} | Partially update note

<a name="patchThreatModelNote"></a>
# **patchThreatModelNote**
> Note patchThreatModelNote(body, threatModelId, noteId)

Partially update note

Apply JSON Patch operations to partially update a note

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.NotesApi();
let body = [new TmiJsClient.JsonPatchDocumentInner()]; // [JsonPatchDocumentInner] | JSON Patch operations to apply to the note
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let noteId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Note identifier

apiInstance.patchThreatModelNote(body, threatModelId, noteId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| JSON Patch operations to apply to the note | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **noteId** | [**String**](.md)| Note identifier | 

### Return type

[**Note**](Note.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

