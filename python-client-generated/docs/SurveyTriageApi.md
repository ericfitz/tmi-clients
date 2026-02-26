# tmi_client.SurveyTriageApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_threat_model_from_survey_response**](SurveyTriageApi.md#create_threat_model_from_survey_response) | **POST** /triage/survey_responses/{survey_response_id}/create_threat_model | Create threat model from survey response
[**create_triage_survey_response_triage_note**](SurveyTriageApi.md#create_triage_survey_response_triage_note) | **POST** /triage/survey_responses/{survey_response_id}/triage_notes | Create a triage note
[**get_triage_survey_response**](SurveyTriageApi.md#get_triage_survey_response) | **GET** /triage/survey_responses/{survey_response_id} | Get survey response for triage
[**get_triage_survey_response_metadata**](SurveyTriageApi.md#get_triage_survey_response_metadata) | **GET** /triage/survey_responses/{survey_response_id}/metadata | Get all metadata for a survey response
[**get_triage_survey_response_metadata_by_key**](SurveyTriageApi.md#get_triage_survey_response_metadata_by_key) | **GET** /triage/survey_responses/{survey_response_id}/metadata/{key} | Get metadata by key for a survey response
[**get_triage_survey_response_triage_note**](SurveyTriageApi.md#get_triage_survey_response_triage_note) | **GET** /triage/survey_responses/{survey_response_id}/triage_notes/{triage_note_id} | Get a specific triage note
[**list_triage_survey_response_triage_notes**](SurveyTriageApi.md#list_triage_survey_response_triage_notes) | **GET** /triage/survey_responses/{survey_response_id}/triage_notes | List triage notes for a survey response
[**list_triage_survey_responses**](SurveyTriageApi.md#list_triage_survey_responses) | **GET** /triage/survey_responses | List survey responses for triage
[**patch_triage_survey_response**](SurveyTriageApi.md#patch_triage_survey_response) | **PATCH** /triage/survey_responses/{survey_response_id} | Partial update survey response for triage

# **create_threat_model_from_survey_response**
> CreateThreatModelFromSurveyResponse create_threat_model_from_survey_response(survey_response_id)

Create threat model from survey response

Creates a new threat model from an approved survey response. Copies answers to TM metadata, sets owner to survey owner, and transitions response to review_created.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyTriageApi(tmi_client.ApiClient(configuration))
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Create threat model from survey response
    api_response = api_instance.create_threat_model_from_survey_response(survey_response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyTriageApi->create_threat_model_from_survey_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 

### Return type

[**CreateThreatModelFromSurveyResponse**](CreateThreatModelFromSurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_triage_survey_response_triage_note**
> TriageNote create_triage_survey_response_triage_note(body, survey_response_id)

Create a triage note

Creates a new triage note on the specified survey response. Only accessible to security reviewers.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyTriageApi(tmi_client.ApiClient(configuration))
body = tmi_client.TriageNoteInput() # TriageNoteInput | Triage note creation data
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Create a triage note
    api_response = api_instance.create_triage_survey_response_triage_note(body, survey_response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyTriageApi->create_triage_survey_response_triage_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TriageNoteInput**](TriageNoteInput.md)| Triage note creation data | 
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 

### Return type

[**TriageNote**](TriageNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_triage_survey_response**
> SurveyResponse get_triage_survey_response(survey_response_id)

Get survey response for triage

Returns a specific survey response for security engineer review.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyTriageApi(tmi_client.ApiClient(configuration))
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Get survey response for triage
    api_response = api_instance.get_triage_survey_response(survey_response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyTriageApi->get_triage_survey_response: %s\n" % e)
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

# **get_triage_survey_response_metadata**
> list[Metadata] get_triage_survey_response_metadata(survey_response_id)

Get all metadata for a survey response

Returns all metadata key-value pairs for the specified survey response (read-only triage access)

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyTriageApi(tmi_client.ApiClient(configuration))
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Get all metadata for a survey response
    api_response = api_instance.get_triage_survey_response_metadata(survey_response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyTriageApi->get_triage_survey_response_metadata: %s\n" % e)
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

# **get_triage_survey_response_metadata_by_key**
> Metadata get_triage_survey_response_metadata_by_key(survey_response_id, key)

Get metadata by key for a survey response

Returns a specific metadata entry by key for the specified survey response (read-only triage access)

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyTriageApi(tmi_client.ApiClient(configuration))
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response
key = 'key_example' # str | Metadata key

try:
    # Get metadata by key for a survey response
    api_response = api_instance.get_triage_survey_response_metadata_by_key(survey_response_id, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyTriageApi->get_triage_survey_response_metadata_by_key: %s\n" % e)
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

# **get_triage_survey_response_triage_note**
> TriageNote get_triage_survey_response_triage_note(survey_response_id, triage_note_id)

Get a specific triage note

Returns details of a specific triage note within the survey response. Only accessible to security reviewers.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyTriageApi(tmi_client.ApiClient(configuration))
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response
triage_note_id = 56 # int | Triage note identifier (sequential within survey response)

try:
    # Get a specific triage note
    api_response = api_instance.get_triage_survey_response_triage_note(survey_response_id, triage_note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyTriageApi->get_triage_survey_response_triage_note: %s\n" % e)
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

# **list_triage_survey_response_triage_notes**
> ListTriageNotesResponse list_triage_survey_response_triage_notes(survey_response_id, limit=limit, offset=offset)

List triage notes for a survey response

Returns a paginated list of triage notes attached to the specified survey response. Only accessible to security reviewers.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyTriageApi(tmi_client.ApiClient(configuration))
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)

try:
    # List triage notes for a survey response
    api_response = api_instance.list_triage_survey_response_triage_notes(survey_response_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyTriageApi->list_triage_survey_response_triage_notes: %s\n" % e)
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

# **list_triage_survey_responses**
> ListSurveyResponsesResponse list_triage_survey_responses(status=status, survey_id=survey_id, is_confidential=is_confidential, limit=limit, offset=offset, sort=sort, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)

List survey responses for triage

Returns a paginated list of survey responses for security engineers to triage. Filter by status=submitted to see the triage queue.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyTriageApi(tmi_client.ApiClient(configuration))
status = 'status_example' # str | Filter by response status (optional)
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter by survey ID (optional)
is_confidential = true # bool | Filter by secret_project flag (optional)
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)
sort = 'created_at:desc' # str | Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) (optional) (default to created_at:desc)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results created after this timestamp (ISO 8601) (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results created before this timestamp (ISO 8601) (optional)
modified_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results modified after this timestamp (ISO 8601) (optional)
modified_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results modified before this timestamp (ISO 8601) (optional)

try:
    # List survey responses for triage
    api_response = api_instance.list_triage_survey_responses(status=status, survey_id=survey_id, is_confidential=is_confidential, limit=limit, offset=offset, sort=sort, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyTriageApi->list_triage_survey_responses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by response status | [optional] 
 **survey_id** | [**str**](.md)| Filter by survey ID | [optional] 
 **is_confidential** | **bool**| Filter by secret_project flag | [optional] 
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

# **patch_triage_survey_response**
> SurveyResponse patch_triage_survey_response(body, survey_response_id)

Partial update survey response for triage

Partially updates a survey response using JSON Patch (RFC 6902). Security Reviewers can change status via /status path. Valid statuses: draft, submitted, needs_revision, ready_for_review, review_created. Transitioning to needs_revision requires revision_notes.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyTriageApi(tmi_client.ApiClient(configuration))
body = [tmi_client.JsonPatchDocumentInner()] # list[JsonPatchDocumentInner] | JSON Patch operations to apply to the survey response during triage
survey_response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey response

try:
    # Partial update survey response for triage
    api_response = api_instance.patch_triage_survey_response(body, survey_response_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyTriageApi->patch_triage_survey_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| JSON Patch operations to apply to the survey response during triage | 
 **survey_response_id** | [**str**](.md)| Unique identifier of the survey response | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

