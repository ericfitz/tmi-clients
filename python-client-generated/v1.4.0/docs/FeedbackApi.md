# tmi_client.FeedbackApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_usability_feedback**](FeedbackApi.md#create_usability_feedback) | **POST** /usability_feedback | Submit usability feedback
[**get_usability_feedback**](FeedbackApi.md#get_usability_feedback) | **GET** /usability_feedback/{id} | Get a single usability feedback entry (admin)
[**list_usability_feedback**](FeedbackApi.md#list_usability_feedback) | **GET** /usability_feedback | List usability feedback (admin)


# **create_usability_feedback**
> UsabilityFeedback create_usability_feedback(usability_feedback_input)

Submit usability feedback

Records a thumbs-up/down with surface tag and client metadata. Any authenticated user.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.usability_feedback import UsabilityFeedback
from tmi_client.models.usability_feedback_input import UsabilityFeedbackInput
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
    api_instance = tmi_client.FeedbackApi(api_client)
    usability_feedback_input = tmi_client.UsabilityFeedbackInput() # UsabilityFeedbackInput | 

    try:
        # Submit usability feedback
        api_response = api_instance.create_usability_feedback(usability_feedback_input)
        print("The response of FeedbackApi->create_usability_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedbackApi->create_usability_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usability_feedback_input** | [**UsabilityFeedbackInput**](UsabilityFeedbackInput.md)|  | 

### Return type

[**UsabilityFeedback**](UsabilityFeedback.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Feedback recorded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad request - invalid or missing parameters |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Unauthorized - missing or invalid authentication credentials |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**413** | Request body exceeds size limits |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usability_feedback**
> UsabilityFeedback get_usability_feedback(id)

Get a single usability feedback entry (admin)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.usability_feedback import UsabilityFeedback
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
    api_instance = tmi_client.FeedbackApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a single usability feedback entry (admin)
        api_response = api_instance.get_usability_feedback(id)
        print("The response of FeedbackApi->get_usability_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedbackApi->get_usability_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**UsabilityFeedback**](UsabilityFeedback.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Feedback entry |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Unauthorized - missing or invalid authentication credentials |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Forbidden - authenticated but not authorized for this operation |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Resource not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usability_feedback**
> ListUsabilityFeedback200Response list_usability_feedback(limit=limit, offset=offset, sentiment=sentiment, client_id=client_id, surface=surface, created_after=created_after, created_before=created_before)

List usability feedback (admin)

Admin-only listing with filters and pagination.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.list_usability_feedback200_response import ListUsabilityFeedback200Response
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
    api_instance = tmi_client.FeedbackApi(api_client)
    limit = 50 # int | Maximum number of results to return (optional) (default to 50)
    offset = 0 # int | Number of results to skip (optional) (default to 0)
    sentiment = 'sentiment_example' # str | Filter by sentiment (optional)
    client_id = 'client_id_example' # str |  (optional)
    surface = 'surface_example' # str |  (optional)
    created_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # List usability feedback (admin)
        api_response = api_instance.list_usability_feedback(limit=limit, offset=offset, sentiment=sentiment, client_id=client_id, surface=surface, created_after=created_after, created_before=created_before)
        print("The response of FeedbackApi->list_usability_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedbackApi->list_usability_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **sentiment** | **str**| Filter by sentiment | [optional] 
 **client_id** | **str**|  | [optional] 
 **surface** | **str**|  | [optional] 
 **created_after** | **datetime**|  | [optional] 
 **created_before** | **datetime**|  | [optional] 

### Return type

[**ListUsabilityFeedback200Response**](ListUsabilityFeedback200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Feedback list |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Unauthorized - missing or invalid authentication credentials |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Forbidden - authenticated but not authorized for this operation |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

