# TmiJsClient.WebSocketApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getWsTicket**](WebSocketApi.md#getWsTicket) | **GET** /ws/ticket | Get a WebSocket authentication ticket

<a name="getWsTicket"></a>
# **getWsTicket**
> WsTicketResponse getWsTicket(sessionId)

Get a WebSocket authentication ticket

Issues a short-lived, single-use authentication ticket for establishing a WebSocket connection to a collaboration session. The ticket is scoped to the specified session and the authenticated user. Tickets expire after 30 seconds and can only be used once.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.WebSocketApi();
let sessionId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | The collaboration session ID the ticket is scoped to

apiInstance.getWsTicket(sessionId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sessionId** | [**String**](.md)| The collaboration session ID the ticket is scoped to | 

### Return type

[**WsTicketResponse**](WsTicketResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

