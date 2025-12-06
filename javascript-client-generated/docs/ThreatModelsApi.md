# TmiJsClient.ThreatModelsApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createThreatModel**](ThreatModelsApi.md#createThreatModel) | **POST** /threat_models | Create a threat model
[**deleteThreatModel**](ThreatModelsApi.md#deleteThreatModel) | **DELETE** /threat_models/{threat_model_id} | Delete a threat model
[**getThreatModel**](ThreatModelsApi.md#getThreatModel) | **GET** /threat_models/{threat_model_id} | Retrieve a threat model
[**listThreatModels**](ThreatModelsApi.md#listThreatModels) | **GET** /threat_models | List threat models
[**patchThreatModel**](ThreatModelsApi.md#patchThreatModel) | **PATCH** /threat_models/{threat_model_id} | Partially update a threat model
[**updateThreatModel**](ThreatModelsApi.md#updateThreatModel) | **PUT** /threat_models/{threat_model_id} | Update a threat model

<a name="createThreatModel"></a>
# **createThreatModel**
> ThreatModel createThreatModel(body)

Create a threat model

Creates a new threat model with the authenticated user as owner

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelsApi();
let body = new TmiJsClient.ThreatModelInput(); // ThreatModelInput | 

apiInstance.createThreatModel(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThreatModelInput**](ThreatModelInput.md)|  | 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteThreatModel"></a>
# **deleteThreatModel**
> deleteThreatModel(threatModelId)

Delete a threat model

Deletes a threat model; restricted to owner role

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelsApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.deleteThreatModel(threatModelId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getThreatModel"></a>
# **getThreatModel**
> ThreatModel getThreatModel(threatModelId)

Retrieve a threat model

Retrieves the full details of a specific threat model if the user has access

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelsApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.getThreatModel(threatModelId).then((data) => {
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

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listThreatModels"></a>
# **listThreatModels**
> [TMListItem] listThreatModels(opts)

List threat models

Returns a list of threat models accessible to the authenticated user with enhanced metadata and entity counts

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelsApi();
let opts = { 
  'limit': 20, // Number | Maximum number of results to return
  'offset': 0, // Number | Number of results to skip
  'owner': "owner_example", // String | Filter by owner name or email
  'name': "name_example", // String | Filter by threat model name (partial match)
  'description': "description_example", // String | Filter by threat model description (partial match)
  'issueUri': "issueUri_example", // String | Filter by issue URI (partial match)
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results created after this timestamp (ISO 8601)
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results created before this timestamp (ISO 8601)
  'modifiedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results modified after this timestamp (ISO 8601)
  'modifiedBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter results modified before this timestamp (ISO 8601)
  'status': "status_example", // String | Filter by status value (exact match). To filter by multiple statuses, use multiple status parameters or comma-separated values.
  'statusUpdatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter threat models where status was updated after this timestamp (RFC3339)
  'statusUpdatedBefore': new Date("2013-10-20T19:20:30+01:00") // Date | Filter threat models where status was updated before this timestamp (RFC3339)
};
apiInstance.listThreatModels(opts).then((data) => {
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
 **owner** | **String**| Filter by owner name or email | [optional] 
 **name** | **String**| Filter by threat model name (partial match) | [optional] 
 **description** | **String**| Filter by threat model description (partial match) | [optional] 
 **issueUri** | **String**| Filter by issue URI (partial match) | [optional] 
 **createdAfter** | **Date**| Filter results created after this timestamp (ISO 8601) | [optional] 
 **createdBefore** | **Date**| Filter results created before this timestamp (ISO 8601) | [optional] 
 **modifiedAfter** | **Date**| Filter results modified after this timestamp (ISO 8601) | [optional] 
 **modifiedBefore** | **Date**| Filter results modified before this timestamp (ISO 8601) | [optional] 
 **status** | **String**| Filter by status value (exact match). To filter by multiple statuses, use multiple status parameters or comma-separated values. | [optional] 
 **statusUpdatedAfter** | **Date**| Filter threat models where status was updated after this timestamp (RFC3339) | [optional] 
 **statusUpdatedBefore** | **Date**| Filter threat models where status was updated before this timestamp (RFC3339) | [optional] 

### Return type

[**[TMListItem]**](TMListItem.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="patchThreatModel"></a>
# **patchThreatModel**
> ThreatModel patchThreatModel(threatModelId, opts)

Partially update a threat model

Applies JSON Patch operations to a threat model; restricted to writer/owner roles

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelsApi();
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier
let opts = { 
  'body': [new TmiJsClient.ThreatModelsThreatModelIdBody()] // [ThreatModelsThreatModelIdBody] | 
};
apiInstance.patchThreatModel(threatModelId, opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Threat model identifier | 
 **body** | [**[ThreatModelsThreatModelIdBody]**](ThreatModelsThreatModelIdBody.md)|  | [optional] 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

<a name="updateThreatModel"></a>
# **updateThreatModel**
> ThreatModel updateThreatModel(body, threatModelId)

Update a threat model

Fully updates a threat model; restricted to writer/owner roles

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ThreatModelsApi();
let body = new TmiJsClient.ThreatModelInput(); // ThreatModelInput | 
let threatModelId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Threat model identifier

apiInstance.updateThreatModel(body, threatModelId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThreatModelInput**](ThreatModelInput.md)|  | 
 **threatModelId** | [**String**](.md)| Threat model identifier | 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

