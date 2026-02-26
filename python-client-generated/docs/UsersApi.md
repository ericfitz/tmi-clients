# tmi_client.UsersApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_account**](UsersApi.md#delete_user_account) | **DELETE** /me | Delete authenticated user account and all data
[**logout_current_user**](UsersApi.md#logout_current_user) | **POST** /me/logout | Logout current user
[**transfer_current_user_ownership**](UsersApi.md#transfer_current_user_ownership) | **POST** /me/transfer | Transfer ownership of all owned resources

# **delete_user_account**
> DeletionChallenge delete_user_account(challenge=challenge)

Delete authenticated user account and all data

Two-step deletion process: 1. First call (no challenge parameter) - Returns challenge string 2. Second call (with challenge parameter) - Confirms deletion  Ownership behavior: - Shared threat models: Transfers ownership to another owner from authorization list - Unshared threat models: Deletes completely along with all child resources

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.UsersApi(tmi_client.ApiClient(configuration))
challenge = 'challenge_example' # str | Challenge string from first request (step 2 only). Must match exactly. (optional)

try:
    # Delete authenticated user account and all data
    api_response = api_instance.delete_user_account(challenge=challenge)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge** | **str**| Challenge string from first request (step 2 only). Must match exactly. | [optional] 

### Return type

[**DeletionChallenge**](DeletionChallenge.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_current_user**
> logout_current_user()

Logout current user

Revokes the authenticated user's current JWT token. This is a convenience endpoint that automatically revokes the token used to authenticate the request, without requiring the token to be passed in the request body. The token is immediately added to the blacklist and cannot be used for further requests.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.UsersApi(tmi_client.ApiClient(configuration))

try:
    # Logout current user
    api_instance.logout_current_user()
except ApiException as e:
    print("Exception when calling UsersApi->logout_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_current_user_ownership**
> TransferOwnershipResult transfer_current_user_ownership(body)

Transfer ownership of all owned resources

Transfers ownership of all threat models and survey responses owned by the current user to the specified target user. The current user is downgraded to writer role on all transferred items.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.UsersApi(tmi_client.ApiClient(configuration))
body = tmi_client.TransferOwnershipRequest() # TransferOwnershipRequest | Ownership transfer request specifying the target user

try:
    # Transfer ownership of all owned resources
    api_response = api_instance.transfer_current_user_ownership(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->transfer_current_user_ownership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransferOwnershipRequest**](TransferOwnershipRequest.md)| Ownership transfer request specifying the target user | 

### Return type

[**TransferOwnershipResult**](TransferOwnershipResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

