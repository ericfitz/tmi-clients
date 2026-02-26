# tmi_client.SurveyIntakeApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_intake_survey_response_metadata**](SurveyIntakeApi.md#bulk_create_intake_survey_response_metadata) | **POST** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk create metadata for a survey response
[**bulk_replace_intake_survey_response_metadata**](SurveyIntakeApi.md#bulk_replace_intake_survey_response_metadata) | **PUT** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk replace metadata for a survey response
[**bulk_upsert_intake_survey_response_metadata**](SurveyIntakeApi.md#bulk_upsert_intake_survey_response_metadata) | **PATCH** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk upsert metadata for a survey response
[**create_intake_survey_response**](SurveyIntakeApi.md#create_intake_survey_response) | **POST** /intake/survey_responses | Create survey response
[**create_intake_survey_response_metadata**](SurveyIntakeApi.md#create_intake_survey_response_metadata) | **POST** /intake/survey_responses/{survey_response_id}/metadata | Add metadata to a survey response
[**delete_intake_survey_response**](SurveyIntakeApi.md#delete_intake_survey_response) | **DELETE** /intake/survey_responses/{survey_response_id} | Delete survey response
[**delete_intake_survey_response_metadata_by_key**](SurveyIntakeApi.md#delete_intake_survey_response_metadata_by_key) | **DELETE** /intake/survey_responses/{survey_response_id}/metadata/{key} | Delete metadata by key for a survey response
[**get_intake_survey**](SurveyIntakeApi.md#get_intake_survey) | **GET** /intake/surveys/{survey_id} | Get an available survey
[**get_intake_survey_response**](SurveyIntakeApi.md#get_intake_survey_response) | **GET** /intake/survey_responses/{survey_response_id} | Get survey response
[**get_intake_survey_response_metadata**](SurveyIntakeApi.md#get_intake_survey_response_metadata) | **GET** /intake/survey_responses/{survey_response_id}/metadata | Get all metadata for a survey response
[**get_intake_survey_response_metadata_by_key**](SurveyIntakeApi.md#get_intake_survey_response_metadata_by_key) | **GET** /intake/survey_responses/{survey_response_id}/metadata/{key} | Get metadata by key for a survey response
[**get_intake_survey_response_triage_note**](SurveyIntakeApi.md#get_intake_survey_response_triage_note) | **GET** /intake/survey_responses/{survey_response_id}/triage_notes/{triage_note_id} | Get a specific triage note
[**list_intake_survey_response_triage_notes**](SurveyIntakeApi.md#list_intake_survey_response_triage_notes) | **GET** /intake/survey_responses/{survey_response_id}/triage_notes | List triage notes for a survey response
[**list_intake_survey_responses**](SurveyIntakeApi.md#list_intake_survey_responses) | **GET** /intake/survey_responses | List user&#x27;s survey responses
[**list_intake_surveys**](SurveyIntakeApi.md#list_intake_surveys) | **GET** /intake/surveys | List available surveys
[**patch_intake_survey_response**](SurveyIntakeApi.md#patch_intake_survey_response) | **PATCH** /intake/survey_responses/{survey_response_id} | Partial update survey response
[**update_intake_survey_response**](SurveyIntakeApi.md#update_intake_survey_response) | **PUT** /intake/survey_responses/{survey_response_id} | Update survey response
[**update_intake_survey_response_metadata_by_key**](SurveyIntakeApi.md#update_intake_survey_response_metadata_by_key) | **PUT** /intake/survey_responses/{survey_response_id}/metadata/{key} | Update metadata by key for a survey response

# **bulk_create_intake_survey_response_metadata**
> list[Metadata] bulk_create_intake_survey_response_metadata(body, survey_response_id)

Bulk create metadata for a survey response

Creates multiple metadata key-value pairs for the specified survey response. Returns 409 Conflict if any of the specified keys already exist.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
body = [tmi_client.Metadata()] # list[Metadata] | Array of metadata key-value pairs to create
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Bulk create metadata for a survey response
    api_response = api_instance.bulk_create_intake_survey_response_metadata(body, survey_response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->bulk_create_intake_survey_response_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Metadata]**](Metadata.md)| Array of metadata key-value pairs to create | 
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_replace_intake_survey_response_metadata**
> list[Metadata] bulk_replace_intake_survey_response_metadata(body, survey_response_id)

Bulk replace metadata for a survey response

Replaces all metadata for the entity. All existing metadata is deleted and replaced with the provided set. To clear all metadata, send an empty array.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
body = [tmi_client.Metadata()] # list[Metadata] | Complete set of metadata key-value pairs to replace existing metadata
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Bulk replace metadata for a survey response
    api_response = api_instance.bulk_replace_intake_survey_response_metadata(body, survey_response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->bulk_replace_intake_survey_response_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Metadata]**](Metadata.md)| Complete set of metadata key-value pairs to replace existing metadata | 
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_intake_survey_response_metadata**
> list[Metadata] bulk_upsert_intake_survey_response_metadata(body, survey_response_id)

Bulk upsert metadata for a survey response

Creates or updates only the provided metadata keys. Keys not included in the request are left unchanged. This is a merge/upsert operation.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
body = [tmi_client.Metadata()] # list[Metadata] | Metadata key-value pairs to create or update (merge)
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Bulk upsert metadata for a survey response
    api_response = api_instance.bulk_upsert_intake_survey_response_metadata(body, survey_response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->bulk_upsert_intake_survey_response_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Metadata]**](Metadata.md)| Metadata key-value pairs to create or update (merge) | 
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_intake_survey_response**
> SurveyResponse create_intake_survey_response(body)

Create survey response

Creates a new survey response in draft status. The secret_project flag can only be set here.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
body = tmi_client.SurveyResponseCreateRequest() # SurveyResponseCreateRequest | Survey response to create

try:
    # Create survey response
    api_response = api_instance.create_intake_survey_response(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->create_intake_survey_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SurveyResponseCreateRequest**](SurveyResponseCreateRequest.md)| Survey response to create | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_intake_survey_response_metadata**
> Metadata create_intake_survey_response_metadata(body, survey_response_id)

Add metadata to a survey response

Adds a new metadata key-value pair to the specified survey response. Returns 409 Conflict if the key already exists.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
body = tmi_client.Metadata() # Metadata | Metadata key-value pair to create
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Add metadata to a survey response
    api_response = api_instance.create_intake_survey_response_metadata(body, survey_response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->create_intake_survey_response_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata key-value pair to create | 
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_intake_survey_response**
> delete_intake_survey_response(survey_response_id)

Delete survey response

Deletes a survey response. Requires owner access.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Delete survey response
    api_instance.delete_intake_survey_response(survey_response_id)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->delete_intake_survey_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_intake_survey_response_metadata_by_key**
> delete_intake_survey_response_metadata_by_key(survey_response_id, key)

Delete metadata by key for a survey response

Deletes a specific metadata entry by key for the specified survey response

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response
key = 'key_example' # str | Metadata key

try:
    # Delete metadata by key for a survey response
    api_instance.delete_intake_survey_response_metadata_by_key(survey_response_id, key)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->delete_intake_survey_response_metadata_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 
 **key** | **str**| Metadata key | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intake_survey**
> Survey get_intake_survey(survey_id)

Get an available survey

Returns a specific active survey with all questions for the developer to fill out.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey

try:
    # Get an available survey
    api_response = api_instance.get_intake_survey(survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->get_intake_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | [**str**](.md)| Unique identifier of the survey | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intake_survey_response**
> SurveyResponse get_intake_survey_response(survey_response_id)

Get survey response

Returns a specific survey response. Requires reader access.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Get survey response
    api_response = api_instance.get_intake_survey_response(survey_response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->get_intake_survey_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intake_survey_response_metadata**
> list[Metadata] get_intake_survey_response_metadata(survey_response_id)

Get all metadata for a survey response

Returns all metadata key-value pairs for the specified survey response

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Get all metadata for a survey response
    api_response = api_instance.get_intake_survey_response_metadata(survey_response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->get_intake_survey_response_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intake_survey_response_metadata_by_key**
> Metadata get_intake_survey_response_metadata_by_key(survey_response_id, key)

Get metadata by key for a survey response

Returns a specific metadata entry by key for the specified survey response

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response
key = 'key_example' # str | Metadata key

try:
    # Get metadata by key for a survey response
    api_response = api_instance.get_intake_survey_response_metadata_by_key(survey_response_id, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->get_intake_survey_response_metadata_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 
 **key** | **str**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intake_survey_response_triage_note**
> TriageNote get_intake_survey_response_triage_note(survey_response_id, triage_note_id)

Get a specific triage note

Returns details of a specific triage note. Read-only access for survey response submitters.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response
triage_note_id = 56 # int | Triage note identifier (sequential within survey response)

try:
    # Get a specific triage note
    api_response = api_instance.get_intake_survey_response_triage_note(survey_response_id, triage_note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->get_intake_survey_response_triage_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 
 **triage_note_id** | **int**| Triage note identifier (sequential within survey response) | 

### Return type

[**TriageNote**](TriageNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_intake_survey_response_triage_notes**
> ListTriageNotesResponse list_intake_survey_response_triage_notes(survey_response_id, limit=limit, offset=offset)

List triage notes for a survey response

Returns a paginated list of triage notes for the specified survey response. Read-only access for survey response submitters.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)

try:
    # List triage notes for a survey response
    api_response = api_instance.list_intake_survey_response_triage_notes(survey_response_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->list_intake_survey_response_triage_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListTriageNotesResponse**](ListTriageNotesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_intake_survey_responses**
> ListSurveyResponsesResponse list_intake_survey_responses(status=status, survey_id=survey_id, limit=limit, offset=offset, sort=sort, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)

List user's survey responses

Returns a paginated list of the current user's survey responses.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
status = 'status_example' # str | Filter by response status (optional)
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter by survey ID (optional)
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)
sort = 'created_at:desc' # str | Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) (optional) (default to created_at:desc)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results created after this timestamp (ISO 8601) (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results created before this timestamp (ISO 8601) (optional)
modified_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results modified after this timestamp (ISO 8601) (optional)
modified_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results modified before this timestamp (ISO 8601) (optional)

try:
    # List user's survey responses
    api_response = api_instance.list_intake_survey_responses(status=status, survey_id=survey_id, limit=limit, offset=offset, sort=sort, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->list_intake_survey_responses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by response status | [optional] 
 **survey_id** | [**str**](.md)| Filter by survey ID | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **sort** | **str**| Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) | [optional] [default to created_at:desc]
 **created_after** | **datetime**| Filter results created after this timestamp (ISO 8601) | [optional] 
 **created_before** | **datetime**| Filter results created before this timestamp (ISO 8601) | [optional] 
 **modified_after** | **datetime**| Filter results modified after this timestamp (ISO 8601) | [optional] 
 **modified_before** | **datetime**| Filter results modified before this timestamp (ISO 8601) | [optional] 

### Return type

[**ListSurveyResponsesResponse**](ListSurveyResponsesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_intake_surveys**
> ListSurveysResponse list_intake_surveys(limit=limit, offset=offset, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)

List available surveys

Returns a list of active surveys available for developers to fill out.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results created after this timestamp (ISO 8601) (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results created before this timestamp (ISO 8601) (optional)
modified_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results modified after this timestamp (ISO 8601) (optional)
modified_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results modified before this timestamp (ISO 8601) (optional)

try:
    # List available surveys
    api_response = api_instance.list_intake_surveys(limit=limit, offset=offset, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->list_intake_surveys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **created_after** | **datetime**| Filter results created after this timestamp (ISO 8601) | [optional] 
 **created_before** | **datetime**| Filter results created before this timestamp (ISO 8601) | [optional] 
 **modified_after** | **datetime**| Filter results modified after this timestamp (ISO 8601) | [optional] 
 **modified_before** | **datetime**| Filter results modified before this timestamp (ISO 8601) | [optional] 

### Return type

[**ListSurveysResponse**](ListSurveysResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_intake_survey_response**
> SurveyResponse patch_intake_survey_response(body, survey_response_id)

Partial update survey response

Partially updates a survey response using JSON Patch (RFC 6902). Status transitions are allowed via /status path. Valid statuses: draft, submitted, needs_revision, ready_for_review, review_created. Transitioning to needs_revision requires revision_notes.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
body = [tmi_client.JsonPatchDocumentInner()] # list[JsonPatchDocumentInner] | JSON Patch operations to apply to the survey response
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Partial update survey response
    api_response = api_instance.patch_intake_survey_response(body, survey_response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->patch_intake_survey_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| JSON Patch operations to apply to the survey response | 
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_intake_survey_response**
> SurveyResponse update_intake_survey_response(body, survey_response_id)

Update survey response

Fully updates a survey response. Only allowed in draft or needs_revision status. Requires writer access.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
body = tmi_client.SurveyResponseInput() # SurveyResponseInput | Complete survey response to replace existing
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Update survey response
    api_response = api_instance.update_intake_survey_response(body, survey_response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->update_intake_survey_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SurveyResponseInput**](SurveyResponseInput.md)| Complete survey response to replace existing | 
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_intake_survey_response_metadata_by_key**
> Metadata update_intake_survey_response_metadata_by_key(body, survey_response_id, key)

Update metadata by key for a survey response

Updates or creates a metadata entry by key for the specified survey response

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyIntakeApi(tmi_client.ApiClient(configuration))
body = tmi_client.Metadata() # Metadata | Metadata key-value pair to update
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response
key = 'key_example' # str | Metadata key

try:
    # Update metadata by key for a survey response
    api_response = api_instance.update_intake_survey_response_metadata_by_key(body, survey_response_id, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyIntakeApi->update_intake_survey_response_metadata_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata key-value pair to update | 
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 
 **key** | **str**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

