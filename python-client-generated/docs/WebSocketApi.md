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
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.WebSocketApi(tmi_client.ApiClient(configuration))
session_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The collaboration session ID the ticket is scoped to

try:
    # Get a WebSocket authentication ticket
    api_response = api_instance.get_ws_ticket(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketApi->get_ws_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | [**str**](.md)| The collaboration session ID the ticket is scoped to | 

### Return type

[**WsTicketResponse**](WsTicketResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

