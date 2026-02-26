# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BulkCreateAdminSurveyMetadata**](SurveyAdministrationApi.md#BulkCreateAdminSurveyMetadata) | **Post** /admin/surveys/{survey_id}/metadata/bulk | Bulk create metadata for a survey
[**BulkReplaceAdminSurveyMetadata**](SurveyAdministrationApi.md#BulkReplaceAdminSurveyMetadata) | **Put** /admin/surveys/{survey_id}/metadata/bulk | Bulk replace metadata for a survey
[**BulkUpsertAdminSurveyMetadata**](SurveyAdministrationApi.md#BulkUpsertAdminSurveyMetadata) | **Patch** /admin/surveys/{survey_id}/metadata/bulk | Bulk upsert metadata for a survey
[**CreateAdminSurvey**](SurveyAdministrationApi.md#CreateAdminSurvey) | **Post** /admin/surveys | Create a survey
[**CreateAdminSurveyMetadata**](SurveyAdministrationApi.md#CreateAdminSurveyMetadata) | **Post** /admin/surveys/{survey_id}/metadata | Add metadata to a survey
[**DeleteAdminSurvey**](SurveyAdministrationApi.md#DeleteAdminSurvey) | **Delete** /admin/surveys/{survey_id} | Delete a survey
[**DeleteAdminSurveyMetadataByKey**](SurveyAdministrationApi.md#DeleteAdminSurveyMetadataByKey) | **Delete** /admin/surveys/{survey_id}/metadata/{key} | Delete metadata by key for a survey
[**GetAdminSurvey**](SurveyAdministrationApi.md#GetAdminSurvey) | **Get** /admin/surveys/{survey_id} | Get a survey
[**GetAdminSurveyMetadata**](SurveyAdministrationApi.md#GetAdminSurveyMetadata) | **Get** /admin/surveys/{survey_id}/metadata | Get all metadata for a survey
[**GetAdminSurveyMetadataByKey**](SurveyAdministrationApi.md#GetAdminSurveyMetadataByKey) | **Get** /admin/surveys/{survey_id}/metadata/{key} | Get metadata by key for a survey
[**ListAdminSurveys**](SurveyAdministrationApi.md#ListAdminSurveys) | **Get** /admin/surveys | List surveys
[**PatchAdminSurvey**](SurveyAdministrationApi.md#PatchAdminSurvey) | **Patch** /admin/surveys/{survey_id} | Partially update a survey
[**UpdateAdminSurvey**](SurveyAdministrationApi.md#UpdateAdminSurvey) | **Put** /admin/surveys/{survey_id} | Update a survey
[**UpdateAdminSurveyMetadataByKey**](SurveyAdministrationApi.md#UpdateAdminSurveyMetadataByKey) | **Put** /admin/surveys/{survey_id}/metadata/{key} | Update metadata by key for a survey

# **BulkCreateAdminSurveyMetadata**
> []Metadata BulkCreateAdminSurveyMetadata(ctx, body, surveyId)
Bulk create metadata for a survey

Creates multiple metadata key-value pairs for the specified survey. Returns 409 Conflict if any of the specified keys already exist.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]Metadata**](Metadata.md)| Array of metadata key-value pairs to create | 
  **surveyId** | [**string**](.md)| Unique identifier of the survey | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **BulkReplaceAdminSurveyMetadata**
> []Metadata BulkReplaceAdminSurveyMetadata(ctx, body, surveyId)
Bulk replace metadata for a survey

Replaces all metadata for the entity. All existing metadata is deleted and replaced with the provided set. To clear all metadata, send an empty array.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]Metadata**](Metadata.md)| Complete set of metadata key-value pairs to replace existing metadata | 
  **surveyId** | [**string**](.md)| Unique identifier of the survey | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **BulkUpsertAdminSurveyMetadata**
> []Metadata BulkUpsertAdminSurveyMetadata(ctx, body, surveyId)
Bulk upsert metadata for a survey

Creates or updates only the provided metadata keys. Keys not included in the request are left unchanged. This is a merge/upsert operation.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]Metadata**](Metadata.md)| Metadata key-value pairs to create or update (merge) | 
  **surveyId** | [**string**](.md)| Unique identifier of the survey | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateAdminSurvey**
> Survey CreateAdminSurvey(ctx, body)
Create a survey

Creates a new survey. Surveys are created in inactive status by default.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**SurveyInput**](SurveyInput.md)| Survey definition to create | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateAdminSurveyMetadata**
> Metadata CreateAdminSurveyMetadata(ctx, body, surveyId)
Add metadata to a survey

Adds a new metadata key-value pair to the specified survey. Returns 409 Conflict if the key already exists.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**Metadata**](Metadata.md)| Metadata key-value pair to create | 
  **surveyId** | [**string**](.md)| Unique identifier of the survey | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteAdminSurvey**
> DeleteAdminSurvey(ctx, surveyId)
Delete a survey

Deletes a survey. Surveys with existing responses cannot be deleted.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyId** | [**string**](.md)| Unique identifier of the survey | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteAdminSurveyMetadataByKey**
> DeleteAdminSurveyMetadataByKey(ctx, surveyId, key)
Delete metadata by key for a survey

Deletes a specific metadata entry by key for the specified survey

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyId** | [**string**](.md)| Unique identifier of the survey | 
  **key** | **string**| Metadata key | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAdminSurvey**
> Survey GetAdminSurvey(ctx, surveyId)
Get a survey

Returns a specific survey by ID.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyId** | [**string**](.md)| Unique identifier of the survey | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAdminSurveyMetadata**
> []Metadata GetAdminSurveyMetadata(ctx, surveyId)
Get all metadata for a survey

Returns all metadata key-value pairs for the specified survey

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyId** | [**string**](.md)| Unique identifier of the survey | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAdminSurveyMetadataByKey**
> Metadata GetAdminSurveyMetadataByKey(ctx, surveyId, key)
Get metadata by key for a survey

Returns a specific metadata entry by key for the specified survey

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyId** | [**string**](.md)| Unique identifier of the survey | 
  **key** | **string**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListAdminSurveys**
> ListSurveysResponse ListAdminSurveys(ctx, optional)
List surveys

Returns a paginated list of all surveys with optional filtering by status.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SurveyAdministrationApiListAdminSurveysOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a SurveyAdministrationApiListAdminSurveysOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **optional.String**| Filter by survey status | 
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]
 **sort** | **optional.String**| Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) | [default to created_at:desc]
 **createdAfter** | **optional.Time**| Filter results created after this timestamp (ISO 8601) | 
 **createdBefore** | **optional.Time**| Filter results created before this timestamp (ISO 8601) | 
 **modifiedAfter** | **optional.Time**| Filter results modified after this timestamp (ISO 8601) | 
 **modifiedBefore** | **optional.Time**| Filter results modified before this timestamp (ISO 8601) | 

### Return type

[**ListSurveysResponse**](ListSurveysResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PatchAdminSurvey**
> Survey PatchAdminSurvey(ctx, body, surveyId)
Partially update a survey

Partially updates a survey using JSON Patch (RFC 6902).

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]JsonPatchDocumentInner**](JsonPatchDocument_inner.md)| JSON Patch operations to apply to the survey | 
  **surveyId** | [**string**](.md)| Unique identifier of the survey | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateAdminSurvey**
> Survey UpdateAdminSurvey(ctx, body, surveyId)
Update a survey

Fully updates a survey. All fields are replaced.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**SurveyInput**](SurveyInput.md)| Complete survey definition to replace existing | 
  **surveyId** | [**string**](.md)| Unique identifier of the survey | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateAdminSurveyMetadataByKey**
> Metadata UpdateAdminSurveyMetadataByKey(ctx, body, surveyId, key)
Update metadata by key for a survey

Updates or creates a metadata entry by key for the specified survey

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**Metadata**](Metadata.md)| Metadata key-value pair to update | 
  **surveyId** | [**string**](.md)| Unique identifier of the survey | 
  **key** | **string**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

