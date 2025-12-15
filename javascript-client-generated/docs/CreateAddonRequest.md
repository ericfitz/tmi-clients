# TmiThreatModelingImprovedApi.CreateAddonRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Display name for the add-on | 
**webhookId** | **String** | UUID of the associated webhook subscription | 
**description** | **String** | Description of what the add-on does | [optional] 
**icon** | **String** | Icon identifier (Material Symbols or FontAwesome format) | [optional] 
**objects** | **[String]** | TMI object types this add-on can operate on | [optional] 
**threatModelId** | **String** | Optional: Scope add-on to specific threat model | [optional] 

<a name="[ObjectsEnum]"></a>
## Enum: [ObjectsEnum]

* `threatModel` (value: `"threat_model"`)
* `diagram` (value: `"diagram"`)
* `asset` (value: `"asset"`)
* `threat` (value: `"threat"`)
* `document` (value: `"document"`)
* `note` (value: `"note"`)
* `repository` (value: `"repository"`)
* `metadata` (value: `"metadata"`)

