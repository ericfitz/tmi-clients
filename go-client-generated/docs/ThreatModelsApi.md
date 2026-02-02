# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateThreatModel**](ThreatModelsApi.md#CreateThreatModel) | **Post** /threat_models | Create a threat model
[**DeleteThreatModel**](ThreatModelsApi.md#DeleteThreatModel) | **Delete** /threat_models/{threat_model_id} | Delete a threat model
[**GetThreatModel**](ThreatModelsApi.md#GetThreatModel) | **Get** /threat_models/{threat_model_id} | Retrieve a threat model
[**ListThreatModels**](ThreatModelsApi.md#ListThreatModels) | **Get** /threat_models | List threat models
[**PatchThreatModel**](ThreatModelsApi.md#PatchThreatModel) | **Patch** /threat_models/{threat_model_id} | Partially update a threat model
[**UpdateThreatModel**](ThreatModelsApi.md#UpdateThreatModel) | **Put** /threat_models/{threat_model_id} | Update a threat model

# **CreateThreatModel**
> ThreatModel CreateThreatModel(ctx, body)
Create a threat model

Creates a new threat model with the authenticated user as owner

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**ThreatModelInput**](ThreatModelInput.md)| Threat Model creation data | 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteThreatModel**
> DeleteThreatModel(ctx, threatModelId)
Delete a threat model

Deletes a threat model; restricted to owner role

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **threatModelId** | [**string**](.md)| Threat model identifier | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetThreatModel**
> ThreatModel GetThreatModel(ctx, threatModelId)
Retrieve a threat model

Retrieves the full details of a specific threat model if the user has access

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **threatModelId** | [**string**](.md)| Threat model identifier | 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListThreatModels**
> ListThreatModelsResponse ListThreatModels(ctx, optional)
List threat models

Returns a list of threat models accessible to the authenticated user with enhanced metadata and entity counts

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***ThreatModelsApiListThreatModelsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ThreatModelsApiListThreatModelsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]
 **owner** | **optional.String**| Filter by owner name or email | 
 **name** | **optional.String**| Filter by threat model name (partial match) | 
 **description** | **optional.String**| Filter by threat model description (partial match) | 
 **issueUri** | **optional.String**| Filter by issue URI (partial match) | 
 **createdAfter** | **optional.Time**| Filter results created after this timestamp (ISO 8601) | 
 **createdBefore** | **optional.Time**| Filter results created before this timestamp (ISO 8601) | 
 **modifiedAfter** | **optional.Time**| Filter results modified after this timestamp (ISO 8601) | 
 **modifiedBefore** | **optional.Time**| Filter results modified before this timestamp (ISO 8601) | 
 **status** | **optional.String**| Filter by status value (exact match). To filter by multiple statuses, use multiple status parameters or comma-separated values. | 
 **statusUpdatedAfter** | **optional.Time**| Filter threat models where status was updated after this timestamp (RFC3339) | 
 **statusUpdatedBefore** | **optional.Time**| Filter threat models where status was updated before this timestamp (RFC3339) | 

### Return type

[**ListThreatModelsResponse**](ListThreatModelsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PatchThreatModel**
> ThreatModel PatchThreatModel(ctx, threatModelId, optional)
Partially update a threat model

Applies JSON Patch operations to a threat model; restricted to writer/owner roles

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **threatModelId** | [**string**](.md)| Threat model identifier | 
 **optional** | ***ThreatModelsApiPatchThreatModelOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ThreatModelsApiPatchThreatModelOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **body** | [**optional.Interface of []JsonPatchDocumentInner**](JsonPatchDocument_inner.md)| JSON Patch operations to apply to the threat model | 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateThreatModel**
> ThreatModel UpdateThreatModel(ctx, body, threatModelId)
Update a threat model

Fully updates a threat model; restricted to writer/owner roles

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**ThreatModelInput**](ThreatModelInput.md)| Complete threat model data for replacement | 
  **threatModelId** | [**string**](.md)| Threat model identifier | 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

