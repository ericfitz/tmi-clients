# \FeedbackAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateUsabilityFeedback**](FeedbackAPI.md#CreateUsabilityFeedback) | **Post** /usability_feedback | Submit usability feedback
[**GetUsabilityFeedback**](FeedbackAPI.md#GetUsabilityFeedback) | **Get** /usability_feedback/{id} | Get a single usability feedback entry (admin)
[**ListUsabilityFeedback**](FeedbackAPI.md#ListUsabilityFeedback) | **Get** /usability_feedback | List usability feedback (admin)



## CreateUsabilityFeedback

> UsabilityFeedback CreateUsabilityFeedback(ctx).UsabilityFeedbackInput(usabilityFeedbackInput).Execute()

Submit usability feedback



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
	usabilityFeedbackInput := *openapiclient.NewUsabilityFeedbackInput("Sentiment_example", "Surface_example", "ClientId_example") // UsabilityFeedbackInput | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FeedbackAPI.CreateUsabilityFeedback(context.Background()).UsabilityFeedbackInput(usabilityFeedbackInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FeedbackAPI.CreateUsabilityFeedback``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateUsabilityFeedback`: UsabilityFeedback
	fmt.Fprintf(os.Stdout, "Response from `FeedbackAPI.CreateUsabilityFeedback`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateUsabilityFeedbackRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usabilityFeedbackInput** | [**UsabilityFeedbackInput**](UsabilityFeedbackInput.md) |  | 

### Return type

[**UsabilityFeedback**](UsabilityFeedback.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetUsabilityFeedback

> UsabilityFeedback GetUsabilityFeedback(ctx, id).Execute()

Get a single usability feedback entry (admin)

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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FeedbackAPI.GetUsabilityFeedback(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FeedbackAPI.GetUsabilityFeedback``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetUsabilityFeedback`: UsabilityFeedback
	fmt.Fprintf(os.Stdout, "Response from `FeedbackAPI.GetUsabilityFeedback`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetUsabilityFeedbackRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**UsabilityFeedback**](UsabilityFeedback.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListUsabilityFeedback

> ListUsabilityFeedback200Response ListUsabilityFeedback(ctx).Limit(limit).Offset(offset).Sentiment(sentiment).ClientId(clientId).Surface(surface).CreatedAfter(createdAfter).CreatedBefore(createdBefore).Execute()

List usability feedback (admin)



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 50)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)
	sentiment := "sentiment_example" // string | Filter by sentiment (optional)
	clientId := "clientId_example" // string |  (optional)
	surface := "surface_example" // string |  (optional)
	createdAfter := time.Now() // time.Time |  (optional)
	createdBefore := time.Now() // time.Time |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FeedbackAPI.ListUsabilityFeedback(context.Background()).Limit(limit).Offset(offset).Sentiment(sentiment).ClientId(clientId).Surface(surface).CreatedAfter(createdAfter).CreatedBefore(createdBefore).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FeedbackAPI.ListUsabilityFeedback``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListUsabilityFeedback`: ListUsabilityFeedback200Response
	fmt.Fprintf(os.Stdout, "Response from `FeedbackAPI.ListUsabilityFeedback`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListUsabilityFeedbackRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Maximum number of results to return | [default to 50]
 **offset** | **int32** | Number of results to skip | [default to 0]
 **sentiment** | **string** | Filter by sentiment | 
 **clientId** | **string** |  | 
 **surface** | **string** |  | 
 **createdAfter** | **time.Time** |  | 
 **createdBefore** | **time.Time** |  | 

### Return type

[**ListUsabilityFeedback200Response**](ListUsabilityFeedback200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

