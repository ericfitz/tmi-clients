# TmiJsClient.AuditEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique identifier for the audit entry | 
**threatModelId** | **String** | ID of the threat model this audit entry belongs to | 
**objectType** | **String** | Type of the entity that was mutated | 
**objectId** | **String** | ID of the entity that was mutated | 
**version** | **Number** | Version number. Null if the version snapshot has been pruned and rollback is no longer available. | [optional] 
**changeType** | **String** | Type of mutation | 
**actor** | [**AuditActor**](AuditActor.md) |  | 
**changeSummary** | **String** | Human-readable summary of what changed | [optional] 
**createdAt** | **Date** | When the mutation occurred | 

<a name="ObjectTypeEnum"></a>
## Enum: ObjectTypeEnum

* `threatModel` (value: `"threat_model"`)
* `diagram` (value: `"diagram"`)
* `threat` (value: `"threat"`)
* `asset` (value: `"asset"`)
* `document` (value: `"document"`)
* `note` (value: `"note"`)
* `repository` (value: `"repository"`)


<a name="ChangeTypeEnum"></a>
## Enum: ChangeTypeEnum

* `created` (value: `"created"`)
* `updated` (value: `"updated"`)
* `patched` (value: `"patched"`)
* `deleted` (value: `"deleted"`)
* `rolledBack` (value: `"rolled_back"`)
* `restored` (value: `"restored"`)

