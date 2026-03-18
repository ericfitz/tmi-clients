# AuditEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the audit entry | 
**threat_model_id** | **str** | ID of the threat model this audit entry belongs to | 
**object_type** | **str** | Type of the entity that was mutated | 
**object_id** | **str** | ID of the entity that was mutated | 
**version** | **int** | Version number. Null if the version snapshot has been pruned and rollback is no longer available. | [optional] 
**change_type** | **str** | Type of mutation | 
**actor** | [**AuditActor**](AuditActor.md) |  | 
**change_summary** | **str** | Human-readable summary of what changed | [optional] 
**created_at** | **datetime** | When the mutation occurred | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

