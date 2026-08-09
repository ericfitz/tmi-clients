# \WebhooksAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateWebhookSubscription**](WebhooksAPI.md#CreateWebhookSubscription) | **Post** /admin/webhooks/subscriptions | Create webhook subscription
[**DeleteWebhookSubscription**](WebhooksAPI.md#DeleteWebhookSubscription) | **Delete** /admin/webhooks/subscriptions/{webhook_id} | Delete webhook subscription
[**GetWebhookDelivery**](WebhooksAPI.md#GetWebhookDelivery) | **Get** /admin/webhooks/deliveries/{delivery_id} | Get webhook delivery
[**GetWebhookSubscription**](WebhooksAPI.md#GetWebhookSubscription) | **Get** /admin/webhooks/subscriptions/{webhook_id} | Get webhook subscription
[**ListWebhookDeliveries**](WebhooksAPI.md#ListWebhookDeliveries) | **Get** /admin/webhooks/deliveries | List webhook deliveries
[**ListWebhookSubscriptions**](WebhooksAPI.md#ListWebhookSubscriptions) | **Get** /admin/webhooks/subscriptions | List webhook subscriptions
[**TestWebhookSubscription**](WebhooksAPI.md#TestWebhookSubscription) | **Post** /admin/webhooks/subscriptions/{webhook_id}/test | Test webhook subscription



## CreateWebhookSubscription

> WebhookSubscription CreateWebhookSubscription(ctx).WebhookSubscriptionInput(webhookSubscriptionInput).Execute()

Create webhook subscription



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
	webhookSubscriptionInput := *openapiclient.NewWebhookSubscriptionInput("Name_example", "Url_example", []string{"Events_example"}) // WebhookSubscriptionInput | Webhook subscription configuration

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhooksAPI.CreateWebhookSubscription(context.Background()).WebhookSubscriptionInput(webhookSubscriptionInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhooksAPI.CreateWebhookSubscription``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateWebhookSubscription`: WebhookSubscription
	fmt.Fprintf(os.Stdout, "Response from `WebhooksAPI.CreateWebhookSubscription`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateWebhookSubscriptionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhookSubscriptionInput** | [**WebhookSubscriptionInput**](WebhookSubscriptionInput.md) | Webhook subscription configuration | 

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteWebhookSubscription

> DeleteWebhookSubscription(ctx, webhookId).Execute()

Delete webhook subscription



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
	webhookId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Webhook subscription identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.WebhooksAPI.DeleteWebhookSubscription(context.Background(), webhookId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhooksAPI.DeleteWebhookSubscription``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**webhookId** | **string** | Webhook subscription identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteWebhookSubscriptionRequest struct via the builder pattern


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


## GetWebhookDelivery

> WebhookDelivery GetWebhookDelivery(ctx, deliveryId).Execute()

Get webhook delivery



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
	deliveryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Webhook delivery identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhooksAPI.GetWebhookDelivery(context.Background(), deliveryId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhooksAPI.GetWebhookDelivery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetWebhookDelivery`: WebhookDelivery
	fmt.Fprintf(os.Stdout, "Response from `WebhooksAPI.GetWebhookDelivery`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**deliveryId** | **string** | Webhook delivery identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetWebhookDeliveryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**WebhookDelivery**](WebhookDelivery.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetWebhookSubscription

> WebhookSubscription GetWebhookSubscription(ctx, webhookId).Execute()

Get webhook subscription



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
	webhookId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Webhook subscription identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhooksAPI.GetWebhookSubscription(context.Background(), webhookId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhooksAPI.GetWebhookSubscription``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetWebhookSubscription`: WebhookSubscription
	fmt.Fprintf(os.Stdout, "Response from `WebhooksAPI.GetWebhookSubscription`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**webhookId** | **string** | Webhook subscription identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetWebhookSubscriptionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListWebhookDeliveries

> ListWebhookDeliveriesResponse ListWebhookDeliveries(ctx).SubscriptionId(subscriptionId).Offset(offset).Limit(limit).Execute()

List webhook deliveries



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
	subscriptionId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Filter by subscription ID (optional)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhooksAPI.ListWebhookDeliveries(context.Background()).SubscriptionId(subscriptionId).Offset(offset).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhooksAPI.ListWebhookDeliveries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListWebhookDeliveries`: ListWebhookDeliveriesResponse
	fmt.Fprintf(os.Stdout, "Response from `WebhooksAPI.ListWebhookDeliveries`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListWebhookDeliveriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **string** | Filter by subscription ID | 
 **offset** | **int32** | Number of results to skip | [default to 0]
 **limit** | **int32** | Maximum number of results to return | [default to 20]

### Return type

[**ListWebhookDeliveriesResponse**](ListWebhookDeliveriesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListWebhookSubscriptions

> ListWebhookSubscriptionsResponse ListWebhookSubscriptions(ctx).ThreatModelId(threatModelId).Offset(offset).Limit(limit).Execute()

List webhook subscriptions



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
	threatModelId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Filter subscriptions by threat model ID (optional)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhooksAPI.ListWebhookSubscriptions(context.Background()).ThreatModelId(threatModelId).Offset(offset).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhooksAPI.ListWebhookSubscriptions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListWebhookSubscriptions`: ListWebhookSubscriptionsResponse
	fmt.Fprintf(os.Stdout, "Response from `WebhooksAPI.ListWebhookSubscriptions`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListWebhookSubscriptionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | **string** | Filter subscriptions by threat model ID | 
 **offset** | **int32** | Number of results to skip | [default to 0]
 **limit** | **int32** | Maximum number of results to return | [default to 20]

### Return type

[**ListWebhookSubscriptionsResponse**](ListWebhookSubscriptionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TestWebhookSubscription

> WebhookTestResponse TestWebhookSubscription(ctx, webhookId).WebhookTestRequest(webhookTestRequest).Execute()

Test webhook subscription



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
	webhookId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Webhook subscription identifier
	webhookTestRequest := *openapiclient.NewWebhookTestRequest() // WebhookTestRequest | Webhook test request configuration (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhooksAPI.TestWebhookSubscription(context.Background(), webhookId).WebhookTestRequest(webhookTestRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhooksAPI.TestWebhookSubscription``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TestWebhookSubscription`: WebhookTestResponse
	fmt.Fprintf(os.Stdout, "Response from `WebhooksAPI.TestWebhookSubscription`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**webhookId** | **string** | Webhook subscription identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiTestWebhookSubscriptionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **webhookTestRequest** | [**WebhookTestRequest**](WebhookTestRequest.md) | Webhook test request configuration | 

### Return type

[**WebhookTestResponse**](WebhookTestResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

