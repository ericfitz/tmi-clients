# tmi_client.OIDCDiscoveryApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_jwks**](OIDCDiscoveryApi.md#get_jwks) | **GET** /.well-known/jwks.json | JSON Web Key Set
[**get_o_auth_authorization_server_metadata**](OIDCDiscoveryApi.md#get_o_auth_authorization_server_metadata) | **GET** /.well-known/oauth-authorization-server | OAuth 2.0 Authorization Server Metadata
[**get_open_id_configuration**](OIDCDiscoveryApi.md#get_open_id_configuration) | **GET** /.well-known/openid-configuration | OpenID Connect Discovery Configuration


# **get_jwks**
> GetJWKS200Response get_jwks()

JSON Web Key Set

Returns the JSON Web Key Set (JWKS) for JWT signature verification

### Example


```python
import tmi_client
from tmi_client.models.get_jwks200_response import GetJWKS200Response
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
    api_instance = tmi_client.OIDCDiscoveryApi(api_client)

    try:
        # JSON Web Key Set
        api_response = api_instance.get_jwks()
        print("The response of OIDCDiscoveryApi->get_jwks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OIDCDiscoveryApi->get_jwks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetJWKS200Response**](GetJWKS200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON Web Key Set |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**503** | Service Unavailable - A required backend service (authentication, database, or cache) is temporarily unavailable. The client should retry the request after the delay indicated in the Retry-After header. |  * Retry-After - Number of seconds to wait before retrying the request <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_authorization_server_metadata**
> GetOAuthAuthorizationServerMetadata200Response get_o_auth_authorization_server_metadata()

OAuth 2.0 Authorization Server Metadata

Returns OAuth 2.0 authorization server metadata as per RFC 8414

### Example


```python
import tmi_client
from tmi_client.models.get_o_auth_authorization_server_metadata200_response import GetOAuthAuthorizationServerMetadata200Response
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
    api_instance = tmi_client.OIDCDiscoveryApi(api_client)

    try:
        # OAuth 2.0 Authorization Server Metadata
        api_response = api_instance.get_o_auth_authorization_server_metadata()
        print("The response of OIDCDiscoveryApi->get_o_auth_authorization_server_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OIDCDiscoveryApi->get_o_auth_authorization_server_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetOAuthAuthorizationServerMetadata200Response**](GetOAuthAuthorizationServerMetadata200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OAuth 2.0 authorization server metadata |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**503** | Service Unavailable - A required backend service (authentication, database, or cache) is temporarily unavailable. The client should retry the request after the delay indicated in the Retry-After header. |  * Retry-After - Number of seconds to wait before retrying the request <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_id_configuration**
> GetOpenIDConfiguration200Response get_open_id_configuration()

OpenID Connect Discovery Configuration

Returns OpenID Connect provider configuration metadata as per RFC 8414

### Example


```python
import tmi_client
from tmi_client.models.get_open_id_configuration200_response import GetOpenIDConfiguration200Response
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
    api_instance = tmi_client.OIDCDiscoveryApi(api_client)

    try:
        # OpenID Connect Discovery Configuration
        api_response = api_instance.get_open_id_configuration()
        print("The response of OIDCDiscoveryApi->get_open_id_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OIDCDiscoveryApi->get_open_id_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetOpenIDConfiguration200Response**](GetOpenIDConfiguration200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenID Connect configuration metadata |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**503** | Service Unavailable - A required backend service (authentication, database, or cache) is temporarily unavailable. The client should retry the request after the delay indicated in the Retry-After header. |  * Retry-After - Number of seconds to wait before retrying the request <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

