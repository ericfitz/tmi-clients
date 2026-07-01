# tmi_client.AssetsApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_threat_model_asset**](AssetsApi.md#patch_threat_model_asset) | **PATCH** /threat_models/{threat_model_id}/assets/{asset_id} | Partially update asset


# **patch_threat_model_asset**
> Asset patch_threat_model_asset(threat_model_id, asset_id, json_patch_document_inner, if_match=if_match)

Partially update asset

Apply JSON Patch operations to partially update a asset

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.asset import Asset
from tmi_client.models.json_patch_document_inner import JsonPatchDocumentInner
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.AssetsApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    asset_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Asset identifier
    json_patch_document_inner = [{"op":"replace","path":"/name","value":"Updated Name"},{"op":"add","path":"/description","value":"New description"}] # List[JsonPatchDocumentInner] | JSON Patch operations to apply to the asset
    if_match = 56 # int | Optimistic-locking precondition. Pass the integer version returned by the previous read (or as the body 'version' field on the previous write). On version mismatch the server returns 409 Conflict. In a future release this header will be required and missing values will return 428 Precondition Required. (optional)

    try:
        # Partially update asset
        api_response = api_instance.patch_threat_model_asset(threat_model_id, asset_id, json_patch_document_inner, if_match=if_match)
        print("The response of AssetsApi->patch_threat_model_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->patch_threat_model_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **asset_id** | **UUID**| Asset identifier | 
 **json_patch_document_inner** | [**List[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| JSON Patch operations to apply to the asset | 
 **if_match** | **int**| Optimistic-locking precondition. Pass the integer version returned by the previous read (or as the body &#39;version&#39; field on the previous write). On version mismatch the server returns 409 Conflict. In a future release this header will be required and missing values will return 428 Precondition Required. | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**405** | Method Not Allowed - The HTTP method is not supported for this endpoint |  * Allow - List of allowed HTTP methods for this endpoint <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**406** | Not Acceptable - The requested media type is not supported. This API only supports application/json |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |
**500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**415** | Unsupported media type - the request Content-Type is not supported for this operation |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**200** | Successfully patched asset |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * ETag - Current optimistic-locking version of the resource (RFC 7232). Echo this value back via If-Match on the next PUT/PATCH. <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**409** | Conflict — the supplied version does not match the resource&#39;s current version. Refetch and retry. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**428** | Precondition Required — the request did not include an If-Match header. This response is returned only when the server has flipped the RequireIfMatch config flag (planned for a future release). |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

