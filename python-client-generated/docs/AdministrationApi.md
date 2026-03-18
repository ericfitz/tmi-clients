# tmi_client.AdministrationApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_member**](AdministrationApi.md#add_group_member) | **POST** /admin/groups/{internal_uuid}/members | Add member to group
[**create_admin_group**](AdministrationApi.md#create_admin_group) | **POST** /admin/groups | Create provider-independent group
[**delete_addon_invocation_quota**](AdministrationApi.md#delete_addon_invocation_quota) | **DELETE** /admin/quotas/addons/{user_id} | Delete addon invocation quota
[**delete_admin_group**](AdministrationApi.md#delete_admin_group) | **DELETE** /admin/groups/{internal_uuid} | Delete group
[**delete_admin_user**](AdministrationApi.md#delete_admin_user) | **DELETE** /admin/users/{internal_uuid} | Delete user
[**delete_system_setting**](AdministrationApi.md#delete_system_setting) | **DELETE** /admin/settings/{key} | Delete system setting
[**delete_user_api_quota**](AdministrationApi.md#delete_user_api_quota) | **DELETE** /admin/quotas/users/{user_id} | Delete user API quota
[**delete_webhook_quota**](AdministrationApi.md#delete_webhook_quota) | **DELETE** /admin/quotas/webhooks/{user_id} | Delete webhook quota
[**get_addon_invocation_quota**](AdministrationApi.md#get_addon_invocation_quota) | **GET** /admin/quotas/addons/{user_id} | Get addon invocation quota
[**get_admin_group**](AdministrationApi.md#get_admin_group) | **GET** /admin/groups/{internal_uuid} | Get group details
[**get_admin_user**](AdministrationApi.md#get_admin_user) | **GET** /admin/users/{internal_uuid} | Get user details
[**get_system_setting**](AdministrationApi.md#get_system_setting) | **GET** /admin/settings/{key} | Get system setting
[**get_user_api_quota**](AdministrationApi.md#get_user_api_quota) | **GET** /admin/quotas/users/{user_id} | Get user API quota
[**get_webhook_quota**](AdministrationApi.md#get_webhook_quota) | **GET** /admin/quotas/webhooks/{user_id} | Get webhook quota
[**list_addon_invocation_quotas**](AdministrationApi.md#list_addon_invocation_quotas) | **GET** /admin/quotas/addons | List all addon invocation quotas
[**list_admin_groups**](AdministrationApi.md#list_admin_groups) | **GET** /admin/groups | List groups
[**list_admin_users**](AdministrationApi.md#list_admin_users) | **GET** /admin/users | List users
[**list_group_members**](AdministrationApi.md#list_group_members) | **GET** /admin/groups/{internal_uuid}/members | List group members
[**list_system_settings**](AdministrationApi.md#list_system_settings) | **GET** /admin/settings | List system settings
[**list_user_api_quotas**](AdministrationApi.md#list_user_api_quotas) | **GET** /admin/quotas/users | List all user API quotas
[**list_webhook_quotas**](AdministrationApi.md#list_webhook_quotas) | **GET** /admin/quotas/webhooks | List all webhook quotas
[**migrate_system_settings**](AdministrationApi.md#migrate_system_settings) | **POST** /admin/settings/migrate | Migrate settings from configuration
[**reencrypt_system_settings**](AdministrationApi.md#reencrypt_system_settings) | **POST** /admin/settings/reencrypt | Re-encrypt all system settings
[**remove_group_member**](AdministrationApi.md#remove_group_member) | **DELETE** /admin/groups/{internal_uuid}/members/{member_uuid} | Remove member from group
[**transfer_admin_user_ownership**](AdministrationApi.md#transfer_admin_user_ownership) | **POST** /admin/users/{internal_uuid}/transfer | Transfer user ownership to another user
[**update_addon_invocation_quota**](AdministrationApi.md#update_addon_invocation_quota) | **PUT** /admin/quotas/addons/{user_id} | Update addon invocation quota
[**update_admin_group**](AdministrationApi.md#update_admin_group) | **PATCH** /admin/groups/{internal_uuid} | Update group metadata
[**update_admin_user**](AdministrationApi.md#update_admin_user) | **PATCH** /admin/users/{internal_uuid} | Update user metadata
[**update_system_setting**](AdministrationApi.md#update_system_setting) | **PUT** /admin/settings/{key} | Update system setting
[**update_user_api_quota**](AdministrationApi.md#update_user_api_quota) | **PUT** /admin/quotas/users/{user_id} | Update user API quota
[**update_webhook_quota**](AdministrationApi.md#update_webhook_quota) | **PUT** /admin/quotas/webhooks/{user_id} | Update webhook quota

# **add_group_member**
> GroupMember add_group_member(body, internal_uuid)

Add member to group

Adds a user to a group. The user must exist in the system. Cannot add members to the special 'everyone' pseudo-group.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
body = tmi_client.AddGroupMemberRequest() # AddGroupMemberRequest | Group membership update
internal_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the user

try:
    # Add member to group
    api_response = api_instance.add_group_member(body, internal_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->add_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddGroupMemberRequest**](AddGroupMemberRequest.md)| Group membership update | 
 **internal_uuid** | [**str**](.md)| Internal system UUID of the user | 

### Return type

[**GroupMember**](GroupMember.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_admin_group**
> AdminGroup create_admin_group(body)

Create provider-independent group

Creates a new provider-independent group (provider=\"*\"). These groups can be used across all providers for authorization and administration.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
body = tmi_client.CreateAdminGroupRequest() # CreateAdminGroupRequest | Group creation request

try:
    # Create provider-independent group
    api_response = api_instance.create_admin_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->create_admin_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAdminGroupRequest**](CreateAdminGroupRequest.md)| Group creation request | 

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_addon_invocation_quota**
> delete_addon_invocation_quota(user_id)

Delete addon invocation quota

Deletes the custom addon invocation quota for a user, reverting to system defaults

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | User ID

try:
    # Delete addon invocation quota
    api_instance.delete_addon_invocation_quota(user_id)
except ApiException as e:
    print("Exception when calling AdministrationApi->delete_addon_invocation_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| User ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_admin_group**
> delete_admin_group(internal_uuid)

Delete group

Deletes a TMI-managed group and handles threat model cleanup. Protected groups like 'everyone' cannot be deleted.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
internal_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the user

try:
    # Delete group
    api_instance.delete_admin_group(internal_uuid)
except ApiException as e:
    print("Exception when calling AdministrationApi->delete_admin_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_uuid** | [**str**](.md)| Internal system UUID of the user | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_admin_user**
> delete_admin_user(internal_uuid)

Delete user

Deletes a user and all associated data. Transfers sole-owned threat models or deletes them if no other owners exist.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
internal_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the user

try:
    # Delete user
    api_instance.delete_admin_user(internal_uuid)
except ApiException as e:
    print("Exception when calling AdministrationApi->delete_admin_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_uuid** | [**str**](.md)| Internal system UUID of the user | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_system_setting**
> delete_system_setting(key)

Delete system setting

Deletes a system setting. Requires administrator privileges.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
key = 'key_example' # str | The setting key

try:
    # Delete system setting
    api_instance.delete_system_setting(key)
except ApiException as e:
    print("Exception when calling AdministrationApi->delete_system_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The setting key | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_api_quota**
> delete_user_api_quota(user_id)

Delete user API quota

Deletes the custom API quota for a user, reverting to system defaults

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | User ID

try:
    # Delete user API quota
    api_instance.delete_user_api_quota(user_id)
except ApiException as e:
    print("Exception when calling AdministrationApi->delete_user_api_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| User ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_quota**
> delete_webhook_quota(user_id)

Delete webhook quota

Deletes the custom webhook quota for a user, reverting to system defaults

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | User ID

try:
    # Delete webhook quota
    api_instance.delete_webhook_quota(user_id)
except ApiException as e:
    print("Exception when calling AdministrationApi->delete_webhook_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| User ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addon_invocation_quota**
> AddonInvocationQuota get_addon_invocation_quota(user_id)

Get addon invocation quota

Retrieves the addon invocation quota for a specific user

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | User ID

try:
    # Get addon invocation quota
    api_response = api_instance.get_addon_invocation_quota(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_addon_invocation_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| User ID | 

### Return type

[**AddonInvocationQuota**](AddonInvocationQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_group**
> AdminGroup get_admin_group(internal_uuid)

Get group details

Returns detailed information about a specific group, including enriched data (usage in authorizations and admin grants).

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
internal_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the user

try:
    # Get group details
    api_response = api_instance.get_admin_group(internal_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_admin_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_uuid** | [**str**](.md)| Internal system UUID of the user | 

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_user**
> AdminUser get_admin_user(internal_uuid)

Get user details

Returns detailed information about a specific user, including enriched data (admin status, groups, threat model counts).

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
internal_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the user

try:
    # Get user details
    api_response = api_instance.get_admin_user(internal_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_admin_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_uuid** | [**str**](.md)| Internal system UUID of the user | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_setting**
> SystemSetting get_system_setting(key)

Get system setting

Returns a specific system setting by key. Requires administrator privileges.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
key = 'key_example' # str | The setting key

try:
    # Get system setting
    api_response = api_instance.get_system_setting(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_system_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The setting key | 

### Return type

[**SystemSetting**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_api_quota**
> UserAPIQuota get_user_api_quota(user_id)

Get user API quota

Retrieves the API rate limit quota for a specific user

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | User ID

try:
    # Get user API quota
    api_response = api_instance.get_user_api_quota(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_user_api_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| User ID | 

### Return type

[**UserAPIQuota**](UserAPIQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_quota**
> WebhookQuota get_webhook_quota(user_id)

Get webhook quota

Retrieves the webhook quota for a specific user

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | User ID

try:
    # Get webhook quota
    api_response = api_instance.get_webhook_quota(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_webhook_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| User ID | 

### Return type

[**WebhookQuota**](WebhookQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_addon_invocation_quotas**
> ListAddonQuotasResponse list_addon_invocation_quotas(limit=limit, offset=offset)

List all addon invocation quotas

Retrieves all custom addon invocation quotas (users with non-default quotas)

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
limit = 50 # int | Maximum number of results to return (optional) (default to 50)
offset = 0 # int | Number of results to skip (optional) (default to 0)

try:
    # List all addon invocation quotas
    api_response = api_instance.list_addon_invocation_quotas(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->list_addon_invocation_quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAddonQuotasResponse**](ListAddonQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_admin_groups**
> AdminGroupListResponse list_admin_groups(provider=provider, group_name=group_name, used_in_authorizations=used_in_authorizations, limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order)

List groups

Returns a paginated list of groups with optional filtering by provider, name, and usage. Includes enriched data (usage in authorizations and admin grants).

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
provider = 'provider_example' # str | Filter by OAuth/SAML provider (optional)
group_name = 'group_name_example' # str | Filter by group name (case-insensitive substring match) (optional)
used_in_authorizations = true # bool | Filter groups used (true) or not used (false) in authorizations (optional)
limit = 50 # int | Maximum number of results to return (optional) (default to 50)
offset = 0 # int | Number of results to skip (optional) (default to 0)
sort_by = 'created_at' # str | Field to sort by (optional) (default to created_at)
sort_order = 'desc' # str | Sort direction (optional) (default to desc)

try:
    # List groups
    api_response = api_instance.list_admin_groups(provider=provider, group_name=group_name, used_in_authorizations=used_in_authorizations, limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->list_admin_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Filter by OAuth/SAML provider | [optional] 
 **group_name** | **str**| Filter by group name (case-insensitive substring match) | [optional] 
 **used_in_authorizations** | **bool**| Filter groups used (true) or not used (false) in authorizations | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **sort_by** | **str**| Field to sort by | [optional] [default to created_at]
 **sort_order** | **str**| Sort direction | [optional] [default to desc]

### Return type

[**AdminGroupListResponse**](AdminGroupListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_admin_users**
> AdminUserListResponse list_admin_users(provider=provider, email=email, created_after=created_after, created_before=created_before, last_login_after=last_login_after, last_login_before=last_login_before, limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order)

List users

Returns a paginated list of users with optional filtering by provider, email, and date ranges. Includes enriched data (admin status, groups, threat model counts).

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
provider = 'provider_example' # str | Filter by OAuth/SAML provider (optional)
email = 'email_example' # str | Filter by email (case-insensitive substring match) (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter users created after this timestamp (RFC3339) (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter users created before this timestamp (RFC3339) (optional)
last_login_after = '2013-10-20T19:20:30+01:00' # datetime | Filter users who logged in after this timestamp (RFC3339) (optional)
last_login_before = '2013-10-20T19:20:30+01:00' # datetime | Filter users who logged in before this timestamp (RFC3339) (optional)
limit = 50 # int | Maximum number of results to return (optional) (default to 50)
offset = 0 # int | Number of results to skip (optional) (default to 0)
sort_by = 'created_at' # str | Field to sort by (optional) (default to created_at)
sort_order = 'desc' # str | Sort direction (optional) (default to desc)

try:
    # List users
    api_response = api_instance.list_admin_users(provider=provider, email=email, created_after=created_after, created_before=created_before, last_login_after=last_login_after, last_login_before=last_login_before, limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->list_admin_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Filter by OAuth/SAML provider | [optional] 
 **email** | **str**| Filter by email (case-insensitive substring match) | [optional] 
 **created_after** | **datetime**| Filter users created after this timestamp (RFC3339) | [optional] 
 **created_before** | **datetime**| Filter users created before this timestamp (RFC3339) | [optional] 
 **last_login_after** | **datetime**| Filter users who logged in after this timestamp (RFC3339) | [optional] 
 **last_login_before** | **datetime**| Filter users who logged in before this timestamp (RFC3339) | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **sort_by** | **str**| Field to sort by | [optional] [default to created_at]
 **sort_order** | **str**| Sort direction | [optional] [default to desc]

### Return type

[**AdminUserListResponse**](AdminUserListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_members**
> GroupMemberListResponse list_group_members(internal_uuid, limit=limit, offset=offset)

List group members

Returns a paginated list of users who are members of the specified group. Includes user details (email, name, provider information).

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
internal_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the user
limit = 50 # int | Maximum number of results to return (optional) (default to 50)
offset = 0 # int | Number of results to skip (optional) (default to 0)

try:
    # List group members
    api_response = api_instance.list_group_members(internal_uuid, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->list_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_uuid** | [**str**](.md)| Internal system UUID of the user | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**GroupMemberListResponse**](GroupMemberListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_system_settings**
> list[SystemSetting] list_system_settings()

List system settings

Returns all system settings. Requires administrator privileges.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))

try:
    # List system settings
    api_response = api_instance.list_system_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->list_system_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SystemSetting]**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_api_quotas**
> ListUserQuotasResponse list_user_api_quotas(limit=limit, offset=offset)

List all user API quotas

Retrieves all custom API rate limit quotas (users with non-default quotas)

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
limit = 50 # int | Maximum number of results to return (optional) (default to 50)
offset = 0 # int | Number of results to skip (optional) (default to 0)

try:
    # List all user API quotas
    api_response = api_instance.list_user_api_quotas(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->list_user_api_quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListUserQuotasResponse**](ListUserQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook_quotas**
> ListWebhookQuotasResponse list_webhook_quotas(limit=limit, offset=offset)

List all webhook quotas

Retrieves all custom webhook quotas (users with non-default quotas)

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
limit = 50 # int | Maximum number of results to return (optional) (default to 50)
offset = 0 # int | Number of results to skip (optional) (default to 0)

try:
    # List all webhook quotas
    api_response = api_instance.list_webhook_quotas(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->list_webhook_quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListWebhookQuotasResponse**](ListWebhookQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_system_settings**
> InlineResponse20010 migrate_system_settings(overwrite=overwrite)

Migrate settings from configuration

Migrates settings from the server configuration (config file or environment variables) to the database. When overwrite is false (default), only settings that don't already exist in the database are added. When overwrite is true, all settings are imported, overwriting existing values. Requires administrator privileges.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
overwrite = false # bool | If true, overwrite existing settings in the database with values from configuration. If false or omitted, only add settings that don't already exist. (optional) (default to false)

try:
    # Migrate settings from configuration
    api_response = api_instance.migrate_system_settings(overwrite=overwrite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->migrate_system_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **overwrite** | **bool**| If true, overwrite existing settings in the database with values from configuration. If false or omitted, only add settings that don&#x27;t already exist. | [optional] [default to false]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reencrypt_system_settings**
> InlineResponse20011 reencrypt_system_settings()

Re-encrypt all system settings

Re-encrypts all system settings with the current encryption key. Use this after rotating the encryption key or when first enabling encryption on existing settings. Requires administrator privileges. Settings that cannot be decrypted are reported as errors but do not prevent other settings from being processed.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))

try:
    # Re-encrypt all system settings
    api_response = api_instance.reencrypt_system_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->reencrypt_system_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_member**
> remove_group_member(internal_uuid, member_uuid, subject_type=subject_type)

Remove member from group

Removes a user or nested group from a group. Use the subject_type query parameter to specify whether the member is a user (default) or a group. Cannot remove members from the special 'everyone' pseudo-group.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
internal_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the user
member_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the member to remove (user UUID when subject_type is user, group UUID when subject_type is group)
subject_type = 'user' # str | Type of member to remove: 'user' (default) for a user member, 'group' for a nested group member (optional) (default to user)

try:
    # Remove member from group
    api_instance.remove_group_member(internal_uuid, member_uuid, subject_type=subject_type)
except ApiException as e:
    print("Exception when calling AdministrationApi->remove_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_uuid** | [**str**](.md)| Internal system UUID of the user | 
 **member_uuid** | [**str**](.md)| Internal system UUID of the member to remove (user UUID when subject_type is user, group UUID when subject_type is group) | 
 **subject_type** | **str**| Type of member to remove: &#x27;user&#x27; (default) for a user member, &#x27;group&#x27; for a nested group member | [optional] [default to user]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_admin_user_ownership**
> TransferOwnershipResult transfer_admin_user_ownership(body, internal_uuid)

Transfer user ownership to another user

Transfers ownership of all threat models and survey responses owned by the specified user to the target user. The source user is downgraded to writer role on all transferred items. Requires administrator privileges.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
body = tmi_client.TransferOwnershipRequest() # TransferOwnershipRequest | Ownership transfer request specifying the target user
internal_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the user

try:
    # Transfer user ownership to another user
    api_response = api_instance.transfer_admin_user_ownership(body, internal_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->transfer_admin_user_ownership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransferOwnershipRequest**](TransferOwnershipRequest.md)| Ownership transfer request specifying the target user | 
 **internal_uuid** | [**str**](.md)| Internal system UUID of the user | 

### Return type

[**TransferOwnershipResult**](TransferOwnershipResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_addon_invocation_quota**
> AddonInvocationQuota update_addon_invocation_quota(body, user_id)

Update addon invocation quota

Creates or updates the addon invocation quota for a specific user

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
body = tmi_client.AddonQuotaUpdate() # AddonQuotaUpdate | Addon quota update configuration
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | User ID

try:
    # Update addon invocation quota
    api_response = api_instance.update_addon_invocation_quota(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->update_addon_invocation_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddonQuotaUpdate**](AddonQuotaUpdate.md)| Addon quota update configuration | 
 **user_id** | [**str**](.md)| User ID | 

### Return type

[**AddonInvocationQuota**](AddonInvocationQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_admin_group**
> AdminGroup update_admin_group(body, internal_uuid)

Update group metadata

Updates group metadata fields (name, description). Only provided fields are updated.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
body = tmi_client.UpdateAdminGroupRequest() # UpdateAdminGroupRequest | Group update details
internal_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the user

try:
    # Update group metadata
    api_response = api_instance.update_admin_group(body, internal_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->update_admin_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAdminGroupRequest**](UpdateAdminGroupRequest.md)| Group update details | 
 **internal_uuid** | [**str**](.md)| Internal system UUID of the user | 

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_admin_user**
> AdminUser update_admin_user(body, internal_uuid)

Update user metadata

Updates user metadata fields (email, name, email_verified). Only provided fields are updated.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
body = tmi_client.UpdateAdminUserRequest() # UpdateAdminUserRequest | User profile update
internal_uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Internal system UUID of the user

try:
    # Update user metadata
    api_response = api_instance.update_admin_user(body, internal_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->update_admin_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAdminUserRequest**](UpdateAdminUserRequest.md)| User profile update | 
 **internal_uuid** | [**str**](.md)| Internal system UUID of the user | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_system_setting**
> SystemSetting update_system_setting(body, key)

Update system setting

Creates or updates a system setting. Requires administrator privileges.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
body = tmi_client.SystemSettingUpdate() # SystemSettingUpdate | The system setting value to create or update
key = 'key_example' # str | The setting key

try:
    # Update system setting
    api_response = api_instance.update_system_setting(body, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->update_system_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemSettingUpdate**](SystemSettingUpdate.md)| The system setting value to create or update | 
 **key** | **str**| The setting key | 

### Return type

[**SystemSetting**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_api_quota**
> UserAPIQuota update_user_api_quota(body, user_id)

Update user API quota

Creates or updates the API rate limit quota for a specific user

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
body = tmi_client.UserQuotaUpdate() # UserQuotaUpdate | User quota update configuration
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | User ID

try:
    # Update user API quota
    api_response = api_instance.update_user_api_quota(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->update_user_api_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserQuotaUpdate**](UserQuotaUpdate.md)| User quota update configuration | 
 **user_id** | [**str**](.md)| User ID | 

### Return type

[**UserAPIQuota**](UserAPIQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_quota**
> WebhookQuota update_webhook_quota(body, user_id)

Update webhook quota

Creates or updates the webhook quota for a specific user

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AdministrationApi(tmi_client.ApiClient(configuration))
body = tmi_client.WebhookQuotaUpdate() # WebhookQuotaUpdate | Webhook quota update configuration
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | User ID

try:
    # Update webhook quota
    api_response = api_instance.update_webhook_quota(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->update_webhook_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookQuotaUpdate**](WebhookQuotaUpdate.md)| Webhook quota update configuration | 
 **user_id** | [**str**](.md)| User ID | 

### Return type

[**WebhookQuota**](WebhookQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

