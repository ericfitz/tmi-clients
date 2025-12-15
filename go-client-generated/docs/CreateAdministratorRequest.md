# CreateAdministratorRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Email** | **string** | User email to grant admin privileges (mutually exclusive with provider_user_id and group_name) | [optional] [default to null]
**ProviderUserId** | **string** | Provider&#x27;s user ID to grant admin privileges (mutually exclusive with email and group_name) | [optional] [default to null]
**GroupName** | **string** | Group name to grant admin privileges (mutually exclusive with email and provider_user_id) | [optional] [default to null]
**Provider** | **string** | OAuth/SAML provider | [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

