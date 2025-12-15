# TmiThreatModelingImprovedApi.SAMLApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listSAMLUsers**](SAMLApi.md#listSAMLUsers) | **GET** /saml/providers/{idp}/users | List SAML users for UI autocomplete

<a name="listSAMLUsers"></a>
# **listSAMLUsers**
> Object listSAMLUsers(idp)

List SAML users for UI autocomplete

Returns a lightweight list of active users for a specific SAML provider. Intended for UI autocomplete/search features. Only accessible to users from the same provider.

### Example
```javascript
import {TmiThreatModelingImprovedApi} from 'tmi__threat_modeling_improved_api';
let defaultClient = TmiThreatModelingImprovedApi.ApiClient.instance;


let apiInstance = new TmiThreatModelingImprovedApi.SAMLApi();
let idp = "idp_example"; // String | Identity provider ID (e.g., saml_okta, saml_azure)

apiInstance.listSAMLUsers(idp, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp** | **String**| Identity provider ID (e.g., saml_okta, saml_azure) | 

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

