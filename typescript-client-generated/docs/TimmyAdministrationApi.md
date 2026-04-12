# TimmyAdministrationApi

All URIs are relative to *https://api.tmi.dev*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTimmyStatus**](TimmyAdministrationApi.md#gettimmystatus) | **GET** /admin/timmy/status | Get Timmy system status |
| [**getTimmyUsage**](TimmyAdministrationApi.md#gettimmyusage) | **GET** /admin/timmy/usage | Get Timmy usage statistics |



## getTimmyStatus

> TimmyStatusResponse getTimmyStatus()

Get Timmy system status

Returns the current system status of the Timmy AI assistant including memory utilization and session metrics

### Example

```ts
import {
  Configuration,
  TimmyAdministrationApi,
} from '@tmiclient/client';
import type { GetTimmyStatusRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TimmyAdministrationApi(config);

  try {
    const data = await api.getTimmyStatus();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**TimmyStatusResponse**](TimmyStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Timmy system status |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getTimmyUsage

> TimmyUsageResponse getTimmyUsage(userId, threatModelId, startDate, endDate)

Get Timmy usage statistics

Returns usage statistics for the Timmy AI assistant, optionally filtered by user, threat model, or date range

### Example

```ts
import {
  Configuration,
  TimmyAdministrationApi,
} from '@tmiclient/client';
import type { GetTimmyUsageRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TimmyAdministrationApi(config);

  const body = {
    // string | Filter usage by user identifier (optional)
    userId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Filter usage by threat model identifier (optional)
    threatModelId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Filter usage records starting from this date (RFC3339) (optional)
    startDate: 2013-10-20T19:20:30+01:00,
    // Date | Filter usage records up to this date (RFC3339) (optional)
    endDate: 2013-10-20T19:20:30+01:00,
  } satisfies GetTimmyUsageRequest;

  try {
    const data = await api.getTimmyUsage(body);
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
| **userId** | `string` | Filter usage by user identifier | [Optional] [Defaults to `undefined`] |
| **threatModelId** | `string` | Filter usage by threat model identifier | [Optional] [Defaults to `undefined`] |
| **startDate** | `Date` | Filter usage records starting from this date (RFC3339) | [Optional] [Defaults to `undefined`] |
| **endDate** | `Date` | Filter usage records up to this date (RFC3339) | [Optional] [Defaults to `undefined`] |

### Return type

[**TimmyUsageResponse**](TimmyUsageResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Timmy usage statistics |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

