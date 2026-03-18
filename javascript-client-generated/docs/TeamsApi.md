# TmiJsClient.TeamsApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkCreateTeamMetadata**](TeamsApi.md#bulkCreateTeamMetadata) | **POST** /teams/{team_id}/metadata/bulk | Bulk create team metadata
[**bulkReplaceTeamMetadata**](TeamsApi.md#bulkReplaceTeamMetadata) | **PUT** /teams/{team_id}/metadata/bulk | Bulk replace team metadata
[**bulkUpsertTeamMetadata**](TeamsApi.md#bulkUpsertTeamMetadata) | **PATCH** /teams/{team_id}/metadata/bulk | Bulk upsert team metadata
[**createTeam**](TeamsApi.md#createTeam) | **POST** /teams | Create a team
[**createTeamMetadata**](TeamsApi.md#createTeamMetadata) | **POST** /teams/{team_id}/metadata | Create team metadata
[**deleteTeam**](TeamsApi.md#deleteTeam) | **DELETE** /teams/{team_id} | Delete a team
[**deleteTeamMetadata**](TeamsApi.md#deleteTeamMetadata) | **DELETE** /teams/{team_id}/metadata/{key} | Delete team metadata
[**getTeam**](TeamsApi.md#getTeam) | **GET** /teams/{team_id} | Get a team
[**getTeamMetadata**](TeamsApi.md#getTeamMetadata) | **GET** /teams/{team_id}/metadata | Get team metadata
[**listTeams**](TeamsApi.md#listTeams) | **GET** /teams | List teams
[**patchTeam**](TeamsApi.md#patchTeam) | **PATCH** /teams/{team_id} | Patch a team
[**updateTeam**](TeamsApi.md#updateTeam) | **PUT** /teams/{team_id} | Update a team
[**updateTeamMetadata**](TeamsApi.md#updateTeamMetadata) | **PUT** /teams/{team_id}/metadata/{key} | Update team metadata

<a name="bulkCreateTeamMetadata"></a>
# **bulkCreateTeamMetadata**
> [Metadata] bulkCreateTeamMetadata(body, teamId)

Bulk create team metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.TeamsApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | Bulk metadata entries to create
let teamId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Team identifier (UUID)

apiInstance.bulkCreateTeamMetadata(body, teamId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)| Bulk metadata entries to create | 
 **teamId** | [**String**](.md)| Team identifier (UUID) | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkReplaceTeamMetadata"></a>
# **bulkReplaceTeamMetadata**
> [Metadata] bulkReplaceTeamMetadata(body, teamId)

Bulk replace team metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.TeamsApi();
let body = [new TmiJsClient.Metadata()]; // [Metadata] | Complete set of metadata entries for replacement
let teamId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Team identifier (UUID)

apiInstance.bulkReplaceTeamMetadata(body, teamId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[Metadata]**](Metadata.md)| Complete set of metadata entries for replacement | 
 **teamId** | [**String**](.md)| Team identifier (UUID) | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="bulkUpsertTeamMetadata"></a>
# **bulkUpsertTeamMetadata**
> [Metadata] bulkUpsertTeamMetadata(body, teamId)

Bulk upsert team metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.TeamsApi();
let body = new TmiJsClient.BulkPatchRequest(); // BulkPatchRequest | Metadata entries to update
let teamId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Team identifier (UUID)

apiInstance.bulkUpsertTeamMetadata(body, teamId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkPatchRequest**](BulkPatchRequest.md)| Metadata entries to update | 
 **teamId** | [**String**](.md)| Team identifier (UUID) | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createTeam"></a>
# **createTeam**
> Team createTeam(body)

Create a team

Creates a new team. The creating user is automatically added as a member.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.TeamsApi();
let body = new TmiJsClient.TeamBase(); // TeamBase | Team creation data

apiInstance.createTeam(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

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

<a name="createTeamMetadata"></a>
# **createTeamMetadata**
> Metadata createTeamMetadata(body, teamId)

Create team metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.TeamsApi();
let body = new TmiJsClient.Metadata(); // Metadata | Metadata entry to create
let teamId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Team identifier (UUID)

apiInstance.createTeamMetadata(body, teamId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata entry to create | 
 **teamId** | [**String**](.md)| Team identifier (UUID) | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteTeam"></a>
# **deleteTeam**
> deleteTeam(teamId)

Delete a team

Deletes a team. Requires owner role or admin access. Returns 409 if the team is referenced by projects.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.TeamsApi();
let teamId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Team UUID

apiInstance.deleteTeam(teamId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | [**String**](.md)| Team UUID | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteTeamMetadata"></a>
# **deleteTeamMetadata**
> deleteTeamMetadata(teamId, key)

Delete team metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.TeamsApi();
let teamId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Team identifier (UUID)
let key = "key_example"; // String | Metadata key

apiInstance.deleteTeamMetadata(teamId, key).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | [**String**](.md)| Team identifier (UUID) | 
 **key** | **String**| Metadata key | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getTeam"></a>
# **getTeam**
> Team getTeam(teamId)

Get a team

Returns a team by ID. Requires team membership or admin access.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.TeamsApi();
let teamId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Team UUID

apiInstance.getTeam(teamId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | [**String**](.md)| Team UUID | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getTeamMetadata"></a>
# **getTeamMetadata**
> [Metadata] getTeamMetadata(teamId)

Get team metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.TeamsApi();
let teamId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Team identifier (UUID)

apiInstance.getTeamMetadata(teamId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | [**String**](.md)| Team identifier (UUID) | 

### Return type

[**[Metadata]**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listTeams"></a>
# **listTeams**
> ListTeamsResponse listTeams(opts)

List teams

Returns a paginated list of teams. Non-admin users see only teams they are members of.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.TeamsApi();
let opts = { 
  'limit': 20, // Number | Maximum number of results per page
  'offset': 0, // Number | Number of results to skip
  'name': "name_example", // String | Filter by team name (partial match)
  'status': "status_example", // String | Filter by status (exact match, comma-separated for multiple)
  'memberUserId': "38400000-8cf0-11bd-b23e-10b96e4ef00d", // String | Filter teams that include this user as a member
  'relatedTo': "38400000-8cf0-11bd-b23e-10b96e4ef00d", // String | Include teams related to this team ID
  'relationship': new TmiJsClient.RelationshipType(), // RelationshipType | Filter related teams by relationship type. Only used with related_to.
  'transitive': false // Boolean | When true with related_to + relationship, follow parent/child chains transitively (max depth 10)
};
apiInstance.listTeams(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **Number**| Maximum number of results per page | [optional] [default to 20]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]
 **name** | **String**| Filter by team name (partial match) | [optional] 
 **status** | **String**| Filter by status (exact match, comma-separated for multiple) | [optional] 
 **memberUserId** | [**String**](.md)| Filter teams that include this user as a member | [optional] 
 **relatedTo** | [**String**](.md)| Include teams related to this team ID | [optional] 
 **relationship** | [**RelationshipType**](.md)| Filter related teams by relationship type. Only used with related_to. | [optional] 
 **transitive** | **Boolean**| When true with related_to + relationship, follow parent/child chains transitively (max depth 10) | [optional] [default to false]

### Return type

[**ListTeamsResponse**](ListTeamsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="patchTeam"></a>
# **patchTeam**
> Team patchTeam(body, teamId)

Patch a team

Partial update of a team using JSON Patch (RFC 6902). Requires team membership or admin access.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.TeamsApi();
let body = [new TmiJsClient.JsonPatchDocumentInner()]; // [JsonPatchDocumentInner] | Partial team data for update
let teamId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Team UUID

apiInstance.patchTeam(body, teamId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md)| Partial team data for update | 
 **teamId** | [**String**](.md)| Team UUID | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

<a name="updateTeam"></a>
# **updateTeam**
> Team updateTeam(body, teamId)

Update a team

Full replacement update of a team. Requires team membership or admin access.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.TeamsApi();
let body = new TmiJsClient.TeamBase(); // TeamBase | Complete team data for replacement
let teamId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Team UUID

apiInstance.updateTeam(body, teamId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamBase**](TeamBase.md)| Complete team data for replacement | 
 **teamId** | [**String**](.md)| Team UUID | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateTeamMetadata"></a>
# **updateTeamMetadata**
> Metadata updateTeamMetadata(body, teamId, key)

Update team metadata

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.TeamsApi();
let body = new TmiJsClient.Metadata(); // Metadata | Metadata value to set for the specified key
let teamId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Team identifier (UUID)
let key = "key_example"; // String | Metadata key

apiInstance.updateTeamMetadata(body, teamId, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| Metadata value to set for the specified key | 
 **teamId** | [**String**](.md)| Team identifier (UUID) | 
 **key** | **String**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

