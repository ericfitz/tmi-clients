# {{classname}}

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateAddon**](AddonsApi.md#CreateAddon) | **Post** /addons | Create add-on
[**DeleteAddon**](AddonsApi.md#DeleteAddon) | **Delete** /addons/{id} | Delete add-on
[**GetAddon**](AddonsApi.md#GetAddon) | **Get** /addons/{id} | Get add-on
[**GetInvocation**](AddonsApi.md#GetInvocation) | **Get** /invocations/{id} | Get invocation
[**InvokeAddon**](AddonsApi.md#InvokeAddon) | **Post** /addons/{id}/invoke | Invoke add-on
[**ListAddons**](AddonsApi.md#ListAddons) | **Get** /addons | List add-ons
[**ListInvocations**](AddonsApi.md#ListInvocations) | **Get** /invocations | List invocations
[**UpdateInvocationStatus**](AddonsApi.md#UpdateInvocationStatus) | **Post** /invocations/{id}/status | Update invocation status

# **CreateAddon**
> AddonResponse CreateAddon(ctx, body)
Create add-on

Create a new add-on (administrators only)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**CreateAddonRequest**](CreateAddonRequest.md)|  | 

### Return type

[**AddonResponse**](AddonResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteAddon**
> DeleteAddon(ctx, id)
Delete add-on

Delete an add-on (administrators only)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | [**string**](.md)| Resource identifier | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAddon**
> AddonResponse GetAddon(ctx, id)
Get add-on

Get a single add-on by ID

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | [**string**](.md)| Resource identifier | 

### Return type

[**AddonResponse**](AddonResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetInvocation**
> InvocationResponse GetInvocation(ctx, id)
Get invocation

Get a single invocation by ID (own invocations or admin)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | [**string**](.md)| Resource identifier | 

### Return type

[**InvocationResponse**](InvocationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **InvokeAddon**
> InvokeAddonResponse InvokeAddon(ctx, body, id)
Invoke add-on

Trigger an add-on invocation (authenticated users)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**InvokeAddonRequest**](InvokeAddonRequest.md)|  | 
  **id** | [**string**](.md)| Resource identifier | 

### Return type

[**InvokeAddonResponse**](InvokeAddonResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListAddons**
> ListAddonsResponse ListAddons(ctx, optional)
List add-ons

List all add-ons (authenticated users)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***AddonsApiListAddonsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AddonsApiListAddonsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]
 **threatModelId** | [**optional.Interface of string**](.md)| Filter subscriptions by threat model ID | 

### Return type

[**ListAddonsResponse**](ListAddonsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListInvocations**
> ListInvocationsResponse ListInvocations(ctx, optional)
List invocations

List add-on invocations (users see own, admins see all)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***AddonsApiListInvocationsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AddonsApiListInvocationsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]
 **status** | **optional.String**| Filter by status value (exact match). To filter by multiple statuses, use multiple status parameters or comma-separated values. | 
 **addonId** | [**optional.Interface of string**](.md)| Filter by add-on | 

### Return type

[**ListInvocationsResponse**](ListInvocationsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateInvocationStatus**
> UpdateInvocationStatusResponse UpdateInvocationStatus(ctx, body, id, xWebhookSignature)
Update invocation status

Update invocation status (webhook callback with HMAC authentication)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**UpdateInvocationStatusRequest**](UpdateInvocationStatusRequest.md)|  | 
  **id** | [**string**](.md)| Resource identifier | 
  **xWebhookSignature** | **string**| HMAC-SHA256 signature (format: sha256&#x3D;{hex_signature}) | 

### Return type

[**UpdateInvocationStatusResponse**](UpdateInvocationStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

