# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetWsTicket**](WebSocketApi.md#GetWsTicket) | **Get** /ws/ticket | Get a WebSocket authentication ticket

# **GetWsTicket**
> WsTicketResponse GetWsTicket(ctx, sessionId)
Get a WebSocket authentication ticket

Issues a short-lived, single-use authentication ticket for establishing a WebSocket connection to a collaboration session. The ticket is scoped to the specified session and the authenticated user. Tickets expire after 30 seconds and can only be used once.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **sessionId** | [**string**](.md)| The collaboration session ID the ticket is scoped to | 

### Return type

[**WsTicketResponse**](WsTicketResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

