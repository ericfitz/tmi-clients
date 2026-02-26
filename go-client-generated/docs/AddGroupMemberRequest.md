# AddGroupMemberRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UserInternalUuid** | **string** | Internal UUID of the user to add to the group | [optional] [default to null]
**Notes** | **string** | Optional notes about this membership | [optional] [default to null]
**SubjectType** | **string** | Type of member to add: user or group | [optional] [default to SUBJECT_TYPE.USER]
**MemberGroupInternalUuid** | **string** | Internal UUID of the group to add as a member (required when subject_type is group) | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

