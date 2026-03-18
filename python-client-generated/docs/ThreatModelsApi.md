# tmi_client.ThreatModelsApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_threat_model**](ThreatModelsApi.md#create_threat_model) | **POST** /threat_models | Create a threat model
[**delete_threat_model**](ThreatModelsApi.md#delete_threat_model) | **DELETE** /threat_models/{threat_model_id} | Delete a threat model
[**get_threat_model**](ThreatModelsApi.md#get_threat_model) | **GET** /threat_models/{threat_model_id} | Retrieve a threat model
[**list_threat_models**](ThreatModelsApi.md#list_threat_models) | **GET** /threat_models | List threat models
[**patch_threat_model**](ThreatModelsApi.md#patch_threat_model) | **PATCH** /threat_models/{threat_model_id} | Partially update a threat model
[**restore_threat_model**](ThreatModelsApi.md#restore_threat_model) | **POST** /threat_models/{threat_model_id}/restore | Restore a soft-deleted threat model
[**update_threat_model**](ThreatModelsApi.md#update_threat_model) | **PUT** /threat_models/{threat_model_id} | Update a threat model

# **create_threat_model**
> ThreatModel create_threat_model(body)

Create a threat model

Creates a new threat model with the authenticated user as owner

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ThreatModelsApi(tmi_client.ApiClient(configuration))
body = tmi_client.ThreatModelInput() # ThreatModelInput | Threat Model creation data

try:
    # Create a threat model
    api_response = api_instance.create_threat_model(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThreatModelsApi->create_threat_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThreatModelInput**](ThreatModelInput.md)| Threat Model creation data | 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threat_model**
> delete_threat_model(threat_model_id)

Delete a threat model

Deletes a threat model; restricted to owner role

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ThreatModelsApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier

try:
    # Delete a threat model
    api_instance.delete_threat_model(threat_model_id)
except ApiException as e:
    print("Exception when calling ThreatModelsApi->delete_threat_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Threat model identifier | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model**
> ThreatModel get_threat_model(threat_model_id)

Retrieve a threat model

Retrieves the full details of a specific threat model if the user has access

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ThreatModelsApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier

try:
    # Retrieve a threat model
    api_response = api_instance.get_threat_model(threat_model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThreatModelsApi->get_threat_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Threat model identifier | 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_threat_models**
> ListThreatModelsResponse list_threat_models(limit=limit, offset=offset, owner=owner, name=name, description=description, issue_uri=issue_uri, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before, status=status, status_updated_after=status_updated_after, status_updated_before=status_updated_before, include_deleted=include_deleted)

List threat models

Returns a list of threat models accessible to the authenticated user with enhanced metadata and entity counts

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ThreatModelsApi(tmi_client.ApiClient(configuration))
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)
owner = 'owner_example' # str | Filter by owner name or email (optional)
name = 'name_example' # str | Filter by name (case-insensitive substring match) (optional)
description = 'description_example' # str | Filter by threat model description (partial match) (optional)
issue_uri = 'issue_uri_example' # str | Filter by issue URI (partial match) (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results created after this timestamp (ISO 8601) (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results created before this timestamp (ISO 8601) (optional)
modified_after = '2013-10-20T19:20:30+01:00' # datetime | Filter results modified after this timestamp (ISO 8601) (optional)
modified_before = '2013-10-20T19:20:30+01:00' # datetime | Filter results modified before this timestamp (ISO 8601) (optional)
status = ['status_example'] # list[str] | Filter by status (OR logic). Returns threats matching ANY of the specified statuses. Example: ?status=identified&status=mitigated (optional)
status_updated_after = '2013-10-20T19:20:30+01:00' # datetime | Filter threat models where status was updated after this timestamp (RFC3339) (optional)
status_updated_before = '2013-10-20T19:20:30+01:00' # datetime | Filter threat models where status was updated before this timestamp (RFC3339) (optional)
include_deleted = false # bool | Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. (optional) (default to false)

try:
    # List threat models
    api_response = api_instance.list_threat_models(limit=limit, offset=offset, owner=owner, name=name, description=description, issue_uri=issue_uri, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before, status=status, status_updated_after=status_updated_after, status_updated_before=status_updated_before, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThreatModelsApi->list_threat_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **owner** | **str**| Filter by owner name or email | [optional] 
 **name** | **str**| Filter by name (case-insensitive substring match) | [optional] 
 **description** | **str**| Filter by threat model description (partial match) | [optional] 
 **issue_uri** | **str**| Filter by issue URI (partial match) | [optional] 
 **created_after** | **datetime**| Filter results created after this timestamp (ISO 8601) | [optional] 
 **created_before** | **datetime**| Filter results created before this timestamp (ISO 8601) | [optional] 
 **modified_after** | **datetime**| Filter results modified after this timestamp (ISO 8601) | [optional] 
 **modified_before** | **datetime**| Filter results modified before this timestamp (ISO 8601) | [optional] 
 **status** | [**list[str]**](str.md)| Filter by status (OR logic). Returns threats matching ANY of the specified statuses. Example: ?status&#x3D;identified&amp;status&#x3D;mitigated | [optional] 
 **status_updated_after** | **datetime**| Filter threat models where status was updated after this timestamp (RFC3339) | [optional] 
 **status_updated_before** | **datetime**| Filter threat models where status was updated before this timestamp (RFC3339) | [optional] 
 **include_deleted** | **bool**| Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. | [optional] [default to false]

### Return type

[**ListThreatModelsResponse**](ListThreatModelsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_threat_model**
> ThreatModel patch_threat_model(threat_model_id, body=body)

Partially update a threat model

Applies JSON Patch operations to a threat model; restricted to writer/owner roles

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ThreatModelsApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier
body = [tmi_client.JsonPatchDocumentInner()] # list[JsonPatchDocumentInner] | JSON Patch operations to apply to the threat model (optional)

try:
    # Partially update a threat model
    api_response = api_instance.patch_threat_model(threat_model_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThreatModelsApi->patch_threat_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Threat model identifier | 
 **body** | [**list[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| JSON Patch operations to apply to the threat model | [optional] 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_threat_model**
> ThreatModel restore_threat_model(threat_model_id)

Restore a soft-deleted threat model

Restores a soft-deleted threat model and all its soft-deleted children (diagrams, threats, assets, documents, notes, repositories). Restricted to owner role or administrators.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ThreatModelsApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier

try:
    # Restore a soft-deleted threat model
    api_response = api_instance.restore_threat_model(threat_model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThreatModelsApi->restore_threat_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Threat model identifier | 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threat_model**
> ThreatModel update_threat_model(body, threat_model_id)

Update a threat model

Fully updates a threat model; restricted to writer/owner roles

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ThreatModelsApi(tmi_client.ApiClient(configuration))
body = tmi_client.ThreatModelInput() # ThreatModelInput | Complete threat model data for replacement
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier

try:
    # Update a threat model
    api_response = api_instance.update_threat_model(body, threat_model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThreatModelsApi->update_threat_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThreatModelInput**](ThreatModelInput.md)| Complete threat model data for replacement | 
 **threat_model_id** | [**str**](.md)| Threat model identifier | 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

