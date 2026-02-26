# GroupMember

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the membership record | [default to null]
**GroupInternalUuid** | **string** | Internal UUID of the group | [default to null]
**UserInternalUuid** | **string** | Internal UUID of the user | [optional] [default to null]
**UserEmail** | **string** | Email address of the user | [optional] [default to null]
**UserName** | **string** | Display name of the user | [optional] [default to null]
**UserProvider** | **string** | OAuth/SAML provider for the user | [optional] [default to null]
**UserProviderUserId** | **string** | Provider-specific user identifier | [optional] [default to null]
**AddedByInternalUuid** | **string** | Internal UUID of the administrator who added this member | [optional] [default to null]
**AddedByEmail** | **string** | Email of the administrator who added this member | [optional] [default to null]
**AddedAt** | [**time.Time**](time.Time.md) | Timestamp when the user was added to the group (RFC3339) | [default to null]
**Notes** | **string** | Optional notes about this membership | [optional] [default to null]
**SubjectType** | **string** | Type of member: user (direct user membership) or group (group-in-group membership) | [default to SUBJECT_TYPE.USER]
**MemberGroupInternalUuid** | **string** | Internal UUID of the member group (when subject_type is group) | [optional] [default to null]
**MemberGroupName** | **string** | Display name of the member group (when subject_type is group) | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

