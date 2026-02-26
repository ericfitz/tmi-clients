# TmiJsClient.AddGroupMemberRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**userInternalUuid** | **String** | Internal UUID of the user to add to the group | [optional] 
**notes** | **String** | Optional notes about this membership | [optional] 
**subjectType** | **String** | Type of member to add: user or group | [optional] [default to &#x27;user&#x27;]
**memberGroupInternalUuid** | **String** | Internal UUID of the group to add as a member (required when subject_type is group) | [optional] 

<a name="SubjectTypeEnum"></a>
## Enum: SubjectTypeEnum

* `user` (value: `"user"`)
* `group` (value: `"group"`)

