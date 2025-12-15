# TmiThreatModelingImprovedApi.CreateAdministratorRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **String** | User email to grant admin privileges (mutually exclusive with provider_user_id and group_name) | [optional] 
**providerUserId** | **String** | Provider&#x27;s user ID to grant admin privileges (mutually exclusive with email and group_name) | [optional] 
**groupName** | **String** | Group name to grant admin privileges (mutually exclusive with email and provider_user_id) | [optional] 
**provider** | **String** | OAuth/SAML provider | 
