# \CollaborationAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateDiagramCollaborationSession**](CollaborationAPI.md#CreateDiagramCollaborationSession) | **Post** /threat_models/{threat_model_id}/diagrams/{diagram_id}/collaborate | Create diagram collaboration session
[**EndDiagramCollaborationSession**](CollaborationAPI.md#EndDiagramCollaborationSession) | **Delete** /threat_models/{threat_model_id}/diagrams/{diagram_id}/collaborate | End diagram collaboration session
[**GetCurrentUserSessions**](CollaborationAPI.md#GetCurrentUserSessions) | **Get** /me/sessions | List active collaboration sessions
[**GetDiagramCollaborationSession**](CollaborationAPI.md#GetDiagramCollaborationSession) | **Get** /threat_models/{threat_model_id}/diagrams/{diagram_id}/collaborate | Get diagram collaboration session



## CreateDiagramCollaborationSession

> CollaborationSession CreateDiagramCollaborationSession(ctx, threatModelId, diagramId).Execute()

Create diagram collaboration session



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
	threatModelId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Threat model identifier
	diagramId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Diagram identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CollaborationAPI.CreateDiagramCollaborationSession(context.Background(), threatModelId, diagramId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CollaborationAPI.CreateDiagramCollaborationSession``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateDiagramCollaborationSession`: CollaborationSession
	fmt.Fprintf(os.Stdout, "Response from `CollaborationAPI.CreateDiagramCollaborationSession`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**diagramId** | **string** | Diagram identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateDiagramCollaborationSessionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**CollaborationSession**](CollaborationSession.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## EndDiagramCollaborationSession

> EndDiagramCollaborationSession(ctx, threatModelId, diagramId).Execute()

End diagram collaboration session



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
	threatModelId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Threat model identifier
	diagramId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Diagram identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CollaborationAPI.EndDiagramCollaborationSession(context.Background(), threatModelId, diagramId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CollaborationAPI.EndDiagramCollaborationSession``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**diagramId** | **string** | Diagram identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiEndDiagramCollaborationSessionRequest struct via the builder pattern


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


## GetCurrentUserSessions

> map[string]interface{} GetCurrentUserSessions(ctx).Execute()

List active collaboration sessions



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CollaborationAPI.GetCurrentUserSessions(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CollaborationAPI.GetCurrentUserSessions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCurrentUserSessions`: map[string]interface{}
	fmt.Fprintf(os.Stdout, "Response from `CollaborationAPI.GetCurrentUserSessions`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetCurrentUserSessionsRequest struct via the builder pattern


### Return type

**map[string]interface{}**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDiagramCollaborationSession

> CollaborationSession GetDiagramCollaborationSession(ctx, threatModelId, diagramId).Execute()

Get diagram collaboration session



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
	threatModelId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Threat model identifier
	diagramId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Diagram identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CollaborationAPI.GetDiagramCollaborationSession(context.Background(), threatModelId, diagramId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CollaborationAPI.GetDiagramCollaborationSession``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetDiagramCollaborationSession`: CollaborationSession
	fmt.Fprintf(os.Stdout, "Response from `CollaborationAPI.GetDiagramCollaborationSession`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**diagramId** | **string** | Diagram identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDiagramCollaborationSessionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**CollaborationSession**](CollaborationSession.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

