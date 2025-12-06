# Principal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_type** | **str** | Type of principal: user (individual) or group | 
**provider** | **str** | Identity provider name (e.g., \&quot;google\&quot;, \&quot;github\&quot;, \&quot;microsoft\&quot;, \&quot;test\&quot;). Use \&quot;*\&quot; for provider-independent groups. | 
**provider_id** | **str** | Provider-assigned identifier. For users: provider_user_id (e.g., email or OAuth sub). For groups: group_name. | 
**display_name** | **str** | Human-readable display name for UI presentation | [optional] 
**email** | **str** | Email address (required for users, optional for groups) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

