# Authorization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **string** | Role: reader (view), writer (edit), owner (full control) | [default to null]
**PrincipalType** | **string** | Type of principal: user (individual) or group | [default to null]
**Provider** | **string** | Identity provider name (e.g., \&quot;google\&quot;, \&quot;github\&quot;, \&quot;microsoft\&quot;, \&quot;tmi\&quot;). Use \&quot;*\&quot; for provider-independent groups. | [default to null]
**ProviderId** | **string** | Provider-assigned identifier. For users: provider_user_id (e.g., email or OAuth sub). For groups: group_name. | [default to null]
**DisplayName** | **string** | Human-readable display name for UI presentation | [optional] [default to null]
**Email** | **string** | Email address (required for users, optional for groups) | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

