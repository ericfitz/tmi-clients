# {{classname}}

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ListSAMLUsers**](SAMLApi.md#ListSAMLUsers) | **Get** /saml/providers/{idp}/users | List SAML users for UI autocomplete

# **ListSAMLUsers**
> interface{} ListSAMLUsers(ctx, idp)
List SAML users for UI autocomplete

Returns a lightweight list of active users for a specific SAML provider. Intended for UI autocomplete/search features. Only accessible to users from the same provider.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **idp** | **string**| Identity provider ID (e.g., saml_okta, saml_azure) | 

### Return type

[**interface{}**](interface{}.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

