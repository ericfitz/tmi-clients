# \UsersAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeleteUserAccount**](UsersAPI.md#DeleteUserAccount) | **Delete** /me | Delete authenticated user account and all data
[**LogoutCurrentUser**](UsersAPI.md#LogoutCurrentUser) | **Post** /me/logout | Logout current user
[**TransferCurrentUserOwnership**](UsersAPI.md#TransferCurrentUserOwnership) | **Post** /me/transfer | Transfer ownership of all owned resources



## DeleteUserAccount

> DeletionChallenge DeleteUserAccount(ctx).Challenge(challenge).Execute()

Delete authenticated user account and all data



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
	challenge := "challenge_example" // string | Challenge string from first request (step 2 only). Must match exactly. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.DeleteUserAccount(context.Background()).Challenge(challenge).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.DeleteUserAccount``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteUserAccount`: DeletionChallenge
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.DeleteUserAccount`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDeleteUserAccountRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge** | **string** | Challenge string from first request (step 2 only). Must match exactly. | 

### Return type

[**DeletionChallenge**](DeletionChallenge.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## LogoutCurrentUser

> LogoutCurrentUser(ctx).Execute()

Logout current user



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.UsersAPI.LogoutCurrentUser(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.LogoutCurrentUser``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiLogoutCurrentUserRequest struct via the builder pattern


### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TransferCurrentUserOwnership

> TransferOwnershipResult TransferCurrentUserOwnership(ctx).TransferOwnershipRequest(transferOwnershipRequest).Execute()

Transfer ownership of all owned resources



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
	transferOwnershipRequest := *openapiclient.NewTransferOwnershipRequest("550e8400-e29b-41d4-a716-446655440000") // TransferOwnershipRequest | Ownership transfer request specifying the target user

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsersAPI.TransferCurrentUserOwnership(context.Background()).TransferOwnershipRequest(transferOwnershipRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsersAPI.TransferCurrentUserOwnership``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TransferCurrentUserOwnership`: TransferOwnershipResult
	fmt.Fprintf(os.Stdout, "Response from `UsersAPI.TransferCurrentUserOwnership`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTransferCurrentUserOwnershipRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferOwnershipRequest** | [**TransferOwnershipRequest**](TransferOwnershipRequest.md) | Ownership transfer request specifying the target user | 

### Return type

[**TransferOwnershipResult**](TransferOwnershipResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

