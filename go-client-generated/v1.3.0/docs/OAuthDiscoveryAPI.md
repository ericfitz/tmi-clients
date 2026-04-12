# \OAuthDiscoveryAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetOAuthProtectedResourceMetadata**](OAuthDiscoveryAPI.md#GetOAuthProtectedResourceMetadata) | **Get** /.well-known/oauth-protected-resource | OAuth 2.0 Protected Resource Metadata



## GetOAuthProtectedResourceMetadata

> OAuthProtectedResourceMetadata GetOAuthProtectedResourceMetadata(ctx).Execute()

OAuth 2.0 Protected Resource Metadata



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
	resp, r, err := apiClient.OAuthDiscoveryAPI.GetOAuthProtectedResourceMetadata(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OAuthDiscoveryAPI.GetOAuthProtectedResourceMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetOAuthProtectedResourceMetadata`: OAuthProtectedResourceMetadata
	fmt.Fprintf(os.Stdout, "Response from `OAuthDiscoveryAPI.GetOAuthProtectedResourceMetadata`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetOAuthProtectedResourceMetadataRequest struct via the builder pattern


### Return type

[**OAuthProtectedResourceMetadata**](OAuthProtectedResourceMetadata.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

