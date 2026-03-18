# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BulkCreateTeamMetadata**](TeamsApi.md#BulkCreateTeamMetadata) | **Post** /teams/{team_id}/metadata/bulk | Bulk create team metadata
[**BulkReplaceTeamMetadata**](TeamsApi.md#BulkReplaceTeamMetadata) | **Put** /teams/{team_id}/metadata/bulk | Bulk replace team metadata
[**BulkUpsertTeamMetadata**](TeamsApi.md#BulkUpsertTeamMetadata) | **Patch** /teams/{team_id}/metadata/bulk | Bulk upsert team metadata
[**CreateTeam**](TeamsApi.md#CreateTeam) | **Post** /teams | Create a team
[**CreateTeamMetadata**](TeamsApi.md#CreateTeamMetadata) | **Post** /teams/{team_id}/metadata | Create team metadata
[**DeleteTeam**](TeamsApi.md#DeleteTeam) | **Delete** /teams/{team_id} | Delete a team
[**DeleteTeamMetadata**](TeamsApi.md#DeleteTeamMetadata) | **Delete** /teams/{team_id}/metadata/{key} | Delete team metadata
[**GetTeam**](TeamsApi.md#GetTeam) | **Get** /teams/{team_id} | Get a team
[**GetTeamMetadata**](TeamsApi.md#GetTeamMetadata) | **Get** /teams/{team_id}/metadata | Get team metadata
[**ListTeams**](TeamsApi.md#ListTeams) | **Get** /teams | List teams
[**PatchTeam**](TeamsApi.md#PatchTeam) | **Patch** /teams/{team_id} | Patch a team
[**UpdateTeam**](TeamsApi.md#UpdateTeam) | **Put** /teams/{team_id} | Update a team
[**UpdateTeamMetadata**](TeamsApi.md#UpdateTeamMetadata) | **Put** /teams/{team_id}/metadata/{key} | Update team metadata

# **BulkCreateTeamMetadata**
> []Metadata BulkCreateTeamMetadata(ctx, body, teamId)
Bulk create team metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]Metadata**](Metadata.md)| Bulk metadata entries to create | 
  **teamId** | [**string**](.md)| Team identifier (UUID) | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **BulkReplaceTeamMetadata**
> []Metadata BulkReplaceTeamMetadata(ctx, body, teamId)
Bulk replace team metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]Metadata**](Metadata.md)| Complete set of metadata entries for replacement | 
  **teamId** | [**string**](.md)| Team identifier (UUID) | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **BulkUpsertTeamMetadata**
> []Metadata BulkUpsertTeamMetadata(ctx, body, teamId)
Bulk upsert team metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**BulkPatchRequest**](BulkPatchRequest.md)| Metadata entries to update | 
  **teamId** | [**string**](.md)| Team identifier (UUID) | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateTeam**
> Team CreateTeam(ctx, body)
Create a team

Creates a new team. The creating user is automatically added as a member.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**TeamBase**](TeamBase.md)| Team creation data | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateTeamMetadata**
> Metadata CreateTeamMetadata(ctx, body, teamId)
Create team metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**Metadata**](Metadata.md)| Metadata entry to create | 
  **teamId** | [**string**](.md)| Team identifier (UUID) | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteTeam**
> DeleteTeam(ctx, teamId)
Delete a team

Deletes a team. Requires owner role or admin access. Returns 409 if the team is referenced by projects.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **teamId** | [**string**](.md)| Team UUID | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteTeamMetadata**
> DeleteTeamMetadata(ctx, teamId, key)
Delete team metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **teamId** | [**string**](.md)| Team identifier (UUID) | 
  **key** | **string**| Metadata key | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetTeam**
> Team GetTeam(ctx, teamId)
Get a team

Returns a team by ID. Requires team membership or admin access.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **teamId** | [**string**](.md)| Team UUID | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetTeamMetadata**
> []Metadata GetTeamMetadata(ctx, teamId)
Get team metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **teamId** | [**string**](.md)| Team identifier (UUID) | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListTeams**
> ListTeamsResponse ListTeams(ctx, optional)
List teams

Returns a paginated list of teams. Non-admin users see only teams they are members of.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***TeamsApiListTeamsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a TeamsApiListTeamsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **optional.Int32**| Maximum number of results per page | [default to 20]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]
 **name** | **optional.String**| Filter by team name (partial match) | 
 **status** | **optional.String**| Filter by status (exact match, comma-separated for multiple) | 
 **memberUserId** | [**optional.Interface of string**](.md)| Filter teams that include this user as a member | 
 **relatedTo** | [**optional.Interface of string**](.md)| Include teams related to this team ID | 
 **relationship** | [**optional.Interface of RelationshipType**](.md)| Filter related teams by relationship type. Only used with related_to. | 
 **transitive** | **optional.Bool**| When true with related_to + relationship, follow parent/child chains transitively (max depth 10) | [default to false]

### Return type

[**ListTeamsResponse**](ListTeamsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PatchTeam**
> Team PatchTeam(ctx, body, teamId)
Patch a team

Partial update of a team using JSON Patch (RFC 6902). Requires team membership or admin access.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]JsonPatchDocumentInner**](JsonPatchDocument_inner.md)| Partial team data for update | 
  **teamId** | [**string**](.md)| Team UUID | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateTeam**
> Team UpdateTeam(ctx, body, teamId)
Update a team

Full replacement update of a team. Requires team membership or admin access.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**TeamBase**](TeamBase.md)| Complete team data for replacement | 
  **teamId** | [**string**](.md)| Team UUID | 

### Return type

[**Team**](Team.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateTeamMetadata**
> Metadata UpdateTeamMetadata(ctx, body, teamId, key)
Update team metadata

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**Metadata**](Metadata.md)| Metadata value to set for the specified key | 
  **teamId** | [**string**](.md)| Team identifier (UUID) | 
  **key** | **string**| Metadata key | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

