# TmiJsClient.AuditTrailApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAssetAuditTrail**](AuditTrailApi.md#getAssetAuditTrail) | **GET** /threat_models/{threat_model_id}/assets/{asset_id}/audit_trail | List audit trail for an asset
[**getAuditEntry**](AuditTrailApi.md#getAuditEntry) | **GET** /threat_models/{threat_model_id}/audit_trail/{entry_id} | Get a single audit trail entry
[**getDiagramAuditTrail**](AuditTrailApi.md#getDiagramAuditTrail) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id}/audit_trail | List audit trail for a diagram
[**getDocumentAuditTrail**](AuditTrailApi.md#getDocumentAuditTrail) | **GET** /threat_models/{threat_model_id}/documents/{document_id}/audit_trail | List audit trail for a document
[**getNoteAuditTrail**](AuditTrailApi.md#getNoteAuditTrail) | **GET** /threat_models/{threat_model_id}/notes/{note_id}/audit_trail | List audit trail for a note
[**getRepositoryAuditTrail**](AuditTrailApi.md#getRepositoryAuditTrail) | **GET** /threat_models/{threat_model_id}/repositories/{repository_id}/audit_trail | List audit trail for a repository
[**getThreatAuditTrail**](AuditTrailApi.md#getThreatAuditTrail) | **GET** /threat_models/{threat_model_id}/threats/{threat_id}/audit_trail | List audit trail for a threat
[**getThreatModelAuditTrail**](AuditTrailApi.md#getThreatModelAuditTrail) | **GET** /threat_models/{threat_model_id}/audit_trail | List audit trail for a threat model and all sub-objects
[**rollbackToVersion**](AuditTrailApi.md#rollbackToVersion) | **POST** /threat_models/{threat_model_id}/audit_trail/{entry_id}/rollback | Rollback an entity to a previous version

<a name="getAssetAuditTrail"></a>
# **getAssetAuditTrail**
> ListAuditTrailResponse getAssetAuditTrail(threatModelId, assetId, opts)

List audit trail for an asset

Returns a paginated list of audit trail entries for a specific resource

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuditTrailApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let assetId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Asset identifier
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.getAssetAuditTrail(threatModelId, assetId, opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **assetId** | [**String**](.md)| Asset identifier | 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getAuditEntry"></a>
# **getAuditEntry**
> AuditEntry getAuditEntry(threatModelId, entryId)

Get a single audit trail entry

Returns a single audit trail entry by ID

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuditTrailApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let entryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the audit entry

apiInstance.getAuditEntry(threatModelId, entryId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **entryId** | [**String**](.md)| Unique identifier of the audit entry | 

### Return type

[**AuditEntry**](AuditEntry.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getDiagramAuditTrail"></a>
# **getDiagramAuditTrail**
> ListAuditTrailResponse getDiagramAuditTrail(threatModelId, diagramId, opts)

List audit trail for a diagram

Returns a paginated list of audit trail entries for a specific resource

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuditTrailApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.getDiagramAuditTrail(threatModelId, diagramId, opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **diagramId** | [**String**](.md)| Diagram identifier | 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getDocumentAuditTrail"></a>
# **getDocumentAuditTrail**
> ListAuditTrailResponse getDocumentAuditTrail(threatModelId, documentId, opts)

List audit trail for a document

Returns a paginated list of audit trail entries for a specific resource

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuditTrailApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let documentId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Document identifier
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.getDocumentAuditTrail(threatModelId, documentId, opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **documentId** | [**String**](.md)| Document identifier | 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getNoteAuditTrail"></a>
# **getNoteAuditTrail**
> ListAuditTrailResponse getNoteAuditTrail(threatModelId, noteId, opts)

List audit trail for a note

Returns a paginated list of audit trail entries for a specific resource

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuditTrailApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let noteId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Note identifier
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.getNoteAuditTrail(threatModelId, noteId, opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **noteId** | [**String**](.md)| Note identifier | 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getRepositoryAuditTrail"></a>
# **getRepositoryAuditTrail**
> ListAuditTrailResponse getRepositoryAuditTrail(threatModelId, repositoryId, opts)

List audit trail for a repository

Returns a paginated list of audit trail entries for a specific resource

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuditTrailApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let repositoryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Repository identifier
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.getRepositoryAuditTrail(threatModelId, repositoryId, opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **repositoryId** | [**String**](.md)| Repository identifier | 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatAuditTrail"></a>
# **getThreatAuditTrail**
> ListAuditTrailResponse getThreatAuditTrail(threatModelId, threatId, opts)

List audit trail for a threat

Returns a paginated list of audit trail entries for a specific resource

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuditTrailApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat identifier
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.getThreatAuditTrail(threatModelId, threatId, opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **threatId** | [**String**](.md)| Threat identifier | 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelAuditTrail"></a>
# **getThreatModelAuditTrail**
> ListAuditTrailResponse getThreatModelAuditTrail(threatModelId, opts)

List audit trail for a threat model and all sub-objects

Returns a paginated list of audit trail entries

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuditTrailApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0, // Number | Number of results to skip
  'objectType': "objectType_example", // String | Filter by object type
  'changeType': "changeType_example", // String | Filter by change type
  'actorEmail': "actorEmail_example", // String | Filter by actor email
  'after': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter entries after this timestamp (ISO 8601)
  'before': new Date("2013-10-20T19:20:30+01:00") // Date | Filter entries before this timestamp (ISO 8601)
};
apiInstance.getThreatModelAuditTrail(threatModelId, opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]
 **objectType** | **String**| Filter by object type | [optional] 
 **changeType** | **String**| Filter by change type | [optional] 
 **actorEmail** | **String**| Filter by actor email | [optional] 
 **after** | **Date**| Filter entries after this timestamp (ISO 8601) | [optional] 
 **before** | **Date**| Filter entries before this timestamp (ISO 8601) | [optional] 

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="rollbackToVersion"></a>
# **rollbackToVersion**
> RollbackResponse rollbackToVersion(threatModelId, entryId)

Rollback an entity to a previous version

Restores an entity to the state captured in the specified audit entry&#x27;s version snapshot. Creates a new audit entry recording the rollback. Returns 410 Gone if the version snapshot has been pruned.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AuditTrailApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let entryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the audit entry

apiInstance.rollbackToVersion(threatModelId, entryId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **entryId** | [**String**](.md)| Unique identifier of the audit entry | 

### Return type

[**RollbackResponse**](RollbackResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

