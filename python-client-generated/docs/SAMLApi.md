# tmi_client.SAMLApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_saml_users**](SAMLApi.md#list_saml_users) | **GET** /saml/providers/{idp}/users | List SAML users for UI autocomplete

# **list_saml_users**
> object list_saml_users(idp)

List SAML users for UI autocomplete

Returns a lightweight list of active users for a specific SAML provider. Intended for UI autocomplete/search features. Only accessible to users from the same provider.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SAMLApi(tmi_client.ApiClient(configuration))
idp = 'idp_example' # str | SAML provider identifier (must start with \"saml_\")

try:
    # List SAML users for UI autocomplete
    api_response = api_instance.list_saml_users(idp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLApi->list_saml_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp** | **str**| SAML provider identifier (must start with \&quot;saml_\&quot;) | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

