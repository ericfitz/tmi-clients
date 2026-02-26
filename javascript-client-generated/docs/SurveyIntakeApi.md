# TmiJsClient.SurveyIntakeApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkCreateIntakeSurveyResponseMetadata**](SurveyIntakeApi.md#bulkCreateIntakeSurveyResponseMetadata) | **POST** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk create metadata for a survey response
[**bulkReplaceIntakeSurveyResponseMetadata**](SurveyIntakeApi.md#bulkReplaceIntakeSurveyResponseMetadata) | **PUT** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk replace metadata for a survey response
[**bulkUpsertIntakeSurveyResponseMetadata**](SurveyIntakeApi.md#bulkUpsertIntakeSurveyResponseMetadata) | **PATCH** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk upsert metadata for a survey response
[**createIntakeSurveyResponse**](SurveyIntakeApi.md#createIntakeSurveyResponse) | **POST** /intake/survey_responses | Create survey response
[**createIntakeSurveyResponseMetadata**](SurveyIntakeApi.md#createIntakeSurveyResponseMetadata) | **POST** /intake/survey_responses/{survey_response_id}/metadata | Add metadata to a survey response
[**deleteIntakeSurveyResponse**](SurveyIntakeApi.md#deleteIntakeSurveyResponse) | **DELETE** /intake/survey_responses/{survey_response_id} | Delete survey response
[**deleteIntakeSurveyResponseMetadataByKey**](SurveyIntakeApi.md#deleteIntakeSurveyResponseMetadataByKey) | **DELETE** /intake/survey_responses/{survey_response_id}/metadata/{key} | Delete metadata by key for a survey response
[**getIntakeSurvey**](SurveyIntakeApi.md#getIntakeSurvey) | **GET** /intake/surveys/{survey_id} | Get an available survey
[**getIntakeSurveyResponse**](SurveyIntakeApi.md#getIntakeSurveyResponse) | **GET** /intake/survey_responses/{survey_response_id} | Get survey response
[**getIntakeSurveyResponseMetadata**](SurveyIntakeApi.md#getIntakeSurveyResponseMetadata) | **GET** /intake/survey_responses/{survey_response_id}/metadata | Get all metadata for a survey response
[**getIntakeSurveyResponseMetadataByKey**](SurveyIntakeApi.md#getIntakeSurveyResponseMetadataByKey) | **GET** /intake/survey_responses/{survey_response_id}/metadata/{key} | Get metadata by key for a survey response
[**getIntakeSurveyResponseTriageNote**](SurveyIntakeApi.md#getIntakeSurveyResponseTriageNote) | **GET** /intake/survey_responses/{survey_response_id}/triage_notes/{triage_note_id} | Get a specific triage note
[**listIntakeSurveyResponseTriageNotes**](SurveyIntakeApi.md#listIntakeSurveyResponseTriageNotes) | **GET** /intake/survey_responses/{survey_response_id}/triage_notes | List triage notes for a survey response
[**listIntakeSurveyResponses**](SurveyIntakeApi.md#listIntakeSurveyResponses) | **GET** /intake/survey_responses | List user&#x27;s survey responses
[**listIntakeSurveys**](SurveyIntakeApi.md#listIntakeSurveys) | **GET** /intake/surveys | List available surveys
[**patchIntakeSurveyResponse**](SurveyIntakeApi.md#patchIntakeSurveyResponse) | **PATCH** /intake/survey_responses/{survey_response_id} | Partial update survey response
[**updateIntakeSurveyResponse**](SurveyIntakeApi.md#updateIntakeSurveyResponse) | **PUT** /intake/survey_responses/{survey_response_id} | Update survey response
[**updateIntakeSurveyResponseMetadataByKey**](SurveyIntakeApi.md#updateIntakeSurveyResponseMetadataByKey) | **PUT** /intake/survey_responses/{survey_response_id}/metadata/{key} | Update metadata by key for a survey response

<a name="bulkCreateIntakeSurveyResponseMetadata"></a>
# **bulkCreateIntakeSurveyResponseMetadata**
> [Metadata] bulkCreateIntakeSurveyResponseMetadata(body, surveyResponseId)

Bulk create metadata for a survey response

Creates multiple metadata key-value pairs for the specified survey response. Returns 409 Conflict if any of the specified keys already exist.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | Array of metadata key-value pairs to create
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.bulkCreateIntakeSurveyResponseMetadata(body, surveyResponseId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)| Array of metadata key-value pairs to create | 
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkReplaceIntakeSurveyResponseMetadata"></a>
# **bulkReplaceIntakeSurveyResponseMetadata**
> [Metadata] bulkReplaceIntakeSurveyResponseMetadata(body, surveyResponseId)

Bulk replace metadata for a survey response

Replaces all metadata for the entity. All existing metadata is deleted and replaced with the provided set. To clear all metadata, send an empty array.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | Complete set of metadata key-value pairs to replace existing metadata
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.bulkReplaceIntakeSurveyResponseMetadata(body, surveyResponseId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)| Complete set of metadata key-value pairs to replace existing metadata | 
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpsertIntakeSurveyResponseMetadata"></a>
# **bulkUpsertIntakeSurveyResponseMetadata**
> [Metadata] bulkUpsertIntakeSurveyResponseMetadata(body, surveyResponseId)

Bulk upsert metadata for a survey response

Creates or updates only the provided metadata keys. Keys not included in the request are left unchanged. This is a merge/upsert operation.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | Metadata key-value pairs to create or update (merge)
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.bulkUpsertIntakeSurveyResponseMetadata(body, surveyResponseId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)| Metadata key-value pairs to create or update (merge) | 
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createIntakeSurveyResponse"></a>
# **createIntakeSurveyResponse**
> SurveyResponse createIntakeSurveyResponse(body)

Create survey response

Creates a new survey response in draft status. The secret_project flag can only be set here.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let body = new TmiJsClient.SurveyResponseCreateRequest(); // SurveyResponseCreateRequest | Survey response to create

apiInstance.createIntakeSurveyResponse(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SurveyResponseCreateRequest**](SurveyResponseCreateRequest.md)| Survey response to create | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createIntakeSurveyResponseMetadata"></a>
# **createIntakeSurveyResponseMetadata**
> Metadata createIntakeSurveyResponseMetadata(body, surveyResponseId)

Add metadata to a survey response

Adds a new metadata key-value pair to the specified survey response. Returns 409 Conflict if the key already exists.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let body = new TmiJsClient.Metadata(); // Metadata | Metadata key-value pair to create
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.createIntakeSurveyResponseMetadata(body, surveyResponseId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata key-value pair to create | 
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteIntakeSurveyResponse"></a>
# **deleteIntakeSurveyResponse**
> deleteIntakeSurveyResponse(surveyResponseId)

Delete survey response

Deletes a survey response. Requires owner access.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.deleteIntakeSurveyResponse(surveyResponseId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteIntakeSurveyResponseMetadataByKey"></a>
# **deleteIntakeSurveyResponseMetadataByKey**
> deleteIntakeSurveyResponseMetadataByKey(surveyResponseId, key)

Delete metadata by key for a survey response

Deletes a specific metadata entry by key for the specified survey response

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response
let key = "key_example"; // String | Metadata key

apiInstance.deleteIntakeSurveyResponseMetadataByKey(surveyResponseId, key).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 
 **key** | **String**| Metadata key | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getIntakeSurvey"></a>
# **getIntakeSurvey**
> Survey getIntakeSurvey(surveyId)

Get an available survey

Returns a specific active survey with all questions for the developer to fill out.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let surveyId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey

apiInstance.getIntakeSurvey(surveyId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyId** | [**String**](.md)| Unique identifier of the survey | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getIntakeSurveyResponse"></a>
# **getIntakeSurveyResponse**
> SurveyResponse getIntakeSurveyResponse(surveyResponseId)

Get survey response

Returns a specific survey response. Requires reader access.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.getIntakeSurveyResponse(surveyResponseId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getIntakeSurveyResponseMetadata"></a>
# **getIntakeSurveyResponseMetadata**
> [Metadata] getIntakeSurveyResponseMetadata(surveyResponseId)

Get all metadata for a survey response

Returns all metadata key-value pairs for the specified survey response

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.getIntakeSurveyResponseMetadata(surveyResponseId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getIntakeSurveyResponseMetadataByKey"></a>
# **getIntakeSurveyResponseMetadataByKey**
> Metadata getIntakeSurveyResponseMetadataByKey(surveyResponseId, key)

Get metadata by key for a survey response

Returns a specific metadata entry by key for the specified survey response

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response
let key = "key_example"; // String | Metadata key

apiInstance.getIntakeSurveyResponseMetadataByKey(surveyResponseId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getIntakeSurveyResponseTriageNote"></a>
# **getIntakeSurveyResponseTriageNote**
> TriageNote getIntakeSurveyResponseTriageNote(surveyResponseId, triageNoteId)

Get a specific triage note

Returns details of a specific triage note. Read-only access for survey response submitters.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response
let triageNoteId = 56; // Number | Triage note identifier (sequential within survey response)

apiInstance.getIntakeSurveyResponseTriageNote(surveyResponseId, triageNoteId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 
 **triageNoteId** | **Number**| Triage note identifier (sequential within survey response) | 

### Return type

[**TriageNote**](TriageNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listIntakeSurveyResponseTriageNotes"></a>
# **listIntakeSurveyResponseTriageNotes**
> ListTriageNotesResponse listIntakeSurveyResponseTriageNotes(surveyResponseId, opts)

List triage notes for a survey response

Returns a paginated list of triage notes for the specified survey response. Read-only access for survey response submitters.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.listIntakeSurveyResponseTriageNotes(surveyResponseId, opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListTriageNotesResponse**](ListTriageNotesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listIntakeSurveyResponses"></a>
# **listIntakeSurveyResponses**
> ListSurveyResponsesResponse listIntakeSurveyResponses(opts)

List user&#x27;s survey responses

Returns a paginated list of the current user&#x27;s survey responses.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let opts = { 
  'status': "status_example", // String | Filter by response status
  'surveyId': "38400000-8cf0-11bd-b23e-10b96e4ef00d", // String | Filter by survey ID
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0, // Number | Number of results to skip
  'sort': "created_at:desc", // String | Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc)
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results created after this timestamp (ISO 8601)
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results created before this timestamp (ISO 8601)
  'modifiedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results modified after this timestamp (ISO 8601)
  'modifiedBefore': new Date("2013-10-20T19:20:30+01:00") // Date | Filter results modified before this timestamp (ISO 8601)
};
apiInstance.listIntakeSurveyResponses(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **String**| Filter by response status | [optional] 
 **surveyId** | [**String**](.md)| Filter by survey ID | [optional] 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]
 **sort** | **String**| Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) | [optional] [default to created_at:desc]
 **createdAfter** | **Date**| Filter results created after this timestamp (ISO 8601) | [optional] 
 **createdBefore** | **Date**| Filter results created before this timestamp (ISO 8601) | [optional] 
 **modifiedAfter** | **Date**| Filter results modified after this timestamp (ISO 8601) | [optional] 
 **modifiedBefore** | **Date**| Filter results modified before this timestamp (ISO 8601) | [optional] 

### Return type

[**ListSurveyResponsesResponse**](ListSurveyResponsesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listIntakeSurveys"></a>
# **listIntakeSurveys**
> ListSurveysResponse listIntakeSurveys(opts)

List available surveys

Returns a list of active surveys available for developers to fill out.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0, // Number | Number of results to skip
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results created after this timestamp (ISO 8601)
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results created before this timestamp (ISO 8601)
  'modifiedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results modified after this timestamp (ISO 8601)
  'modifiedBefore': new Date("2013-10-20T19:20:30+01:00") // Date | Filter results modified before this timestamp (ISO 8601)
};
apiInstance.listIntakeSurveys(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]
 **createdAfter** | **Date**| Filter results created after this timestamp (ISO 8601) | [optional] 
 **createdBefore** | **Date**| Filter results created before this timestamp (ISO 8601) | [optional] 
 **modifiedAfter** | **Date**| Filter results modified after this timestamp (ISO 8601) | [optional] 
 **modifiedBefore** | **Date**| Filter results modified before this timestamp (ISO 8601) | [optional] 

### Return type

[**ListSurveysResponse**](ListSurveysResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="patchIntakeSurveyResponse"></a>
# **patchIntakeSurveyResponse**
> SurveyResponse patchIntakeSurveyResponse(body, surveyResponseId)

Partial update survey response

Partially updates a survey response using JSON Patch (RFC 6902). Status transitions are allowed via /status path. Valid statuses: draft, submitted, needs_revision, ready_for_review, review_created. Transitioning to needs_revision requires revision_notes.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let body = [new TmiJsClient.JsonPatchDocumentInner()]; // [JsonPatchDocumentInner] | JSON Patch operations to apply to the survey response
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.patchIntakeSurveyResponse(body, surveyResponseId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| JSON Patch operations to apply to the survey response | 
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

<a name="updateIntakeSurveyResponse"></a>
# **updateIntakeSurveyResponse**
> SurveyResponse updateIntakeSurveyResponse(body, surveyResponseId)

Update survey response

Fully updates a survey response. Only allowed in draft or needs_revision status. Requires writer access.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let body = new TmiJsClient.SurveyResponseInput(); // SurveyResponseInput | Complete survey response to replace existing
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.updateIntakeSurveyResponse(body, surveyResponseId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SurveyResponseInput**](SurveyResponseInput.md)| Complete survey response to replace existing | 
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateIntakeSurveyResponseMetadataByKey"></a>
# **updateIntakeSurveyResponseMetadataByKey**
> Metadata updateIntakeSurveyResponseMetadataByKey(body, surveyResponseId, key)

Update metadata by key for a survey response

Updates or creates a metadata entry by key for the specified survey response

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyIntakeApi();
let body = new TmiJsClient.Metadata(); // Metadata | Metadata key-value pair to update
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response
let key = "key_example"; // String | Metadata key

apiInstance.updateIntakeSurveyResponseMetadataByKey(body, surveyResponseId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata key-value pair to update | 
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

