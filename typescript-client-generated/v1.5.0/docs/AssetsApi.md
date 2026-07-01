# AssetsApi

All URIs are relative to *https://api.tmi.dev*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**patchThreatModelAsset**](AssetsApi.md#patchthreatmodelasset) | **PATCH** /threat_models/{threat_model_id}/assets/{asset_id} | Partially update asset |



## patchThreatModelAsset

> Asset patchThreatModelAsset(threatModelId, assetId, jsonPatchDocumentInner, ifMatch)

Partially update asset

Apply JSON Patch operations to partially update a asset

### Example

```ts
import {
  Configuration,
  AssetsApi,
} from '@tmiclient/client';
import type { PatchThreatModelAssetRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AssetsApi(config);

  const body = {
    // string | Threat model identifier
    threatModelId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Asset identifier
    assetId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Array<JsonPatchDocumentInner> | JSON Patch operations to apply to the asset
    jsonPatchDocumentInner: [{"op":"replace","path":"/name","value":"Updated Name"},{"op":"add","path":"/description","value":"New description"}],
    // number | Optimistic-locking precondition. Pass the integer version returned by the previous read (or as the body \'version\' field on the previous write). On version mismatch the server returns 409 Conflict. In a future release this header will be required and missing values will return 428 Precondition Required. (optional)
    ifMatch: 56,
  } satisfies PatchThreatModelAssetRequest;

  try {
    const data = await api.patchThreatModelAsset(body);
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
| **assetId** | `string` | Asset identifier | [Defaults to `undefined`] |
| **jsonPatchDocumentInner** | `Array<JsonPatchDocumentInner>` | JSON Patch operations to apply to the asset | |
| **ifMatch** | `number` | Optimistic-locking precondition. Pass the integer version returned by the previous read (or as the body \&#39;version\&#39; field on the previous write). On version mismatch the server returns 409 Conflict. In a future release this header will be required and missing values will return 428 Precondition Required. | [Optional] [Defaults to `undefined`] |

### Return type

[**Asset**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json-patch+json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **405** | Method Not Allowed - The HTTP method is not supported for this endpoint |  * Allow - List of allowed HTTP methods for this endpoint <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **406** | Not Acceptable - The requested media type is not supported. This API only supports application/json |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **415** | Unsupported media type - the request Content-Type is not supported for this operation |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **200** | Successfully patched asset |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * ETag - Current optimistic-locking version of the resource (RFC 7232). Echo this value back via If-Match on the next PUT/PATCH. <br>  |
| **401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **409** | Conflict — the supplied version does not match the resource\&#39;s current version. Refetch and retry. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **428** | Precondition Required — the request did not include an If-Match header. This response is returned only when the server has flipped the RequireIfMatch config flag (planned for a future release). |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

