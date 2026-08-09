# tmi_client.SAMLApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_saml_users**](SAMLApi.md#list_saml_users) | **GET** /saml/providers/{idp}/users | List SAML users for UI autocomplete


# **list_saml_users**
> ListSAMLUsers200Response list_saml_users(idp, email=email, limit=limit, offset=offset)

List SAML users for UI autocomplete

Returns a lightweight list of active users for a specific SAML provider. Intended for UI autocomplete/search features. Only accessible to users from the same provider.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.list_saml_users200_response import ListSAMLUsers200Response
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
    api_instance = tmi_client.SAMLApi(api_client)
    idp = 'idp_example' # str | Identity provider ID (e.g., saml_okta, saml_azure)
    email = 'email_example' # str | Filter by email (case-insensitive substring match) (optional)
    limit = 100 # int | Maximum number of users to return. (optional) (default to 100)
    offset = 0 # int | Number of users to skip before starting to return results. (optional) (default to 0)

    try:
        # List SAML users for UI autocomplete
        api_response = api_instance.list_saml_users(idp, email=email, limit=limit, offset=offset)
        print("The response of SAMLApi->list_saml_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLApi->list_saml_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp** | **str**| Identity provider ID (e.g., saml_okta, saml_azure) | 
 **email** | **str**| Filter by email (case-insensitive substring match) | [optional] 
 **limit** | **int**| Maximum number of users to return. | [optional] [default to 100]
 **offset** | **int**| Number of users to skip before starting to return results. | [optional] [default to 0]

### Return type

[**ListSAMLUsers200Response**](ListSAMLUsers200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**405** | Method Not Allowed - The HTTP method is not supported for this endpoint |  * Allow - List of allowed HTTP methods for this endpoint <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**406** | Not Acceptable - The requested media type is not supported. This API only supports application/json |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**500** | Internal server error |  -  |
**200** | Success |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Forbidden - User is not from the same SAML provider |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Resource not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**503** | Service Unavailable - A required backend service (authentication, database, or cache) is temporarily unavailable. The client should retry the request after the delay indicated in the Retry-After header. |  * Retry-After - Number of seconds to wait before retrying the request <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

