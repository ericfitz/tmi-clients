# {{classname}}

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BulkDeleteThreatModelThreats**](ThreatsApi.md#BulkDeleteThreatModelThreats) | **Delete** /threat_models/{threat_model_id}/threats/bulk | Bulk DELETE threats
[**BulkPatchThreatModelThreats**](ThreatsApi.md#BulkPatchThreatModelThreats) | **Patch** /threat_models/{threat_model_id}/threats/bulk | Bulk PATCH threats

# **BulkDeleteThreatModelThreats**
> InlineResponse2008 BulkDeleteThreatModelThreats(ctx, threatModelId, threatIds)
Bulk DELETE threats

Delete multiple threats in a single request

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **threatModelId** | [**string**](.md)| Threat model identifier | 
  **threatIds** | [**[]string**](string.md)| Comma-separated list of threat IDs to delete (UUID format) | 

### Return type

[**InlineResponse2008**](inline_response_200_8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **BulkPatchThreatModelThreats**
> []Threat BulkPatchThreatModelThreats(ctx, body, threatModelId)
Bulk PATCH threats

Apply JSON Patch operations to multiple threats in a single request

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**ThreatsBulkBody**](ThreatsBulkBody.md)|  | 
  **threatModelId** | [**string**](.md)| Threat model identifier | 

### Return type

[**[]Threat**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

