# WebhookDeliveriesApi

All URIs are relative to *https://api.tmi.dev*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelWebhookDelivery**](WebhookDeliveriesApi.md#cancelwebhookdelivery) | **DELETE** /webhook-deliveries/{delivery_id} | Cancel a webhook delivery |
| [**getWebhookDeliveryStatus**](WebhookDeliveriesApi.md#getwebhookdeliverystatus) | **GET** /webhook-deliveries/{delivery_id} | Get webhook delivery status |
| [**listMyWebhookDeliveries**](WebhookDeliveriesApi.md#listmywebhookdeliveries) | **GET** /webhook-deliveries | List my webhook deliveries |
| [**updateWebhookDeliveryStatus**](WebhookDeliveriesApi.md#updatewebhookdeliverystatusoperation) | **POST** /webhook-deliveries/{delivery_id}/status | Update webhook delivery status |



## cancelWebhookDelivery

> cancelWebhookDelivery(deliveryId)

Cancel a webhook delivery

Mark a pending or in-progress delivery as cancelled (terminal). Allowed for admins, the subscription owner, the addon invoker, and a client-credentials identity linked to the delivery\&#39;s addon. Addons poll GET /webhook-deliveries/{delivery_id} and abort when they see cancelled; a later POST .../status from the addon returns 409.

### Example

```ts
import {
  Configuration,
  WebhookDeliveriesApi,
} from '@tmi-dev/client';
import type { CancelWebhookDeliveryRequest } from '@tmi-dev/client';

async function example() {
  console.log("🚀 Testing @tmi-dev/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhookDeliveriesApi(config);

  const body = {
    // string | Webhook delivery identifier
    deliveryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CancelWebhookDeliveryRequest;

  try {
    const data = await api.cancelWebhookDelivery(body);
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

### Return type

`void` (Empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content - delivery cancelled |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **409** | Conflict - delivery is already delivered, failed, or cancelled |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **405** | Method Not Allowed - The HTTP method is not supported for this endpoint |  * Allow - List of allowed HTTP methods for this endpoint <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **406** | Not Acceptable - The requested media type is not supported. This API only supports application/json |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **503** | Service Unavailable - A required backend service (authentication, database, or cache) is temporarily unavailable. The client should retry the request after the delay indicated in the Retry-After header. |  * Retry-After - Number of seconds to wait before retrying the request <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getWebhookDeliveryStatus

> WebhookDelivery getWebhookDeliveryStatus(deliveryId, xWebhookSignature)

Get webhook delivery status

Retrieve the status of a webhook delivery. Supports JWT (owner/invoker/admin) or HMAC (webhook receiver) authentication.

### Example

```ts
import {
  Configuration,
  WebhookDeliveriesApi,
} from '@tmi-dev/client';
import type { GetWebhookDeliveryStatusRequest } from '@tmi-dev/client';

async function example() {
  console.log("🚀 Testing @tmi-dev/client SDK...");
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
| **400** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **405** | Method Not Allowed - The HTTP method is not supported for this endpoint |  * Allow - List of allowed HTTP methods for this endpoint <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **406** | Not Acceptable - The requested media type is not supported. This API only supports application/json |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **200** | Webhook delivery status |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **503** | Service Unavailable - A required backend service (authentication, database, or cache) is temporarily unavailable. The client should retry the request after the delay indicated in the Retry-After header. |  * Retry-After - Number of seconds to wait before retrying the request <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listMyWebhookDeliveries

> ListWebhookDeliveriesResponse listMyWebhookDeliveries(offset, limit)

List my webhook deliveries

List deliveries the caller may see: admins see every delivery; other callers see deliveries they invoked, deliveries of subscriptions they own, and (for a client-credentials identity linked to an addon) every delivery of that addon. Newest first.

### Example

```ts
import {
  Configuration,
  WebhookDeliveriesApi,
} from '@tmi-dev/client';
import type { ListMyWebhookDeliveriesRequest } from '@tmi-dev/client';

async function example() {
  console.log("🚀 Testing @tmi-dev/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhookDeliveriesApi(config);

  const body = {
    // number | Number of results to skip (optional)
    offset: 56,
    // number | Maximum number of results to return (optional)
    limit: 56,
  } satisfies ListMyWebhookDeliveriesRequest;

  try {
    const data = await api.listMyWebhookDeliveries(body);
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
| **offset** | `number` | Number of results to skip | [Optional] [Defaults to `0`] |
| **limit** | `number` | Maximum number of results to return | [Optional] [Defaults to `20`] |

### Return type

[**ListWebhookDeliveriesResponse**](ListWebhookDeliveriesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated list of deliveries visible to the caller |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **405** | Method Not Allowed - The HTTP method is not supported for this endpoint |  * Allow - List of allowed HTTP methods for this endpoint <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **406** | Not Acceptable - The requested media type is not supported. This API only supports application/json |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **503** | Service Unavailable - A required backend service (authentication, database, or cache) is temporarily unavailable. The client should retry the request after the delay indicated in the Retry-After header. |  * Retry-After - Number of seconds to wait before retrying the request <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

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
} from '@tmi-dev/client';
import type { UpdateWebhookDeliveryStatusOperationRequest } from '@tmi-dev/client';

async function example() {
  console.log("🚀 Testing @tmi-dev/client SDK...");
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
    updateWebhookDeliveryStatusRequest: {"status":"in_progress","status_percent":50,"status_message":"Processing document chunks"},
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
| **400** | Bad request |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **405** | Method Not Allowed - The HTTP method is not supported for this endpoint |  * Allow - List of allowed HTTP methods for this endpoint <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **406** | Not Acceptable - The requested media type is not supported. This API only supports application/json |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **415** | Unsupported media type - the request Content-Type is not supported for this operation |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **200** | Status updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **409** | Conflict - delivery is already in a terminal state (delivered, failed, or cancelled) |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **503** | Service Unavailable - A required backend service (authentication, database, or cache) is temporarily unavailable. The client should retry the request after the delay indicated in the Retry-After header. |  * Retry-After - Number of seconds to wait before retrying the request <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

