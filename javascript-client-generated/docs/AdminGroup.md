# TmiThreatModelingImprovedApi.AdminGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internalUuid** | **String** | Internal system UUID for the group | 
**provider** | **String** | OAuth/SAML provider identifier, or \&quot;*\&quot; for provider-independent groups | 
**groupName** | **String** | Provider-assigned group name | 
**name** | **String** | Human-readable group name | [optional] 
**description** | **String** | Group description | [optional] 
**firstUsed** | **Date** | First time this group was referenced | 
**lastUsed** | **Date** | Last time this group was referenced | 
**usageCount** | **Number** | Number of times this group has been referenced | 
**usedInAuthorizations** | **Boolean** | Whether this group is used in any authorizations (enriched) | [optional] 
**usedInAdminGrants** | **Boolean** | Whether this group is used in any admin grants (enriched) | [optional] 
**memberCount** | **Number** | Number of members in the group from IdP (enriched, if available) | [optional] 
