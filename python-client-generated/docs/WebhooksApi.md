# tmi_client.WebhooksApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_subscription**](WebhooksApi.md#create_webhook_subscription) | **POST** /webhooks/subscriptions | Create webhook subscription
[**delete_webhook_subscription**](WebhooksApi.md#delete_webhook_subscription) | **DELETE** /webhooks/subscriptions/{webhook_id} | Delete webhook subscription
[**get_webhook_delivery**](WebhooksApi.md#get_webhook_delivery) | **GET** /webhooks/deliveries/{delivery_id} | Get webhook delivery
[**get_webhook_subscription**](WebhooksApi.md#get_webhook_subscription) | **GET** /webhooks/subscriptions/{webhook_id} | Get webhook subscription
[**list_webhook_deliveries**](WebhooksApi.md#list_webhook_deliveries) | **GET** /webhooks/deliveries | List webhook deliveries
[**list_webhook_subscriptions**](WebhooksApi.md#list_webhook_subscriptions) | **GET** /webhooks/subscriptions | List webhook subscriptions
[**test_webhook_subscription**](WebhooksApi.md#test_webhook_subscription) | **POST** /webhooks/subscriptions/{webhook_id}/test | Test webhook subscription

# **create_webhook_subscription**
> WebhookSubscription create_webhook_subscription(body)

Create webhook subscription

Create a new webhook subscription. The subscription will be in pending_verification status until the challenge is completed.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.WebhooksApi(tmi_client.ApiClient(configuration))
body = tmi_client.WebhookSubscriptionInput() # WebhookSubscriptionInput | 

try:
    # Create webhook subscription
    api_response = api_instance.create_webhook_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->create_webhook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookSubscriptionInput**](WebhookSubscriptionInput.md)|  | 

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_subscription**
> delete_webhook_subscription(webhook_id)

Delete webhook subscription

Delete a webhook subscription. Only the owner can delete a subscription.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.WebhooksApi(tmi_client.ApiClient(configuration))
webhook_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Webhook subscription identifier

try:
    # Delete webhook subscription
    api_instance.delete_webhook_subscription(webhook_id)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_webhook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | [**str**](.md)| Webhook subscription identifier | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_delivery**
> WebhookDelivery get_webhook_delivery(delivery_id)

Get webhook delivery

Get details of a specific webhook delivery

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.WebhooksApi(tmi_client.ApiClient(configuration))
delivery_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Webhook delivery identifier

try:
    # Get webhook delivery
    api_response = api_instance.get_webhook_delivery(delivery_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook_delivery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | [**str**](.md)| Webhook delivery identifier | 

### Return type

[**WebhookDelivery**](WebhookDelivery.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_subscription**
> WebhookSubscription get_webhook_subscription(webhook_id)

Get webhook subscription

Get a specific webhook subscription by ID

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.WebhooksApi(tmi_client.ApiClient(configuration))
webhook_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Webhook subscription identifier

try:
    # Get webhook subscription
    api_response = api_instance.get_webhook_subscription(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | [**str**](.md)| Webhook subscription identifier | 

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook_deliveries**
> list[WebhookDelivery] list_webhook_deliveries(subscription_id=subscription_id, offset=offset, limit=limit)

List webhook deliveries

List webhook deliveries for the authenticated user's subscriptions

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.WebhooksApi(tmi_client.ApiClient(configuration))
subscription_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter by subscription ID (optional)
offset = 0 # int | Number of results to skip (optional) (default to 0)
limit = 20 # int | Maximum number of results to return (optional) (default to 20)

try:
    # List webhook deliveries
    api_response = api_instance.list_webhook_deliveries(subscription_id=subscription_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->list_webhook_deliveries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Filter by subscription ID | [optional] 
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]

### Return type

[**list[WebhookDelivery]**](WebhookDelivery.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook_subscriptions**
> list[WebhookSubscription] list_webhook_subscriptions(threat_model_id=threat_model_id, offset=offset, limit=limit)

List webhook subscriptions

List all webhook subscriptions owned by the authenticated user. Optionally filter by threat_model_id.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.WebhooksApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter subscriptions by threat model ID (optional)
offset = 0 # int | Number of results to skip (optional) (default to 0)
limit = 20 # int | Maximum number of results to return (optional) (default to 20)

try:
    # List webhook subscriptions
    api_response = api_instance.list_webhook_subscriptions(threat_model_id=threat_model_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->list_webhook_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Filter subscriptions by threat model ID | [optional] 
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]

### Return type

[**list[WebhookSubscription]**](WebhookSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_webhook_subscription**
> WebhookTestResponse test_webhook_subscription(webhook_id, body=body)

Test webhook subscription

Send a test event to the webhook URL to verify it's working correctly

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.WebhooksApi(tmi_client.ApiClient(configuration))
webhook_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Webhook subscription identifier
body = tmi_client.WebhookTestRequest() # WebhookTestRequest |  (optional)

try:
    # Test webhook subscription
    api_response = api_instance.test_webhook_subscription(webhook_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->test_webhook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | [**str**](.md)| Webhook subscription identifier | 
 **body** | [**WebhookTestRequest**](WebhookTestRequest.md)|  | [optional] 

### Return type

[**WebhookTestResponse**](WebhookTestResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

