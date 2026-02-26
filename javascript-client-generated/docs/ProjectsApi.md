# TmiJsClient.ProjectsApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkCreateProjectMetadata**](ProjectsApi.md#bulkCreateProjectMetadata) | **POST** /projects/{project_id}/metadata/bulk | Bulk create project metadata
[**bulkReplaceProjectMetadata**](ProjectsApi.md#bulkReplaceProjectMetadata) | **PUT** /projects/{project_id}/metadata/bulk | Bulk replace project metadata
[**bulkUpsertProjectMetadata**](ProjectsApi.md#bulkUpsertProjectMetadata) | **PATCH** /projects/{project_id}/metadata/bulk | Bulk upsert project metadata
[**createProject**](ProjectsApi.md#createProject) | **POST** /projects | Create a project
[**createProjectMetadata**](ProjectsApi.md#createProjectMetadata) | **POST** /projects/{project_id}/metadata | Create project metadata
[**deleteProject**](ProjectsApi.md#deleteProject) | **DELETE** /projects/{project_id} | Delete a project
[**deleteProjectMetadata**](ProjectsApi.md#deleteProjectMetadata) | **DELETE** /projects/{project_id}/metadata/{key} | Delete project metadata
[**getProject**](ProjectsApi.md#getProject) | **GET** /projects/{project_id} | Get a project
[**getProjectMetadata**](ProjectsApi.md#getProjectMetadata) | **GET** /projects/{project_id}/metadata | Get project metadata
[**listProjects**](ProjectsApi.md#listProjects) | **GET** /projects | List projects
[**patchProject**](ProjectsApi.md#patchProject) | **PATCH** /projects/{project_id} | Patch a project
[**updateProject**](ProjectsApi.md#updateProject) | **PUT** /projects/{project_id} | Update a project
[**updateProjectMetadata**](ProjectsApi.md#updateProjectMetadata) | **PUT** /projects/{project_id}/metadata/{key} | Update project metadata

<a name="bulkCreateProjectMetadata"></a>
# **bulkCreateProjectMetadata**
> [Metadata] bulkCreateProjectMetadata(body, projectId)

Bulk create project metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ProjectsApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | Bulk metadata entries to create
let projectId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Project identifier (UUID)

apiInstance.bulkCreateProjectMetadata(body, projectId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)| Bulk metadata entries to create | 
 **projectId** | [**String**](.md)| Project identifier (UUID) | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkReplaceProjectMetadata"></a>
# **bulkReplaceProjectMetadata**
> [Metadata] bulkReplaceProjectMetadata(body, projectId)

Bulk replace project metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ProjectsApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | Complete set of metadata entries for replacement
let projectId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Project identifier (UUID)

apiInstance.bulkReplaceProjectMetadata(body, projectId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)| Complete set of metadata entries for replacement | 
 **projectId** | [**String**](.md)| Project identifier (UUID) | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpsertProjectMetadata"></a>
# **bulkUpsertProjectMetadata**
> [Metadata] bulkUpsertProjectMetadata(body, projectId)

Bulk upsert project metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ProjectsApi();
let body = new TmiJsClient.BulkPatchRequest(); // BulkPatchRequest | Metadata entries to update
let projectId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Project identifier (UUID)

apiInstance.bulkUpsertProjectMetadata(body, projectId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkPatchRequest**](BulkPatchRequest.md)| Metadata entries to update | 
 **projectId** | [**String**](.md)| Project identifier (UUID) | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createProject"></a>
# **createProject**
> Project createProject(body)

Create a project

Creates a new project. Requires membership in the referenced team.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ProjectsApi();
let body = new TmiJsClient.ProjectBase(); // ProjectBase | Project creation data

apiInstance.createProject(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectBase**](ProjectBase.md)| Project creation data | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createProjectMetadata"></a>
# **createProjectMetadata**
> Metadata createProjectMetadata(body, projectId)

Create project metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ProjectsApi();
let body = new TmiJsClient.Metadata(); // Metadata | Metadata entry to create
let projectId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Project identifier (UUID)

apiInstance.createProjectMetadata(body, projectId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata entry to create | 
 **projectId** | [**String**](.md)| Project identifier (UUID) | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteProject"></a>
# **deleteProject**
> deleteProject(projectId)

Delete a project

Deletes a project. Requires owner role or admin access. Returns 409 if the project is referenced by threat models.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ProjectsApi();
let projectId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Project UUID

apiInstance.deleteProject(projectId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | [**String**](.md)| Project UUID | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteProjectMetadata"></a>
# **deleteProjectMetadata**
> deleteProjectMetadata(projectId, key)

Delete project metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ProjectsApi();
let projectId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Project identifier (UUID)
let key = "key_example"; // String | Metadata key

apiInstance.deleteProjectMetadata(projectId, key).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | [**String**](.md)| Project identifier (UUID) | 
 **key** | **String**| Metadata key | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getProject"></a>
# **getProject**
> Project getProject(projectId)

Get a project

Returns a project by ID. Requires membership in the project&#x27;s team or admin access.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ProjectsApi();
let projectId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Project UUID

apiInstance.getProject(projectId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | [**String**](.md)| Project UUID | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getProjectMetadata"></a>
# **getProjectMetadata**
> [Metadata] getProjectMetadata(projectId)

Get project metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ProjectsApi();
let projectId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Project identifier (UUID)

apiInstance.getProjectMetadata(projectId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | [**String**](.md)| Project identifier (UUID) | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listProjects"></a>
# **listProjects**
> ListProjectsResponse listProjects(opts)

List projects

Returns a paginated list of projects. Non-admin users see only projects belonging to teams they are members of.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ProjectsApi();
let opts = { 
  'limit': 20, // Number | Maximum number of results per page
  'offset': 0, // Number | Number of results to skip
  'name': "name_example", // String | Filter by project name (partial match)
  'status': "status_example", // String | Filter by status (exact match, comma-separated for multiple)
  'teamId': "38400000-8cf0-11bd-b23e-10b96e4ef00d", // String | Filter by team
  'relatedTo': "38400000-8cf0-11bd-b23e-10b96e4ef00d", // String | Include projects related to this project ID
  'relationship': new TmiJsClient.RelationshipType(), // RelationshipType | Filter related projects by relationship type. Only used with related_to.
  'transitive': false // Boolean | When true with related_to + relationship, follow parent/child chains transitively (max depth 10)
};
apiInstance.listProjects(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **Number**| Maximum number of results per page | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]
 **name** | **String**| Filter by project name (partial match) | [optional] 
 **status** | **String**| Filter by status (exact match, comma-separated for multiple) | [optional] 
 **teamId** | [**String**](.md)| Filter by team | [optional] 
 **relatedTo** | [**String**](.md)| Include projects related to this project ID | [optional] 
 **relationship** | [**RelationshipType**](.md)| Filter related projects by relationship type. Only used with related_to. | [optional] 
 **transitive** | **Boolean**| When true with related_to + relationship, follow parent/child chains transitively (max depth 10) | [optional] [default to false]

### Return type

[**ListProjectsResponse**](ListProjectsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="patchProject"></a>
# **patchProject**
> Project patchProject(body, projectId)

Patch a project

Partial update of a project using JSON Patch (RFC 6902). Requires membership in the project&#x27;s team or admin access.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ProjectsApi();
let body = [new TmiJsClient.JsonPatchDocumentInner()]; // [JsonPatchDocumentInner] | Partial project data for update
let projectId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Project UUID

apiInstance.patchProject(body, projectId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| Partial project data for update | 
 **projectId** | [**String**](.md)| Project UUID | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

<a name="updateProject"></a>
# **updateProject**
> Project updateProject(body, projectId)

Update a project

Full replacement update of a project. Requires membership in the project&#x27;s team or admin access.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ProjectsApi();
let body = new TmiJsClient.ProjectBase(); // ProjectBase | Complete project data for replacement
let projectId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Project UUID

apiInstance.updateProject(body, projectId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectBase**](ProjectBase.md)| Complete project data for replacement | 
 **projectId** | [**String**](.md)| Project UUID | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateProjectMetadata"></a>
# **updateProjectMetadata**
> Metadata updateProjectMetadata(body, projectId, key)

Update project metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.ProjectsApi();
let body = new TmiJsClient.Metadata(); // Metadata | Metadata value to set for the specified key
let projectId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Project identifier (UUID)
let key = "key_example"; // String | Metadata key

apiInstance.updateProjectMetadata(body, projectId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata value to set for the specified key | 
 **projectId** | [**String**](.md)| Project identifier (UUID) | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

