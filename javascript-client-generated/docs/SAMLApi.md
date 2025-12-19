# TmiJsClient.SAMLApi

All URIs are relative to *https://api.tmi.dev*

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
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.SAMLApi();
let idp = "idp_example"; // String | Identity provider ID (e.g., saml_okta, saml_azure)

apiInstance.listSAMLUsers(idp).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
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

