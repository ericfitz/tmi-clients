# tmi_client.WebhookDeliveriesApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_webhook_delivery_status**](WebhookDeliveriesApi.md#get_webhook_delivery_status) | **GET** /webhook-deliveries/{delivery_id} | Get webhook delivery status
[**update_webhook_delivery_status**](WebhookDeliveriesApi.md#update_webhook_delivery_status) | **POST** /webhook-deliveries/{delivery_id}/status | Update webhook delivery status


# **get_webhook_delivery_status**
> WebhookDelivery get_webhook_delivery_status(delivery_id, x_webhook_signature=x_webhook_signature)

Get webhook delivery status

Retrieve the status of a webhook delivery. Supports JWT (owner/invoker/admin) or HMAC (webhook receiver) authentication.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.webhook_delivery import WebhookDelivery
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
    api_instance = tmi_client.WebhookDeliveriesApi(api_client)
    delivery_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Webhook delivery identifier
    x_webhook_signature = 'x_webhook_signature_example' # str | HMAC-SHA256 signature (format: sha256={hex_signature}). Required for HMAC authentication, optional when using JWT. (optional)

    try:
        # Get webhook delivery status
        api_response = api_instance.get_webhook_delivery_status(delivery_id, x_webhook_signature=x_webhook_signature)
        print("The response of WebhookDeliveriesApi->get_webhook_delivery_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookDeliveriesApi->get_webhook_delivery_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **UUID**| Webhook delivery identifier | 
 **x_webhook_signature** | **str**| HMAC-SHA256 signature (format: sha256&#x3D;{hex_signature}). Required for HMAC authentication, optional when using JWT. | [optional] 

### Return type

[**WebhookDelivery**](WebhookDelivery.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook delivery status |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Forbidden |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_delivery_status**
> UpdateWebhookDeliveryStatusResponse update_webhook_delivery_status(delivery_id, x_webhook_signature, update_webhook_delivery_status_request)

Update webhook delivery status

Update the status of a webhook delivery via callback. Requires HMAC signature authentication.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.update_webhook_delivery_status_request import UpdateWebhookDeliveryStatusRequest
from tmi_client.models.update_webhook_delivery_status_response import UpdateWebhookDeliveryStatusResponse
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
    api_instance = tmi_client.WebhookDeliveriesApi(api_client)
    delivery_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Webhook delivery identifier
    x_webhook_signature = 'x_webhook_signature_example' # str | HMAC-SHA256 signature (format: sha256={hex_signature})
    update_webhook_delivery_status_request = tmi_client.UpdateWebhookDeliveryStatusRequest() # UpdateWebhookDeliveryStatusRequest | Webhook delivery status update

    try:
        # Update webhook delivery status
        api_response = api_instance.update_webhook_delivery_status(delivery_id, x_webhook_signature, update_webhook_delivery_status_request)
        print("The response of WebhookDeliveriesApi->update_webhook_delivery_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookDeliveriesApi->update_webhook_delivery_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **UUID**| Webhook delivery identifier | 
 **x_webhook_signature** | **str**| HMAC-SHA256 signature (format: sha256&#x3D;{hex_signature}) | 
 **update_webhook_delivery_status_request** | [**UpdateWebhookDeliveryStatusRequest**](UpdateWebhookDeliveryStatusRequest.md)| Webhook delivery status update | 

### Return type

[**UpdateWebhookDeliveryStatusResponse**](UpdateWebhookDeliveryStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad request |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**409** | Conflict - invalid status transition |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

