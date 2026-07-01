# \WebSocketAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetWsTicket**](WebSocketAPI.md#GetWsTicket) | **Get** /ws/ticket | Get a WebSocket authentication ticket



## GetWsTicket

> WsTicketResponse GetWsTicket(ctx).SessionId(sessionId).Execute()

Get a WebSocket authentication ticket



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	sessionId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The collaboration session ID the ticket is scoped to

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WebSocketAPI.GetWsTicket(context.Background()).SessionId(sessionId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WebSocketAPI.GetWsTicket``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetWsTicket`: WsTicketResponse
	fmt.Fprintf(os.Stdout, "Response from `WebSocketAPI.GetWsTicket`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetWsTicketRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sessionId** | **string** | The collaboration session ID the ticket is scoped to | 

### Return type

[**WsTicketResponse**](WsTicketResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

