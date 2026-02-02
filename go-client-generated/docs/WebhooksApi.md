# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateWebhookSubscription**](WebhooksApi.md#CreateWebhookSubscription) | **Post** /webhooks/subscriptions | Create webhook subscription
[**DeleteWebhookSubscription**](WebhooksApi.md#DeleteWebhookSubscription) | **Delete** /webhooks/subscriptions/{webhook_id} | Delete webhook subscription
[**GetWebhookDelivery**](WebhooksApi.md#GetWebhookDelivery) | **Get** /webhooks/deliveries/{delivery_id} | Get webhook delivery
[**GetWebhookSubscription**](WebhooksApi.md#GetWebhookSubscription) | **Get** /webhooks/subscriptions/{webhook_id} | Get webhook subscription
[**ListWebhookDeliveries**](WebhooksApi.md#ListWebhookDeliveries) | **Get** /webhooks/deliveries | List webhook deliveries
[**ListWebhookSubscriptions**](WebhooksApi.md#ListWebhookSubscriptions) | **Get** /webhooks/subscriptions | List webhook subscriptions
[**TestWebhookSubscription**](WebhooksApi.md#TestWebhookSubscription) | **Post** /webhooks/subscriptions/{webhook_id}/test | Test webhook subscription

# **CreateWebhookSubscription**
> WebhookSubscription CreateWebhookSubscription(ctx, body)
Create webhook subscription

Create a new webhook subscription. Requires administrator privileges. The subscription will be in pending_verification status until the challenge is completed.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**WebhookSubscriptionInput**](WebhookSubscriptionInput.md)| Webhook subscription configuration | 

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteWebhookSubscription**
> DeleteWebhookSubscription(ctx, webhookId)
Delete webhook subscription

Delete a webhook subscription and all its associated deliveries. Requires administrator privileges.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **webhookId** | [**string**](.md)| Webhook subscription identifier | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetWebhookDelivery**
> WebhookDelivery GetWebhookDelivery(ctx, deliveryId)
Get webhook delivery

Retrieve details of a specific webhook delivery including payload and delivery attempts. Requires administrator privileges.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **deliveryId** | [**string**](.md)| Webhook delivery identifier | 

### Return type

[**WebhookDelivery**](WebhookDelivery.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetWebhookSubscription**
> WebhookSubscription GetWebhookSubscription(ctx, webhookId)
Get webhook subscription

Retrieve details of a specific webhook subscription. Requires administrator privileges.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **webhookId** | [**string**](.md)| Webhook subscription identifier | 

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListWebhookDeliveries**
> ListWebhookDeliveriesResponse ListWebhookDeliveries(ctx, optional)
List webhook deliveries

List webhook deliveries. Requires administrator privileges. Optionally filter by subscription_id.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***WebhooksApiListWebhookDeliveriesOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a WebhooksApiListWebhookDeliveriesOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | [**optional.Interface of string**](.md)| Filter by subscription ID | 
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]

### Return type

[**ListWebhookDeliveriesResponse**](ListWebhookDeliveriesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListWebhookSubscriptions**
> ListWebhookSubscriptionsResponse ListWebhookSubscriptions(ctx, optional)
List webhook subscriptions

List all webhook subscriptions. Requires administrator privileges.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***WebhooksApiListWebhookSubscriptionsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a WebhooksApiListWebhookSubscriptionsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**optional.Interface of string**](.md)| Filter subscriptions by threat model ID | 
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]

### Return type

[**ListWebhookSubscriptionsResponse**](ListWebhookSubscriptionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **TestWebhookSubscription**
> WebhookTestResponse TestWebhookSubscription(ctx, webhookId, optional)
Test webhook subscription

Send a test event to the webhook endpoint. Requires administrator privileges. Returns a delivery ID that can be used to track the test delivery status.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **webhookId** | [**string**](.md)| Webhook subscription identifier | 
 **optional** | ***WebhooksApiTestWebhookSubscriptionOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a WebhooksApiTestWebhookSubscriptionOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **body** | [**optional.Interface of WebhookTestRequest**](WebhookTestRequest.md)| Webhook test request configuration | 

### Return type

[**WebhookTestResponse**](WebhookTestResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

