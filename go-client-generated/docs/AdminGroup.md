# AdminGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InternalUuid** | **string** | Internal system UUID for the group | [default to null]
**Provider** | **string** | OAuth/SAML provider identifier, or \&quot;*\&quot; for provider-independent groups | [default to null]
**GroupName** | **string** | Provider-assigned group name | [default to null]
**Name** | **string** | Human-readable group name | [optional] [default to null]
**Description** | **string** | Group description | [optional] [default to null]
**FirstUsed** | [**time.Time**](time.Time.md) | First time this group was referenced | [default to null]
**LastUsed** | [**time.Time**](time.Time.md) | Last time this group was referenced | [default to null]
**UsageCount** | **int32** | Number of times this group has been referenced | [default to null]
**UsedInAuthorizations** | **bool** | Whether this group is used in any authorizations (enriched) | [optional] [default to null]
**UsedInAdminGrants** | **bool** | Whether this group is used in any admin grants (enriched) | [optional] [default to null]
**MemberCount** | **int32** | Number of members in the group from IdP (enriched, if available) | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

