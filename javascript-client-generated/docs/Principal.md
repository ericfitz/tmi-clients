# TmiJsClient.Principal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principalType** | **String** | Type of principal: user (individual) or group | 
**provider** | **String** | Identity provider name (e.g., \&quot;google\&quot;, \&quot;github\&quot;, \&quot;microsoft\&quot;, \&quot;tmi\&quot;). Use \&quot;*\&quot; for provider-independent groups. | 
**providerId** | **String** | Provider-assigned identifier. For users: provider_user_id (e.g., email or OAuth sub). For groups: group_name. | 
**displayName** | **String** | Human-readable display name for UI presentation | [optional] 
**email** | **String** | Email address (required for users, optional for groups) | [optional] 

<a name="PrincipalTypeEnum"></a>
## Enum: PrincipalTypeEnum

* `user` (value: `"user"`)
* `group` (value: `"group"`)

