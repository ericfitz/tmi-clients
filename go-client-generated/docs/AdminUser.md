# AdminUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InternalUuid** | **string** | Internal system UUID for the user | [default to null]
**Provider** | **string** | OAuth/SAML provider identifier | [default to null]
**ProviderUserId** | **string** | Provider-assigned user identifier | [default to null]
**Email** | **string** | User email address | [default to null]
**Name** | **string** | User display name | [default to null]
**EmailVerified** | **bool** | Whether the email has been verified | [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Account creation timestamp | [default to null]
**ModifiedAt** | [**time.Time**](time.Time.md) | Last modification timestamp | [default to null]
**LastLogin** | [**time.Time**](time.Time.md) | Last login timestamp | [optional] [default to null]
**IsAdmin** | **bool** | Whether the user has administrator privileges (enriched) | [optional] [default to null]
**Groups** | **[]string** | List of group names the user belongs to (enriched) | [optional] [default to null]
**ActiveThreatModels** | **int32** | Number of active threat models owned by user (enriched) | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

