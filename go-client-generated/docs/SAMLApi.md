# \SAMLAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ListSAMLUsers**](SAMLAPI.md#ListSAMLUsers) | **Get** /saml/providers/{idp}/users | List SAML users for UI autocomplete



## ListSAMLUsers

> map[string]interface{} ListSAMLUsers(ctx, idp).Execute()

List SAML users for UI autocomplete



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
	idp := "idp_example" // string | Identity provider ID (e.g., saml_okta, saml_azure)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SAMLAPI.ListSAMLUsers(context.Background(), idp).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SAMLAPI.ListSAMLUsers``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSAMLUsers`: map[string]interface{}
	fmt.Fprintf(os.Stdout, "Response from `SAMLAPI.ListSAMLUsers`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**idp** | **string** | Identity provider ID (e.g., saml_okta, saml_azure) | 

### Other Parameters

Other parameters are passed through a pointer to a apiListSAMLUsersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**map[string]interface{}**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

