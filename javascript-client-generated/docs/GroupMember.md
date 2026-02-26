# TmiJsClient.GroupMember

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique identifier for the membership record | 
**groupInternalUuid** | **String** | Internal UUID of the group | 
**userInternalUuid** | **String** | Internal UUID of the user | [optional] 
**userEmail** | **String** | Email address of the user | [optional] 
**userName** | **String** | Display name of the user | [optional] 
**userProvider** | **String** | OAuth/SAML provider for the user | [optional] 
**userProviderUserId** | **String** | Provider-specific user identifier | [optional] 
**addedByInternalUuid** | **String** | Internal UUID of the administrator who added this member | [optional] 
**addedByEmail** | **String** | Email of the administrator who added this member | [optional] 
**addedAt** | **Date** | Timestamp when the user was added to the group (RFC3339) | 
**notes** | **String** | Optional notes about this membership | [optional] 
**subjectType** | **String** | Type of member: user (direct user membership) or group (group-in-group membership) | [default to &#x27;user&#x27;]
**memberGroupInternalUuid** | **String** | Internal UUID of the member group (when subject_type is group) | [optional] 
**memberGroupName** | **String** | Display name of the member group (when subject_type is group) | [optional] 

<a name="SubjectTypeEnum"></a>
## Enum: SubjectTypeEnum

* `user` (value: `"user"`)
* `group` (value: `"group"`)

