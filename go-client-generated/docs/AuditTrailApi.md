# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetAssetAuditTrail**](AuditTrailApi.md#GetAssetAuditTrail) | **Get** /threat_models/{threat_model_id}/assets/{asset_id}/audit_trail | List audit trail for an asset
[**GetAuditEntry**](AuditTrailApi.md#GetAuditEntry) | **Get** /threat_models/{threat_model_id}/audit_trail/{entry_id} | Get a single audit trail entry
[**GetDiagramAuditTrail**](AuditTrailApi.md#GetDiagramAuditTrail) | **Get** /threat_models/{threat_model_id}/diagrams/{diagram_id}/audit_trail | List audit trail for a diagram
[**GetDocumentAuditTrail**](AuditTrailApi.md#GetDocumentAuditTrail) | **Get** /threat_models/{threat_model_id}/documents/{document_id}/audit_trail | List audit trail for a document
[**GetNoteAuditTrail**](AuditTrailApi.md#GetNoteAuditTrail) | **Get** /threat_models/{threat_model_id}/notes/{note_id}/audit_trail | List audit trail for a note
[**GetRepositoryAuditTrail**](AuditTrailApi.md#GetRepositoryAuditTrail) | **Get** /threat_models/{threat_model_id}/repositories/{repository_id}/audit_trail | List audit trail for a repository
[**GetThreatAuditTrail**](AuditTrailApi.md#GetThreatAuditTrail) | **Get** /threat_models/{threat_model_id}/threats/{threat_id}/audit_trail | List audit trail for a threat
[**GetThreatModelAuditTrail**](AuditTrailApi.md#GetThreatModelAuditTrail) | **Get** /threat_models/{threat_model_id}/audit_trail | List audit trail for a threat model and all sub-objects
[**RollbackToVersion**](AuditTrailApi.md#RollbackToVersion) | **Post** /threat_models/{threat_model_id}/audit_trail/{entry_id}/rollback | Rollback an entity to a previous version

# **GetAssetAuditTrail**
> ListAuditTrailResponse GetAssetAuditTrail(ctx, threatModelId, assetId, optional)
List audit trail for an asset

Returns a paginated list of audit trail entries for a specific resource

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **threatModelId** | [**string**](.md)| Threat model identifier | 
  **assetId** | [**string**](.md)| Asset identifier | 
 **optional** | ***AuditTrailApiGetAssetAuditTrailOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuditTrailApiGetAssetAuditTrailOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAuditEntry**
> AuditEntry GetAuditEntry(ctx, threatModelId, entryId)
Get a single audit trail entry

Returns a single audit trail entry by ID

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **threatModelId** | [**string**](.md)| Threat model identifier | 
  **entryId** | [**string**](.md)| Unique identifier of the audit entry | 

### Return type

[**AuditEntry**](AuditEntry.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetDiagramAuditTrail**
> ListAuditTrailResponse GetDiagramAuditTrail(ctx, threatModelId, diagramId, optional)
List audit trail for a diagram

Returns a paginated list of audit trail entries for a specific resource

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **threatModelId** | [**string**](.md)| Threat model identifier | 
  **diagramId** | [**string**](.md)| Diagram identifier | 
 **optional** | ***AuditTrailApiGetDiagramAuditTrailOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuditTrailApiGetDiagramAuditTrailOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetDocumentAuditTrail**
> ListAuditTrailResponse GetDocumentAuditTrail(ctx, threatModelId, documentId, optional)
List audit trail for a document

Returns a paginated list of audit trail entries for a specific resource

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **threatModelId** | [**string**](.md)| Threat model identifier | 
  **documentId** | [**string**](.md)| Document identifier | 
 **optional** | ***AuditTrailApiGetDocumentAuditTrailOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuditTrailApiGetDocumentAuditTrailOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetNoteAuditTrail**
> ListAuditTrailResponse GetNoteAuditTrail(ctx, threatModelId, noteId, optional)
List audit trail for a note

Returns a paginated list of audit trail entries for a specific resource

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **threatModelId** | [**string**](.md)| Threat model identifier | 
  **noteId** | [**string**](.md)| Note identifier | 
 **optional** | ***AuditTrailApiGetNoteAuditTrailOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuditTrailApiGetNoteAuditTrailOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetRepositoryAuditTrail**
> ListAuditTrailResponse GetRepositoryAuditTrail(ctx, threatModelId, repositoryId, optional)
List audit trail for a repository

Returns a paginated list of audit trail entries for a specific resource

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **threatModelId** | [**string**](.md)| Threat model identifier | 
  **repositoryId** | [**string**](.md)| Repository identifier | 
 **optional** | ***AuditTrailApiGetRepositoryAuditTrailOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuditTrailApiGetRepositoryAuditTrailOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetThreatAuditTrail**
> ListAuditTrailResponse GetThreatAuditTrail(ctx, threatModelId, threatId, optional)
List audit trail for a threat

Returns a paginated list of audit trail entries for a specific resource

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **threatModelId** | [**string**](.md)| Threat model identifier | 
  **threatId** | [**string**](.md)| Threat identifier | 
 **optional** | ***AuditTrailApiGetThreatAuditTrailOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuditTrailApiGetThreatAuditTrailOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetThreatModelAuditTrail**
> ListAuditTrailResponse GetThreatModelAuditTrail(ctx, threatModelId, optional)
List audit trail for a threat model and all sub-objects

Returns a paginated list of audit trail entries

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **threatModelId** | [**string**](.md)| Threat model identifier | 
 **optional** | ***AuditTrailApiGetThreatModelAuditTrailOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AuditTrailApiGetThreatModelAuditTrailOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]
 **objectType** | **optional.String**| Filter by object type | 
 **changeType** | **optional.String**| Filter by change type | 
 **actorEmail** | **optional.String**| Filter by actor email | 
 **after** | **optional.Time**| Filter entries after this timestamp (ISO 8601) | 
 **before** | **optional.Time**| Filter entries before this timestamp (ISO 8601) | 

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **RollbackToVersion**
> RollbackResponse RollbackToVersion(ctx, threatModelId, entryId)
Rollback an entity to a previous version

Restores an entity to the state captured in the specified audit entry's version snapshot. Creates a new audit entry recording the rollback. Returns 410 Gone if the version snapshot has been pruned.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **threatModelId** | [**string**](.md)| Threat model identifier | 
  **entryId** | [**string**](.md)| Unique identifier of the audit entry | 

### Return type

[**RollbackResponse**](RollbackResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

