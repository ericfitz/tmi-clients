# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BulkCreateProjectMetadata**](ProjectsApi.md#BulkCreateProjectMetadata) | **Post** /projects/{project_id}/metadata/bulk | Bulk create project metadata
[**BulkReplaceProjectMetadata**](ProjectsApi.md#BulkReplaceProjectMetadata) | **Put** /projects/{project_id}/metadata/bulk | Bulk replace project metadata
[**BulkUpsertProjectMetadata**](ProjectsApi.md#BulkUpsertProjectMetadata) | **Patch** /projects/{project_id}/metadata/bulk | Bulk upsert project metadata
[**CreateProject**](ProjectsApi.md#CreateProject) | **Post** /projects | Create a project
[**CreateProjectMetadata**](ProjectsApi.md#CreateProjectMetadata) | **Post** /projects/{project_id}/metadata | Create project metadata
[**DeleteProject**](ProjectsApi.md#DeleteProject) | **Delete** /projects/{project_id} | Delete a project
[**DeleteProjectMetadata**](ProjectsApi.md#DeleteProjectMetadata) | **Delete** /projects/{project_id}/metadata/{key} | Delete project metadata
[**GetProject**](ProjectsApi.md#GetProject) | **Get** /projects/{project_id} | Get a project
[**GetProjectMetadata**](ProjectsApi.md#GetProjectMetadata) | **Get** /projects/{project_id}/metadata | Get project metadata
[**ListProjects**](ProjectsApi.md#ListProjects) | **Get** /projects | List projects
[**PatchProject**](ProjectsApi.md#PatchProject) | **Patch** /projects/{project_id} | Patch a project
[**UpdateProject**](ProjectsApi.md#UpdateProject) | **Put** /projects/{project_id} | Update a project
[**UpdateProjectMetadata**](ProjectsApi.md#UpdateProjectMetadata) | **Put** /projects/{project_id}/metadata/{key} | Update project metadata

# **BulkCreateProjectMetadata**
> []Metadata BulkCreateProjectMetadata(ctx, body, projectId)
Bulk create project metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]Metadata**](Metadata.md)| Bulk metadata entries to create | 
  **projectId** | [**string**](.md)| Project identifier (UUID) | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **BulkReplaceProjectMetadata**
> []Metadata BulkReplaceProjectMetadata(ctx, body, projectId)
Bulk replace project metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]Metadata**](Metadata.md)| Complete set of metadata entries for replacement | 
  **projectId** | [**string**](.md)| Project identifier (UUID) | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **BulkUpsertProjectMetadata**
> []Metadata BulkUpsertProjectMetadata(ctx, body, projectId)
Bulk upsert project metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**BulkPatchRequest**](BulkPatchRequest.md)| Metadata entries to update | 
  **projectId** | [**string**](.md)| Project identifier (UUID) | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateProject**
> Project CreateProject(ctx, body)
Create a project

Creates a new project. Requires membership in the referenced team.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**ProjectBase**](ProjectBase.md)| Project creation data | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateProjectMetadata**
> Metadata CreateProjectMetadata(ctx, body, projectId)
Create project metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**Metadata**](Metadata.md)| Metadata entry to create | 
  **projectId** | [**string**](.md)| Project identifier (UUID) | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteProject**
> DeleteProject(ctx, projectId)
Delete a project

Deletes a project. Requires owner role or admin access. Returns 409 if the project is referenced by threat models.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **projectId** | [**string**](.md)| Project UUID | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteProjectMetadata**
> DeleteProjectMetadata(ctx, projectId, key)
Delete project metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **projectId** | [**string**](.md)| Project identifier (UUID) | 
  **key** | **string**| Metadata key | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetProject**
> Project GetProject(ctx, projectId)
Get a project

Returns a project by ID. Requires membership in the project's team or admin access.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **projectId** | [**string**](.md)| Project UUID | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetProjectMetadata**
> []Metadata GetProjectMetadata(ctx, projectId)
Get project metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **projectId** | [**string**](.md)| Project identifier (UUID) | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListProjects**
> ListProjectsResponse ListProjects(ctx, optional)
List projects

Returns a paginated list of projects. Non-admin users see only projects belonging to teams they are members of.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***ProjectsApiListProjectsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ProjectsApiListProjectsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **optional.Int32**| Maximum number of results per page | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]
 **name** | **optional.String**| Filter by project name (partial match) | 
 **status** | **optional.String**| Filter by status (exact match, comma-separated for multiple) | 
 **teamId** | [**optional.Interface of string**](.md)| Filter by team | 
 **relatedTo** | [**optional.Interface of string**](.md)| Include projects related to this project ID | 
 **relationship** | [**optional.Interface of RelationshipType**](.md)| Filter related projects by relationship type. Only used with related_to. | 
 **transitive** | **optional.Bool**| When true with related_to + relationship, follow parent/child chains transitively (max depth 10) | [default to false]

### Return type

[**ListProjectsResponse**](ListProjectsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PatchProject**
> Project PatchProject(ctx, body, projectId)
Patch a project

Partial update of a project using JSON Patch (RFC 6902). Requires membership in the project's team or admin access.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]JsonPatchDocumentInner**](JsonPatchDocument_inner.md)| Partial project data for update | 
  **projectId** | [**string**](.md)| Project UUID | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateProject**
> Project UpdateProject(ctx, body, projectId)
Update a project

Full replacement update of a project. Requires membership in the project's team or admin access.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**ProjectBase**](ProjectBase.md)| Complete project data for replacement | 
  **projectId** | [**string**](.md)| Project UUID | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateProjectMetadata**
> Metadata UpdateProjectMetadata(ctx, body, projectId, key)
Update project metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**Metadata**](Metadata.md)| Metadata value to set for the specified key | 
  **projectId** | [**string**](.md)| Project identifier (UUID) | 
  **key** | **string**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

