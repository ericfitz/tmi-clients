# tmi_client.AuditTrailApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_audit_trail**](AuditTrailApi.md#get_asset_audit_trail) | **GET** /threat_models/{threat_model_id}/assets/{asset_id}/audit_trail | List audit trail for an asset
[**get_audit_entry**](AuditTrailApi.md#get_audit_entry) | **GET** /threat_models/{threat_model_id}/audit_trail/{entry_id} | Get a single audit trail entry
[**get_diagram_audit_trail**](AuditTrailApi.md#get_diagram_audit_trail) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id}/audit_trail | List audit trail for a diagram
[**get_document_audit_trail**](AuditTrailApi.md#get_document_audit_trail) | **GET** /threat_models/{threat_model_id}/documents/{document_id}/audit_trail | List audit trail for a document
[**get_note_audit_trail**](AuditTrailApi.md#get_note_audit_trail) | **GET** /threat_models/{threat_model_id}/notes/{note_id}/audit_trail | List audit trail for a note
[**get_repository_audit_trail**](AuditTrailApi.md#get_repository_audit_trail) | **GET** /threat_models/{threat_model_id}/repositories/{repository_id}/audit_trail | List audit trail for a repository
[**get_threat_audit_trail**](AuditTrailApi.md#get_threat_audit_trail) | **GET** /threat_models/{threat_model_id}/threats/{threat_id}/audit_trail | List audit trail for a threat
[**get_threat_model_audit_trail**](AuditTrailApi.md#get_threat_model_audit_trail) | **GET** /threat_models/{threat_model_id}/audit_trail | List audit trail for a threat model and all sub-objects
[**rollback_to_version**](AuditTrailApi.md#rollback_to_version) | **POST** /threat_models/{threat_model_id}/audit_trail/{entry_id}/rollback | Rollback an entity to a previous version

# **get_asset_audit_trail**
> ListAuditTrailResponse get_asset_audit_trail(threat_model_id, asset_id, limit=limit, offset=offset)

List audit trail for an asset

Returns a paginated list of audit trail entries for a specific resource

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AuditTrailApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Asset identifier
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)

try:
    # List audit trail for an asset
    api_response = api_instance.get_asset_audit_trail(threat_model_id, asset_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditTrailApi->get_asset_audit_trail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Threat model identifier | 
 **asset_id** | [**str**](.md)| Asset identifier | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_entry**
> AuditEntry get_audit_entry(threat_model_id, entry_id)

Get a single audit trail entry

Returns a single audit trail entry by ID

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AuditTrailApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier
entry_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the audit entry

try:
    # Get a single audit trail entry
    api_response = api_instance.get_audit_entry(threat_model_id, entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditTrailApi->get_audit_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Threat model identifier | 
 **entry_id** | [**str**](.md)| Unique identifier of the audit entry | 

### Return type

[**AuditEntry**](AuditEntry.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagram_audit_trail**
> ListAuditTrailResponse get_diagram_audit_trail(threat_model_id, diagram_id, limit=limit, offset=offset)

List audit trail for a diagram

Returns a paginated list of audit trail entries for a specific resource

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AuditTrailApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier
diagram_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Diagram identifier
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)

try:
    # List audit trail for a diagram
    api_response = api_instance.get_diagram_audit_trail(threat_model_id, diagram_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditTrailApi->get_diagram_audit_trail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Threat model identifier | 
 **diagram_id** | [**str**](.md)| Diagram identifier | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_audit_trail**
> ListAuditTrailResponse get_document_audit_trail(threat_model_id, document_id, limit=limit, offset=offset)

List audit trail for a document

Returns a paginated list of audit trail entries for a specific resource

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AuditTrailApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier
document_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Document identifier
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)

try:
    # List audit trail for a document
    api_response = api_instance.get_document_audit_trail(threat_model_id, document_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditTrailApi->get_document_audit_trail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Threat model identifier | 
 **document_id** | [**str**](.md)| Document identifier | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_audit_trail**
> ListAuditTrailResponse get_note_audit_trail(threat_model_id, note_id, limit=limit, offset=offset)

List audit trail for a note

Returns a paginated list of audit trail entries for a specific resource

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AuditTrailApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier
note_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Note identifier
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)

try:
    # List audit trail for a note
    api_response = api_instance.get_note_audit_trail(threat_model_id, note_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditTrailApi->get_note_audit_trail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Threat model identifier | 
 **note_id** | [**str**](.md)| Note identifier | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_audit_trail**
> ListAuditTrailResponse get_repository_audit_trail(threat_model_id, repository_id, limit=limit, offset=offset)

List audit trail for a repository

Returns a paginated list of audit trail entries for a specific resource

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AuditTrailApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier
repository_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Repository identifier
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)

try:
    # List audit trail for a repository
    api_response = api_instance.get_repository_audit_trail(threat_model_id, repository_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditTrailApi->get_repository_audit_trail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Threat model identifier | 
 **repository_id** | [**str**](.md)| Repository identifier | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_audit_trail**
> ListAuditTrailResponse get_threat_audit_trail(threat_model_id, threat_id, limit=limit, offset=offset)

List audit trail for a threat

Returns a paginated list of audit trail entries for a specific resource

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AuditTrailApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier
threat_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat identifier
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)

try:
    # List audit trail for a threat
    api_response = api_instance.get_threat_audit_trail(threat_model_id, threat_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditTrailApi->get_threat_audit_trail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Threat model identifier | 
 **threat_id** | [**str**](.md)| Threat identifier | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threat_model_audit_trail**
> ListAuditTrailResponse get_threat_model_audit_trail(threat_model_id, limit=limit, offset=offset, object_type=object_type, change_type=change_type, actor_email=actor_email, after=after, before=before)

List audit trail for a threat model and all sub-objects

Returns a paginated list of audit trail entries

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AuditTrailApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier
limit = 20 # int | Maximum number of results to return (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)
object_type = 'object_type_example' # str | Filter by object type (optional)
change_type = 'change_type_example' # str | Filter by change type (optional)
actor_email = 'actor_email_example' # str | Filter by actor email (optional)
after = '2013-10-20T19:20:30+01:00' # datetime | Filter entries after this timestamp (ISO 8601) (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Filter entries before this timestamp (ISO 8601) (optional)

try:
    # List audit trail for a threat model and all sub-objects
    api_response = api_instance.get_threat_model_audit_trail(threat_model_id, limit=limit, offset=offset, object_type=object_type, change_type=change_type, actor_email=actor_email, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditTrailApi->get_threat_model_audit_trail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Threat model identifier | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **object_type** | **str**| Filter by object type | [optional] 
 **change_type** | **str**| Filter by change type | [optional] 
 **actor_email** | **str**| Filter by actor email | [optional] 
 **after** | **datetime**| Filter entries after this timestamp (ISO 8601) | [optional] 
 **before** | **datetime**| Filter entries before this timestamp (ISO 8601) | [optional] 

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_to_version**
> RollbackResponse rollback_to_version(threat_model_id, entry_id)

Rollback an entity to a previous version

Restores an entity to the state captured in the specified audit entry's version snapshot. Creates a new audit entry recording the rollback. Returns 410 Gone if the version snapshot has been pruned.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.AuditTrailApi(tmi_client.ApiClient(configuration))
threat_model_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Threat model identifier
entry_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique identifier of the audit entry

try:
    # Rollback an entity to a previous version
    api_response = api_instance.rollback_to_version(threat_model_id, entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditTrailApi->rollback_to_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_model_id** | [**str**](.md)| Threat model identifier | 
 **entry_id** | [**str**](.md)| Unique identifier of the audit entry | 

### Return type

[**RollbackResponse**](RollbackResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

