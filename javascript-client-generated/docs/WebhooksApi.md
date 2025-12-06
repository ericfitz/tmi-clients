# TmiJsClient.WebhooksApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWebhookSubscription**](WebhooksApi.md#createWebhookSubscription) | **POST** /webhooks/subscriptions | Create webhook subscription
[**deleteWebhookSubscription**](WebhooksApi.md#deleteWebhookSubscription) | **DELETE** /webhooks/subscriptions/{webhook_id} | Delete webhook subscription
[**getWebhookDelivery**](WebhooksApi.md#getWebhookDelivery) | **GET** /webhooks/deliveries/{delivery_id} | Get webhook delivery
[**getWebhookSubscription**](WebhooksApi.md#getWebhookSubscription) | **GET** /webhooks/subscriptions/{webhook_id} | Get webhook subscription
[**listWebhookDeliveries**](WebhooksApi.md#listWebhookDeliveries) | **GET** /webhooks/deliveries | List webhook deliveries
[**listWebhookSubscriptions**](WebhooksApi.md#listWebhookSubscriptions) | **GET** /webhooks/subscriptions | List webhook subscriptions
[**testWebhookSubscription**](WebhooksApi.md#testWebhookSubscription) | **POST** /webhooks/subscriptions/{webhook_id}/test | Test webhook subscription

<a name="createWebhookSubscription"></a>
# **createWebhookSubscription**
> WebhookSubscription createWebhookSubscription(body)

Create webhook subscription

Create a new webhook subscription. The subscription will be in pending_verification status until the challenge is completed.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.WebhooksApi();
let body = new TmiJsClient.WebhookSubscriptionInput(); // WebhookSubscriptionInput | 

apiInstance.createWebhookSubscription(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookSubscriptionInput**](WebhookSubscriptionInput.md)|  | 

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteWebhookSubscription"></a>
# **deleteWebhookSubscription**
> deleteWebhookSubscription(webhookId)

Delete webhook subscription

Delete a webhook subscription. Only the owner can delete a subscription.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.WebhooksApi();
let webhookId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Webhook subscription identifier

apiInstance.deleteWebhookSubscription(webhookId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhookId** | [**String**](.md)| Webhook subscription identifier | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getWebhookDelivery"></a>
# **getWebhookDelivery**
> WebhookDelivery getWebhookDelivery(deliveryId)

Get webhook delivery

Get details of a specific webhook delivery

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.WebhooksApi();
let deliveryId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Webhook delivery identifier

apiInstance.getWebhookDelivery(deliveryId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deliveryId** | [**String**](.md)| Webhook delivery identifier | 

### Return type

[**WebhookDelivery**](WebhookDelivery.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getWebhookSubscription"></a>
# **getWebhookSubscription**
> WebhookSubscription getWebhookSubscription(webhookId)

Get webhook subscription

Get a specific webhook subscription by ID

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.WebhooksApi();
let webhookId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Webhook subscription identifier

apiInstance.getWebhookSubscription(webhookId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhookId** | [**String**](.md)| Webhook subscription identifier | 

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listWebhookDeliveries"></a>
# **listWebhookDeliveries**
> [WebhookDelivery] listWebhookDeliveries(opts)

List webhook deliveries

List webhook deliveries for the authenticated user&#x27;s subscriptions

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.WebhooksApi();
let opts = { 
  'subscriptionId': "38400000-8cf0-11bd-b23e-10b96e4ef00d", // String | Filter by subscription ID
  'offset': 0, // Number | Number of results to skip
  'limit': 20 // Number | Maximum number of results to return
};
apiInstance.listWebhookDeliveries(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | [**String**](.md)| Filter by subscription ID | [optional] 
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]

### Return type

[**[WebhookDelivery]**](WebhookDelivery.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listWebhookSubscriptions"></a>
# **listWebhookSubscriptions**
> [WebhookSubscription] listWebhookSubscriptions(opts)

List webhook subscriptions

List all webhook subscriptions owned by the authenticated user. Optionally filter by threat_model_id.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.WebhooksApi();
let opts = { 
  'threatModelId': "38400000-8cf0-11bd-b23e-10b96e4ef00d", // String | Filter subscriptions by threat model ID
  'offset': 0, // Number | Number of results to skip
  'limit': 20 // Number | Maximum number of results to return
};
apiInstance.listWebhookSubscriptions(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelId** | [**String**](.md)| Filter subscriptions by threat model ID | [optional] 
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 20]

### Return type

[**[WebhookSubscription]**](WebhookSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="testWebhookSubscription"></a>
# **testWebhookSubscription**
> WebhookTestResponse testWebhookSubscription(webhookId, opts)

Test webhook subscription

Send a test event to the webhook URL to verify it&#x27;s working correctly

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.WebhooksApi();
let webhookId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Webhook subscription identifier
let opts = { 
  'body': new TmiJsClient.WebhookTestRequest() // WebhookTestRequest | 
};
apiInstance.testWebhookSubscription(webhookId, opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhookId** | [**String**](.md)| Webhook subscription identifier | 
 **body** | [**WebhookTestRequest**](WebhookTestRequest.md)|  | [optional] 

### Return type

[**WebhookTestResponse**](WebhookTestResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

