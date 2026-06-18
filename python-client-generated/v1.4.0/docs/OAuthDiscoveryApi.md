# tmi_client.OAuthDiscoveryApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_o_auth_protected_resource_metadata**](OAuthDiscoveryApi.md#get_o_auth_protected_resource_metadata) | **GET** /.well-known/oauth-protected-resource | OAuth 2.0 Protected Resource Metadata


# **get_o_auth_protected_resource_metadata**
> OAuthProtectedResourceMetadata get_o_auth_protected_resource_metadata()

OAuth 2.0 Protected Resource Metadata

Returns OAuth 2.0 protected resource metadata as per RFC 9728

### Example


```python
import tmi_client
from tmi_client.models.o_auth_protected_resource_metadata import OAuthProtectedResourceMetadata
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)


# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.OAuthDiscoveryApi(api_client)

    try:
        # OAuth 2.0 Protected Resource Metadata
        api_response = api_instance.get_o_auth_protected_resource_metadata()
        print("The response of OAuthDiscoveryApi->get_o_auth_protected_resource_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthDiscoveryApi->get_o_auth_protected_resource_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OAuthProtectedResourceMetadata**](OAuthProtectedResourceMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OAuth 2.0 protected resource metadata |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**503** | Service Unavailable - A required backend service (authentication, database, or cache) is temporarily unavailable. The client should retry the request after the delay indicated in the Retry-After header. |  * Retry-After - Number of seconds to wait before retrying the request <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

