# tmi_client.ProjectsApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_project_metadata**](ProjectsApi.md#bulk_create_project_metadata) | **POST** /projects/{project_id}/metadata/bulk | Bulk create project metadata
[**bulk_replace_project_metadata**](ProjectsApi.md#bulk_replace_project_metadata) | **PUT** /projects/{project_id}/metadata/bulk | Bulk replace project metadata
[**bulk_upsert_project_metadata**](ProjectsApi.md#bulk_upsert_project_metadata) | **PATCH** /projects/{project_id}/metadata/bulk | Bulk upsert project metadata
[**create_project**](ProjectsApi.md#create_project) | **POST** /projects | Create a project
[**create_project_metadata**](ProjectsApi.md#create_project_metadata) | **POST** /projects/{project_id}/metadata | Create project metadata
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /projects/{project_id} | Delete a project
[**delete_project_metadata**](ProjectsApi.md#delete_project_metadata) | **DELETE** /projects/{project_id}/metadata/{key} | Delete project metadata
[**get_project**](ProjectsApi.md#get_project) | **GET** /projects/{project_id} | Get a project
[**get_project_metadata**](ProjectsApi.md#get_project_metadata) | **GET** /projects/{project_id}/metadata | Get project metadata
[**list_projects**](ProjectsApi.md#list_projects) | **GET** /projects | List projects
[**patch_project**](ProjectsApi.md#patch_project) | **PATCH** /projects/{project_id} | Patch a project
[**update_project**](ProjectsApi.md#update_project) | **PUT** /projects/{project_id} | Update a project
[**update_project_metadata**](ProjectsApi.md#update_project_metadata) | **PUT** /projects/{project_id}/metadata/{key} | Update project metadata

# **bulk_create_project_metadata**
> list[Metadata] bulk_create_project_metadata(body, project_id)

Bulk create project metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ProjectsApi(tmi_client.ApiClient(configuration))
body = [tmi_client.Metadata()] # list[Metadata] | Bulk metadata entries to create
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Project identifier (UUID)

try:
    # Bulk create project metadata
    api_response = api_instance.bulk_create_project_metadata(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->bulk_create_project_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Metadata]**](Metadata.md)| Bulk metadata entries to create | 
 **project_id** | [**str**](.md)| Project identifier (UUID) | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_replace_project_metadata**
> list[Metadata] bulk_replace_project_metadata(body, project_id)

Bulk replace project metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ProjectsApi(tmi_client.ApiClient(configuration))
body = [tmi_client.Metadata()] # list[Metadata] | Complete set of metadata entries for replacement
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Project identifier (UUID)

try:
    # Bulk replace project metadata
    api_response = api_instance.bulk_replace_project_metadata(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->bulk_replace_project_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Metadata]**](Metadata.md)| Complete set of metadata entries for replacement | 
 **project_id** | [**str**](.md)| Project identifier (UUID) | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_project_metadata**
> list[Metadata] bulk_upsert_project_metadata(body, project_id)

Bulk upsert project metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ProjectsApi(tmi_client.ApiClient(configuration))
body = tmi_client.BulkPatchRequest() # BulkPatchRequest | Metadata entries to update
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Project identifier (UUID)

try:
    # Bulk upsert project metadata
    api_response = api_instance.bulk_upsert_project_metadata(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->bulk_upsert_project_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkPatchRequest**](BulkPatchRequest.md)| Metadata entries to update | 
 **project_id** | [**str**](.md)| Project identifier (UUID) | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(body)

Create a project

Creates a new project. Requires membership in the referenced team.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ProjectsApi(tmi_client.ApiClient(configuration))
body = tmi_client.ProjectBase() # ProjectBase | Project creation data

try:
    # Create a project
    api_response = api_instance.create_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectBase**](ProjectBase.md)| Project creation data | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_metadata**
> Metadata create_project_metadata(body, project_id)

Create project metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ProjectsApi(tmi_client.ApiClient(configuration))
body = tmi_client.Metadata() # Metadata | Metadata entry to create
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Project identifier (UUID)

try:
    # Create project metadata
    api_response = api_instance.create_project_metadata(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata entry to create | 
 **project_id** | [**str**](.md)| Project identifier (UUID) | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_id)

Delete a project

Deletes a project. Requires owner role or admin access. Returns 409 if the project is referenced by threat models.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ProjectsApi(tmi_client.ApiClient(configuration))
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Project UUID

try:
    # Delete a project
    api_instance.delete_project(project_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| Project UUID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_metadata**
> delete_project_metadata(project_id, key)

Delete project metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ProjectsApi(tmi_client.ApiClient(configuration))
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Project identifier (UUID)
key = 'key_example' # str | Metadata key

try:
    # Delete project metadata
    api_instance.delete_project_metadata(project_id, key)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| Project identifier (UUID) | 
 **key** | **str**| Metadata key | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(project_id)

Get a project

Returns a project by ID. Requires membership in the project's team or admin access.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ProjectsApi(tmi_client.ApiClient(configuration))
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Project UUID

try:
    # Get a project
    api_response = api_instance.get_project(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| Project UUID | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_metadata**
> list[Metadata] get_project_metadata(project_id)

Get project metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ProjectsApi(tmi_client.ApiClient(configuration))
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Project identifier (UUID)

try:
    # Get project metadata
    api_response = api_instance.get_project_metadata(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| Project identifier (UUID) | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> ListProjectsResponse list_projects(limit=limit, offset=offset, name=name, status=status, team_id=team_id, related_to=related_to, relationship=relationship, transitive=transitive)

List projects

Returns a paginated list of projects. Non-admin users see only projects belonging to teams they are members of.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ProjectsApi(tmi_client.ApiClient(configuration))
limit = 20 # int | Maximum number of results per page (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)
name = 'name_example' # str | Filter by project name (partial match) (optional)
status = 'status_example' # str | Filter by status (exact match, comma-separated for multiple) (optional)
team_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter by team (optional)
related_to = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Include projects related to this project ID (optional)
relationship = tmi_client.RelationshipType() # RelationshipType | Filter related projects by relationship type. Only used with related_to. (optional)
transitive = false # bool | When true with related_to + relationship, follow parent/child chains transitively (max depth 10) (optional) (default to false)

try:
    # List projects
    api_response = api_instance.list_projects(limit=limit, offset=offset, name=name, status=status, team_id=team_id, related_to=related_to, relationship=relationship, transitive=transitive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results per page | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **name** | **str**| Filter by project name (partial match) | [optional] 
 **status** | **str**| Filter by status (exact match, comma-separated for multiple) | [optional] 
 **team_id** | [**str**](.md)| Filter by team | [optional] 
 **related_to** | [**str**](.md)| Include projects related to this project ID | [optional] 
 **relationship** | [**RelationshipType**](.md)| Filter related projects by relationship type. Only used with related_to. | [optional] 
 **transitive** | **bool**| When true with related_to + relationship, follow parent/child chains transitively (max depth 10) | [optional] [default to false]

### Return type

[**ListProjectsResponse**](ListProjectsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_project**
> Project patch_project(body, project_id)

Patch a project

Partial update of a project using JSON Patch (RFC 6902). Requires membership in the project's team or admin access.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ProjectsApi(tmi_client.ApiClient(configuration))
body = [tmi_client.JsonPatchDocumentInner()] # list[JsonPatchDocumentInner] | Partial project data for update
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Project UUID

try:
    # Patch a project
    api_response = api_instance.patch_project(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->patch_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| Partial project data for update | 
 **project_id** | [**str**](.md)| Project UUID | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(body, project_id)

Update a project

Full replacement update of a project. Requires membership in the project's team or admin access.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ProjectsApi(tmi_client.ApiClient(configuration))
body = tmi_client.ProjectBase() # ProjectBase | Complete project data for replacement
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Project UUID

try:
    # Update a project
    api_response = api_instance.update_project(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectBase**](ProjectBase.md)| Complete project data for replacement | 
 **project_id** | [**str**](.md)| Project UUID | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_metadata**
> Metadata update_project_metadata(body, project_id, key)

Update project metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.ProjectsApi(tmi_client.ApiClient(configuration))
body = tmi_client.Metadata() # Metadata | Metadata value to set for the specified key
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Project identifier (UUID)
key = 'key_example' # str | Metadata key

try:
    # Update project metadata
    api_response = api_instance.update_project_metadata(body, project_id, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata value to set for the specified key | 
 **project_id** | [**str**](.md)| Project identifier (UUID) | 
 **key** | **str**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

