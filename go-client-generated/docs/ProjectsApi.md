# \ProjectsAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BulkCreateProjectMetadata**](ProjectsAPI.md#BulkCreateProjectMetadata) | **Post** /projects/{project_id}/metadata/bulk | Bulk create project metadata
[**BulkReplaceProjectMetadata**](ProjectsAPI.md#BulkReplaceProjectMetadata) | **Put** /projects/{project_id}/metadata/bulk | Bulk replace project metadata
[**BulkUpsertProjectMetadata**](ProjectsAPI.md#BulkUpsertProjectMetadata) | **Patch** /projects/{project_id}/metadata/bulk | Bulk upsert project metadata
[**CreateProject**](ProjectsAPI.md#CreateProject) | **Post** /projects | Create a project
[**CreateProjectMetadata**](ProjectsAPI.md#CreateProjectMetadata) | **Post** /projects/{project_id}/metadata | Create project metadata
[**CreateProjectNote**](ProjectsAPI.md#CreateProjectNote) | **Post** /projects/{project_id}/notes | Create a new project note
[**DeleteProject**](ProjectsAPI.md#DeleteProject) | **Delete** /projects/{project_id} | Delete a project
[**DeleteProjectMetadata**](ProjectsAPI.md#DeleteProjectMetadata) | **Delete** /projects/{project_id}/metadata/{key} | Delete project metadata
[**DeleteProjectNote**](ProjectsAPI.md#DeleteProjectNote) | **Delete** /projects/{project_id}/notes/{project_note_id} | Delete a project note
[**GetProject**](ProjectsAPI.md#GetProject) | **Get** /projects/{project_id} | Get a project
[**GetProjectMetadata**](ProjectsAPI.md#GetProjectMetadata) | **Get** /projects/{project_id}/metadata | Get project metadata
[**GetProjectNote**](ProjectsAPI.md#GetProjectNote) | **Get** /projects/{project_id}/notes/{project_note_id} | Get a specific project note
[**ListProjectNotes**](ProjectsAPI.md#ListProjectNotes) | **Get** /projects/{project_id}/notes | List notes in a project
[**ListProjects**](ProjectsAPI.md#ListProjects) | **Get** /projects | List projects
[**PatchProject**](ProjectsAPI.md#PatchProject) | **Patch** /projects/{project_id} | Patch a project
[**PatchProjectNote**](ProjectsAPI.md#PatchProjectNote) | **Patch** /projects/{project_id}/notes/{project_note_id} | Partially update a project note
[**UpdateProject**](ProjectsAPI.md#UpdateProject) | **Put** /projects/{project_id} | Update a project
[**UpdateProjectMetadata**](ProjectsAPI.md#UpdateProjectMetadata) | **Put** /projects/{project_id}/metadata/{key} | Update project metadata
[**UpdateProjectNote**](ProjectsAPI.md#UpdateProjectNote) | **Put** /projects/{project_id}/notes/{project_note_id} | Update a project note



## BulkCreateProjectMetadata

> []Metadata BulkCreateProjectMetadata(ctx, projectId).Metadata(metadata).Execute()

Bulk create project metadata



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project identifier (UUID)
	metadata := []openapiclient.Metadata{*openapiclient.NewMetadata("Key_example", "Value_example")} // []Metadata | Bulk metadata entries to create

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.BulkCreateProjectMetadata(context.Background(), projectId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.BulkCreateProjectMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkCreateProjectMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.BulkCreateProjectMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkCreateProjectMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **metadata** | [**[]Metadata**](Metadata.md) | Bulk metadata entries to create | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BulkReplaceProjectMetadata

> []Metadata BulkReplaceProjectMetadata(ctx, projectId).Metadata(metadata).Execute()

Bulk replace project metadata



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project identifier (UUID)
	metadata := []openapiclient.Metadata{*openapiclient.NewMetadata("Key_example", "Value_example")} // []Metadata | Complete set of metadata entries for replacement

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.BulkReplaceProjectMetadata(context.Background(), projectId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.BulkReplaceProjectMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkReplaceProjectMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.BulkReplaceProjectMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkReplaceProjectMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **metadata** | [**[]Metadata**](Metadata.md) | Complete set of metadata entries for replacement | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BulkUpsertProjectMetadata

> []Metadata BulkUpsertProjectMetadata(ctx, projectId).BulkPatchRequest(bulkPatchRequest).Execute()

Bulk upsert project metadata



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project identifier (UUID)
	bulkPatchRequest := *openapiclient.NewBulkPatchRequest([]openapiclient.BulkPatchRequestPatchesInner{*openapiclient.NewBulkPatchRequestPatchesInner("Id_example", []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")})}) // BulkPatchRequest | Metadata entries to update

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.BulkUpsertProjectMetadata(context.Background(), projectId).BulkPatchRequest(bulkPatchRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.BulkUpsertProjectMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkUpsertProjectMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.BulkUpsertProjectMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkUpsertProjectMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **bulkPatchRequest** | [**BulkPatchRequest**](BulkPatchRequest.md) | Metadata entries to update | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateProject

> Project CreateProject(ctx).Body(body).Execute()

Create a project



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	body := ProjectBase({"name":"API Gateway Modernization","description":"Migrate legacy API gateway to cloud-native architecture","team_id":"550e8400-e29b-41d4-a716-446655440000"}) // ProjectBase | Project creation data

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.CreateProject(context.Background()).Body(body).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.CreateProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateProject`: Project
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.CreateProject`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **ProjectBase** | Project creation data | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateProjectMetadata

> Metadata CreateProjectMetadata(ctx, projectId).Metadata(metadata).Execute()

Create project metadata



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project identifier (UUID)
	metadata := *openapiclient.NewMetadata("Key_example", "Value_example") // Metadata | Metadata entry to create

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.CreateProjectMetadata(context.Background(), projectId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.CreateProjectMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateProjectMetadata`: Metadata
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.CreateProjectMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateProjectMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **metadata** | [**Metadata**](Metadata.md) | Metadata entry to create | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateProjectNote

> ProjectNote CreateProjectNote(ctx, projectId).Body(body).Execute()

Create a new project note



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project UUID
	body := TeamProjectNoteBase({"name":"Architecture Decision Record","content":"# ADR: Authentication Redesign\n\nContext and decision details."}) // TeamProjectNoteBase | Project note creation data

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.CreateProjectNote(context.Background(), projectId).Body(body).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.CreateProjectNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateProjectNote`: ProjectNote
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.CreateProjectNote`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project UUID | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateProjectNoteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **body** | **TeamProjectNoteBase** | Project note creation data | 

### Return type

[**ProjectNote**](ProjectNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteProject

> DeleteProject(ctx, projectId).Execute()

Delete a project



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project UUID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ProjectsAPI.DeleteProject(context.Background(), projectId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.DeleteProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project UUID | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteProjectMetadata

> DeleteProjectMetadata(ctx, projectId, key).Execute()

Delete project metadata



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project identifier (UUID)
	key := "key_example" // string | Metadata key

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ProjectsAPI.DeleteProjectMetadata(context.Background(), projectId, key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.DeleteProjectMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project identifier (UUID) | 
**key** | **string** | Metadata key | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteProjectMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteProjectNote

> DeleteProjectNote(ctx, projectId, projectNoteId).Execute()

Delete a project note



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project UUID
	projectNoteId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project note identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ProjectsAPI.DeleteProjectNote(context.Background(), projectId, projectNoteId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.DeleteProjectNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project UUID | 
**projectNoteId** | **string** | Project note identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteProjectNoteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProject

> Project GetProject(ctx, projectId).Execute()

Get a project



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project UUID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.GetProject(context.Background(), projectId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.GetProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetProject`: Project
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.GetProject`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project UUID | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProjectMetadata

> []Metadata GetProjectMetadata(ctx, projectId).Execute()

Get project metadata



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project identifier (UUID)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.GetProjectMetadata(context.Background(), projectId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.GetProjectMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetProjectMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.GetProjectMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetProjectMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProjectNote

> ProjectNote GetProjectNote(ctx, projectId, projectNoteId).Execute()

Get a specific project note



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project UUID
	projectNoteId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project note identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.GetProjectNote(context.Background(), projectId, projectNoteId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.GetProjectNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetProjectNote`: ProjectNote
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.GetProjectNote`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project UUID | 
**projectNoteId** | **string** | Project note identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetProjectNoteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**ProjectNote**](ProjectNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListProjectNotes

> ListProjectNotesResponse ListProjectNotes(ctx, projectId).Limit(limit).Offset(offset).Execute()

List notes in a project



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project UUID
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.ListProjectNotes(context.Background(), projectId).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.ListProjectNotes``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListProjectNotes`: ListProjectNotesResponse
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.ListProjectNotes`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project UUID | 

### Other Parameters

Other parameters are passed through a pointer to a apiListProjectNotesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListProjectNotesResponse**](ListProjectNotesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListProjects

> ListProjectsResponse ListProjects(ctx).Limit(limit).Offset(offset).Name(name).Status(status).TeamId(teamId).RelatedTo(relatedTo).Relationship(relationship).Transitive(transitive).Execute()

List projects



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	limit := int32(56) // int32 | Maximum number of results per page (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)
	name := "name_example" // string | Filter by project name (partial match) (optional)
	status := "status_example" // string | Filter by status (exact match, comma-separated for multiple) (optional)
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Filter by team (optional)
	relatedTo := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Include projects related to this project ID (optional)
	relationship := openapiclient.RelationshipType("parent") // RelationshipType | Filter related projects by relationship type. Only used with related_to. (optional)
	transitive := true // bool | When true with related_to + relationship, follow parent/child chains transitively (max depth 10) (optional) (default to false)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.ListProjects(context.Background()).Limit(limit).Offset(offset).Name(name).Status(status).TeamId(teamId).RelatedTo(relatedTo).Relationship(relationship).Transitive(transitive).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.ListProjects``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListProjects`: ListProjectsResponse
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.ListProjects`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListProjectsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Maximum number of results per page | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]
 **name** | **string** | Filter by project name (partial match) | 
 **status** | **string** | Filter by status (exact match, comma-separated for multiple) | 
 **teamId** | **string** | Filter by team | 
 **relatedTo** | **string** | Include projects related to this project ID | 
 **relationship** | [**RelationshipType**](RelationshipType.md) | Filter related projects by relationship type. Only used with related_to. | 
 **transitive** | **bool** | When true with related_to + relationship, follow parent/child chains transitively (max depth 10) | [default to false]

### Return type

[**ListProjectsResponse**](ListProjectsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchProject

> Project PatchProject(ctx, projectId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()

Patch a project



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project UUID
	jsonPatchDocumentInner := []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")} // []JsonPatchDocumentInner | Partial project data for update

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.PatchProject(context.Background(), projectId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.PatchProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchProject`: Project
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.PatchProject`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project UUID | 

### Other Parameters

Other parameters are passed through a pointer to a apiPatchProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **jsonPatchDocumentInner** | [**[]JsonPatchDocumentInner**](JsonPatchDocumentInner.md) | Partial project data for update | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchProjectNote

> ProjectNote PatchProjectNote(ctx, projectId, projectNoteId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()

Partially update a project note



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project UUID
	projectNoteId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project note identifier
	jsonPatchDocumentInner := []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")} // []JsonPatchDocumentInner | JSON Patch operations to apply to the project note

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.PatchProjectNote(context.Background(), projectId, projectNoteId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.PatchProjectNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchProjectNote`: ProjectNote
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.PatchProjectNote`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project UUID | 
**projectNoteId** | **string** | Project note identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiPatchProjectNoteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **jsonPatchDocumentInner** | [**[]JsonPatchDocumentInner**](JsonPatchDocumentInner.md) | JSON Patch operations to apply to the project note | 

### Return type

[**ProjectNote**](ProjectNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateProject

> Project UpdateProject(ctx, projectId).Body(body).Execute()

Update a project



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project UUID
	body := ProjectBase({"name":"API Gateway Modernization","description":"Updated project description","team_id":"550e8400-e29b-41d4-a716-446655440000"}) // ProjectBase | Complete project data for replacement

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.UpdateProject(context.Background(), projectId).Body(body).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.UpdateProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateProject`: Project
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.UpdateProject`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project UUID | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **body** | **ProjectBase** | Complete project data for replacement | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateProjectMetadata

> Metadata UpdateProjectMetadata(ctx, projectId, key).Metadata(metadata).Execute()

Update project metadata



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project identifier (UUID)
	key := "key_example" // string | Metadata key
	metadata := *openapiclient.NewMetadata("Key_example", "Value_example") // Metadata | Metadata value to set for the specified key

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.UpdateProjectMetadata(context.Background(), projectId, key).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.UpdateProjectMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateProjectMetadata`: Metadata
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.UpdateProjectMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project identifier (UUID) | 
**key** | **string** | Metadata key | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateProjectMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **metadata** | [**Metadata**](Metadata.md) | Metadata value to set for the specified key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateProjectNote

> ProjectNote UpdateProjectNote(ctx, projectId, projectNoteId).Body(body).Execute()

Update a project note



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project UUID
	projectNoteId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Project note identifier
	body := TeamProjectNoteBase({"name":"Architecture Decision Record (Updated)","content":"# ADR: Authentication Redesign\n\nUpdated context and decision details."}) // TeamProjectNoteBase | Complete project note data for replacement

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.UpdateProjectNote(context.Background(), projectId, projectNoteId).Body(body).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.UpdateProjectNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateProjectNote`: ProjectNote
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.UpdateProjectNote`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** | Project UUID | 
**projectNoteId** | **string** | Project note identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateProjectNoteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | **TeamProjectNoteBase** | Complete project note data for replacement | 

### Return type

[**ProjectNote**](ProjectNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

