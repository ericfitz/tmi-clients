# tmi_client.AdminUsersApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_admin_user_client_credential**](AdminUsersApi.md#create_admin_user_client_credential) | **POST** /admin/users/{internal_uuid}/client_credentials | Create a client credential for an automation user
[**create_automation_account**](AdminUsersApi.md#create_automation_account) | **POST** /admin/users/automation | Create an automation (service) account
[**delete_admin_user_client_credential**](AdminUsersApi.md#delete_admin_user_client_credential) | **DELETE** /admin/users/{internal_uuid}/client_credentials/{credential_id} | Delete a client credential for an automation user
[**list_admin_user_client_credentials**](AdminUsersApi.md#list_admin_user_client_credentials) | **GET** /admin/users/{internal_uuid}/client_credentials | List client credentials for an automation user

# **create_admin_user_client_credential**
> ClientCredentialResponse create_admin_user_client_credential(body, internal_uuid)

Create a client credential for an automation user

Creates a new client credential for the specified automation user. Only accessible for users with automation=true. The client_secret is returned only once. Admin operations bypass quota limits.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdminUsersApi(tmi_client.ApiClient(configuration))
body = tmi_client.InternalUuidClientCredentialsBody() # InternalUuidClientCredentialsBody | 
internal_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the user

try:
    # Create a client credential for an automation user
    api_response = api_instance.create_admin_user_client_credential(body, internal_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->create_admin_user_client_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InternalUuidClientCredentialsBody**](InternalUuidClientCredentialsBody.md)|  | 
 **internal_uuid** | [**str**](.md)| Internal system UUID of the user | 

### Return type

[**ClientCredentialResponse**](ClientCredentialResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_automation_account**
> CreateAutomationAccountResponse create_automation_account(body)

Create an automation (service) account

Creates a new automation account with the TMI provider, sets the automation flag, adds the account to the TMI Automation built-in group, and creates a client credential. The client secret is returned only once and cannot be retrieved later. Requires administrator privileges.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdminUsersApi(tmi_client.ApiClient(configuration))
body = tmi_client.CreateAutomationAccountRequest() # CreateAutomationAccountRequest | 

try:
    # Create an automation (service) account
    api_response = api_instance.create_automation_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->create_automation_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAutomationAccountRequest**](CreateAutomationAccountRequest.md)|  | 

### Return type

[**CreateAutomationAccountResponse**](CreateAutomationAccountResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_admin_user_client_credential**
> delete_admin_user_client_credential(internal_uuid, credential_id)

Delete a client credential for an automation user

Deletes and revokes a client credential for the specified automation user. Only accessible for users with automation=true.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdminUsersApi(tmi_client.ApiClient(configuration))
internal_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the user
credential_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal UUID of the client credential (the \"id\" field from the list response, not the \"client_id\")

try:
    # Delete a client credential for an automation user
    api_instance.delete_admin_user_client_credential(internal_uuid, credential_id)
except ApiException as e:
    print("Exception when calling AdminUsersApi->delete_admin_user_client_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_uuid** | [**str**](.md)| Internal system UUID of the user | 
 **credential_id** | [**str**](.md)| Internal UUID of the client credential (the \&quot;id\&quot; field from the list response, not the \&quot;client_id\&quot;) | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_admin_user_client_credentials**
> ListClientCredentialsResponse list_admin_user_client_credentials(internal_uuid, limit=limit, offset=offset)

List client credentials for an automation user

Lists all client credentials for the specified automation user. Only accessible for users with automation=true. Secrets are never returned.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdminUsersApi(tmi_client.ApiClient(configuration))
internal_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the user
limit = 50 # int | Maximum number of results to return (optional) (default to 50)
offset = 0 # int | Number of results to skip (optional) (default to 0)

try:
    # List client credentials for an automation user
    api_response = api_instance.list_admin_user_client_credentials(internal_uuid, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminUsersApi->list_admin_user_client_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_uuid** | [**str**](.md)| Internal system UUID of the user | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListClientCredentialsResponse**](ListClientCredentialsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

