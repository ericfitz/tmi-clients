# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateThreatModelFromSurveyResponse**](SurveyTriageApi.md#CreateThreatModelFromSurveyResponse) | **Post** /triage/survey_responses/{survey_response_id}/create_threat_model | Create threat model from survey response
[**CreateTriageSurveyResponseTriageNote**](SurveyTriageApi.md#CreateTriageSurveyResponseTriageNote) | **Post** /triage/survey_responses/{survey_response_id}/triage_notes | Create a triage note
[**GetTriageSurveyResponse**](SurveyTriageApi.md#GetTriageSurveyResponse) | **Get** /triage/survey_responses/{survey_response_id} | Get survey response for triage
[**GetTriageSurveyResponseMetadata**](SurveyTriageApi.md#GetTriageSurveyResponseMetadata) | **Get** /triage/survey_responses/{survey_response_id}/metadata | Get all metadata for a survey response
[**GetTriageSurveyResponseMetadataByKey**](SurveyTriageApi.md#GetTriageSurveyResponseMetadataByKey) | **Get** /triage/survey_responses/{survey_response_id}/metadata/{key} | Get metadata by key for a survey response
[**GetTriageSurveyResponseTriageNote**](SurveyTriageApi.md#GetTriageSurveyResponseTriageNote) | **Get** /triage/survey_responses/{survey_response_id}/triage_notes/{triage_note_id} | Get a specific triage note
[**ListTriageSurveyResponseTriageNotes**](SurveyTriageApi.md#ListTriageSurveyResponseTriageNotes) | **Get** /triage/survey_responses/{survey_response_id}/triage_notes | List triage notes for a survey response
[**ListTriageSurveyResponses**](SurveyTriageApi.md#ListTriageSurveyResponses) | **Get** /triage/survey_responses | List survey responses for triage
[**PatchTriageSurveyResponse**](SurveyTriageApi.md#PatchTriageSurveyResponse) | **Patch** /triage/survey_responses/{survey_response_id} | Partial update survey response for triage

# **CreateThreatModelFromSurveyResponse**
> CreateThreatModelFromSurveyResponse CreateThreatModelFromSurveyResponse(ctx, surveyResponseId)
Create threat model from survey response

Creates a new threat model from an approved survey response. Copies answers to TM metadata, sets owner to survey owner, and transitions response to review_created.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 

### Return type

[**CreateThreatModelFromSurveyResponse**](CreateThreatModelFromSurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateTriageSurveyResponseTriageNote**
> TriageNote CreateTriageSurveyResponseTriageNote(ctx, body, surveyResponseId)
Create a triage note

Creates a new triage note on the specified survey response. Only accessible to security reviewers.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**TriageNoteInput**](TriageNoteInput.md)| Triage note creation data | 
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 

### Return type

[**TriageNote**](TriageNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetTriageSurveyResponse**
> SurveyResponse GetTriageSurveyResponse(ctx, surveyResponseId)
Get survey response for triage

Returns a specific survey response for security engineer review.

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

# **GetTriageSurveyResponseMetadata**
> []Metadata GetTriageSurveyResponseMetadata(ctx, surveyResponseId)
Get all metadata for a survey response

Returns all metadata key-value pairs for the specified survey response (read-only triage access)

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

# **GetTriageSurveyResponseMetadataByKey**
> Metadata GetTriageSurveyResponseMetadataByKey(ctx, surveyResponseId, key)
Get metadata by key for a survey response

Returns a specific metadata entry by key for the specified survey response (read-only triage access)

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

# **GetTriageSurveyResponseTriageNote**
> TriageNote GetTriageSurveyResponseTriageNote(ctx, surveyResponseId, triageNoteId)
Get a specific triage note

Returns details of a specific triage note within the survey response. Only accessible to security reviewers.

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

# **ListTriageSurveyResponseTriageNotes**
> ListTriageNotesResponse ListTriageSurveyResponseTriageNotes(ctx, surveyResponseId, optional)
List triage notes for a survey response

Returns a paginated list of triage notes attached to the specified survey response. Only accessible to security reviewers.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 
 **optional** | ***SurveyTriageApiListTriageSurveyResponseTriageNotesOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a SurveyTriageApiListTriageSurveyResponseTriageNotesOpts struct
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

# **ListTriageSurveyResponses**
> ListSurveyResponsesResponse ListTriageSurveyResponses(ctx, optional)
List survey responses for triage

Returns a paginated list of survey responses for security engineers to triage. Filter by status=submitted to see the triage queue.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***SurveyTriageApiListTriageSurveyResponsesOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a SurveyTriageApiListTriageSurveyResponsesOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **optional.String**| Filter by response status | 
 **surveyId** | [**optional.Interface of string**](.md)| Filter by survey ID | 
 **isConfidential** | **optional.Bool**| Filter by secret_project flag | 
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

# **PatchTriageSurveyResponse**
> SurveyResponse PatchTriageSurveyResponse(ctx, body, surveyResponseId)
Partial update survey response for triage

Partially updates a survey response using JSON Patch (RFC 6902). Security Reviewers can change status via /status path. Valid statuses: draft, submitted, needs_revision, ready_for_review, review_created. Transitioning to needs_revision requires revision_notes.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]JsonPatchDocumentInner**](JsonPatchDocument_inner.md)| JSON Patch operations to apply to the survey response during triage | 
  **surveyResponseId** | [**string**](.md)| Unique identifier of the survey response | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

