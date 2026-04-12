# \TimmyChatAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateTimmyChatMessage**](TimmyChatAPI.md#CreateTimmyChatMessage) | **Post** /threat_models/{threat_model_id}/chat/sessions/{session_id}/messages | Send a message to Timmy
[**CreateTimmyChatSession**](TimmyChatAPI.md#CreateTimmyChatSession) | **Post** /threat_models/{threat_model_id}/chat/sessions | Create a new Timmy chat session
[**DeleteTimmyChatSession**](TimmyChatAPI.md#DeleteTimmyChatSession) | **Delete** /threat_models/{threat_model_id}/chat/sessions/{session_id} | Delete a Timmy chat session
[**GetTimmyChatSession**](TimmyChatAPI.md#GetTimmyChatSession) | **Get** /threat_models/{threat_model_id}/chat/sessions/{session_id} | Get a Timmy chat session
[**ListTimmyChatMessages**](TimmyChatAPI.md#ListTimmyChatMessages) | **Get** /threat_models/{threat_model_id}/chat/sessions/{session_id}/messages | List messages in a Timmy chat session
[**ListTimmyChatSessions**](TimmyChatAPI.md#ListTimmyChatSessions) | **Get** /threat_models/{threat_model_id}/chat/sessions | List Timmy chat sessions
[**RefreshTimmySources**](TimmyChatAPI.md#RefreshTimmySources) | **Post** /threat_models/{threat_model_id}/chat/sessions/{session_id}/refresh_sources | Refresh session sources



## CreateTimmyChatMessage

> string CreateTimmyChatMessage(ctx, threatModelId, sessionId).CreateTimmyMessageRequest(createTimmyMessageRequest).Execute()

Send a message to Timmy



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
	sessionId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Chat session identifier
	createTimmyMessageRequest := *openapiclient.NewCreateTimmyMessageRequest("Content_example") // CreateTimmyMessageRequest | Message content to send to Timmy

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TimmyChatAPI.CreateTimmyChatMessage(context.Background(), threatModelId, sessionId).CreateTimmyMessageRequest(createTimmyMessageRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TimmyChatAPI.CreateTimmyChatMessage``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateTimmyChatMessage`: string
	fmt.Fprintf(os.Stdout, "Response from `TimmyChatAPI.CreateTimmyChatMessage`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**sessionId** | **string** | Chat session identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateTimmyChatMessageRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **createTimmyMessageRequest** | [**CreateTimmyMessageRequest**](CreateTimmyMessageRequest.md) | Message content to send to Timmy | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/event-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateTimmyChatSession

> string CreateTimmyChatSession(ctx, threatModelId).CreateTimmySessionRequest(createTimmySessionRequest).Execute()

Create a new Timmy chat session



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
	createTimmySessionRequest := *openapiclient.NewCreateTimmySessionRequest() // CreateTimmySessionRequest | Optional session configuration (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TimmyChatAPI.CreateTimmyChatSession(context.Background(), threatModelId).CreateTimmySessionRequest(createTimmySessionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TimmyChatAPI.CreateTimmyChatSession``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateTimmyChatSession`: string
	fmt.Fprintf(os.Stdout, "Response from `TimmyChatAPI.CreateTimmyChatSession`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateTimmyChatSessionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **createTimmySessionRequest** | [**CreateTimmySessionRequest**](CreateTimmySessionRequest.md) | Optional session configuration | 

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/event-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteTimmyChatSession

> DeleteTimmyChatSession(ctx, threatModelId, sessionId).Execute()

Delete a Timmy chat session



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
	sessionId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Chat session identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TimmyChatAPI.DeleteTimmyChatSession(context.Background(), threatModelId, sessionId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TimmyChatAPI.DeleteTimmyChatSession``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**sessionId** | **string** | Chat session identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteTimmyChatSessionRequest struct via the builder pattern


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


## GetTimmyChatSession

> TimmyChatSession GetTimmyChatSession(ctx, threatModelId, sessionId).Execute()

Get a Timmy chat session



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
	sessionId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Chat session identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TimmyChatAPI.GetTimmyChatSession(context.Background(), threatModelId, sessionId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TimmyChatAPI.GetTimmyChatSession``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTimmyChatSession`: TimmyChatSession
	fmt.Fprintf(os.Stdout, "Response from `TimmyChatAPI.GetTimmyChatSession`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**sessionId** | **string** | Chat session identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTimmyChatSessionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**TimmyChatSession**](TimmyChatSession.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListTimmyChatMessages

> ListTimmyMessagesResponse ListTimmyChatMessages(ctx, threatModelId, sessionId).Limit(limit).Offset(offset).Execute()

List messages in a Timmy chat session



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
	sessionId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Chat session identifier
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TimmyChatAPI.ListTimmyChatMessages(context.Background(), threatModelId, sessionId).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TimmyChatAPI.ListTimmyChatMessages``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListTimmyChatMessages`: ListTimmyMessagesResponse
	fmt.Fprintf(os.Stdout, "Response from `TimmyChatAPI.ListTimmyChatMessages`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**sessionId** | **string** | Chat session identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiListTimmyChatMessagesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListTimmyMessagesResponse**](ListTimmyMessagesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListTimmyChatSessions

> ListTimmySessionsResponse ListTimmyChatSessions(ctx, threatModelId).Limit(limit).Offset(offset).Execute()

List Timmy chat sessions



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
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TimmyChatAPI.ListTimmyChatSessions(context.Background(), threatModelId).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TimmyChatAPI.ListTimmyChatSessions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListTimmyChatSessions`: ListTimmySessionsResponse
	fmt.Fprintf(os.Stdout, "Response from `TimmyChatAPI.ListTimmyChatSessions`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiListTimmyChatSessionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListTimmySessionsResponse**](ListTimmySessionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RefreshTimmySources

> RefreshTimmySources200Response RefreshTimmySources(ctx, threatModelId, sessionId).Execute()

Refresh session sources



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
	sessionId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Chat session identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TimmyChatAPI.RefreshTimmySources(context.Background(), threatModelId, sessionId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TimmyChatAPI.RefreshTimmySources``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RefreshTimmySources`: RefreshTimmySources200Response
	fmt.Fprintf(os.Stdout, "Response from `TimmyChatAPI.RefreshTimmySources`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**sessionId** | **string** | Chat session identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiRefreshTimmySourcesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**RefreshTimmySources200Response**](RefreshTimmySources200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

