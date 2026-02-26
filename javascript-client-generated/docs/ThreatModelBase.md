# TmiJsClient.ThreatModelBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Name of the threat model | 
**description** | **String** | Description of the threat model | [optional] 
**owner** | **AllOfThreatModelBaseOwner** | User who owns the threat model (can be null for orphaned models) | 
**threatModelFramework** | **String** | The framework used for this threat model | 
**authorization** | [**[Authorization]**](Authorization.md) | List of users and their roles for this threat model | 
**metadata** | [**[Metadata]**](Metadata.md) | Key-value pairs for additional threat model metadata | [optional] 
**issueUri** | **String** | URL to an issue in an issue tracking system for this threat model | [optional] 
**status** | **String** | Status of the threat model in the organization&#x27;s threat modeling or SDLC process. Examples: \&quot;Not started\&quot;, \&quot;In progress\&quot;, \&quot;Review\&quot;, \&quot;Approved\&quot;, \&quot;Closed\&quot; | [optional] 
**alias** | **[String]** | Alternative names or identifiers for the threat model | [optional] 
**securityReviewer** | **AllOfThreatModelBaseSecurityReviewer** | Security reviewer assigned to this threat model. When set, the security reviewer is automatically added to the authorization list with the owner role. The security reviewer&#x27;s owner role cannot be removed via authorization changes while they remain assigned as security reviewer. To change the security reviewer&#x27;s authorization, first unassign them as security reviewer. | [optional] 
**projectId** | **String** | Optional reference to the project this threat model belongs to | [optional] 
