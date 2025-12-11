# TmiJsClient.ThreatModelSubResourcesApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkCreateDiagramMetadata**](ThreatModelSubResourcesApi.md#bulkCreateDiagramMetadata) | **POST** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/bulk | Bulk create diagram metadata
[**bulkCreateDocumentMetadata**](ThreatModelSubResourcesApi.md#bulkCreateDocumentMetadata) | **POST** /threat_models/{threat_model_id}/documents/{document_id}/metadata/bulk | Bulk create document metadata
[**bulkCreateNoteMetadata**](ThreatModelSubResourcesApi.md#bulkCreateNoteMetadata) | **POST** /threat_models/{threat_model_id}/notes/{note_id}/metadata/bulk | Bulk create note metadata
[**bulkCreateRepositoryMetadata**](ThreatModelSubResourcesApi.md#bulkCreateRepositoryMetadata) | **POST** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/bulk | Bulk create source metadata
[**bulkCreateThreatMetadata**](ThreatModelSubResourcesApi.md#bulkCreateThreatMetadata) | **POST** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/bulk | Bulk create threat metadata
[**bulkCreateThreatModelAssetMetadata**](ThreatModelSubResourcesApi.md#bulkCreateThreatModelAssetMetadata) | **POST** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/bulk | Bulk create asset metadata
[**bulkCreateThreatModelAssets**](ThreatModelSubResourcesApi.md#bulkCreateThreatModelAssets) | **POST** /threat_models/{threat_model_id}/assets/bulk | Bulk create assets
[**bulkCreateThreatModelDocuments**](ThreatModelSubResourcesApi.md#bulkCreateThreatModelDocuments) | **POST** /threat_models/{threat_model_id}/documents/bulk | Bulk create documents
[**bulkCreateThreatModelMetadata**](ThreatModelSubResourcesApi.md#bulkCreateThreatModelMetadata) | **POST** /threat_models/{threat_model_id}/metadata/bulk | Bulk create threat model metadata
[**bulkCreateThreatModelRepositories**](ThreatModelSubResourcesApi.md#bulkCreateThreatModelRepositories) | **POST** /threat_models/{threat_model_id}/repositories/bulk | Bulk create sources
[**bulkCreateThreatModelThreats**](ThreatModelSubResourcesApi.md#bulkCreateThreatModelThreats) | **POST** /threat_models/{threat_model_id}/threats/bulk | Bulk create threats
[**bulkUpdateNoteMetadata**](ThreatModelSubResourcesApi.md#bulkUpdateNoteMetadata) | **PUT** /threat_models/{threat_model_id}/notes/{note_id}/metadata/bulk | Bulk update note metadata
[**bulkUpdateThreatModelThreats**](ThreatModelSubResourcesApi.md#bulkUpdateThreatModelThreats) | **PUT** /threat_models/{threat_model_id}/threats/bulk | Bulk update threats
[**bulkUpsertDiagramMetadata**](ThreatModelSubResourcesApi.md#bulkUpsertDiagramMetadata) | **PUT** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/bulk | Bulk upsert diagram metadata
[**bulkUpsertDocumentMetadata**](ThreatModelSubResourcesApi.md#bulkUpsertDocumentMetadata) | **PUT** /threat_models/{threat_model_id}/documents/{document_id}/metadata/bulk | Bulk upsert document metadata
[**bulkUpsertRepositoryMetadata**](ThreatModelSubResourcesApi.md#bulkUpsertRepositoryMetadata) | **PUT** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/bulk | Bulk upsert repository metadata
[**bulkUpsertThreatMetadata**](ThreatModelSubResourcesApi.md#bulkUpsertThreatMetadata) | **PUT** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/bulk | Bulk upsert threat metadata
[**bulkUpsertThreatModelAssetMetadata**](ThreatModelSubResourcesApi.md#bulkUpsertThreatModelAssetMetadata) | **PUT** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/bulk | Bulk upsert asset metadata
[**bulkUpsertThreatModelAssets**](ThreatModelSubResourcesApi.md#bulkUpsertThreatModelAssets) | **PUT** /threat_models/{threat_model_id}/assets/bulk | Bulk upsert assets
[**bulkUpsertThreatModelDocuments**](ThreatModelSubResourcesApi.md#bulkUpsertThreatModelDocuments) | **PUT** /threat_models/{threat_model_id}/documents/bulk | Bulk upsert documents
[**bulkUpsertThreatModelMetadata**](ThreatModelSubResourcesApi.md#bulkUpsertThreatModelMetadata) | **PUT** /threat_models/{threat_model_id}/metadata/bulk | Bulk upsert threat model metadata
[**bulkUpsertThreatModelRepositories**](ThreatModelSubResourcesApi.md#bulkUpsertThreatModelRepositories) | **PUT** /threat_models/{threat_model_id}/repositories/bulk | Bulk upsert repositories
[**createDiagramMetadata**](ThreatModelSubResourcesApi.md#createDiagramMetadata) | **POST** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata | Create diagram metadata
[**createDocumentMetadata**](ThreatModelSubResourcesApi.md#createDocumentMetadata) | **POST** /threat_models/{threat_model_id}/documents/{document_id}/metadata | Create document metadata
[**createNoteMetadata**](ThreatModelSubResourcesApi.md#createNoteMetadata) | **POST** /threat_models/{threat_model_id}/notes/{note_id}/metadata | Create note metadata
[**createRepositoryMetadata**](ThreatModelSubResourcesApi.md#createRepositoryMetadata) | **POST** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata | Create source metadata
[**createThreatMetadata**](ThreatModelSubResourcesApi.md#createThreatMetadata) | **POST** /threat_models/{threat_model_id}/threats/{threat_id}/metadata | Create threat metadata
[**createThreatModelAsset**](ThreatModelSubResourcesApi.md#createThreatModelAsset) | **POST** /threat_models/{threat_model_id}/assets | Create a new asset
[**createThreatModelAssetMetadata**](ThreatModelSubResourcesApi.md#createThreatModelAssetMetadata) | **POST** /threat_models/{threat_model_id}/assets/{asset_id}/metadata | Add metadata to an asset
[**createThreatModelDiagram**](ThreatModelSubResourcesApi.md#createThreatModelDiagram) | **POST** /threat_models/{threat_model_id}/diagrams | Create a new diagram
[**createThreatModelDocument**](ThreatModelSubResourcesApi.md#createThreatModelDocument) | **POST** /threat_models/{threat_model_id}/documents | Create a new document
[**createThreatModelMetadata**](ThreatModelSubResourcesApi.md#createThreatModelMetadata) | **POST** /threat_models/{threat_model_id}/metadata | Create threat model metadata
[**createThreatModelNote**](ThreatModelSubResourcesApi.md#createThreatModelNote) | **POST** /threat_models/{threat_model_id}/notes | Create a new note
[**createThreatModelRepository**](ThreatModelSubResourcesApi.md#createThreatModelRepository) | **POST** /threat_models/{threat_model_id}/repositories | Create a new source reference
[**createThreatModelThreat**](ThreatModelSubResourcesApi.md#createThreatModelThreat) | **POST** /threat_models/{threat_model_id}/threats | Create a new threat
[**deleteDiagramMetadataByKey**](ThreatModelSubResourcesApi.md#deleteDiagramMetadataByKey) | **DELETE** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/{key} | Delete diagram metadata by key
[**deleteDocumentMetadataByKey**](ThreatModelSubResourcesApi.md#deleteDocumentMetadataByKey) | **DELETE** /threat_models/{threat_model_id}/documents/{document_id}/metadata/{key} | Delete document metadata by key
[**deleteNoteMetadataByKey**](ThreatModelSubResourcesApi.md#deleteNoteMetadataByKey) | **DELETE** /threat_models/{threat_model_id}/notes/{note_id}/metadata/{key} | Delete note metadata by key
[**deleteRepositoryMetadataByKey**](ThreatModelSubResourcesApi.md#deleteRepositoryMetadataByKey) | **DELETE** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/{key} | Delete source metadata by key
[**deleteThreatMetadataByKey**](ThreatModelSubResourcesApi.md#deleteThreatMetadataByKey) | **DELETE** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/{key} | Delete threat metadata by key
[**deleteThreatModelAsset**](ThreatModelSubResourcesApi.md#deleteThreatModelAsset) | **DELETE** /threat_models/{threat_model_id}/assets/{asset_id} | Delete an asset
[**deleteThreatModelAssetMetadata**](ThreatModelSubResourcesApi.md#deleteThreatModelAssetMetadata) | **DELETE** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/{key} | Delete asset metadata
[**deleteThreatModelDiagram**](ThreatModelSubResourcesApi.md#deleteThreatModelDiagram) | **DELETE** /threat_models/{threat_model_id}/diagrams/{diagram_id} | Delete a diagram
[**deleteThreatModelDocument**](ThreatModelSubResourcesApi.md#deleteThreatModelDocument) | **DELETE** /threat_models/{threat_model_id}/documents/{document_id} | Delete a document
[**deleteThreatModelMetadataByKey**](ThreatModelSubResourcesApi.md#deleteThreatModelMetadataByKey) | **DELETE** /threat_models/{threat_model_id}/metadata/{key} | Delete threat model metadata by key
[**deleteThreatModelNote**](ThreatModelSubResourcesApi.md#deleteThreatModelNote) | **DELETE** /threat_models/{threat_model_id}/notes/{note_id} | Delete a note
[**deleteThreatModelRepository**](ThreatModelSubResourcesApi.md#deleteThreatModelRepository) | **DELETE** /threat_models/{threat_model_id}/repositories/{repository_id} | Delete a source reference
[**deleteThreatModelThreat**](ThreatModelSubResourcesApi.md#deleteThreatModelThreat) | **DELETE** /threat_models/{threat_model_id}/threats/{threat_id} | Delete a threat
[**getDiagramMetadata**](ThreatModelSubResourcesApi.md#getDiagramMetadata) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata | Get diagram metadata
[**getDiagramMetadataByKey**](ThreatModelSubResourcesApi.md#getDiagramMetadataByKey) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/{key} | Get diagram metadata by key
[**getDocumentMetadata**](ThreatModelSubResourcesApi.md#getDocumentMetadata) | **GET** /threat_models/{threat_model_id}/documents/{document_id}/metadata | Get document metadata
[**getDocumentMetadataByKey**](ThreatModelSubResourcesApi.md#getDocumentMetadataByKey) | **GET** /threat_models/{threat_model_id}/documents/{document_id}/metadata/{key} | Get document metadata by key
[**getNoteMetadata**](ThreatModelSubResourcesApi.md#getNoteMetadata) | **GET** /threat_models/{threat_model_id}/notes/{note_id}/metadata | Get note metadata
[**getNoteMetadataByKey**](ThreatModelSubResourcesApi.md#getNoteMetadataByKey) | **GET** /threat_models/{threat_model_id}/notes/{note_id}/metadata/{key} | Get note metadata by key
[**getRepositoryMetadata**](ThreatModelSubResourcesApi.md#getRepositoryMetadata) | **GET** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata | Get source metadata
[**getRepositoryMetadataByKey**](ThreatModelSubResourcesApi.md#getRepositoryMetadataByKey) | **GET** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/{key} | Get source metadata by key
[**getThreatMetadata**](ThreatModelSubResourcesApi.md#getThreatMetadata) | **GET** /threat_models/{threat_model_id}/threats/{threat_id}/metadata | Get threat metadata
[**getThreatMetadataByKey**](ThreatModelSubResourcesApi.md#getThreatMetadataByKey) | **GET** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/{key} | Get threat metadata by key
[**getThreatModelAsset**](ThreatModelSubResourcesApi.md#getThreatModelAsset) | **GET** /threat_models/{threat_model_id}/assets/{asset_id} | Get a specific asset
[**getThreatModelAssetMetadata**](ThreatModelSubResourcesApi.md#getThreatModelAssetMetadata) | **GET** /threat_models/{threat_model_id}/assets/{asset_id}/metadata | Get all metadata for an asset
[**getThreatModelAssetMetadataByKey**](ThreatModelSubResourcesApi.md#getThreatModelAssetMetadataByKey) | **GET** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/{key} | Get specific metadata for an asset
[**getThreatModelAssets**](ThreatModelSubResourcesApi.md#getThreatModelAssets) | **GET** /threat_models/{threat_model_id}/assets | List assets in a threat model
[**getThreatModelDiagram**](ThreatModelSubResourcesApi.md#getThreatModelDiagram) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id} | Get a specific diagram
[**getThreatModelDiagrams**](ThreatModelSubResourcesApi.md#getThreatModelDiagrams) | **GET** /threat_models/{threat_model_id}/diagrams | List threat model diagrams
[**getThreatModelDocument**](ThreatModelSubResourcesApi.md#getThreatModelDocument) | **GET** /threat_models/{threat_model_id}/documents/{document_id} | Get a specific document
[**getThreatModelDocuments**](ThreatModelSubResourcesApi.md#getThreatModelDocuments) | **GET** /threat_models/{threat_model_id}/documents | List documents in a threat model
[**getThreatModelMetadata**](ThreatModelSubResourcesApi.md#getThreatModelMetadata) | **GET** /threat_models/{threat_model_id}/metadata | Get threat model metadata
[**getThreatModelMetadataByKey**](ThreatModelSubResourcesApi.md#getThreatModelMetadataByKey) | **GET** /threat_models/{threat_model_id}/metadata/{key} | Get threat model metadata by key
[**getThreatModelNote**](ThreatModelSubResourcesApi.md#getThreatModelNote) | **GET** /threat_models/{threat_model_id}/notes/{note_id} | Get a specific note
[**getThreatModelNotes**](ThreatModelSubResourcesApi.md#getThreatModelNotes) | **GET** /threat_models/{threat_model_id}/notes | List notes in a threat model
[**getThreatModelRepositories**](ThreatModelSubResourcesApi.md#getThreatModelRepositories) | **GET** /threat_models/{threat_model_id}/repositories | List sources in a threat model
[**getThreatModelRepository**](ThreatModelSubResourcesApi.md#getThreatModelRepository) | **GET** /threat_models/{threat_model_id}/repositories/{repository_id} | Get a specific source reference
[**getThreatModelThreat**](ThreatModelSubResourcesApi.md#getThreatModelThreat) | **GET** /threat_models/{threat_model_id}/threats/{threat_id} | Get a specific threat
[**getThreatModelThreats**](ThreatModelSubResourcesApi.md#getThreatModelThreats) | **GET** /threat_models/{threat_model_id}/threats | List threats in a threat model
[**patchThreatModelDiagram**](ThreatModelSubResourcesApi.md#patchThreatModelDiagram) | **PATCH** /threat_models/{threat_model_id}/diagrams/{diagram_id} | Partially update a diagram
[**patchThreatModelThreat**](ThreatModelSubResourcesApi.md#patchThreatModelThreat) | **PATCH** /threat_models/{threat_model_id}/threats/{threat_id} | Partially update a threat
[**updateDiagramMetadataByKey**](ThreatModelSubResourcesApi.md#updateDiagramMetadataByKey) | **PUT** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/{key} | Update diagram metadata by key
[**updateDocumentMetadataByKey**](ThreatModelSubResourcesApi.md#updateDocumentMetadataByKey) | **PUT** /threat_models/{threat_model_id}/documents/{document_id}/metadata/{key} | Update document metadata by key
[**updateNoteMetadataByKey**](ThreatModelSubResourcesApi.md#updateNoteMetadataByKey) | **PUT** /threat_models/{threat_model_id}/notes/{note_id}/metadata/{key} | Update note metadata by key
[**updateRepositoryMetadataByKey**](ThreatModelSubResourcesApi.md#updateRepositoryMetadataByKey) | **PUT** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/{key} | Update source metadata by key
[**updateThreatMetadataByKey**](ThreatModelSubResourcesApi.md#updateThreatMetadataByKey) | **PUT** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/{key} | Update threat metadata by key
[**updateThreatModelAsset**](ThreatModelSubResourcesApi.md#updateThreatModelAsset) | **PUT** /threat_models/{threat_model_id}/assets/{asset_id} | Update an asset
[**updateThreatModelAssetMetadata**](ThreatModelSubResourcesApi.md#updateThreatModelAssetMetadata) | **PUT** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/{key} | Update asset metadata
[**updateThreatModelDiagram**](ThreatModelSubResourcesApi.md#updateThreatModelDiagram) | **PUT** /threat_models/{threat_model_id}/diagrams/{diagram_id} | Update a diagram
[**updateThreatModelDocument**](ThreatModelSubResourcesApi.md#updateThreatModelDocument) | **PUT** /threat_models/{threat_model_id}/documents/{document_id} | Update a document
[**updateThreatModelMetadataByKey**](ThreatModelSubResourcesApi.md#updateThreatModelMetadataByKey) | **PUT** /threat_models/{threat_model_id}/metadata/{key} | Update threat model metadata by key
[**updateThreatModelNote**](ThreatModelSubResourcesApi.md#updateThreatModelNote) | **PUT** /threat_models/{threat_model_id}/notes/{note_id} | Update a note
[**updateThreatModelRepository**](ThreatModelSubResourcesApi.md#updateThreatModelRepository) | **PUT** /threat_models/{threat_model_id}/repositories/{repository_id} | Update a source reference
[**updateThreatModelThreat**](ThreatModelSubResourcesApi.md#updateThreatModelThreat) | **PUT** /threat_models/{threat_model_id}/threats/{threat_id} | Update a threat

<a name="bulkCreateDiagramMetadata"></a>
# **bulkCreateDiagramMetadata**
> [Metadata] bulkCreateDiagramMetadata(body, threatModelId, diagramId)

Bulk create diagram metadata

Creates multiple metadata entries in a single operation for the specified diagram

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier

apiInstance.bulkCreateDiagramMetadata(body, threatModelId, diagramId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **diagramId** | [**String**](.md)| Diagram identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkCreateDocumentMetadata"></a>
# **bulkCreateDocumentMetadata**
> [Metadata] bulkCreateDocumentMetadata(body, threatModelId, documentId)

Bulk create document metadata

Creates multiple metadata entries in a single operation for the specified document

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let documentId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Document identifier

apiInstance.bulkCreateDocumentMetadata(body, threatModelId, documentId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **documentId** | [**String**](.md)| Document identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkCreateNoteMetadata"></a>
# **bulkCreateNoteMetadata**
> [Metadata] bulkCreateNoteMetadata(body, threatModelId, noteId)

Bulk create note metadata

Creates multiple metadata key-value pairs for the specified note

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let noteId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Note identifier

apiInstance.bulkCreateNoteMetadata(body, threatModelId, noteId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **noteId** | [**String**](.md)| Note identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkCreateRepositoryMetadata"></a>
# **bulkCreateRepositoryMetadata**
> [Metadata] bulkCreateRepositoryMetadata(body, threatModelId, repositoryId)

Bulk create source metadata

Creates multiple metadata entries in a single operation for the specified source reference

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let repositoryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Repository identifier

apiInstance.bulkCreateRepositoryMetadata(body, threatModelId, repositoryId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **repositoryId** | [**String**](.md)| Repository identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkCreateThreatMetadata"></a>
# **bulkCreateThreatMetadata**
> [Metadata] bulkCreateThreatMetadata(body, threatModelId, threatId)

Bulk create threat metadata

Creates multiple metadata entries in a single operation for the specified threat

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat identifier

apiInstance.bulkCreateThreatMetadata(body, threatModelId, threatId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **threatId** | [**String**](.md)| Threat identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkCreateThreatModelAssetMetadata"></a>
# **bulkCreateThreatModelAssetMetadata**
> [Metadata] bulkCreateThreatModelAssetMetadata(body, threatModelId, assetId)

Bulk create asset metadata

Creates multiple metadata key-value pairs for the specified asset

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let assetId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Asset identifier

apiInstance.bulkCreateThreatModelAssetMetadata(body, threatModelId, assetId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **assetId** | [**String**](.md)| Asset identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkCreateThreatModelAssets"></a>
# **bulkCreateThreatModelAssets**
> [Asset] bulkCreateThreatModelAssets(body, threatModelId)

Bulk create assets

Creates multiple assets within the specified threat model (maximum 50 per request)

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Asset()]; // [Asset] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.bulkCreateThreatModelAssets(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Asset]**](Asset.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**[Asset]**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkCreateThreatModelDocuments"></a>
# **bulkCreateThreatModelDocuments**
> [Document] bulkCreateThreatModelDocuments(body, threatModelId)

Bulk create documents

Creates multiple documents in a single operation for the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Document()]; // [Document] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.bulkCreateThreatModelDocuments(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Document]**](Document.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**[Document]**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkCreateThreatModelMetadata"></a>
# **bulkCreateThreatModelMetadata**
> [Metadata] bulkCreateThreatModelMetadata(body, threatModelId)

Bulk create threat model metadata

Creates multiple metadata entries in a single operation for the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.bulkCreateThreatModelMetadata(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkCreateThreatModelRepositories"></a>
# **bulkCreateThreatModelRepositories**
> [Repository] bulkCreateThreatModelRepositories(body, threatModelId)

Bulk create sources

Creates multiple source references in a single operation for the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Repository()]; // [Repository] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.bulkCreateThreatModelRepositories(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Repository]**](Repository.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**[Repository]**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkCreateThreatModelThreats"></a>
# **bulkCreateThreatModelThreats**
> [Threat] bulkCreateThreatModelThreats(body, threatModelId)

Bulk create threats

Creates multiple threats in a single operation for the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Threat()]; // [Threat] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.bulkCreateThreatModelThreats(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Threat]**](Threat.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**[Threat]**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpdateNoteMetadata"></a>
# **bulkUpdateNoteMetadata**
> [Metadata] bulkUpdateNoteMetadata(body, threatModelId, noteId)

Bulk update note metadata

Updates multiple metadata entries for the specified note in a single operation

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let noteId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Note identifier

apiInstance.bulkUpdateNoteMetadata(body, threatModelId, noteId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **noteId** | [**String**](.md)| Note identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpdateThreatModelThreats"></a>
# **bulkUpdateThreatModelThreats**
> [Threat] bulkUpdateThreatModelThreats(body, threatModelId)

Bulk update threats

Updates multiple threats in a single operation for the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Threat()]; // [Threat] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.bulkUpdateThreatModelThreats(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Threat]**](Threat.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**[Threat]**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpsertDiagramMetadata"></a>
# **bulkUpsertDiagramMetadata**
> [Metadata] bulkUpsertDiagramMetadata(body, threatModelId, diagramId)

Bulk upsert diagram metadata

Creates or updates multiple metadata key-value pairs for the specified diagram

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier

apiInstance.bulkUpsertDiagramMetadata(body, threatModelId, diagramId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **diagramId** | [**String**](.md)| Diagram identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpsertDocumentMetadata"></a>
# **bulkUpsertDocumentMetadata**
> [Metadata] bulkUpsertDocumentMetadata(body, threatModelId, documentId)

Bulk upsert document metadata

Creates or updates multiple metadata key-value pairs for the specified document

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let documentId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Document identifier

apiInstance.bulkUpsertDocumentMetadata(body, threatModelId, documentId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **documentId** | [**String**](.md)| Document identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpsertRepositoryMetadata"></a>
# **bulkUpsertRepositoryMetadata**
> [Metadata] bulkUpsertRepositoryMetadata(body, threatModelId, repositoryId)

Bulk upsert repository metadata

Creates or updates multiple metadata key-value pairs for the specified repository

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let repositoryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Repository identifier

apiInstance.bulkUpsertRepositoryMetadata(body, threatModelId, repositoryId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **repositoryId** | [**String**](.md)| Repository identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpsertThreatMetadata"></a>
# **bulkUpsertThreatMetadata**
> [Metadata] bulkUpsertThreatMetadata(body, threatModelId, threatId)

Bulk upsert threat metadata

Creates or updates multiple metadata key-value pairs for the specified threat

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat identifier

apiInstance.bulkUpsertThreatMetadata(body, threatModelId, threatId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **threatId** | [**String**](.md)| Threat identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpsertThreatModelAssetMetadata"></a>
# **bulkUpsertThreatModelAssetMetadata**
> [Metadata] bulkUpsertThreatModelAssetMetadata(body, threatModelId, assetId)

Bulk upsert asset metadata

Creates or updates multiple metadata key-value pairs for the specified asset

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let assetId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Asset identifier

apiInstance.bulkUpsertThreatModelAssetMetadata(body, threatModelId, assetId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **assetId** | [**String**](.md)| Asset identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpsertThreatModelAssets"></a>
# **bulkUpsertThreatModelAssets**
> [Asset] bulkUpsertThreatModelAssets(body, threatModelId)

Bulk upsert assets

Create or update multiple assets in a single request

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Asset()]; // [Asset] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.bulkUpsertThreatModelAssets(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Asset]**](Asset.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**[Asset]**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpsertThreatModelDocuments"></a>
# **bulkUpsertThreatModelDocuments**
> [Document] bulkUpsertThreatModelDocuments(body, threatModelId)

Bulk upsert documents

Create or update multiple documents in a single request

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Document()]; // [Document] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.bulkUpsertThreatModelDocuments(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Document]**](Document.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**[Document]**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpsertThreatModelMetadata"></a>
# **bulkUpsertThreatModelMetadata**
> [Metadata] bulkUpsertThreatModelMetadata(body, threatModelId)

Bulk upsert threat model metadata

Creates or updates multiple metadata key-value pairs for the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.bulkUpsertThreatModelMetadata(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpsertThreatModelRepositories"></a>
# **bulkUpsertThreatModelRepositories**
> [Repository] bulkUpsertThreatModelRepositories(body, threatModelId)

Bulk upsert repositories

Create or update multiple repositories in a single request

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.Repository()]; // [Repository] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.bulkUpsertThreatModelRepositories(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Repository]**](Repository.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**[Repository]**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createDiagramMetadata"></a>
# **createDiagramMetadata**
> Metadata createDiagramMetadata(body, threatModelId, diagramId)

Create diagram metadata

Creates a new metadata entry for the specified diagram

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.Metadata(); // Metadata | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier

apiInstance.createDiagramMetadata(body, threatModelId, diagramId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **diagramId** | [**String**](.md)| Diagram identifier | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createDocumentMetadata"></a>
# **createDocumentMetadata**
> Metadata createDocumentMetadata(body, threatModelId, documentId)

Create document metadata

Creates new metadata entry for the specified document

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.Metadata(); // Metadata | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let documentId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Document identifier

apiInstance.createDocumentMetadata(body, threatModelId, documentId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **documentId** | [**String**](.md)| Document identifier | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createNoteMetadata"></a>
# **createNoteMetadata**
> Metadata createNoteMetadata(body, threatModelId, noteId)

Create note metadata

Creates new metadata entry for the specified note

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.Metadata(); // Metadata | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let noteId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Note identifier

apiInstance.createNoteMetadata(body, threatModelId, noteId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **noteId** | [**String**](.md)| Note identifier | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createRepositoryMetadata"></a>
# **createRepositoryMetadata**
> Metadata createRepositoryMetadata(body, threatModelId, repositoryId)

Create source metadata

Creates new metadata entry for the specified source reference

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.Metadata(); // Metadata | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let repositoryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Repository identifier

apiInstance.createRepositoryMetadata(body, threatModelId, repositoryId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **repositoryId** | [**String**](.md)| Repository identifier | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createThreatMetadata"></a>
# **createThreatMetadata**
> Metadata createThreatMetadata(body, threatModelId, threatId)

Create threat metadata

Creates new metadata entry for the specified threat

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.Metadata(); // Metadata | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat identifier

apiInstance.createThreatMetadata(body, threatModelId, threatId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **threatId** | [**String**](.md)| Threat identifier | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createThreatModelAsset"></a>
# **createThreatModelAsset**
> Asset createThreatModelAsset(body, threatModelId)

Create a new asset

Creates a new asset within the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.AssetInput(); // AssetInput | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.createThreatModelAsset(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetInput**](AssetInput.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**Asset**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createThreatModelAssetMetadata"></a>
# **createThreatModelAssetMetadata**
> Metadata createThreatModelAssetMetadata(body, threatModelId, assetId)

Add metadata to an asset

Adds a new metadata key-value pair to the specified asset

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.Metadata(); // Metadata | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let assetId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Asset identifier

apiInstance.createThreatModelAssetMetadata(body, threatModelId, assetId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **assetId** | [**String**](.md)| Asset identifier | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createThreatModelDiagram"></a>
# **createThreatModelDiagram**
> DfdDiagram createThreatModelDiagram(body, threatModelId)

Create a new diagram

Creates a new diagram within the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.CreateDiagramRequest(); // CreateDiagramRequest | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.createThreatModelDiagram(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDiagramRequest**](CreateDiagramRequest.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**DfdDiagram**](DfdDiagram.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createThreatModelDocument"></a>
# **createThreatModelDocument**
> Document createThreatModelDocument(body, threatModelId)

Create a new document

Creates a new document within the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.DocumentInput(); // DocumentInput | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.createThreatModelDocument(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentInput**](DocumentInput.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createThreatModelMetadata"></a>
# **createThreatModelMetadata**
> Metadata createThreatModelMetadata(body, threatModelId)

Create threat model metadata

Creates new metadata entry for the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.Metadata(); // Metadata | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.createThreatModelMetadata(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createThreatModelNote"></a>
# **createThreatModelNote**
> Note createThreatModelNote(body, threatModelId)

Create a new note

Creates a new note within the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.NoteInput(); // NoteInput | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.createThreatModelNote(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NoteInput**](NoteInput.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**Note**](Note.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createThreatModelRepository"></a>
# **createThreatModelRepository**
> Repository createThreatModelRepository(body, threatModelId)

Create a new source reference

Creates a new source code reference within the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.RepositoryInput(); // RepositoryInput | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.createThreatModelRepository(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepositoryInput**](RepositoryInput.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**Repository**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createThreatModelThreat"></a>
# **createThreatModelThreat**
> Threat createThreatModelThreat(body, threatModelId)

Create a new threat

Creates a new threat within the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.ThreatInput(); // ThreatInput | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.createThreatModelThreat(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThreatInput**](ThreatInput.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**Threat**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteDiagramMetadataByKey"></a>
# **deleteDiagramMetadataByKey**
> deleteDiagramMetadataByKey(threatModelId, diagramId, key)

Delete diagram metadata by key

Removes a specific metadata entry for the diagram by key

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier
let key = "key_example"; // String | Metadata key

apiInstance.deleteDiagramMetadataByKey(threatModelId, diagramId, key).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **diagramId** | [**String**](.md)| Diagram identifier | 
 **key** | **String**| Metadata key | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteDocumentMetadataByKey"></a>
# **deleteDocumentMetadataByKey**
> deleteDocumentMetadataByKey(threatModelId, documentId, key)

Delete document metadata by key

Deletes a specific metadata entry by key for the specified document

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let documentId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Document identifier
let key = "key_example"; // String | Metadata key

apiInstance.deleteDocumentMetadataByKey(threatModelId, documentId, key).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **documentId** | [**String**](.md)| Document identifier | 
 **key** | **String**| Metadata key | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteNoteMetadataByKey"></a>
# **deleteNoteMetadataByKey**
> deleteNoteMetadataByKey(threatModelId, noteId, key)

Delete note metadata by key

Deletes a specific metadata entry by key for the specified note

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let noteId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Note identifier
let key = "key_example"; // String | Metadata key

apiInstance.deleteNoteMetadataByKey(threatModelId, noteId, key).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **noteId** | [**String**](.md)| Note identifier | 
 **key** | **String**| Metadata key | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteRepositoryMetadataByKey"></a>
# **deleteRepositoryMetadataByKey**
> deleteRepositoryMetadataByKey(threatModelId, repositoryId, key)

Delete source metadata by key

Deletes a specific metadata entry by key for the specified source reference

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let repositoryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Repository identifier
let key = "key_example"; // String | Metadata key

apiInstance.deleteRepositoryMetadataByKey(threatModelId, repositoryId, key).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **repositoryId** | [**String**](.md)| Repository identifier | 
 **key** | **String**| Metadata key | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteThreatMetadataByKey"></a>
# **deleteThreatMetadataByKey**
> deleteThreatMetadataByKey(threatModelId, threatId, key)

Delete threat metadata by key

Deletes a specific metadata entry by key for the specified threat

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat identifier
let key = "key_example"; // String | Metadata key

apiInstance.deleteThreatMetadataByKey(threatModelId, threatId, key).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **threatId** | [**String**](.md)| Threat identifier | 
 **key** | **String**| Metadata key | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteThreatModelAsset"></a>
# **deleteThreatModelAsset**
> deleteThreatModelAsset(threatModelId, assetId)

Delete an asset

Deletes an asset from the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let assetId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Asset identifier

apiInstance.deleteThreatModelAsset(threatModelId, assetId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **assetId** | [**String**](.md)| Asset identifier | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteThreatModelAssetMetadata"></a>
# **deleteThreatModelAssetMetadata**
> deleteThreatModelAssetMetadata(threatModelId, assetId, key)

Delete asset metadata

Deletes a metadata key-value pair from the specified asset

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let assetId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Asset identifier
let key = "key_example"; // String | Metadata key

apiInstance.deleteThreatModelAssetMetadata(threatModelId, assetId, key).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **assetId** | [**String**](.md)| Asset identifier | 
 **key** | **String**| Metadata key | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteThreatModelDiagram"></a>
# **deleteThreatModelDiagram**
> deleteThreatModelDiagram(threatModelId, diagramId)

Delete a diagram

Permanently removes a diagram from the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier

apiInstance.deleteThreatModelDiagram(threatModelId, diagramId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **diagramId** | [**String**](.md)| Diagram identifier | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteThreatModelDocument"></a>
# **deleteThreatModelDocument**
> deleteThreatModelDocument(threatModelId, documentId)

Delete a document

Deletes a specific document from the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let documentId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Document identifier

apiInstance.deleteThreatModelDocument(threatModelId, documentId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **documentId** | [**String**](.md)| Document identifier | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteThreatModelMetadataByKey"></a>
# **deleteThreatModelMetadataByKey**
> deleteThreatModelMetadataByKey(threatModelId, key)

Delete threat model metadata by key

Deletes a specific metadata entry by key for the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let key = "key_example"; // String | Metadata key

apiInstance.deleteThreatModelMetadataByKey(threatModelId, key).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **key** | **String**| Metadata key | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteThreatModelNote"></a>
# **deleteThreatModelNote**
> deleteThreatModelNote(threatModelId, noteId)

Delete a note

Deletes a specific note from the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let noteId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Note identifier

apiInstance.deleteThreatModelNote(threatModelId, noteId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **noteId** | [**String**](.md)| Note identifier | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteThreatModelRepository"></a>
# **deleteThreatModelRepository**
> deleteThreatModelRepository(threatModelId, repositoryId)

Delete a source reference

Deletes a specific source code reference from the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let repositoryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Repository identifier

apiInstance.deleteThreatModelRepository(threatModelId, repositoryId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **repositoryId** | [**String**](.md)| Repository identifier | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteThreatModelThreat"></a>
# **deleteThreatModelThreat**
> deleteThreatModelThreat(threatModelId, threatId)

Delete a threat

Deletes a specific threat from the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat identifier

apiInstance.deleteThreatModelThreat(threatModelId, threatId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **threatId** | [**String**](.md)| Threat identifier | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getDiagramMetadata"></a>
# **getDiagramMetadata**
> [Metadata] getDiagramMetadata(threatModelId, diagramId)

Get diagram metadata

Retrieves all metadata entries for the specified diagram

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier

apiInstance.getDiagramMetadata(threatModelId, diagramId).then((data) => {
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

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getDiagramMetadataByKey"></a>
# **getDiagramMetadataByKey**
> Metadata getDiagramMetadataByKey(threatModelId, diagramId, key)

Get diagram metadata by key

Retrieves a specific metadata entry for the diagram by key

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier
let key = "key_example"; // String | Metadata key

apiInstance.getDiagramMetadataByKey(threatModelId, diagramId, key).then((data) => {
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
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getDocumentMetadata"></a>
# **getDocumentMetadata**
> [Metadata] getDocumentMetadata(threatModelId, documentId)

Get document metadata

Returns all metadata key-value pairs for the specified document

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let documentId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Document identifier

apiInstance.getDocumentMetadata(threatModelId, documentId).then((data) => {
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

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getDocumentMetadataByKey"></a>
# **getDocumentMetadataByKey**
> Metadata getDocumentMetadataByKey(threatModelId, documentId, key)

Get document metadata by key

Returns a specific metadata entry by key for the specified document

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let documentId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Document identifier
let key = "key_example"; // String | Metadata key

apiInstance.getDocumentMetadataByKey(threatModelId, documentId, key).then((data) => {
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
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getNoteMetadata"></a>
# **getNoteMetadata**
> [Metadata] getNoteMetadata(threatModelId, noteId)

Get note metadata

Returns all metadata key-value pairs for the specified note

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let noteId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Note identifier

apiInstance.getNoteMetadata(threatModelId, noteId).then((data) => {
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

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getNoteMetadataByKey"></a>
# **getNoteMetadataByKey**
> Metadata getNoteMetadataByKey(threatModelId, noteId, key)

Get note metadata by key

Returns a specific metadata entry by key for the specified note

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let noteId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Note identifier
let key = "key_example"; // String | Metadata key

apiInstance.getNoteMetadataByKey(threatModelId, noteId, key).then((data) => {
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
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getRepositoryMetadata"></a>
# **getRepositoryMetadata**
> [Metadata] getRepositoryMetadata(threatModelId, repositoryId)

Get source metadata

Returns all metadata key-value pairs for the specified source reference

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let repositoryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Repository identifier

apiInstance.getRepositoryMetadata(threatModelId, repositoryId).then((data) => {
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

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getRepositoryMetadataByKey"></a>
# **getRepositoryMetadataByKey**
> Metadata getRepositoryMetadataByKey(threatModelId, repositoryId, key)

Get source metadata by key

Returns a specific metadata entry by key for the specified source reference

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let repositoryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Repository identifier
let key = "key_example"; // String | Metadata key

apiInstance.getRepositoryMetadataByKey(threatModelId, repositoryId, key).then((data) => {
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
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatMetadata"></a>
# **getThreatMetadata**
> [Metadata] getThreatMetadata(threatModelId, threatId)

Get threat metadata

Returns all metadata key-value pairs for the specified threat

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat identifier

apiInstance.getThreatMetadata(threatModelId, threatId).then((data) => {
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

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatMetadataByKey"></a>
# **getThreatMetadataByKey**
> Metadata getThreatMetadataByKey(threatModelId, threatId, key)

Get threat metadata by key

Returns a specific metadata entry by key for the specified threat

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat identifier
let key = "key_example"; // String | Metadata key

apiInstance.getThreatMetadataByKey(threatModelId, threatId, key).then((data) => {
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
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelAsset"></a>
# **getThreatModelAsset**
> Asset getThreatModelAsset(threatModelId, assetId)

Get a specific asset

Returns a single asset by its ID

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let assetId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Asset identifier

apiInstance.getThreatModelAsset(threatModelId, assetId).then((data) => {
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

### Return type

[**Asset**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelAssetMetadata"></a>
# **getThreatModelAssetMetadata**
> [Metadata] getThreatModelAssetMetadata(threatModelId, assetId)

Get all metadata for an asset

Returns all metadata key-value pairs for the specified asset

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let assetId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Asset identifier

apiInstance.getThreatModelAssetMetadata(threatModelId, assetId).then((data) => {
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

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelAssetMetadataByKey"></a>
# **getThreatModelAssetMetadataByKey**
> Metadata getThreatModelAssetMetadataByKey(threatModelId, assetId, key)

Get specific metadata for an asset

Returns a single metadata value by its key

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let assetId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Asset identifier
let key = "key_example"; // String | Metadata key

apiInstance.getThreatModelAssetMetadataByKey(threatModelId, assetId, key).then((data) => {
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
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelAssets"></a>
# **getThreatModelAssets**
> [Asset] getThreatModelAssets(threatModelId, opts)

List assets in a threat model

Returns a paginated list of assets within the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.getThreatModelAssets(threatModelId, opts).then((data) => {
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

### Return type

[**[Asset]**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelDiagram"></a>
# **getThreatModelDiagram**
> DfdDiagram getThreatModelDiagram(threatModelId, diagramId)

Get a specific diagram

Retrieves a specific diagram from the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier

apiInstance.getThreatModelDiagram(threatModelId, diagramId).then((data) => {
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

### Return type

[**DfdDiagram**](DfdDiagram.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelDiagrams"></a>
# **getThreatModelDiagrams**
> [DiagramListItem] getThreatModelDiagrams(threatModelId, opts)

List threat model diagrams

Returns all diagrams associated with a specific threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.getThreatModelDiagrams(threatModelId, opts).then((data) => {
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

### Return type

[**[DiagramListItem]**](DiagramListItem.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelDocument"></a>
# **getThreatModelDocument**
> Document getThreatModelDocument(threatModelId, documentId)

Get a specific document

Returns details of a specific document within the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let documentId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Document identifier

apiInstance.getThreatModelDocument(threatModelId, documentId).then((data) => {
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

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelDocuments"></a>
# **getThreatModelDocuments**
> [Document] getThreatModelDocuments(threatModelId, opts)

List documents in a threat model

Returns a paginated list of documents within the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.getThreatModelDocuments(threatModelId, opts).then((data) => {
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

### Return type

[**[Document]**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelMetadata"></a>
# **getThreatModelMetadata**
> [Metadata] getThreatModelMetadata(threatModelId)

Get threat model metadata

Returns all metadata key-value pairs for the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.getThreatModelMetadata(threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelMetadataByKey"></a>
# **getThreatModelMetadataByKey**
> Metadata getThreatModelMetadataByKey(threatModelId, key)

Get threat model metadata by key

Returns a specific metadata entry by key for the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let key = "key_example"; // String | Metadata key

apiInstance.getThreatModelMetadataByKey(threatModelId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelNote"></a>
# **getThreatModelNote**
> Note getThreatModelNote(threatModelId, noteId)

Get a specific note

Returns details of a specific note within the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let noteId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Note identifier

apiInstance.getThreatModelNote(threatModelId, noteId).then((data) => {
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

### Return type

[**Note**](Note.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelNotes"></a>
# **getThreatModelNotes**
> [NoteListItem] getThreatModelNotes(threatModelId, opts)

List notes in a threat model

Returns a paginated list of notes within the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.getThreatModelNotes(threatModelId, opts).then((data) => {
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

### Return type

[**[NoteListItem]**](NoteListItem.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelRepositories"></a>
# **getThreatModelRepositories**
> [Repository] getThreatModelRepositories(threatModelId, opts)

List sources in a threat model

Returns a paginated list of source code references within the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.getThreatModelRepositories(threatModelId, opts).then((data) => {
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

### Return type

[**[Repository]**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelRepository"></a>
# **getThreatModelRepository**
> Repository getThreatModelRepository(threatModelId, repositoryId)

Get a specific source reference

Returns details of a specific source code reference within the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let repositoryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Repository identifier

apiInstance.getThreatModelRepository(threatModelId, repositoryId).then((data) => {
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

### Return type

[**Repository**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelThreat"></a>
# **getThreatModelThreat**
> Threat getThreatModelThreat(threatModelId, threatId)

Get a specific threat

Returns details of a specific threat within the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat identifier

apiInstance.getThreatModelThreat(threatModelId, threatId).then((data) => {
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

### Return type

[**Threat**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModelThreats"></a>
# **getThreatModelThreats**
> [Threat] getThreatModelThreats(threatModelId, opts)

List threats in a threat model

Returns a paginated list of threats within the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0, // Number | Number of results to skip
  'sort': "created_at:desc", // String | Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc)
  'name': "name_example", // String | Filter by threat name (partial match)
  'description': "description_example", // String | Filter by threat description (partial match)
  'threatType': ["threatType_example"], // [String] | Filter by threat types (AND logic). Threat must contain ALL specified types. Example: ?threat_type=Tampering&threat_type=Spoofing
  'severity': "severity_example", // String | Filter by severity level (exact match)
  'priority': "priority_example", // String | Filter by priority (exact match)
  'status': "status_example", // String | Filter by status (exact match)
  'diagramId': "38400000-8cf0-11bd-b23e-10b96e4ef00d", // String | Filter by diagram ID (exact match)
  'cellId': "38400000-8cf0-11bd-b23e-10b96e4ef00d", // String | Filter by cell ID (exact match)
  'scoreGt': 1.2, // Number | Filter threats with score greater than this value
  'scoreLt': 1.2, // Number | Filter threats with score less than this value
  'scoreEq': 1.2, // Number | Filter threats with score equal to this value
  'scoreGe': 1.2, // Number | Filter threats with score greater than or equal to this value
  'scoreLe': 1.2, // Number | Filter threats with score less than or equal to this value
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results created after this timestamp (ISO 8601)
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results created before this timestamp (ISO 8601)
  'modifiedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results modified after this timestamp (ISO 8601)
  'modifiedBefore': new Date("2013-10-20T19:20:30+01:00") // Date | Filter results modified before this timestamp (ISO 8601)
};
apiInstance.getThreatModelThreats(threatModelId, opts).then((data) => {
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
 **sort** | **String**| Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) | [optional] [default to created_at:desc]
 **name** | **String**| Filter by threat name (partial match) | [optional] 
 **description** | **String**| Filter by threat description (partial match) | [optional] 
 **threatType** | [**[String]**](String.md)| Filter by threat types (AND logic). Threat must contain ALL specified types. Example: ?threat_type&#x3D;Tampering&amp;threat_type&#x3D;Spoofing | [optional] 
 **severity** | **String**| Filter by severity level (exact match) | [optional] 
 **priority** | **String**| Filter by priority (exact match) | [optional] 
 **status** | **String**| Filter by status (exact match) | [optional] 
 **diagramId** | [**String**](.md)| Filter by diagram ID (exact match) | [optional] 
 **cellId** | [**String**](.md)| Filter by cell ID (exact match) | [optional] 
 **scoreGt** | **Number**| Filter threats with score greater than this value | [optional] 
 **scoreLt** | **Number**| Filter threats with score less than this value | [optional] 
 **scoreEq** | **Number**| Filter threats with score equal to this value | [optional] 
 **scoreGe** | **Number**| Filter threats with score greater than or equal to this value | [optional] 
 **scoreLe** | **Number**| Filter threats with score less than or equal to this value | [optional] 
 **createdAfter** | **Date**| Filter results created after this timestamp (ISO 8601) | [optional] 
 **createdBefore** | **Date**| Filter results created before this timestamp (ISO 8601) | [optional] 
 **modifiedAfter** | **Date**| Filter results modified after this timestamp (ISO 8601) | [optional] 
 **modifiedBefore** | **Date**| Filter results modified before this timestamp (ISO 8601) | [optional] 

### Return type

[**[Threat]**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="patchThreatModelDiagram"></a>
# **patchThreatModelDiagram**
> DfdDiagram patchThreatModelDiagram(body, threatModelId, diagramId)

Partially update a diagram

Apply JSON Patch operations to update specific parts of a diagram

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.ThreatsThreatIdBody()]; // [ThreatsThreatIdBody] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier

apiInstance.patchThreatModelDiagram(body, threatModelId, diagramId).then((data) => {
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
 **diagramId** | [**String**](.md)| Diagram identifier | 

### Return type

[**DfdDiagram**](DfdDiagram.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

<a name="patchThreatModelThreat"></a>
# **patchThreatModelThreat**
> Threat patchThreatModelThreat(body, threatModelId, threatId)

Partially update a threat

Applies JSON patch operations to a specific threat within the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = [new TmiJsClient.ThreatsThreatIdBody()]; // [ThreatsThreatIdBody] | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat identifier

apiInstance.patchThreatModelThreat(body, threatModelId, threatId).then((data) => {
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
 **threatId** | [**String**](.md)| Threat identifier | 

### Return type

[**Threat**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

<a name="updateDiagramMetadataByKey"></a>
# **updateDiagramMetadataByKey**
> Metadata updateDiagramMetadataByKey(body, threatModelId, diagramId, key)

Update diagram metadata by key

Updates or creates a metadata entry for the diagram with the specified key

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.MetadataKeyBody4(); // MetadataKeyBody4 | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier
let key = "key_example"; // String | Metadata key

apiInstance.updateDiagramMetadataByKey(body, threatModelId, diagramId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataKeyBody4**](MetadataKeyBody4.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **diagramId** | [**String**](.md)| Diagram identifier | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateDocumentMetadataByKey"></a>
# **updateDocumentMetadataByKey**
> Metadata updateDocumentMetadataByKey(body, threatModelId, documentId, key)

Update document metadata by key

Updates a specific metadata entry by key for the specified document

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.MetadataKeyBody1(); // MetadataKeyBody1 | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let documentId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Document identifier
let key = "key_example"; // String | Metadata key

apiInstance.updateDocumentMetadataByKey(body, threatModelId, documentId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataKeyBody1**](MetadataKeyBody1.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **documentId** | [**String**](.md)| Document identifier | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateNoteMetadataByKey"></a>
# **updateNoteMetadataByKey**
> Metadata updateNoteMetadataByKey(body, threatModelId, noteId, key)

Update note metadata by key

Updates a specific metadata entry by key for the specified note

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.MetadataKeyBody5(); // MetadataKeyBody5 | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let noteId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Note identifier
let key = "key_example"; // String | Metadata key

apiInstance.updateNoteMetadataByKey(body, threatModelId, noteId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataKeyBody5**](MetadataKeyBody5.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **noteId** | [**String**](.md)| Note identifier | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateRepositoryMetadataByKey"></a>
# **updateRepositoryMetadataByKey**
> Metadata updateRepositoryMetadataByKey(body, threatModelId, repositoryId, key)

Update source metadata by key

Updates a specific metadata entry by key for the specified source reference

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.MetadataKeyBody2(); // MetadataKeyBody2 | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let repositoryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Repository identifier
let key = "key_example"; // String | Metadata key

apiInstance.updateRepositoryMetadataByKey(body, threatModelId, repositoryId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataKeyBody2**](MetadataKeyBody2.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **repositoryId** | [**String**](.md)| Repository identifier | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateThreatMetadataByKey"></a>
# **updateThreatMetadataByKey**
> Metadata updateThreatMetadataByKey(body, threatModelId, threatId, key)

Update threat metadata by key

Updates a specific metadata entry by key for the specified threat

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.MetadataKeyBody(); // MetadataKeyBody | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat identifier
let key = "key_example"; // String | Metadata key

apiInstance.updateThreatMetadataByKey(body, threatModelId, threatId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataKeyBody**](MetadataKeyBody.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **threatId** | [**String**](.md)| Threat identifier | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateThreatModelAsset"></a>
# **updateThreatModelAsset**
> Asset updateThreatModelAsset(body, threatModelId, assetId)

Update an asset

Updates an existing asset within the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.AssetInput(); // AssetInput | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let assetId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Asset identifier

apiInstance.updateThreatModelAsset(body, threatModelId, assetId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetInput**](AssetInput.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **assetId** | [**String**](.md)| Asset identifier | 

### Return type

[**Asset**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateThreatModelAssetMetadata"></a>
# **updateThreatModelAssetMetadata**
> Metadata updateThreatModelAssetMetadata(body, threatModelId, assetId, key)

Update asset metadata

Updates an existing metadata value by its key

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.Metadata(); // Metadata | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let assetId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Asset identifier
let key = "key_example"; // String | Metadata key

apiInstance.updateThreatModelAssetMetadata(body, threatModelId, assetId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **assetId** | [**String**](.md)| Asset identifier | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateThreatModelDiagram"></a>
# **updateThreatModelDiagram**
> DfdDiagram updateThreatModelDiagram(body, threatModelId, diagramId)

Update a diagram

Completely replaces a diagram with new data. Use DfdDiagramInput schema which excludes readOnly fields (id, created_at, modified_at, update_vector).

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.DfdDiagramInput(); // DfdDiagramInput | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let diagramId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Diagram identifier

apiInstance.updateThreatModelDiagram(body, threatModelId, diagramId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfdDiagramInput**](DfdDiagramInput.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **diagramId** | [**String**](.md)| Diagram identifier | 

### Return type

[**DfdDiagram**](DfdDiagram.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateThreatModelDocument"></a>
# **updateThreatModelDocument**
> Document updateThreatModelDocument(body, threatModelId, documentId)

Update a document

Updates a specific document within the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.DocumentInput(); // DocumentInput | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let documentId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Document identifier

apiInstance.updateThreatModelDocument(body, threatModelId, documentId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentInput**](DocumentInput.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **documentId** | [**String**](.md)| Document identifier | 

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateThreatModelMetadataByKey"></a>
# **updateThreatModelMetadataByKey**
> Metadata updateThreatModelMetadataByKey(body, threatModelId, key)

Update threat model metadata by key

Updates a specific metadata entry by key for the specified threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.MetadataKeyBody3(); // MetadataKeyBody3 | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let key = "key_example"; // String | Metadata key

apiInstance.updateThreatModelMetadataByKey(body, threatModelId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataKeyBody3**](MetadataKeyBody3.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateThreatModelNote"></a>
# **updateThreatModelNote**
> Note updateThreatModelNote(body, threatModelId, noteId)

Update a note

Updates a specific note within the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.NoteInput(); // NoteInput | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let noteId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Note identifier

apiInstance.updateThreatModelNote(body, threatModelId, noteId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NoteInput**](NoteInput.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **noteId** | [**String**](.md)| Note identifier | 

### Return type

[**Note**](Note.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateThreatModelRepository"></a>
# **updateThreatModelRepository**
> Repository updateThreatModelRepository(body, threatModelId, repositoryId)

Update a source reference

Updates a specific source code reference within the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.RepositoryInput(); // RepositoryInput | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let repositoryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Repository identifier

apiInstance.updateThreatModelRepository(body, threatModelId, repositoryId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepositoryInput**](RepositoryInput.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **repositoryId** | [**String**](.md)| Repository identifier | 

### Return type

[**Repository**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateThreatModelThreat"></a>
# **updateThreatModelThreat**
> Threat updateThreatModelThreat(body, threatModelId, threatId)

Update a threat

Updates a specific threat within the threat model

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelSubResourcesApi();
let body = new TmiJsClient.ThreatInput(); // ThreatInput | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let threatId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat identifier

apiInstance.updateThreatModelThreat(body, threatModelId, threatId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThreatInput**](ThreatInput.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **threatId** | [**String**](.md)| Threat identifier | 

### Return type

[**Threat**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

