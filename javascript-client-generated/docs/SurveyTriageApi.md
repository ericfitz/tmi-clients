# TmiJsClient.SurveyTriageApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createThreatModelFromSurveyResponse**](SurveyTriageApi.md#createThreatModelFromSurveyResponse) | **POST** /triage/survey_responses/{survey_response_id}/create_threat_model | Create threat model from survey response
[**createTriageSurveyResponseTriageNote**](SurveyTriageApi.md#createTriageSurveyResponseTriageNote) | **POST** /triage/survey_responses/{survey_response_id}/triage_notes | Create a triage note
[**getTriageSurveyResponse**](SurveyTriageApi.md#getTriageSurveyResponse) | **GET** /triage/survey_responses/{survey_response_id} | Get survey response for triage
[**getTriageSurveyResponseMetadata**](SurveyTriageApi.md#getTriageSurveyResponseMetadata) | **GET** /triage/survey_responses/{survey_response_id}/metadata | Get all metadata for a survey response
[**getTriageSurveyResponseMetadataByKey**](SurveyTriageApi.md#getTriageSurveyResponseMetadataByKey) | **GET** /triage/survey_responses/{survey_response_id}/metadata/{key} | Get metadata by key for a survey response
[**getTriageSurveyResponseTriageNote**](SurveyTriageApi.md#getTriageSurveyResponseTriageNote) | **GET** /triage/survey_responses/{survey_response_id}/triage_notes/{triage_note_id} | Get a specific triage note
[**listTriageSurveyResponseTriageNotes**](SurveyTriageApi.md#listTriageSurveyResponseTriageNotes) | **GET** /triage/survey_responses/{survey_response_id}/triage_notes | List triage notes for a survey response
[**listTriageSurveyResponses**](SurveyTriageApi.md#listTriageSurveyResponses) | **GET** /triage/survey_responses | List survey responses for triage
[**patchTriageSurveyResponse**](SurveyTriageApi.md#patchTriageSurveyResponse) | **PATCH** /triage/survey_responses/{survey_response_id} | Partial update survey response for triage

<a name="createThreatModelFromSurveyResponse"></a>
# **createThreatModelFromSurveyResponse**
> CreateThreatModelFromSurveyResponse createThreatModelFromSurveyResponse(surveyResponseId)

Create threat model from survey response

Creates a new threat model from an approved survey response. Copies answers to TM metadata, sets owner to survey owner, and transitions response to review_created.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyTriageApi();
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.createThreatModelFromSurveyResponse(surveyResponseId).then((data) => {
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

[**CreateThreatModelFromSurveyResponse**](CreateThreatModelFromSurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="createTriageSurveyResponseTriageNote"></a>
# **createTriageSurveyResponseTriageNote**
> TriageNote createTriageSurveyResponseTriageNote(body, surveyResponseId)

Create a triage note

Creates a new triage note on the specified survey response. Only accessible to security reviewers.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyTriageApi();
let body = new TmiJsClient.TriageNoteInput(); // TriageNoteInput | Triage note creation data
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.createTriageSurveyResponseTriageNote(body, surveyResponseId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TriageNoteInput**](TriageNoteInput.md)| Triage note creation data | 
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 

### Return type

[**TriageNote**](TriageNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="getTriageSurveyResponse"></a>
# **getTriageSurveyResponse**
> SurveyResponse getTriageSurveyResponse(surveyResponseId)

Get survey response for triage

Returns a specific survey response for security engineer review.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyTriageApi();
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.getTriageSurveyResponse(surveyResponseId).then((data) => {
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

<a name="getTriageSurveyResponseMetadata"></a>
# **getTriageSurveyResponseMetadata**
> [Metadata] getTriageSurveyResponseMetadata(surveyResponseId)

Get all metadata for a survey response

Returns all metadata key-value pairs for the specified survey response (read-only triage access)

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyTriageApi();
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.getTriageSurveyResponseMetadata(surveyResponseId).then((data) => {
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

<a name="getTriageSurveyResponseMetadataByKey"></a>
# **getTriageSurveyResponseMetadataByKey**
> Metadata getTriageSurveyResponseMetadataByKey(surveyResponseId, key)

Get metadata by key for a survey response

Returns a specific metadata entry by key for the specified survey response (read-only triage access)

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyTriageApi();
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response
let key = "key_example"; // String | Metadata key

apiInstance.getTriageSurveyResponseMetadataByKey(surveyResponseId, key).then((data) => {
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

<a name="getTriageSurveyResponseTriageNote"></a>
# **getTriageSurveyResponseTriageNote**
> TriageNote getTriageSurveyResponseTriageNote(surveyResponseId, triageNoteId)

Get a specific triage note

Returns details of a specific triage note within the survey response. Only accessible to security reviewers.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyTriageApi();
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response
let triageNoteId = 56; // Number | Triage note identifier (sequential within survey response)

apiInstance.getTriageSurveyResponseTriageNote(surveyResponseId, triageNoteId).then((data) => {
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

<a name="listTriageSurveyResponseTriageNotes"></a>
# **listTriageSurveyResponseTriageNotes**
> ListTriageNotesResponse listTriageSurveyResponseTriageNotes(surveyResponseId, opts)

List triage notes for a survey response

Returns a paginated list of triage notes attached to the specified survey response. Only accessible to security reviewers.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyTriageApi();
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.listTriageSurveyResponseTriageNotes(surveyResponseId, opts).then((data) => {
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

<a name="listTriageSurveyResponses"></a>
# **listTriageSurveyResponses**
> ListSurveyResponsesResponse listTriageSurveyResponses(opts)

List survey responses for triage

Returns a paginated list of survey responses for security engineers to triage. Filter by status&#x3D;submitted to see the triage queue.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyTriageApi();
let opts = { 
  'status': "status_example", // String | Filter by response status
  'surveyId': "38400000-8cf0-11bd-b23e-10b96e4ef00d", // String | Filter by survey ID
  'isConfidential': true, // Boolean | Filter by secret_project flag
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0, // Number | Number of results to skip
  'sort': "created_at:desc", // String | Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc)
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results created after this timestamp (ISO 8601)
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results created before this timestamp (ISO 8601)
  'modifiedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results modified after this timestamp (ISO 8601)
  'modifiedBefore': new Date("2013-10-20T19:20:30+01:00") // Date | Filter results modified before this timestamp (ISO 8601)
};
apiInstance.listTriageSurveyResponses(opts).then((data) => {
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
 **isConfidential** | **Boolean**| Filter by secret_project flag | [optional] 
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

<a name="patchTriageSurveyResponse"></a>
# **patchTriageSurveyResponse**
> SurveyResponse patchTriageSurveyResponse(body, surveyResponseId)

Partial update survey response for triage

Partially updates a survey response using JSON Patch (RFC 6902). Security Reviewers can change status via /status path. Valid statuses: draft, submitted, needs_revision, ready_for_review, review_created. Transitioning to needs_revision requires revision_notes.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyTriageApi();
let body = [new TmiJsClient.JsonPatchDocumentInner()]; // [JsonPatchDocumentInner] | JSON Patch operations to apply to the survey response during triage
let surveyResponseId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey response

apiInstance.patchTriageSurveyResponse(body, surveyResponseId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| JSON Patch operations to apply to the survey response during triage | 
 **surveyResponseId** | [**String**](.md)| Unique identifier of the survey response | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

