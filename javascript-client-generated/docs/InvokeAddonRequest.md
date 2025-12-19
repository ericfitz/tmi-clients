# TmiJsClient.InvokeAddonRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threatModelId** | **String** | Threat model context for invocation | 
**objectType** | **String** | Optional: Specific object type to operate on | [optional] 
**objectId** | **String** | Optional: Specific object ID to operate on | [optional] 
**payload** | **{String: Object}** | User-provided data for the add-on (max 1KB JSON-serialized) | [optional] 

<a name="ObjectTypeEnum"></a>
## Enum: ObjectTypeEnum

* `threatModel` (value: `"threat_model"`)
* `diagram` (value: `"diagram"`)
* `asset` (value: `"asset"`)
* `threat` (value: `"threat"`)
* `document` (value: `"document"`)
* `note` (value: `"note"`)
* `repository` (value: `"repository"`)
* `metadata` (value: `"metadata"`)

