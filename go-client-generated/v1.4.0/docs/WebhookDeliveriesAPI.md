# \WebhookDeliveriesAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetWebhookDeliveryStatus**](WebhookDeliveriesAPI.md#GetWebhookDeliveryStatus) | **Get** /webhook-deliveries/{delivery_id} | Get webhook delivery status
[**UpdateWebhookDeliveryStatus**](WebhookDeliveriesAPI.md#UpdateWebhookDeliveryStatus) | **Post** /webhook-deliveries/{delivery_id}/status | Update webhook delivery status



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
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
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
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	deliveryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Webhook delivery identifier
	xWebhookSignature := "xWebhookSignature_example" // string | HMAC-SHA256 signature (format: sha256={hex_signature})
	updateWebhookDeliveryStatusRequest := *openapiclient.NewUpdateWebhookDeliveryStatusRequest("Status_example") // UpdateWebhookDeliveryStatusRequest | Webhook delivery status update

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

