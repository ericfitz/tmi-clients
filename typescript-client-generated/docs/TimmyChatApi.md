# TimmyChatApi

All URIs are relative to *https://api.tmi.dev*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTimmyChatMessage**](TimmyChatApi.md#createtimmychatmessage) | **POST** /threat_models/{threat_model_id}/chat/sessions/{session_id}/messages | Send a message to Timmy |
| [**createTimmyChatSession**](TimmyChatApi.md#createtimmychatsession) | **POST** /threat_models/{threat_model_id}/chat/sessions | Create a new Timmy chat session |
| [**deleteTimmyChatSession**](TimmyChatApi.md#deletetimmychatsession) | **DELETE** /threat_models/{threat_model_id}/chat/sessions/{session_id} | Delete a Timmy chat session |
| [**getTimmyChatSession**](TimmyChatApi.md#gettimmychatsession) | **GET** /threat_models/{threat_model_id}/chat/sessions/{session_id} | Get a Timmy chat session |
| [**listTimmyChatMessages**](TimmyChatApi.md#listtimmychatmessages) | **GET** /threat_models/{threat_model_id}/chat/sessions/{session_id}/messages | List messages in a Timmy chat session |
| [**listTimmyChatSessions**](TimmyChatApi.md#listtimmychatsessions) | **GET** /threat_models/{threat_model_id}/chat/sessions | List Timmy chat sessions |
| [**refreshTimmySources**](TimmyChatApi.md#refreshtimmysources) | **POST** /threat_models/{threat_model_id}/chat/sessions/{session_id}/refresh_sources | Refresh session sources |



## createTimmyChatMessage

> string createTimmyChatMessage(threatModelId, sessionId, createTimmyMessageRequest)

Send a message to Timmy

Sends a user message to the Timmy AI assistant and returns an SSE stream of the assistant response

### Example

```ts
import {
  Configuration,
  TimmyChatApi,
} from '@tmiclient/client';
import type { CreateTimmyChatMessageRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TimmyChatApi(config);

  const body = {
    // string | Threat model identifier
    threatModelId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Chat session identifier
    sessionId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // CreateTimmyMessageRequest | Message content to send to Timmy
    createTimmyMessageRequest: ...,
  } satisfies CreateTimmyChatMessageRequest;

  try {
    const data = await api.createTimmyChatMessage(body);
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
| **threatModelId** | `string` | Threat model identifier | [Defaults to `undefined`] |
| **sessionId** | `string` | Chat session identifier | [Defaults to `undefined`] |
| **createTimmyMessageRequest** | [CreateTimmyMessageRequest](CreateTimmyMessageRequest.md) | Message content to send to Timmy | |

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `text/event-stream`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SSE stream of the assistant response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createTimmyChatSession

> string createTimmyChatSession(threatModelId, createTimmySessionRequest)

Create a new Timmy chat session

Creates a new AI assistant chat session for the specified threat model. Returns an SSE stream of session creation progress including context loading status.

### Example

```ts
import {
  Configuration,
  TimmyChatApi,
} from '@tmiclient/client';
import type { CreateTimmyChatSessionRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TimmyChatApi(config);

  const body = {
    // string | Threat model identifier
    threatModelId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // CreateTimmySessionRequest | Optional session configuration (optional)
    createTimmySessionRequest: ...,
  } satisfies CreateTimmyChatSessionRequest;

  try {
    const data = await api.createTimmyChatSession(body);
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
| **threatModelId** | `string` | Threat model identifier | [Defaults to `undefined`] |
| **createTimmySessionRequest** | [CreateTimmySessionRequest](CreateTimmySessionRequest.md) | Optional session configuration | [Optional] |

### Return type

**string**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `text/event-stream`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SSE stream of session creation progress |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **503** | Service Unavailable - A required backend service (authentication, database, or cache) is temporarily unavailable. The client should retry the request after the delay indicated in the Retry-After header. |  * Retry-After - Number of seconds to wait before retrying the request <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteTimmyChatSession

> deleteTimmyChatSession(threatModelId, sessionId)

Delete a Timmy chat session

Deletes a specific Timmy chat session and all associated messages

### Example

```ts
import {
  Configuration,
  TimmyChatApi,
} from '@tmiclient/client';
import type { DeleteTimmyChatSessionRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TimmyChatApi(config);

  const body = {
    // string | Threat model identifier
    threatModelId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Chat session identifier
    sessionId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteTimmyChatSessionRequest;

  try {
    const data = await api.deleteTimmyChatSession(body);
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
| **threatModelId** | `string` | Threat model identifier | [Defaults to `undefined`] |
| **sessionId** | `string` | Chat session identifier | [Defaults to `undefined`] |

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
| **204** | Chat session deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getTimmyChatSession

> TimmyChatSession getTimmyChatSession(threatModelId, sessionId)

Get a Timmy chat session

Returns the details of a specific Timmy chat session

### Example

```ts
import {
  Configuration,
  TimmyChatApi,
} from '@tmiclient/client';
import type { GetTimmyChatSessionRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TimmyChatApi(config);

  const body = {
    // string | Threat model identifier
    threatModelId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Chat session identifier
    sessionId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetTimmyChatSessionRequest;

  try {
    const data = await api.getTimmyChatSession(body);
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
| **threatModelId** | `string` | Threat model identifier | [Defaults to `undefined`] |
| **sessionId** | `string` | Chat session identifier | [Defaults to `undefined`] |

### Return type

[**TimmyChatSession**](TimmyChatSession.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Chat session details |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listTimmyChatMessages

> ListTimmyMessagesResponse listTimmyChatMessages(threatModelId, sessionId, limit, offset)

List messages in a Timmy chat session

Returns a paginated list of messages within the specified Timmy chat session

### Example

```ts
import {
  Configuration,
  TimmyChatApi,
} from '@tmiclient/client';
import type { ListTimmyChatMessagesRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TimmyChatApi(config);

  const body = {
    // string | Threat model identifier
    threatModelId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Chat session identifier
    sessionId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Maximum number of results to return (optional)
    limit: 56,
    // number | Number of results to skip (optional)
    offset: 56,
  } satisfies ListTimmyChatMessagesRequest;

  try {
    const data = await api.listTimmyChatMessages(body);
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
| **threatModelId** | `string` | Threat model identifier | [Defaults to `undefined`] |
| **sessionId** | `string` | Chat session identifier | [Defaults to `undefined`] |
| **limit** | `number` | Maximum number of results to return | [Optional] [Defaults to `20`] |
| **offset** | `number` | Number of results to skip | [Optional] [Defaults to `0`] |

### Return type

[**ListTimmyMessagesResponse**](ListTimmyMessagesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated list of chat messages |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listTimmyChatSessions

> ListTimmySessionsResponse listTimmyChatSessions(threatModelId, limit, offset)

List Timmy chat sessions

Returns a paginated list of Timmy chat sessions for the specified threat model

### Example

```ts
import {
  Configuration,
  TimmyChatApi,
} from '@tmiclient/client';
import type { ListTimmyChatSessionsRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TimmyChatApi(config);

  const body = {
    // string | Threat model identifier
    threatModelId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Maximum number of results to return (optional)
    limit: 56,
    // number | Number of results to skip (optional)
    offset: 56,
  } satisfies ListTimmyChatSessionsRequest;

  try {
    const data = await api.listTimmyChatSessions(body);
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
| **threatModelId** | `string` | Threat model identifier | [Defaults to `undefined`] |
| **limit** | `number` | Maximum number of results to return | [Optional] [Defaults to `20`] |
| **offset** | `number` | Number of results to skip | [Optional] [Defaults to `0`] |

### Return type

[**ListTimmySessionsResponse**](ListTimmySessionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated list of chat sessions |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## refreshTimmySources

> RefreshTimmySources200Response refreshTimmySources(threatModelId, sessionId)

Refresh session sources

Re-scans sources for an active Timmy session, picking up any documents whose access status has changed.

### Example

```ts
import {
  Configuration,
  TimmyChatApi,
} from '@tmiclient/client';
import type { RefreshTimmySourcesRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TimmyChatApi(config);

  const body = {
    // string | Threat model identifier
    threatModelId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Chat session identifier
    sessionId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies RefreshTimmySourcesRequest;

  try {
    const data = await api.refreshTimmySources(body);
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
| **threatModelId** | `string` | Threat model identifier | [Defaults to `undefined`] |
| **sessionId** | `string` | Chat session identifier | [Defaults to `undefined`] |

### Return type

[**RefreshTimmySources200Response**](RefreshTimmySources200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sources refreshed |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

