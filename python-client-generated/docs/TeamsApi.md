# tmi_client.TeamsApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_team_metadata**](TeamsApi.md#bulk_create_team_metadata) | **POST** /teams/{team_id}/metadata/bulk | Bulk create team metadata
[**bulk_replace_team_metadata**](TeamsApi.md#bulk_replace_team_metadata) | **PUT** /teams/{team_id}/metadata/bulk | Bulk replace team metadata
[**bulk_upsert_team_metadata**](TeamsApi.md#bulk_upsert_team_metadata) | **PATCH** /teams/{team_id}/metadata/bulk | Bulk upsert team metadata
[**create_team**](TeamsApi.md#create_team) | **POST** /teams | Create a team
[**create_team_metadata**](TeamsApi.md#create_team_metadata) | **POST** /teams/{team_id}/metadata | Create team metadata
[**delete_team**](TeamsApi.md#delete_team) | **DELETE** /teams/{team_id} | Delete a team
[**delete_team_metadata**](TeamsApi.md#delete_team_metadata) | **DELETE** /teams/{team_id}/metadata/{key} | Delete team metadata
[**get_team**](TeamsApi.md#get_team) | **GET** /teams/{team_id} | Get a team
[**get_team_metadata**](TeamsApi.md#get_team_metadata) | **GET** /teams/{team_id}/metadata | Get team metadata
[**list_teams**](TeamsApi.md#list_teams) | **GET** /teams | List teams
[**patch_team**](TeamsApi.md#patch_team) | **PATCH** /teams/{team_id} | Patch a team
[**update_team**](TeamsApi.md#update_team) | **PUT** /teams/{team_id} | Update a team
[**update_team_metadata**](TeamsApi.md#update_team_metadata) | **PUT** /teams/{team_id}/metadata/{key} | Update team metadata

# **bulk_create_team_metadata**
> list[Metadata] bulk_create_team_metadata(body, team_id)

Bulk create team metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.TeamsApi(tmi_client.ApiClient(configuration))
body = [tmi_client.Metadata()] # list[Metadata] | Bulk metadata entries to create
team_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Team identifier (UUID)

try:
    # Bulk create team metadata
    api_response = api_instance.bulk_create_team_metadata(body, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->bulk_create_team_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Metadata]**](Metadata.md)| Bulk metadata entries to create | 
 **team_id** | [**str**](.md)| Team identifier (UUID) | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_replace_team_metadata**
> list[Metadata] bulk_replace_team_metadata(body, team_id)

Bulk replace team metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.TeamsApi(tmi_client.ApiClient(configuration))
body = [tmi_client.Metadata()] # list[Metadata] | Complete set of metadata entries for replacement
team_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Team identifier (UUID)

try:
    # Bulk replace team metadata
    api_response = api_instance.bulk_replace_team_metadata(body, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->bulk_replace_team_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Metadata]**](Metadata.md)| Complete set of metadata entries for replacement | 
 **team_id** | [**str**](.md)| Team identifier (UUID) | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_team_metadata**
> list[Metadata] bulk_upsert_team_metadata(body, team_id)

Bulk upsert team metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.TeamsApi(tmi_client.ApiClient(configuration))
body = tmi_client.BulkPatchRequest() # BulkPatchRequest | Metadata entries to update
team_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Team identifier (UUID)

try:
    # Bulk upsert team metadata
    api_response = api_instance.bulk_upsert_team_metadata(body, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->bulk_upsert_team_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkPatchRequest**](BulkPatchRequest.md)| Metadata entries to update | 
 **team_id** | [**str**](.md)| Team identifier (UUID) | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_team**
> Team create_team(body)

Create a team

Creates a new team. The creating user is automatically added as a member.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.TeamsApi(tmi_client.ApiClient(configuration))
body = tmi_client.TeamBase() # TeamBase | Team creation data

try:
    # Create a team
    api_response = api_instance.create_team(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamBase**](TeamBase.md)| Team creation data | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_team_metadata**
> Metadata create_team_metadata(body, team_id)

Create team metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.TeamsApi(tmi_client.ApiClient(configuration))
body = tmi_client.Metadata() # Metadata | Metadata entry to create
team_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Team identifier (UUID)

try:
    # Create team metadata
    api_response = api_instance.create_team_metadata(body, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->create_team_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata entry to create | 
 **team_id** | [**str**](.md)| Team identifier (UUID) | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team**
> delete_team(team_id)

Delete a team

Deletes a team. Requires owner role or admin access. Returns 409 if the team is referenced by projects.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.TeamsApi(tmi_client.ApiClient(configuration))
team_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Team UUID

try:
    # Delete a team
    api_instance.delete_team(team_id)
except ApiException as e:
    print("Exception when calling TeamsApi->delete_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | [**str**](.md)| Team UUID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_metadata**
> delete_team_metadata(team_id, key)

Delete team metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.TeamsApi(tmi_client.ApiClient(configuration))
team_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Team identifier (UUID)
key = 'key_example' # str | Metadata key

try:
    # Delete team metadata
    api_instance.delete_team_metadata(team_id, key)
except ApiException as e:
    print("Exception when calling TeamsApi->delete_team_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | [**str**](.md)| Team identifier (UUID) | 
 **key** | **str**| Metadata key | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> Team get_team(team_id)

Get a team

Returns a team by ID. Requires team membership or admin access.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.TeamsApi(tmi_client.ApiClient(configuration))
team_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Team UUID

try:
    # Get a team
    api_response = api_instance.get_team(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | [**str**](.md)| Team UUID | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_metadata**
> list[Metadata] get_team_metadata(team_id)

Get team metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.TeamsApi(tmi_client.ApiClient(configuration))
team_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Team identifier (UUID)

try:
    # Get team metadata
    api_response = api_instance.get_team_metadata(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | [**str**](.md)| Team identifier (UUID) | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_teams**
> ListTeamsResponse list_teams(limit=limit, offset=offset, name=name, status=status, member_user_id=member_user_id, related_to=related_to, relationship=relationship, transitive=transitive)

List teams

Returns a paginated list of teams. Non-admin users see only teams they are members of.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.TeamsApi(tmi_client.ApiClient(configuration))
limit = 20 # int | Maximum number of results per page (optional) (default to 20)
offset = 0 # int | Number of results to skip (optional) (default to 0)
name = 'name_example' # str | Filter by team name (partial match) (optional)
status = 'status_example' # str | Filter by status (exact match, comma-separated for multiple) (optional)
member_user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter teams that include this user as a member (optional)
related_to = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Include teams related to this team ID (optional)
relationship = tmi_client.RelationshipType() # RelationshipType | Filter related teams by relationship type. Only used with related_to. (optional)
transitive = false # bool | When true with related_to + relationship, follow parent/child chains transitively (max depth 10) (optional) (default to false)

try:
    # List teams
    api_response = api_instance.list_teams(limit=limit, offset=offset, name=name, status=status, member_user_id=member_user_id, related_to=related_to, relationship=relationship, transitive=transitive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->list_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results per page | [optional] [default to 20]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
 **name** | **str**| Filter by team name (partial match) | [optional] 
 **status** | **str**| Filter by status (exact match, comma-separated for multiple) | [optional] 
 **member_user_id** | [**str**](.md)| Filter teams that include this user as a member | [optional] 
 **related_to** | [**str**](.md)| Include teams related to this team ID | [optional] 
 **relationship** | [**RelationshipType**](.md)| Filter related teams by relationship type. Only used with related_to. | [optional] 
 **transitive** | **bool**| When true with related_to + relationship, follow parent/child chains transitively (max depth 10) | [optional] [default to false]

### Return type

[**ListTeamsResponse**](ListTeamsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_team**
> Team patch_team(body, team_id)

Patch a team

Partial update of a team using JSON Patch (RFC 6902). Requires team membership or admin access.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.TeamsApi(tmi_client.ApiClient(configuration))
body = [tmi_client.JsonPatchDocumentInner()] # list[JsonPatchDocumentInner] | Partial team data for update
team_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Team UUID

try:
    # Patch a team
    api_response = api_instance.patch_team(body, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->patch_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| Partial team data for update | 
 **team_id** | [**str**](.md)| Team UUID | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> Team update_team(body, team_id)

Update a team

Full replacement update of a team. Requires team membership or admin access.

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.TeamsApi(tmi_client.ApiClient(configuration))
body = tmi_client.TeamBase() # TeamBase | Complete team data for replacement
team_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Team UUID

try:
    # Update a team
    api_response = api_instance.update_team(body, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamBase**](TeamBase.md)| Complete team data for replacement | 
 **team_id** | [**str**](.md)| Team UUID | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team_metadata**
> Metadata update_team_metadata(body, team_id, key)

Update team metadata

### Example
```python
from __future__ import print_function
import time
import tmi_client
from tmi_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = tmi_client.TeamsApi(tmi_client.ApiClient(configuration))
body = tmi_client.Metadata() # Metadata | Metadata value to set for the specified key
team_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Team identifier (UUID)
key = 'key_example' # str | Metadata key

try:
    # Update team metadata
    api_response = api_instance.update_team_metadata(body, team_id, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update_team_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata value to set for the specified key | 
 **team_id** | [**str**](.md)| Team identifier (UUID) | 
 **key** | **str**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

