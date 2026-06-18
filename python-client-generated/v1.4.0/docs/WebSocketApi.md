# tmi_client.WebSocketApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ws_ticket**](WebSocketApi.md#get_ws_ticket) | **GET** /ws/ticket | Get a WebSocket authentication ticket


# **get_ws_ticket**
> WsTicketResponse get_ws_ticket(session_id)

Get a WebSocket authentication ticket

Issues a short-lived, single-use authentication ticket for establishing a WebSocket connection to a collaboration session. The ticket is scoped to the specified session and the authenticated user. Tickets expire after 30 seconds and can only be used once.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.ws_ticket_response import WsTicketResponse
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
    api_instance = tmi_client.WebSocketApi(api_client)
    session_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The collaboration session ID the ticket is scoped to

    try:
        # Get a WebSocket authentication ticket
        api_response = api_instance.get_ws_ticket(session_id)
        print("The response of WebSocketApi->get_ws_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebSocketApi->get_ws_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **UUID**| The collaboration session ID the ticket is scoped to | 

### Return type

[**WsTicketResponse**](WsTicketResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ticket issued successfully |  * Cache-Control - Set to no-store to prevent caching <br>  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Missing or invalid session_id parameter |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Unauthorized - missing or invalid authentication |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Session not found or user is not a participant |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |
**500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

