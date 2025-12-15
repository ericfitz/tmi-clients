# tmi_client.AddonsApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_addon**](AddonsApi.md#create_addon) | **POST** /addons | Create add-on
[**delete_addon**](AddonsApi.md#delete_addon) | **DELETE** /addons/{id} | Delete add-on
[**get_addon**](AddonsApi.md#get_addon) | **GET** /addons/{id} | Get add-on
[**get_invocation**](AddonsApi.md#get_invocation) | **GET** /invocations/{id} | Get invocation
[**invoke_addon**](AddonsApi.md#invoke_addon) | **POST** /addons/{id}/invoke | Invoke add-on
[**list_addons**](AddonsApi.md#list_addons) | **GET** /addons | List add-ons
[**list_invocations**](AddonsApi.md#list_invocations) | **GET** /invocations | List invocations
[**update_invocation_status**](AddonsApi.md#update_invocation_status) | **POST** /invocations/{id}/status | Update invocation status

# **create_addon**
> AddonResponse create_addon(body)

Create add-on

Create a new add-on (administrators only)

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AddonsApi(tmi_client.ApiClient(configuration))
body = tmi_client.CreateAddonRequest() # CreateAddonRequest | 

try:
    # Create add-on
    api_response = api_instance.create_addon(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonsApi->create_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAddonRequest**](CreateAddonRequest.md)|  | 

### Return type

[**AddonResponse**](AddonResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_addon**
> delete_addon(id)

Delete add-on

Delete an add-on (administrators only)

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AddonsApi(tmi_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Resource identifier

try:
    # Delete add-on
    api_instance.delete_addon(id)
except ApiException as e:
    print("Exception when calling AddonsApi->delete_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Resource identifier | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addon**
> AddonResponse get_addon(id)

Get add-on

Get a single add-on by ID

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AddonsApi(tmi_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Resource identifier

try:
    # Get add-on
    api_response = api_instance.get_addon(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonsApi->get_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Resource identifier | 

### Return type

[**AddonResponse**](AddonResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invocation**
> InvocationResponse get_invocation(id)

Get invocation

Get a single invocation by ID (own invocations or admin)

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AddonsApi(tmi_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Resource identifier

try:
    # Get invocation
    api_response = api_instance.get_invocation(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonsApi->get_invocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Resource identifier | 

### Return type

[**InvocationResponse**](InvocationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_addon**
> InvokeAddonResponse invoke_addon(body, id)

Invoke add-on

Trigger an add-on invocation (authenticated users)

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AddonsApi(tmi_client.ApiClient(configuration))
body = tmi_client.InvokeAddonRequest() # InvokeAddonRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Resource identifier

try:
    # Invoke add-on
    api_response = api_instance.invoke_addon(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonsApi->invoke_addon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvokeAddonRequest**](InvokeAddonRequest.md)|  | 
 **id** | [**str**](.md)| Resource identifier | 

### Return type

[**InvokeAddonResponse**](InvokeAddonResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_addons**
> ListAddonsResponse list_addons(limit=limit, offset=offset, threat_model_id=threat_model_id)

List add-ons

List all add-ons (authenticated users)

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AddonsApi(tmi_client.ApiClient(configuration))
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter subscriptions by threat model ID (optional)

try:
    # List add-ons
    api_response = api_instance.list_addons(limit=limit, offset=offset, threat_model_id=threat_model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonsApi->list_addons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **threat_model_id** | [**str**](.md)| Filter subscriptions by threat model ID | [optional] 

### Return type

[**ListAddonsResponse**](ListAddonsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invocations**
> ListInvocationsResponse list_invocations(limit=limit, offset=offset, status=status, addon_id=addon_id)

List invocations

List add-on invocations (users see own, admins see all)

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AddonsApi(tmi_client.ApiClient(configuration))
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)
status = 'status_example' # str | Filter by status value (exact match). To filter by multiple statuses, use multiple status parameters or comma-separated values. (optional)
addon_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter by add-on (optional)

try:
    # List invocations
    api_response = api_instance.list_invocations(limit=limit, offset=offset, status=status, addon_id=addon_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonsApi->list_invocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **status** | **str**| Filter by status value (exact match). To filter by multiple statuses, use multiple status parameters or comma-separated values. | [optional] 
 **addon_id** | [**str**](.md)| Filter by add-on | [optional] 

### Return type

[**ListInvocationsResponse**](ListInvocationsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invocation_status**
> UpdateInvocationStatusResponse update_invocation_status(body, x_webhook_signature, id)

Update invocation status

Update invocation status (webhook callback with HMAC authentication)

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AddonsApi(tmi_client.ApiClient(configuration))
body = tmi_client.UpdateInvocationStatusRequest() # UpdateInvocationStatusRequest | 
x_webhook_signature = 'x_webhook_signature_example' # str | HMAC-SHA256 signature (format: sha256={hex_signature})
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Resource identifier

try:
    # Update invocation status
    api_response = api_instance.update_invocation_status(body, x_webhook_signature, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddonsApi->update_invocation_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateInvocationStatusRequest**](UpdateInvocationStatusRequest.md)|  | 
 **x_webhook_signature** | **str**| HMAC-SHA256 signature (format: sha256&#x3D;{hex_signature}) | 
 **id** | [**str**](.md)| Resource identifier | 

### Return type

[**UpdateInvocationStatusResponse**](UpdateInvocationStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

