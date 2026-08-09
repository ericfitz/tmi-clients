# \OIDCDiscoveryAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetJWKS**](OIDCDiscoveryAPI.md#GetJWKS) | **Get** /.well-known/jwks.json | JSON Web Key Set
[**GetOAuthAuthorizationServerMetadata**](OIDCDiscoveryAPI.md#GetOAuthAuthorizationServerMetadata) | **Get** /.well-known/oauth-authorization-server | OAuth 2.0 Authorization Server Metadata
[**GetOpenIDConfiguration**](OIDCDiscoveryAPI.md#GetOpenIDConfiguration) | **Get** /.well-known/openid-configuration | OpenID Connect Discovery Configuration



## GetJWKS

> GetJWKS200Response GetJWKS(ctx).Execute()

JSON Web Key Set



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
	resp, r, err := apiClient.OIDCDiscoveryAPI.GetJWKS(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OIDCDiscoveryAPI.GetJWKS``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetJWKS`: GetJWKS200Response
	fmt.Fprintf(os.Stdout, "Response from `OIDCDiscoveryAPI.GetJWKS`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetJWKSRequest struct via the builder pattern


### Return type

[**GetJWKS200Response**](GetJWKS200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetOAuthAuthorizationServerMetadata

> GetOAuthAuthorizationServerMetadata200Response GetOAuthAuthorizationServerMetadata(ctx).Execute()

OAuth 2.0 Authorization Server Metadata



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
	resp, r, err := apiClient.OIDCDiscoveryAPI.GetOAuthAuthorizationServerMetadata(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OIDCDiscoveryAPI.GetOAuthAuthorizationServerMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetOAuthAuthorizationServerMetadata`: GetOAuthAuthorizationServerMetadata200Response
	fmt.Fprintf(os.Stdout, "Response from `OIDCDiscoveryAPI.GetOAuthAuthorizationServerMetadata`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetOAuthAuthorizationServerMetadataRequest struct via the builder pattern


### Return type

[**GetOAuthAuthorizationServerMetadata200Response**](GetOAuthAuthorizationServerMetadata200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetOpenIDConfiguration

> GetOpenIDConfiguration200Response GetOpenIDConfiguration(ctx).Execute()

OpenID Connect Discovery Configuration



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
	resp, r, err := apiClient.OIDCDiscoveryAPI.GetOpenIDConfiguration(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OIDCDiscoveryAPI.GetOpenIDConfiguration``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetOpenIDConfiguration`: GetOpenIDConfiguration200Response
	fmt.Fprintf(os.Stdout, "Response from `OIDCDiscoveryAPI.GetOpenIDConfiguration`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetOpenIDConfigurationRequest struct via the builder pattern


### Return type

[**GetOpenIDConfiguration200Response**](GetOpenIDConfiguration200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

