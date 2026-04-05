# tmi_client.AdminUsersApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_admin_user_client_credential**](AdminUsersApi.md#create_admin_user_client_credential) | **POST** /admin/users/{internal_uuid}/client_credentials | Create a client credential for an automation user
[**create_automation_account**](AdminUsersApi.md#create_automation_account) | **POST** /admin/users/automation | Create an automation (service) account
[**delete_admin_user_client_credential**](AdminUsersApi.md#delete_admin_user_client_credential) | **DELETE** /admin/users/{internal_uuid}/client_credentials/{credential_id} | Delete a client credential for an automation user
[**list_admin_user_client_credentials**](AdminUsersApi.md#list_admin_user_client_credentials) | **GET** /admin/users/{internal_uuid}/client_credentials | List client credentials for an automation user


# **create_admin_user_client_credential**
> ClientCredentialResponse create_admin_user_client_credential(internal_uuid, create_current_user_client_credential_request)

Create a client credential for an automation user

Creates a new client credential for the specified automation user. Only accessible for users with automation=true. The client_secret is returned only once. Admin operations bypass quota limits.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.client_credential_response import ClientCredentialResponse
from tmi_client.models.create_current_user_client_credential_request import CreateCurrentUserClientCredentialRequest
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.AdminUsersApi(api_client)
    internal_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Internal system UUID of the user
    create_current_user_client_credential_request = tmi_client.CreateCurrentUserClientCredentialRequest() # CreateCurrentUserClientCredentialRequest | Client credential creation parameters

    try:
        # Create a client credential for an automation user
        api_response = api_instance.create_admin_user_client_credential(internal_uuid, create_current_user_client_credential_request)
        print("The response of AdminUsersApi->create_admin_user_client_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->create_admin_user_client_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_uuid** | **UUID**| Internal system UUID of the user | 
 **create_current_user_client_credential_request** | [**CreateCurrentUserClientCredentialRequest**](CreateCurrentUserClientCredentialRequest.md)| Client credential creation parameters | 

### Return type

[**ClientCredentialResponse**](ClientCredentialResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Client credential created. WARNING: client_secret is only returned once. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Invalid request (validation error) |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Not authenticated |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Not authorized or target user is not an automation account |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | User not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_automation_account**
> CreateAutomationAccountResponse create_automation_account(create_automation_account_request)

Create an automation (service) account

Creates a new automation account with the TMI provider, sets the automation flag, adds the account to the TMI Automation built-in group, and creates a client credential. The client secret is returned only once and cannot be retrieved later. Requires administrator privileges.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.create_automation_account_request import CreateAutomationAccountRequest
from tmi_client.models.create_automation_account_response import CreateAutomationAccountResponse
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.AdminUsersApi(api_client)
    create_automation_account_request = tmi_client.CreateAutomationAccountRequest() # CreateAutomationAccountRequest | Automation account creation parameters

    try:
        # Create an automation (service) account
        api_response = api_instance.create_automation_account(create_automation_account_request)
        print("The response of AdminUsersApi->create_automation_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->create_automation_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_automation_account_request** | [**CreateAutomationAccountRequest**](CreateAutomationAccountRequest.md)| Automation account creation parameters | 

### Return type

[**CreateAutomationAccountResponse**](CreateAutomationAccountResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Automation account created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Invalid request (validation error) |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Not authenticated |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Not authorized (requires administrator role) |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**409** | Conflict - an account with the same email or provider ID already exists |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_admin_user_client_credential**
> delete_admin_user_client_credential(internal_uuid, credential_id)

Delete a client credential for an automation user

Deletes and revokes a client credential for the specified automation user. Only accessible for users with automation=true.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.AdminUsersApi(api_client)
    internal_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Internal system UUID of the user
    credential_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Internal UUID of the client credential (the \"id\" field from the list response, not the \"client_id\")

    try:
        # Delete a client credential for an automation user
        api_instance.delete_admin_user_client_credential(internal_uuid, credential_id)
    except Exception as e:
        print("Exception when calling AdminUsersApi->delete_admin_user_client_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_uuid** | **UUID**| Internal system UUID of the user | 
 **credential_id** | **UUID**| Internal UUID of the client credential (the \&quot;id\&quot; field from the list response, not the \&quot;client_id\&quot;) | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Client credential deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Not authenticated |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Not authorized or target user is not an automation account |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | User or credential not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_admin_user_client_credentials**
> ListClientCredentialsResponse list_admin_user_client_credentials(internal_uuid, limit=limit, offset=offset)

List client credentials for an automation user

Lists all client credentials for the specified automation user. Only accessible for users with automation=true. Secrets are never returned.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.list_client_credentials_response import ListClientCredentialsResponse
from tmi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tmi.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = tmi_client.Configuration(
    host = "https://api.tmi.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = tmi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tmi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tmi_client.AdminUsersApi(api_client)
    internal_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Internal system UUID of the user
    limit = 50 # int | Maximum number of results to return (optional) (default to 50)
    offset = 0 # int | Number of results to skip (optional) (default to 0)

    try:
        # List client credentials for an automation user
        api_response = api_instance.list_admin_user_client_credentials(internal_uuid, limit=limit, offset=offset)
        print("The response of AdminUsersApi->list_admin_user_client_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->list_admin_user_client_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_uuid** | **UUID**| Internal system UUID of the user | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListClientCredentialsResponse**](ListClientCredentialsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of client credentials (without secrets) |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Not authenticated |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Not authorized or target user is not an automation account |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | User not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid query parameters |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

