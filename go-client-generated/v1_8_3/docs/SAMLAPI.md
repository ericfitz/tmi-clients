# \SAMLAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ListSAMLUsers**](SAMLAPI.md#ListSAMLUsers) | **Get** /saml/providers/{idp}/users | List SAML users for UI autocomplete



## ListSAMLUsers

> ListSAMLUsers200Response ListSAMLUsers(ctx, idp).Email(email).Limit(limit).Offset(offset).Execute()

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
	email := "email_example" // string | Filter by email (case-insensitive substring match) (optional)
	limit := int32(56) // int32 | Maximum number of users to return. (optional) (default to 100)
	offset := int32(56) // int32 | Number of users to skip before starting to return results. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SAMLAPI.ListSAMLUsers(context.Background(), idp).Email(email).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SAMLAPI.ListSAMLUsers``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSAMLUsers`: ListSAMLUsers200Response
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

 **email** | **string** | Filter by email (case-insensitive substring match) | 
 **limit** | **int32** | Maximum number of users to return. | [default to 100]
 **offset** | **int32** | Number of users to skip before starting to return results. | [default to 0]

### Return type

[**ListSAMLUsers200Response**](ListSAMLUsers200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

