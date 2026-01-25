# tmi_client.UserAccountApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_current_user_preferences**](UserAccountApi.md#create_current_user_preferences) | **POST** /me/preferences | Create user preferences
[**get_current_user_preferences**](UserAccountApi.md#get_current_user_preferences) | **GET** /me/preferences | Get user preferences
[**update_current_user_preferences**](UserAccountApi.md#update_current_user_preferences) | **PUT** /me/preferences | Update user preferences

# **create_current_user_preferences**
> UserPreferences create_current_user_preferences(body)

Create user preferences

Creates preferences for the current user. Fails with 409 Conflict if preferences already exist (use PUT to update).

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.UserAccountApi(tmi_client.ApiClient(configuration))
body = NULL # dict(str, dict(str, object)) | 

try:
    # Create user preferences
    api_response = api_instance.create_current_user_preferences(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountApi->create_current_user_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, dict(str, object))**](dict.md)|  | 

### Return type

[**UserPreferences**](UserPreferences.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_preferences**
> UserPreferences get_current_user_preferences()

Get user preferences

Retrieves the current user's preferences. Returns an empty object {} if no preferences have been set.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.UserAccountApi(tmi_client.ApiClient(configuration))

try:
    # Get user preferences
    api_response = api_instance.get_current_user_preferences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountApi->get_current_user_preferences: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserPreferences**](UserPreferences.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_user_preferences**
> UserPreferences update_current_user_preferences(body)

Update user preferences

Creates or replaces the current user's preferences. This is an upsert operation - creates if not exists, replaces entirely if exists.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.UserAccountApi(tmi_client.ApiClient(configuration))
body = NULL # dict(str, dict(str, object)) | 

try:
    # Update user preferences
    api_response = api_instance.update_current_user_preferences(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountApi->update_current_user_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, dict(str, object))**](dict.md)|  | 

### Return type

[**UserPreferences**](UserPreferences.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

