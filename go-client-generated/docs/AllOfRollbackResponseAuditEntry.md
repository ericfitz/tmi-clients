# AllOfRollbackResponseAuditEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the audit entry | [default to null]
**ThreatModelId** | **string** | ID of the threat model this audit entry belongs to | [default to null]
**ObjectType** | **string** | Type of the entity that was mutated | [default to null]
**ObjectId** | **string** | ID of the entity that was mutated | [default to null]
**Version** | **int32** | Version number. Null if the version snapshot has been pruned and rollback is no longer available. | [optional] [default to null]
**ChangeType** | **string** | Type of mutation | [default to null]
**Actor** | [***AuditActor**](AuditActor.md) |  | [default to null]
**ChangeSummary** | **string** | Human-readable summary of what changed | [optional] [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | When the mutation occurred | [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

