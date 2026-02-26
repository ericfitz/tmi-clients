# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BulkCreateIntakeSurveyResponseMetadata**](SurveyIntakeApi.md#BulkCreateIntakeSurveyResponseMetadata) | **Post** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk create metadata for a survey response
[**BulkReplaceIntakeSurveyResponseMetadata**](SurveyIntakeApi.md#BulkReplaceIntakeSurveyResponseMetadata) | **Put** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk replace metadata for a survey response
[**BulkUpsertIntakeSurveyResponseMetadata**](SurveyIntakeApi.md#BulkUpsertIntakeSurveyResponseMetadata) | **Patch** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk upsert metadata for a survey response
[**CreateIntakeSurveyResponse**](SurveyIntakeApi.md#CreateIntakeSurveyResponse) | **Post** /intake/survey_responses | Create survey response
[**CreateIntakeSurveyResponseMetadata**](SurveyIntakeApi.md#CreateIntakeSurveyResponseMetadata) | **Post** /intake/survey_responses/{survey_response_id}/metadata | Add metadata to a survey response
[**DeleteIntakeSurveyResponse**](SurveyIntakeApi.md#DeleteIntakeSurveyResponse) | **Delete** /intake/survey_responses/{survey_response_id} | Delete survey response
[**DeleteIntakeSurveyResponseMetadataByKey**](SurveyIntakeApi.md#DeleteIntakeSurveyResponseMetadataByKey) | **Delete** /intake/survey_responses/{survey_response_id}/metadata/{key} | Delete metadata by key for a survey response
[**GetIntakeSurvey**](SurveyIntakeApi.md#GetIntakeSurvey) | **Get** /intake/surveys/{survey_id} | Get an available survey
[**GetIntakeSurveyResponse**](SurveyIntakeApi.md#GetIntakeSurveyResponse) | **Get** /intake/survey_responses/{survey_response_id} | Get survey response
[**GetIntakeSurveyResponseMetadata**](SurveyIntakeApi.md#GetIntakeSurveyResponseMetadata) | **Get** /intake/survey_responses/{survey_response_id}/metadata | Get all metadata for a survey response
[**GetIntakeSurveyResponseMetadataByKey**](SurveyIntakeApi.md#GetIntakeSurveyResponseMetadataByKey) | **Get** /intake/survey_responses/{survey_response_id}/metadata/{key} | Get metadata by key for a survey response
[**GetIntakeSurveyResponseTriageNote**](SurveyIntakeApi.md#GetIntakeSurveyResponseTriageNote) | **Get** /intake/survey_responses/{survey_response_id}/triage_notes/{triage_note_id} | Get a specific triage note
[**ListIntakeSurveyResponseTriageNotes**](SurveyIntakeApi.md#ListIntakeSurveyResponseTriageNotes) | **Get** /intake/survey_responses/{survey_response_id}/triage_notes | List triage notes for a survey response
[**ListIntakeSurveyResponses**](SurveyIntakeApi.md#ListIntakeSurveyResponses) | **Get** /intake/survey_responses | List user&#x27;s survey responses
[**ListIntakeSurveys**](SurveyIntakeApi.md#ListIntakeSurveys) | **Get** /intake/surveys | List available surveys
[**PatchIntakeSurveyResponse**](SurveyIntakeApi.md#PatchIntakeSurveyResponse) | **Patch** /intake/survey_responses/{survey_response_id} | Partial update survey response
[**UpdateIntakeSurveyResponse**](SurveyIntakeApi.md#UpdateIntakeSurveyResponse) | **Put** /intake/survey_responses/{survey_response_id} | Update survey response
[**UpdateIntakeSurveyResponseMetadataByKey**](SurveyIntakeApi.md#UpdateIntakeSurveyResponseMetadataByKey) | **Put** /intake/survey_responses/{survey_response_id}/metadata/{key} | Update metadata by key for a survey response

# **BulkCreateIntakeSurveyResponseMetadata**
> []Metadata BulkCreateIntakeSurveyResponseMetadata(ctx, body, surveyResponseId)
Bulk create metadata for a survey response

Creates multiple metadata key-value pairs for the specified survey response. Returns 409 Conflict if any of the specified keys already exist.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]Metadata**](Metadata.md)| Array of metadata key-value pairs to create | 
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **BulkReplaceIntakeSurveyResponseMetadata**
> []Metadata BulkReplaceIntakeSurveyResponseMetadata(ctx, body, surveyResponseId)
Bulk replace metadata for a survey response

Replaces all metadata for the entity. All existing metadata is deleted and replaced with the provided set. To clear all metadata, send an empty array.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]Metadata**](Metadata.md)| Complete set of metadata key-value pairs to replace existing metadata | 
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **BulkUpsertIntakeSurveyResponseMetadata**
> []Metadata BulkUpsertIntakeSurveyResponseMetadata(ctx, body, surveyResponseId)
Bulk upsert metadata for a survey response

Creates or updates only the provided metadata keys. Keys not included in the request are left unchanged. This is a merge/upsert operation.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]Metadata**](Metadata.md)| Metadata key-value pairs to create or update (merge) | 
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateIntakeSurveyResponse**
> SurveyResponse CreateIntakeSurveyResponse(ctx, body)
Create survey response

Creates a new survey response in draft status. The secret_project flag can only be set here.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**SurveyResponseCreateRequest**](SurveyResponseCreateRequest.md)| Survey response to create | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateIntakeSurveyResponseMetadata**
> Metadata CreateIntakeSurveyResponseMetadata(ctx, body, surveyResponseId)
Add metadata to a survey response

Adds a new metadata key-value pair to the specified survey response. Returns 409 Conflict if the key already exists.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**Metadata**](Metadata.md)| Metadata key-value pair to create | 
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteIntakeSurveyResponse**
> DeleteIntakeSurveyResponse(ctx, surveyResponseId)
Delete survey response

Deletes a survey response. Requires owner access.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteIntakeSurveyResponseMetadataByKey**
> DeleteIntakeSurveyResponseMetadataByKey(ctx, surveyResponseId, key)
Delete metadata by key for a survey response

Deletes a specific metadata entry by key for the specified survey response

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 
  **key** | **string**| Metadata key | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetIntakeSurvey**
> Survey GetIntakeSurvey(ctx, surveyId)
Get an available survey

Returns a specific active survey with all questions for the developer to fill out.

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

# **GetIntakeSurveyResponse**
> SurveyResponse GetIntakeSurveyResponse(ctx, surveyResponseId)
Get survey response

Returns a specific survey response. Requires reader access.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetIntakeSurveyResponseMetadata**
> []Metadata GetIntakeSurveyResponseMetadata(ctx, surveyResponseId)
Get all metadata for a survey response

Returns all metadata key-value pairs for the specified survey response

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetIntakeSurveyResponseMetadataByKey**
> Metadata GetIntakeSurveyResponseMetadataByKey(ctx, surveyResponseId, key)
Get metadata by key for a survey response

Returns a specific metadata entry by key for the specified survey response

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 
  **key** | **string**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetIntakeSurveyResponseTriageNote**
> TriageNote GetIntakeSurveyResponseTriageNote(ctx, surveyResponseId, triageNoteId)
Get a specific triage note

Returns details of a specific triage note. Read-only access for survey response submitters.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 
  **triageNoteId** | **int32**| Triage note identifier (sequential within survey response) | 

### Return type

[**TriageNote**](TriageNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListIntakeSurveyResponseTriageNotes**
> ListTriageNotesResponse ListIntakeSurveyResponseTriageNotes(ctx, surveyResponseId, optional)
List triage notes for a survey response

Returns a paginated list of triage notes for the specified survey response. Read-only access for survey response submitters.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 
 **optional** | ***SurveyIntakeApiListIntakeSurveyResponseTriageNotesOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a SurveyIntakeApiListIntakeSurveyResponseTriageNotesOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**ListTriageNotesResponse**](ListTriageNotesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListIntakeSurveyResponses**
> ListSurveyResponsesResponse ListIntakeSurveyResponses(ctx, optional)
List user's survey responses

Returns a paginated list of the current user's survey responses.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SurveyIntakeApiListIntakeSurveyResponsesOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a SurveyIntakeApiListIntakeSurveyResponsesOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **optional.String**| Filter by response status | 
 **surveyId** | [**optional.Interface of string**](.md)| Filter by survey ID | 
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]
 **sort** | **optional.String**| Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) | [default to created_at:desc]
 **createdAfter** | **optional.Time**| Filter results created after this timestamp (ISO 8601) | 
 **createdBefore** | **optional.Time**| Filter results created before this timestamp (ISO 8601) | 
 **modifiedAfter** | **optional.Time**| Filter results modified after this timestamp (ISO 8601) | 
 **modifiedBefore** | **optional.Time**| Filter results modified before this timestamp (ISO 8601) | 

### Return type

[**ListSurveyResponsesResponse**](ListSurveyResponsesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListIntakeSurveys**
> ListSurveysResponse ListIntakeSurveys(ctx, optional)
List available surveys

Returns a list of active surveys available for developers to fill out.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SurveyIntakeApiListIntakeSurveysOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a SurveyIntakeApiListIntakeSurveysOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]
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

# **PatchIntakeSurveyResponse**
> SurveyResponse PatchIntakeSurveyResponse(ctx, body, surveyResponseId)
Partial update survey response

Partially updates a survey response using JSON Patch (RFC 6902). Status transitions are allowed via /status path. Valid statuses: draft, submitted, needs_revision, ready_for_review, review_created. Transitioning to needs_revision requires revision_notes.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]JsonPatchDocumentInner**](JsonPatchDocument_inner.md)| JSON Patch operations to apply to the survey response | 
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateIntakeSurveyResponse**
> SurveyResponse UpdateIntakeSurveyResponse(ctx, body, surveyResponseId)
Update survey response

Fully updates a survey response. Only allowed in draft or needs_revision status. Requires writer access.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**SurveyResponseInput**](SurveyResponseInput.md)| Complete survey response to replace existing | 
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateIntakeSurveyResponseMetadataByKey**
> Metadata UpdateIntakeSurveyResponseMetadataByKey(ctx, body, surveyResponseId, key)
Update metadata by key for a survey response

Updates or creates a metadata entry by key for the specified survey response

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**Metadata**](Metadata.md)| Metadata key-value pair to update | 
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 
  **key** | **string**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

