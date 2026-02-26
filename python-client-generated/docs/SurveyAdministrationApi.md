# tmi_client.SurveyAdministrationApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_admin_survey_metadata**](SurveyAdministrationApi.md#bulk_create_admin_survey_metadata) | **POST** /admin/surveys/{survey_id}/metadata/bulk | Bulk create metadata for a survey
[**bulk_replace_admin_survey_metadata**](SurveyAdministrationApi.md#bulk_replace_admin_survey_metadata) | **PUT** /admin/surveys/{survey_id}/metadata/bulk | Bulk replace metadata for a survey
[**bulk_upsert_admin_survey_metadata**](SurveyAdministrationApi.md#bulk_upsert_admin_survey_metadata) | **PATCH** /admin/surveys/{survey_id}/metadata/bulk | Bulk upsert metadata for a survey
[**create_admin_survey**](SurveyAdministrationApi.md#create_admin_survey) | **POST** /admin/surveys | Create a survey
[**create_admin_survey_metadata**](SurveyAdministrationApi.md#create_admin_survey_metadata) | **POST** /admin/surveys/{survey_id}/metadata | Add metadata to a survey
[**delete_admin_survey**](SurveyAdministrationApi.md#delete_admin_survey) | **DELETE** /admin/surveys/{survey_id} | Delete a survey
[**delete_admin_survey_metadata_by_key**](SurveyAdministrationApi.md#delete_admin_survey_metadata_by_key) | **DELETE** /admin/surveys/{survey_id}/metadata/{key} | Delete metadata by key for a survey
[**get_admin_survey**](SurveyAdministrationApi.md#get_admin_survey) | **GET** /admin/surveys/{survey_id} | Get a survey
[**get_admin_survey_metadata**](SurveyAdministrationApi.md#get_admin_survey_metadata) | **GET** /admin/surveys/{survey_id}/metadata | Get all metadata for a survey
[**get_admin_survey_metadata_by_key**](SurveyAdministrationApi.md#get_admin_survey_metadata_by_key) | **GET** /admin/surveys/{survey_id}/metadata/{key} | Get metadata by key for a survey
[**list_admin_surveys**](SurveyAdministrationApi.md#list_admin_surveys) | **GET** /admin/surveys | List surveys
[**patch_admin_survey**](SurveyAdministrationApi.md#patch_admin_survey) | **PATCH** /admin/surveys/{survey_id} | Partially update a survey
[**update_admin_survey**](SurveyAdministrationApi.md#update_admin_survey) | **PUT** /admin/surveys/{survey_id} | Update a survey
[**update_admin_survey_metadata_by_key**](SurveyAdministrationApi.md#update_admin_survey_metadata_by_key) | **PUT** /admin/surveys/{survey_id}/metadata/{key} | Update metadata by key for a survey

# **bulk_create_admin_survey_metadata**
> list[Metadata] bulk_create_admin_survey_metadata(body, survey_id)

Bulk create metadata for a survey

Creates multiple metadata key-value pairs for the specified survey. Returns 409 Conflict if any of the specified keys already exist.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
body = [tmi_client.Metadata()] # list[Metadata] | Array of metadata key-value pairs to create
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey

try:
    # Bulk create metadata for a survey
    api_response = api_instance.bulk_create_admin_survey_metadata(body, survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->bulk_create_admin_survey_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Metadata]**](Metadata.md)| Array of metadata key-value pairs to create | 
 **survey_id** | [**str**](.md)| Unique identifier of the survey | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_replace_admin_survey_metadata**
> list[Metadata] bulk_replace_admin_survey_metadata(body, survey_id)

Bulk replace metadata for a survey

Replaces all metadata for the entity. All existing metadata is deleted and replaced with the provided set. To clear all metadata, send an empty array.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
body = [tmi_client.Metadata()] # list[Metadata] | Complete set of metadata key-value pairs to replace existing metadata
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey

try:
    # Bulk replace metadata for a survey
    api_response = api_instance.bulk_replace_admin_survey_metadata(body, survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->bulk_replace_admin_survey_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Metadata]**](Metadata.md)| Complete set of metadata key-value pairs to replace existing metadata | 
 **survey_id** | [**str**](.md)| Unique identifier of the survey | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_admin_survey_metadata**
> list[Metadata] bulk_upsert_admin_survey_metadata(body, survey_id)

Bulk upsert metadata for a survey

Creates or updates only the provided metadata keys. Keys not included in the request are left unchanged. This is a merge/upsert operation.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
body = [tmi_client.Metadata()] # list[Metadata] | Metadata key-value pairs to create or update (merge)
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey

try:
    # Bulk upsert metadata for a survey
    api_response = api_instance.bulk_upsert_admin_survey_metadata(body, survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->bulk_upsert_admin_survey_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Metadata]**](Metadata.md)| Metadata key-value pairs to create or update (merge) | 
 **survey_id** | [**str**](.md)| Unique identifier of the survey | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_admin_survey**
> Survey create_admin_survey(body)

Create a survey

Creates a new survey. Surveys are created in inactive status by default.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
body = tmi_client.SurveyInput() # SurveyInput | Survey definition to create

try:
    # Create a survey
    api_response = api_instance.create_admin_survey(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->create_admin_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SurveyInput**](SurveyInput.md)| Survey definition to create | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_admin_survey_metadata**
> Metadata create_admin_survey_metadata(body, survey_id)

Add metadata to a survey

Adds a new metadata key-value pair to the specified survey. Returns 409 Conflict if the key already exists.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
body = tmi_client.Metadata() # Metadata | Metadata key-value pair to create
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey

try:
    # Add metadata to a survey
    api_response = api_instance.create_admin_survey_metadata(body, survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->create_admin_survey_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata key-value pair to create | 
 **survey_id** | [**str**](.md)| Unique identifier of the survey | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_admin_survey**
> delete_admin_survey(survey_id)

Delete a survey

Deletes a survey. Surveys with existing responses cannot be deleted.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey

try:
    # Delete a survey
    api_instance.delete_admin_survey(survey_id)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->delete_admin_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | [**str**](.md)| Unique identifier of the survey | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_admin_survey_metadata_by_key**
> delete_admin_survey_metadata_by_key(survey_id, key)

Delete metadata by key for a survey

Deletes a specific metadata entry by key for the specified survey

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey
key = 'key_example' # str | Metadata key

try:
    # Delete metadata by key for a survey
    api_instance.delete_admin_survey_metadata_by_key(survey_id, key)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->delete_admin_survey_metadata_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | [**str**](.md)| Unique identifier of the survey | 
 **key** | **str**| Metadata key | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_survey**
> Survey get_admin_survey(survey_id)

Get a survey

Returns a specific survey by ID.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey

try:
    # Get a survey
    api_response = api_instance.get_admin_survey(survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->get_admin_survey: %s\n" % e)
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

# **get_admin_survey_metadata**
> list[Metadata] get_admin_survey_metadata(survey_id)

Get all metadata for a survey

Returns all metadata key-value pairs for the specified survey

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey

try:
    # Get all metadata for a survey
    api_response = api_instance.get_admin_survey_metadata(survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->get_admin_survey_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | [**str**](.md)| Unique identifier of the survey | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_survey_metadata_by_key**
> Metadata get_admin_survey_metadata_by_key(survey_id, key)

Get metadata by key for a survey

Returns a specific metadata entry by key for the specified survey

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey
key = 'key_example' # str | Metadata key

try:
    # Get metadata by key for a survey
    api_response = api_instance.get_admin_survey_metadata_by_key(survey_id, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->get_admin_survey_metadata_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | [**str**](.md)| Unique identifier of the survey | 
 **key** | **str**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_admin_surveys**
> ListSurveysResponse list_admin_surveys(status=status, limit=limit, offset=offset, sort=sort, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)

List surveys

Returns a paginated list of all surveys with optional filtering by status.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
status = 'status_example' # str | Filter by survey status (optional)
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)
sort = 'created_at:desc' # str | Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) (optional) (default to created_at:desc)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results created after this timestamp (ISO 8601) (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results created before this timestamp (ISO 8601) (optional)
modified_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results modified after this timestamp (ISO 8601) (optional)
modified_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results modified before this timestamp (ISO 8601) (optional)

try:
    # List surveys
    api_response = api_instance.list_admin_surveys(status=status, limit=limit, offset=offset, sort=sort, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->list_admin_surveys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by survey status | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **sort** | **str**| Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) | [optional] [default to created_at:desc]
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

# **patch_admin_survey**
> Survey patch_admin_survey(body, survey_id)

Partially update a survey

Partially updates a survey using JSON Patch (RFC 6902).

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
body = [tmi_client.JsonPatchDocumentInner()] # list[JsonPatchDocumentInner] | JSON Patch operations to apply to the survey
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey

try:
    # Partially update a survey
    api_response = api_instance.patch_admin_survey(body, survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->patch_admin_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| JSON Patch operations to apply to the survey | 
 **survey_id** | [**str**](.md)| Unique identifier of the survey | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_admin_survey**
> Survey update_admin_survey(body, survey_id)

Update a survey

Fully updates a survey. All fields are replaced.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
body = tmi_client.SurveyInput() # SurveyInput | Complete survey definition to replace existing
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey

try:
    # Update a survey
    api_response = api_instance.update_admin_survey(body, survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->update_admin_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SurveyInput**](SurveyInput.md)| Complete survey definition to replace existing | 
 **survey_id** | [**str**](.md)| Unique identifier of the survey | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_admin_survey_metadata_by_key**
> Metadata update_admin_survey_metadata_by_key(body, survey_id, key)

Update metadata by key for a survey

Updates or creates a metadata entry by key for the specified survey

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.SurveyAdministrationApi(tmi_client.ApiClient(configuration))
body = tmi_client.Metadata() # Metadata | Metadata key-value pair to update
survey_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the survey
key = 'key_example' # str | Metadata key

try:
    # Update metadata by key for a survey
    api_response = api_instance.update_admin_survey_metadata_by_key(body, survey_id, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyAdministrationApi->update_admin_survey_metadata_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata key-value pair to update | 
 **survey_id** | [**str**](.md)| Unique identifier of the survey | 
 **key** | **str**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

