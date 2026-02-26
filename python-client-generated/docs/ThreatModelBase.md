# ThreatModelBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the threat model | 
**description** | **str** | Description of the threat model | [optional] 
**owner** | **AllOfThreatModelBaseOwner** | User who owns the threat model (can be null for orphaned models) | 
**threat_model_framework** | **str** | The framework used for this threat model | 
**authorization** | [**list[Authorization]**](Authorization.md) | List of users and their roles for this threat model | 
**metadata** | [**list[Metadata]**](Metadata.md) | Key-value pairs for additional threat model metadata | [optional] 
**issue_uri** | **str** | URL to an issue in an issue tracking system for this threat model | [optional] 
**status** | **str** | Status of the threat model in the organization&#x27;s threat modeling or SDLC process. Examples: \&quot;Not started\&quot;, \&quot;In progress\&quot;, \&quot;Review\&quot;, \&quot;Approved\&quot;, \&quot;Closed\&quot; | [optional] 
**alias** | **list[str]** | Alternative names or identifiers for the threat model | [optional] 
**security_reviewer** | **AllOfThreatModelBaseSecurityReviewer** | Security reviewer assigned to this threat model. When set, the security reviewer is automatically added to the authorization list with the owner role. The security reviewer&#x27;s owner role cannot be removed via authorization changes while they remain assigned as security reviewer. To change the security reviewer&#x27;s authorization, first unassign them as security reviewer. | [optional] 
**project_id** | **str** | Optional reference to the project this threat model belongs to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

