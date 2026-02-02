# tmi_client.ConfigurationApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_config**](ConfigurationApi.md#get_client_config) | **GET** /config | Get client configuration

# **get_client_config**
> ClientConfig get_client_config()

Get client configuration

Returns configuration settings for client applications such as tmi-ux. This endpoint is public and cacheable.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tmi_client.ConfigurationApi()

try:
    # Get client configuration
    api_response = api_instance.get_client_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_client_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientConfig**](ClientConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

