# TmiThreatModelingImprovedApi.AdminUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internalUuid** | **String** | Internal system UUID for the user | 
**provider** | **String** | OAuth/SAML provider identifier | 
**providerUserId** | **String** | Provider-assigned user identifier | 
**email** | **String** | User email address | 
**name** | **String** | User display name | 
**emailVerified** | **Boolean** | Whether the email has been verified | 
**createdAt** | **Date** | Account creation timestamp | 
**modifiedAt** | **Date** | Last modification timestamp | 
**lastLogin** | **Date** | Last login timestamp | [optional] 
**isAdmin** | **Boolean** | Whether the user has administrator privileges (enriched) | [optional] 
**groups** | **[String]** | List of group names the user belongs to (enriched) | [optional] 
**activeThreatModels** | **Number** | Number of active threat models owned by user (enriched) | [optional] 
