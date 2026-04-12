# \TeamsAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BulkCreateTeamMetadata**](TeamsAPI.md#BulkCreateTeamMetadata) | **Post** /teams/{team_id}/metadata/bulk | Bulk create team metadata
[**BulkReplaceTeamMetadata**](TeamsAPI.md#BulkReplaceTeamMetadata) | **Put** /teams/{team_id}/metadata/bulk | Bulk replace team metadata
[**BulkUpsertTeamMetadata**](TeamsAPI.md#BulkUpsertTeamMetadata) | **Patch** /teams/{team_id}/metadata/bulk | Bulk upsert team metadata
[**CreateTeam**](TeamsAPI.md#CreateTeam) | **Post** /teams | Create a team
[**CreateTeamMetadata**](TeamsAPI.md#CreateTeamMetadata) | **Post** /teams/{team_id}/metadata | Create team metadata
[**CreateTeamNote**](TeamsAPI.md#CreateTeamNote) | **Post** /teams/{team_id}/notes | Create a new team note
[**DeleteTeam**](TeamsAPI.md#DeleteTeam) | **Delete** /teams/{team_id} | Delete a team
[**DeleteTeamMetadata**](TeamsAPI.md#DeleteTeamMetadata) | **Delete** /teams/{team_id}/metadata/{key} | Delete team metadata
[**DeleteTeamNote**](TeamsAPI.md#DeleteTeamNote) | **Delete** /teams/{team_id}/notes/{team_note_id} | Delete a team note
[**GetTeam**](TeamsAPI.md#GetTeam) | **Get** /teams/{team_id} | Get a team
[**GetTeamMetadata**](TeamsAPI.md#GetTeamMetadata) | **Get** /teams/{team_id}/metadata | Get team metadata
[**GetTeamNote**](TeamsAPI.md#GetTeamNote) | **Get** /teams/{team_id}/notes/{team_note_id} | Get a specific team note
[**ListTeamNotes**](TeamsAPI.md#ListTeamNotes) | **Get** /teams/{team_id}/notes | List notes in a team
[**ListTeams**](TeamsAPI.md#ListTeams) | **Get** /teams | List teams
[**PatchTeam**](TeamsAPI.md#PatchTeam) | **Patch** /teams/{team_id} | Patch a team
[**PatchTeamNote**](TeamsAPI.md#PatchTeamNote) | **Patch** /teams/{team_id}/notes/{team_note_id} | Partially update a team note
[**UpdateTeam**](TeamsAPI.md#UpdateTeam) | **Put** /teams/{team_id} | Update a team
[**UpdateTeamMetadata**](TeamsAPI.md#UpdateTeamMetadata) | **Put** /teams/{team_id}/metadata/{key} | Update team metadata
[**UpdateTeamNote**](TeamsAPI.md#UpdateTeamNote) | **Put** /teams/{team_id}/notes/{team_note_id} | Update a team note



## BulkCreateTeamMetadata

> []Metadata BulkCreateTeamMetadata(ctx, teamId).Metadata(metadata).Execute()

Bulk create team metadata



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team identifier (UUID)
	metadata := []openapiclient.Metadata{*openapiclient.NewMetadata("Key_example", "Value_example")} // []Metadata | Bulk metadata entries to create

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.BulkCreateTeamMetadata(context.Background(), teamId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.BulkCreateTeamMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkCreateTeamMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.BulkCreateTeamMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkCreateTeamMetadataRequest struct via the builder pattern


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


## BulkReplaceTeamMetadata

> []Metadata BulkReplaceTeamMetadata(ctx, teamId).Metadata(metadata).Execute()

Bulk replace team metadata



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team identifier (UUID)
	metadata := []openapiclient.Metadata{*openapiclient.NewMetadata("Key_example", "Value_example")} // []Metadata | Complete set of metadata entries for replacement

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.BulkReplaceTeamMetadata(context.Background(), teamId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.BulkReplaceTeamMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkReplaceTeamMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.BulkReplaceTeamMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkReplaceTeamMetadataRequest struct via the builder pattern


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


## BulkUpsertTeamMetadata

> []Metadata BulkUpsertTeamMetadata(ctx, teamId).BulkPatchRequest(bulkPatchRequest).Execute()

Bulk upsert team metadata



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team identifier (UUID)
	bulkPatchRequest := *openapiclient.NewBulkPatchRequest([]openapiclient.BulkPatchRequestPatchesInner{*openapiclient.NewBulkPatchRequestPatchesInner("Id_example", []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")})}) // BulkPatchRequest | Metadata entries to update

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.BulkUpsertTeamMetadata(context.Background(), teamId).BulkPatchRequest(bulkPatchRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.BulkUpsertTeamMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkUpsertTeamMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.BulkUpsertTeamMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkUpsertTeamMetadataRequest struct via the builder pattern


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


## CreateTeam

> Team CreateTeam(ctx).Body(body).Execute()

Create a team



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
	body := TeamBase({"name":"Platform Engineering","description":"Core platform infrastructure team"}) // TeamBase | Team creation data

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.CreateTeam(context.Background()).Body(body).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.CreateTeam``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateTeam`: Team
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.CreateTeam`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateTeamRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **TeamBase** | Team creation data | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateTeamMetadata

> Metadata CreateTeamMetadata(ctx, teamId).Metadata(metadata).Execute()

Create team metadata



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team identifier (UUID)
	metadata := *openapiclient.NewMetadata("Key_example", "Value_example") // Metadata | Metadata entry to create

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.CreateTeamMetadata(context.Background(), teamId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.CreateTeamMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateTeamMetadata`: Metadata
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.CreateTeamMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateTeamMetadataRequest struct via the builder pattern


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


## CreateTeamNote

> TeamNote CreateTeamNote(ctx, teamId).Body(body).Execute()

Create a new team note



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team UUID
	body := TeamProjectNoteBase({"name":"Security Review Notes","content":"# Security Review\n\nFindings from the quarterly review."}) // TeamProjectNoteBase | Team note creation data

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.CreateTeamNote(context.Background(), teamId).Body(body).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.CreateTeamNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateTeamNote`: TeamNote
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.CreateTeamNote`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team UUID | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateTeamNoteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **body** | **TeamProjectNoteBase** | Team note creation data | 

### Return type

[**TeamNote**](TeamNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteTeam

> DeleteTeam(ctx, teamId).Execute()

Delete a team



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team UUID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TeamsAPI.DeleteTeam(context.Background(), teamId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.DeleteTeam``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team UUID | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteTeamRequest struct via the builder pattern


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


## DeleteTeamMetadata

> DeleteTeamMetadata(ctx, teamId, key).Execute()

Delete team metadata



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team identifier (UUID)
	key := "key_example" // string | Metadata key

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TeamsAPI.DeleteTeamMetadata(context.Background(), teamId, key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.DeleteTeamMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team identifier (UUID) | 
**key** | **string** | Metadata key | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteTeamMetadataRequest struct via the builder pattern


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


## DeleteTeamNote

> DeleteTeamNote(ctx, teamId, teamNoteId).Execute()

Delete a team note



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team UUID
	teamNoteId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team note identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TeamsAPI.DeleteTeamNote(context.Background(), teamId, teamNoteId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.DeleteTeamNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team UUID | 
**teamNoteId** | **string** | Team note identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteTeamNoteRequest struct via the builder pattern


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


## GetTeam

> Team GetTeam(ctx, teamId).Execute()

Get a team



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team UUID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.GetTeam(context.Background(), teamId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.GetTeam``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTeam`: Team
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.GetTeam`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team UUID | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTeamRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTeamMetadata

> []Metadata GetTeamMetadata(ctx, teamId).Execute()

Get team metadata



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team identifier (UUID)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.GetTeamMetadata(context.Background(), teamId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.GetTeamMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTeamMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.GetTeamMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team identifier (UUID) | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTeamMetadataRequest struct via the builder pattern


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


## GetTeamNote

> TeamNote GetTeamNote(ctx, teamId, teamNoteId).Execute()

Get a specific team note



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team UUID
	teamNoteId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team note identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.GetTeamNote(context.Background(), teamId, teamNoteId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.GetTeamNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTeamNote`: TeamNote
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.GetTeamNote`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team UUID | 
**teamNoteId** | **string** | Team note identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTeamNoteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**TeamNote**](TeamNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListTeamNotes

> ListTeamNotesResponse ListTeamNotes(ctx, teamId).Limit(limit).Offset(offset).Execute()

List notes in a team



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team UUID
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.ListTeamNotes(context.Background(), teamId).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.ListTeamNotes``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListTeamNotes`: ListTeamNotesResponse
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.ListTeamNotes`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team UUID | 

### Other Parameters

Other parameters are passed through a pointer to a apiListTeamNotesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListTeamNotesResponse**](ListTeamNotesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListTeams

> ListTeamsResponse ListTeams(ctx).Limit(limit).Offset(offset).Name(name).Status(status).MemberUserId(memberUserId).RelatedTo(relatedTo).Relationship(relationship).Transitive(transitive).Execute()

List teams



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
	name := "name_example" // string | Filter by team name (partial match) (optional)
	status := "status_example" // string | Filter by team lifecycle status (exact match, comma-separated for multiple). Valid values: active, on_hold, winding_down, archived, forming, merging, splitting (optional)
	memberUserId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Filter teams that include this user as a member (optional)
	relatedTo := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Include teams related to this team ID (optional)
	relationship := openapiclient.RelationshipType("parent") // RelationshipType | Filter related teams by relationship type. Only used with related_to. (optional)
	transitive := true // bool | When true with related_to + relationship, follow parent/child chains transitively (max depth 10) (optional) (default to false)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.ListTeams(context.Background()).Limit(limit).Offset(offset).Name(name).Status(status).MemberUserId(memberUserId).RelatedTo(relatedTo).Relationship(relationship).Transitive(transitive).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.ListTeams``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListTeams`: ListTeamsResponse
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.ListTeams`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListTeamsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Maximum number of results per page | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]
 **name** | **string** | Filter by team name (partial match) | 
 **status** | **string** | Filter by team lifecycle status (exact match, comma-separated for multiple). Valid values: active, on_hold, winding_down, archived, forming, merging, splitting | 
 **memberUserId** | **string** | Filter teams that include this user as a member | 
 **relatedTo** | **string** | Include teams related to this team ID | 
 **relationship** | [**RelationshipType**](RelationshipType.md) | Filter related teams by relationship type. Only used with related_to. | 
 **transitive** | **bool** | When true with related_to + relationship, follow parent/child chains transitively (max depth 10) | [default to false]

### Return type

[**ListTeamsResponse**](ListTeamsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchTeam

> Team PatchTeam(ctx, teamId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()

Patch a team



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team UUID
	jsonPatchDocumentInner := []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")} // []JsonPatchDocumentInner | Partial team data for update

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.PatchTeam(context.Background(), teamId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.PatchTeam``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchTeam`: Team
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.PatchTeam`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team UUID | 

### Other Parameters

Other parameters are passed through a pointer to a apiPatchTeamRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **jsonPatchDocumentInner** | [**[]JsonPatchDocumentInner**](JsonPatchDocumentInner.md) | Partial team data for update | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchTeamNote

> TeamNote PatchTeamNote(ctx, teamId, teamNoteId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()

Partially update a team note



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team UUID
	teamNoteId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team note identifier
	jsonPatchDocumentInner := []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")} // []JsonPatchDocumentInner | JSON Patch operations to apply to the team note

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.PatchTeamNote(context.Background(), teamId, teamNoteId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.PatchTeamNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchTeamNote`: TeamNote
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.PatchTeamNote`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team UUID | 
**teamNoteId** | **string** | Team note identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiPatchTeamNoteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **jsonPatchDocumentInner** | [**[]JsonPatchDocumentInner**](JsonPatchDocumentInner.md) | JSON Patch operations to apply to the team note | 

### Return type

[**TeamNote**](TeamNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateTeam

> Team UpdateTeam(ctx, teamId).Body(body).Execute()

Update a team



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team UUID
	body := TeamBase({"name":"Platform Engineering","description":"Core platform infrastructure team - updated"}) // TeamBase | Complete team data for replacement

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.UpdateTeam(context.Background(), teamId).Body(body).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.UpdateTeam``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateTeam`: Team
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.UpdateTeam`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team UUID | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateTeamRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **body** | **TeamBase** | Complete team data for replacement | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateTeamMetadata

> Metadata UpdateTeamMetadata(ctx, teamId, key).Metadata(metadata).Execute()

Update team metadata



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team identifier (UUID)
	key := "key_example" // string | Metadata key
	metadata := *openapiclient.NewMetadata("Key_example", "Value_example") // Metadata | Metadata value to set for the specified key

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.UpdateTeamMetadata(context.Background(), teamId, key).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.UpdateTeamMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateTeamMetadata`: Metadata
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.UpdateTeamMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team identifier (UUID) | 
**key** | **string** | Metadata key | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateTeamMetadataRequest struct via the builder pattern


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


## UpdateTeamNote

> TeamNote UpdateTeamNote(ctx, teamId, teamNoteId).Body(body).Execute()

Update a team note



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
	teamId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team UUID
	teamNoteId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Team note identifier
	body := TeamProjectNoteBase({"name":"Security Review Notes (Updated)","content":"# Security Review\n\nUpdated findings from the quarterly review."}) // TeamProjectNoteBase | Complete team note data for replacement

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TeamsAPI.UpdateTeamNote(context.Background(), teamId, teamNoteId).Body(body).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TeamsAPI.UpdateTeamNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateTeamNote`: TeamNote
	fmt.Fprintf(os.Stdout, "Response from `TeamsAPI.UpdateTeamNote`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**teamId** | **string** | Team UUID | 
**teamNoteId** | **string** | Team note identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateTeamNoteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | **TeamProjectNoteBase** | Complete team note data for replacement | 

### Return type

[**TeamNote**](TeamNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

