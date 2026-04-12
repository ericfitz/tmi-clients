# \AdminUsersAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateAdminUserClientCredential**](AdminUsersAPI.md#CreateAdminUserClientCredential) | **Post** /admin/users/{internal_uuid}/client_credentials | Create a client credential for an automation user
[**CreateAutomationAccount**](AdminUsersAPI.md#CreateAutomationAccount) | **Post** /admin/users/automation | Create an automation (service) account
[**DeleteAdminUserClientCredential**](AdminUsersAPI.md#DeleteAdminUserClientCredential) | **Delete** /admin/users/{internal_uuid}/client_credentials/{credential_id} | Delete a client credential for an automation user
[**ListAdminUserClientCredentials**](AdminUsersAPI.md#ListAdminUserClientCredentials) | **Get** /admin/users/{internal_uuid}/client_credentials | List client credentials for an automation user



## CreateAdminUserClientCredential

> ClientCredentialResponse CreateAdminUserClientCredential(ctx, internalUuid).CreateCurrentUserClientCredentialRequest(createCurrentUserClientCredentialRequest).Execute()

Create a client credential for an automation user



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
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user
	createCurrentUserClientCredentialRequest := *openapiclient.NewCreateCurrentUserClientCredentialRequest("CI/CD Pipeline") // CreateCurrentUserClientCredentialRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdminUsersAPI.CreateAdminUserClientCredential(context.Background(), internalUuid).CreateCurrentUserClientCredentialRequest(createCurrentUserClientCredentialRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdminUsersAPI.CreateAdminUserClientCredential``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateAdminUserClientCredential`: ClientCredentialResponse
	fmt.Fprintf(os.Stdout, "Response from `AdminUsersAPI.CreateAdminUserClientCredential`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateAdminUserClientCredentialRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **createCurrentUserClientCredentialRequest** | [**CreateCurrentUserClientCredentialRequest**](CreateCurrentUserClientCredentialRequest.md) |  | 

### Return type

[**ClientCredentialResponse**](ClientCredentialResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateAutomationAccount

> CreateAutomationAccountResponse CreateAutomationAccount(ctx).CreateAutomationAccountRequest(createAutomationAccountRequest).Execute()

Create an automation (service) account



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
	createAutomationAccountRequest := *openapiclient.NewCreateAutomationAccountRequest("Name_example") // CreateAutomationAccountRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdminUsersAPI.CreateAutomationAccount(context.Background()).CreateAutomationAccountRequest(createAutomationAccountRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdminUsersAPI.CreateAutomationAccount``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateAutomationAccount`: CreateAutomationAccountResponse
	fmt.Fprintf(os.Stdout, "Response from `AdminUsersAPI.CreateAutomationAccount`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateAutomationAccountRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createAutomationAccountRequest** | [**CreateAutomationAccountRequest**](CreateAutomationAccountRequest.md) |  | 

### Return type

[**CreateAutomationAccountResponse**](CreateAutomationAccountResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteAdminUserClientCredential

> DeleteAdminUserClientCredential(ctx, internalUuid, credentialId).Execute()

Delete a client credential for an automation user



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
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user
	credentialId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal UUID of the client credential (the \"id\" field from the list response, not the \"client_id\")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AdminUsersAPI.DeleteAdminUserClientCredential(context.Background(), internalUuid, credentialId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdminUsersAPI.DeleteAdminUserClientCredential``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 
**credentialId** | **string** | Internal UUID of the client credential (the \&quot;id\&quot; field from the list response, not the \&quot;client_id\&quot;) | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteAdminUserClientCredentialRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



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


## ListAdminUserClientCredentials

> ListClientCredentialsResponse ListAdminUserClientCredentials(ctx, internalUuid).Limit(limit).Offset(offset).Execute()

List client credentials for an automation user



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
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 50)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdminUsersAPI.ListAdminUserClientCredentials(context.Background(), internalUuid).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdminUsersAPI.ListAdminUserClientCredentials``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListAdminUserClientCredentials`: ListClientCredentialsResponse
	fmt.Fprintf(os.Stdout, "Response from `AdminUsersAPI.ListAdminUserClientCredentials`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 

### Other Parameters

Other parameters are passed through a pointer to a apiListAdminUserClientCredentialsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** | Maximum number of results to return | [default to 50]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListClientCredentialsResponse**](ListClientCredentialsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

