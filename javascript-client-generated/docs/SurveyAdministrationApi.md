# TmiJsClient.SurveyAdministrationApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkCreateAdminSurveyMetadata**](SurveyAdministrationApi.md#bulkCreateAdminSurveyMetadata) | **POST** /admin/surveys/{survey_id}/metadata/bulk | Bulk create metadata for a survey
[**bulkReplaceAdminSurveyMetadata**](SurveyAdministrationApi.md#bulkReplaceAdminSurveyMetadata) | **PUT** /admin/surveys/{survey_id}/metadata/bulk | Bulk replace metadata for a survey
[**bulkUpsertAdminSurveyMetadata**](SurveyAdministrationApi.md#bulkUpsertAdminSurveyMetadata) | **PATCH** /admin/surveys/{survey_id}/metadata/bulk | Bulk upsert metadata for a survey
[**createAdminSurvey**](SurveyAdministrationApi.md#createAdminSurvey) | **POST** /admin/surveys | Create a survey
[**createAdminSurveyMetadata**](SurveyAdministrationApi.md#createAdminSurveyMetadata) | **POST** /admin/surveys/{survey_id}/metadata | Add metadata to a survey
[**deleteAdminSurvey**](SurveyAdministrationApi.md#deleteAdminSurvey) | **DELETE** /admin/surveys/{survey_id} | Delete a survey
[**deleteAdminSurveyMetadataByKey**](SurveyAdministrationApi.md#deleteAdminSurveyMetadataByKey) | **DELETE** /admin/surveys/{survey_id}/metadata/{key} | Delete metadata by key for a survey
[**getAdminSurvey**](SurveyAdministrationApi.md#getAdminSurvey) | **GET** /admin/surveys/{survey_id} | Get a survey
[**getAdminSurveyMetadata**](SurveyAdministrationApi.md#getAdminSurveyMetadata) | **GET** /admin/surveys/{survey_id}/metadata | Get all metadata for a survey
[**getAdminSurveyMetadataByKey**](SurveyAdministrationApi.md#getAdminSurveyMetadataByKey) | **GET** /admin/surveys/{survey_id}/metadata/{key} | Get metadata by key for a survey
[**listAdminSurveys**](SurveyAdministrationApi.md#listAdminSurveys) | **GET** /admin/surveys | List surveys
[**patchAdminSurvey**](SurveyAdministrationApi.md#patchAdminSurvey) | **PATCH** /admin/surveys/{survey_id} | Partially update a survey
[**updateAdminSurvey**](SurveyAdministrationApi.md#updateAdminSurvey) | **PUT** /admin/surveys/{survey_id} | Update a survey
[**updateAdminSurveyMetadataByKey**](SurveyAdministrationApi.md#updateAdminSurveyMetadataByKey) | **PUT** /admin/surveys/{survey_id}/metadata/{key} | Update metadata by key for a survey

<a name="bulkCreateAdminSurveyMetadata"></a>
# **bulkCreateAdminSurveyMetadata**
> [Metadata] bulkCreateAdminSurveyMetadata(body, surveyId)

Bulk create metadata for a survey

Creates multiple metadata key-value pairs for the specified survey. Returns 409 Conflict if any of the specified keys already exist.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | Array of metadata key-value pairs to create
let surveyId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey

apiInstance.bulkCreateAdminSurveyMetadata(body, surveyId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)| Array of metadata key-value pairs to create | 
 **surveyId** | [**String**](.md)| Unique identifier of the survey | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkReplaceAdminSurveyMetadata"></a>
# **bulkReplaceAdminSurveyMetadata**
> [Metadata] bulkReplaceAdminSurveyMetadata(body, surveyId)

Bulk replace metadata for a survey

Replaces all metadata for the entity. All existing metadata is deleted and replaced with the provided set. To clear all metadata, send an empty array.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | Complete set of metadata key-value pairs to replace existing metadata
let surveyId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey

apiInstance.bulkReplaceAdminSurveyMetadata(body, surveyId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)| Complete set of metadata key-value pairs to replace existing metadata | 
 **surveyId** | [**String**](.md)| Unique identifier of the survey | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpsertAdminSurveyMetadata"></a>
# **bulkUpsertAdminSurveyMetadata**
> [Metadata] bulkUpsertAdminSurveyMetadata(body, surveyId)

Bulk upsert metadata for a survey

Creates or updates only the provided metadata keys. Keys not included in the request are left unchanged. This is a merge/upsert operation.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | Metadata key-value pairs to create or update (merge)
let surveyId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey

apiInstance.bulkUpsertAdminSurveyMetadata(body, surveyId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)| Metadata key-value pairs to create or update (merge) | 
 **surveyId** | [**String**](.md)| Unique identifier of the survey | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createAdminSurvey"></a>
# **createAdminSurvey**
> Survey createAdminSurvey(body)

Create a survey

Creates a new survey. Surveys are created in inactive status by default.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let body = new TmiJsClient.SurveyInput(); // SurveyInput | Survey definition to create

apiInstance.createAdminSurvey(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SurveyInput**](SurveyInput.md)| Survey definition to create | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createAdminSurveyMetadata"></a>
# **createAdminSurveyMetadata**
> Metadata createAdminSurveyMetadata(body, surveyId)

Add metadata to a survey

Adds a new metadata key-value pair to the specified survey. Returns 409 Conflict if the key already exists.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let body = new TmiJsClient.Metadata(); // Metadata | Metadata key-value pair to create
let surveyId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey

apiInstance.createAdminSurveyMetadata(body, surveyId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata key-value pair to create | 
 **surveyId** | [**String**](.md)| Unique identifier of the survey | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteAdminSurvey"></a>
# **deleteAdminSurvey**
> deleteAdminSurvey(surveyId)

Delete a survey

Deletes a survey. Surveys with existing responses cannot be deleted.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let surveyId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey

apiInstance.deleteAdminSurvey(surveyId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyId** | [**String**](.md)| Unique identifier of the survey | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteAdminSurveyMetadataByKey"></a>
# **deleteAdminSurveyMetadataByKey**
> deleteAdminSurveyMetadataByKey(surveyId, key)

Delete metadata by key for a survey

Deletes a specific metadata entry by key for the specified survey

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let surveyId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey
let key = "key_example"; // String | Metadata key

apiInstance.deleteAdminSurveyMetadataByKey(surveyId, key).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyId** | [**String**](.md)| Unique identifier of the survey | 
 **key** | **String**| Metadata key | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getAdminSurvey"></a>
# **getAdminSurvey**
> Survey getAdminSurvey(surveyId)

Get a survey

Returns a specific survey by ID.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let surveyId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey

apiInstance.getAdminSurvey(surveyId).then((data) => {
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

<a name="getAdminSurveyMetadata"></a>
# **getAdminSurveyMetadata**
> [Metadata] getAdminSurveyMetadata(surveyId)

Get all metadata for a survey

Returns all metadata key-value pairs for the specified survey

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let surveyId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey

apiInstance.getAdminSurveyMetadata(surveyId).then((data) => {
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

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getAdminSurveyMetadataByKey"></a>
# **getAdminSurveyMetadataByKey**
> Metadata getAdminSurveyMetadataByKey(surveyId, key)

Get metadata by key for a survey

Returns a specific metadata entry by key for the specified survey

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let surveyId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey
let key = "key_example"; // String | Metadata key

apiInstance.getAdminSurveyMetadataByKey(surveyId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyId** | [**String**](.md)| Unique identifier of the survey | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listAdminSurveys"></a>
# **listAdminSurveys**
> ListSurveysResponse listAdminSurveys(opts)

List surveys

Returns a paginated list of all surveys with optional filtering by status.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let opts = { 
  'status': "status_example", // String | Filter by survey status
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0, // Number | Number of results to skip
  'sort': "created_at:desc", // String | Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc)
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results created after this timestamp (ISO 8601)
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results created before this timestamp (ISO 8601)
  'modifiedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results modified after this timestamp (ISO 8601)
  'modifiedBefore': new Date("2013-10-20T19:20:30+01:00") // Date | Filter results modified before this timestamp (ISO 8601)
};
apiInstance.listAdminSurveys(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **String**| Filter by survey status | [optional] 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]
 **sort** | **String**| Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) | [optional] [default to created_at:desc]
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

<a name="patchAdminSurvey"></a>
# **patchAdminSurvey**
> Survey patchAdminSurvey(body, surveyId)

Partially update a survey

Partially updates a survey using JSON Patch (RFC 6902).

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let body = [new TmiJsClient.JsonPatchDocumentInner()]; // [JsonPatchDocumentInner] | JSON Patch operations to apply to the survey
let surveyId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey

apiInstance.patchAdminSurvey(body, surveyId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| JSON Patch operations to apply to the survey | 
 **surveyId** | [**String**](.md)| Unique identifier of the survey | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

<a name="updateAdminSurvey"></a>
# **updateAdminSurvey**
> Survey updateAdminSurvey(body, surveyId)

Update a survey

Fully updates a survey. All fields are replaced.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let body = new TmiJsClient.SurveyInput(); // SurveyInput | Complete survey definition to replace existing
let surveyId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey

apiInstance.updateAdminSurvey(body, surveyId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SurveyInput**](SurveyInput.md)| Complete survey definition to replace existing | 
 **surveyId** | [**String**](.md)| Unique identifier of the survey | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateAdminSurveyMetadataByKey"></a>
# **updateAdminSurveyMetadataByKey**
> Metadata updateAdminSurveyMetadataByKey(body, surveyId, key)

Update metadata by key for a survey

Updates or creates a metadata entry by key for the specified survey

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SurveyAdministrationApi();
let body = new TmiJsClient.Metadata(); // Metadata | Metadata key-value pair to update
let surveyId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Unique identifier of the survey
let key = "key_example"; // String | Metadata key

apiInstance.updateAdminSurveyMetadataByKey(body, surveyId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata key-value pair to update | 
 **surveyId** | [**String**](.md)| Unique identifier of the survey | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

