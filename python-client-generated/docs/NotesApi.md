# tmi_client.NotesApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_threat_model_note**](NotesApi.md#patch_threat_model_note) | **PATCH** /threat_models/{threat_model_id}/notes/{note_id} | Partially update note


# **patch_threat_model_note**
> Note patch_threat_model_note(threat_model_id, note_id, json_patch_document_inner)

Partially update note

Apply JSON Patch operations to partially update a note

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import tmi_client
from tmi_client.models.json_patch_document_inner import JsonPatchDocumentInner
from tmi_client.models.note import Note
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
    api_instance = tmi_client.NotesApi(api_client)
    threat_model_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Threat model identifier
    note_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Note identifier
    json_patch_document_inner = [{"op":"replace","path":"/name","value":"Updated Name"},{"op":"add","path":"/description","value":"New description"}] # List[JsonPatchDocumentInner] | JSON Patch operations to apply to the note

    try:
        # Partially update note
        api_response = api_instance.patch_threat_model_note(threat_model_id, note_id, json_patch_document_inner)
        print("The response of NotesApi->patch_threat_model_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->patch_threat_model_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | **UUID**| Threat model identifier | 
 **note_id** | **UUID**| Note identifier | 
 **json_patch_document_inner** | [**List[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| JSON Patch operations to apply to the note | 

### Return type

[**Note**](Note.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully patched note |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**401** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**403** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**404** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
**429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
**500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

