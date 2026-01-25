# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateCurrentUserPreferences**](UserAccountApi.md#CreateCurrentUserPreferences) | **Post** /me/preferences | Create user preferences
[**GetCurrentUserPreferences**](UserAccountApi.md#GetCurrentUserPreferences) | **Get** /me/preferences | Get user preferences
[**UpdateCurrentUserPreferences**](UserAccountApi.md#UpdateCurrentUserPreferences) | **Put** /me/preferences | Update user preferences

# **CreateCurrentUserPreferences**
> map[string]ModelMap CreateCurrentUserPreferences(ctx, body)
Create user preferences

Creates preferences for the current user. Fails with 409 Conflict if preferences already exist (use PUT to update).

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**map[string]ModelMap**](map.md)|  | 

### Return type

[**map[string]ModelMap**](map.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCurrentUserPreferences**
> map[string]ModelMap GetCurrentUserPreferences(ctx, )
Get user preferences

Retrieves the current user's preferences. Returns an empty object {} if no preferences have been set.

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**map[string]ModelMap**](map.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateCurrentUserPreferences**
> map[string]ModelMap UpdateCurrentUserPreferences(ctx, body)
Update user preferences

Creates or replaces the current user's preferences. This is an upsert operation - creates if not exists, replaces entirely if exists.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**map[string]ModelMap**](map.md)|  | 

### Return type

[**map[string]ModelMap**](map.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

