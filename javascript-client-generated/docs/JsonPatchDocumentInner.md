# TmiJsClient.JsonPatchDocumentInner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **String** | Patch operation type | 
**path** | **String** | JSON path to target | 
**value** | **OneOfJsonPatchDocumentInnerValue** | The value to use for add/replace/test operations. Can be any JSON value per RFC 6902 (string, number, boolean, object, array, or null). | [optional] 

<a name="OpEnum"></a>
## Enum: OpEnum

* `add` (value: `"add"`)
* `replace` (value: `"replace"`)
* `remove` (value: `"remove"`)
* `move` (value: `"move"`)
* `copy` (value: `"copy"`)
* `test` (value: `"test"`)

