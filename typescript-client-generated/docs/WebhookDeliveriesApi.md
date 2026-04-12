# WebhookDeliveriesApi

All URIs are relative to *https://api.tmi.dev*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getWebhookDeliveryStatus**](WebhookDeliveriesApi.md#getwebhookdeliverystatus) | **GET** /webhook-deliveries/{delivery_id} | Get webhook delivery status |
| [**updateWebhookDeliveryStatus**](WebhookDeliveriesApi.md#updatewebhookdeliverystatusoperation) | **POST** /webhook-deliveries/{delivery_id}/status | Update webhook delivery status |



## getWebhookDeliveryStatus

> WebhookDelivery getWebhookDeliveryStatus(deliveryId, xWebhookSignature)

Get webhook delivery status

Retrieve the status of a webhook delivery. Supports JWT (owner/invoker/admin) or HMAC (webhook receiver) authentication.

### Example

```ts
import {
  Configuration,
  WebhookDeliveriesApi,
} from '@tmiclient/client';
import type { GetWebhookDeliveryStatusRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhookDeliveriesApi(config);

  const body = {
    // string | Webhook delivery identifier
    deliveryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | HMAC-SHA256 signature (format: sha256={hex_signature}). Required for HMAC authentication, optional when using JWT. (optional)
    xWebhookSignature: xWebhookSignature_example,
  } satisfies GetWebhookDeliveryStatusRequest;

  try {
    const data = await api.getWebhookDeliveryStatus(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **deliveryId** | `string` | Webhook delivery identifier | [Defaults to `undefined`] |
| **xWebhookSignature** | `string` | HMAC-SHA256 signature (format: sha256&#x3D;{hex_signature}). Required for HMAC authentication, optional when using JWT. | [Optional] [Defaults to `undefined`] |

### Return type

[**WebhookDelivery**](WebhookDelivery.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook delivery status |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateWebhookDeliveryStatus

> UpdateWebhookDeliveryStatusResponse updateWebhookDeliveryStatus(deliveryId, xWebhookSignature, updateWebhookDeliveryStatusRequest)

Update webhook delivery status

Update the status of a webhook delivery via callback. Requires HMAC signature authentication.

### Example

```ts
import {
  Configuration,
  WebhookDeliveriesApi,
} from '@tmiclient/client';
import type { UpdateWebhookDeliveryStatusOperationRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhookDeliveriesApi(config);

  const body = {
    // string | Webhook delivery identifier
    deliveryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | HMAC-SHA256 signature (format: sha256={hex_signature})
    xWebhookSignature: xWebhookSignature_example,
    // UpdateWebhookDeliveryStatusRequest | Webhook delivery status update
    updateWebhookDeliveryStatusRequest: ...,
  } satisfies UpdateWebhookDeliveryStatusOperationRequest;

  try {
    const data = await api.updateWebhookDeliveryStatus(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **deliveryId** | `string` | Webhook delivery identifier | [Defaults to `undefined`] |
| **xWebhookSignature** | `string` | HMAC-SHA256 signature (format: sha256&#x3D;{hex_signature}) | [Defaults to `undefined`] |
| **updateWebhookDeliveryStatusRequest** | [UpdateWebhookDeliveryStatusRequest](UpdateWebhookDeliveryStatusRequest.md) | Webhook delivery status update | |

### Return type

[**UpdateWebhookDeliveryStatusResponse**](UpdateWebhookDeliveryStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad request |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **409** | Conflict - invalid status transition |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

