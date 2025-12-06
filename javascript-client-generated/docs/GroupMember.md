# TmiJsClient.GroupMember

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique identifier for the membership record | 
**groupInternalUuid** | **String** | Internal UUID of the group | 
**userInternalUuid** | **String** | Internal UUID of the user | 
**userEmail** | **String** | Email address of the user | 
**userName** | **String** | Display name of the user | 
**userProvider** | **String** | OAuth/SAML provider for the user | 
**userProviderUserId** | **String** | Provider-specific user identifier | 
**addedByInternalUuid** | **String** | Internal UUID of the administrator who added this member | [optional] 
**addedByEmail** | **String** | Email of the administrator who added this member | [optional] 
**addedAt** | **Date** | Timestamp when the user was added to the group (RFC3339) | 
**notes** | **String** | Optional notes about this membership | [optional] 
