# \WebhookDeliveriesAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CancelWebhookDelivery**](WebhookDeliveriesAPI.md#CancelWebhookDelivery) | **Delete** /webhook-deliveries/{delivery_id} | Cancel a webhook delivery
[**GetWebhookDeliveryStatus**](WebhookDeliveriesAPI.md#GetWebhookDeliveryStatus) | **Get** /webhook-deliveries/{delivery_id} | Get webhook delivery status
[**ListMyWebhookDeliveries**](WebhookDeliveriesAPI.md#ListMyWebhookDeliveries) | **Get** /webhook-deliveries | List my webhook deliveries
[**UpdateWebhookDeliveryStatus**](WebhookDeliveriesAPI.md#UpdateWebhookDeliveryStatus) | **Post** /webhook-deliveries/{delivery_id}/status | Update webhook delivery status



## CancelWebhookDelivery

> CancelWebhookDelivery(ctx, deliveryId).Execute()

Cancel a webhook delivery



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated/v2_0_0/v2"
)

func main() {
	deliveryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Webhook delivery identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.WebhookDeliveriesAPI.CancelWebhookDelivery(context.Background(), deliveryId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhookDeliveriesAPI.CancelWebhookDelivery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**deliveryId** | **string** | Webhook delivery identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiCancelWebhookDeliveryRequest struct via the builder pattern


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


## GetWebhookDeliveryStatus

> WebhookDelivery GetWebhookDeliveryStatus(ctx, deliveryId).XWebhookSignature(xWebhookSignature).Execute()

Get webhook delivery status



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated/v2_0_0/v2"
)

func main() {
	deliveryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Webhook delivery identifier
	xWebhookSignature := "xWebhookSignature_example" // string | HMAC-SHA256 signature (format: sha256={hex_signature}). Required for HMAC authentication, optional when using JWT. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhookDeliveriesAPI.GetWebhookDeliveryStatus(context.Background(), deliveryId).XWebhookSignature(xWebhookSignature).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhookDeliveriesAPI.GetWebhookDeliveryStatus``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetWebhookDeliveryStatus`: WebhookDelivery
	fmt.Fprintf(os.Stdout, "Response from `WebhookDeliveriesAPI.GetWebhookDeliveryStatus`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**deliveryId** | **string** | Webhook delivery identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetWebhookDeliveryStatusRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xWebhookSignature** | **string** | HMAC-SHA256 signature (format: sha256&#x3D;{hex_signature}). Required for HMAC authentication, optional when using JWT. | 

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


## ListMyWebhookDeliveries

> ListWebhookDeliveriesResponse ListMyWebhookDeliveries(ctx).Offset(offset).Limit(limit).Execute()

List my webhook deliveries



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated/v2_0_0/v2"
)

func main() {
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhookDeliveriesAPI.ListMyWebhookDeliveries(context.Background()).Offset(offset).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhookDeliveriesAPI.ListMyWebhookDeliveries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListMyWebhookDeliveries`: ListWebhookDeliveriesResponse
	fmt.Fprintf(os.Stdout, "Response from `WebhookDeliveriesAPI.ListMyWebhookDeliveries`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListMyWebhookDeliveriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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


## UpdateWebhookDeliveryStatus

> UpdateWebhookDeliveryStatusResponse UpdateWebhookDeliveryStatus(ctx, deliveryId).XWebhookSignature(xWebhookSignature).UpdateWebhookDeliveryStatusRequest(updateWebhookDeliveryStatusRequest).Execute()

Update webhook delivery status



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated/v2_0_0/v2"
)

func main() {
	deliveryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Webhook delivery identifier
	xWebhookSignature := "xWebhookSignature_example" // string | HMAC-SHA256 signature (format: sha256={hex_signature})
	updateWebhookDeliveryStatusRequest := *openapiclient.NewUpdateWebhookDeliveryStatusRequest("in_progress") // UpdateWebhookDeliveryStatusRequest | Webhook delivery status update

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebhookDeliveriesAPI.UpdateWebhookDeliveryStatus(context.Background(), deliveryId).XWebhookSignature(xWebhookSignature).UpdateWebhookDeliveryStatusRequest(updateWebhookDeliveryStatusRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebhookDeliveriesAPI.UpdateWebhookDeliveryStatus``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateWebhookDeliveryStatus`: UpdateWebhookDeliveryStatusResponse
	fmt.Fprintf(os.Stdout, "Response from `WebhookDeliveriesAPI.UpdateWebhookDeliveryStatus`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**deliveryId** | **string** | Webhook delivery identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateWebhookDeliveryStatusRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xWebhookSignature** | **string** | HMAC-SHA256 signature (format: sha256&#x3D;{hex_signature}) | 
 **updateWebhookDeliveryStatusRequest** | [**UpdateWebhookDeliveryStatusRequest**](UpdateWebhookDeliveryStatusRequest.md) | Webhook delivery status update | 

### Return type

[**UpdateWebhookDeliveryStatusResponse**](UpdateWebhookDeliveryStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

