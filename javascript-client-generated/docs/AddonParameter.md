# TmiJsClient.AddonParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Parameter name (used as key in invocation data payload) | 
**type** | **String** | Parameter type determining client UI control | 
**description** | **String** | Human-readable description for UI display | [optional] 
**required** | **Boolean** | Whether the parameter must be provided on invocation | [optional] [default to false]
**enumValues** | **[String]** | Allowed values (applicable when type is &#x27;enum&#x27;) | [optional] 
**defaultValue** | **String** | Default value if not provided by user | [optional] 
**metadataKey** | **String** | Metadata key name to auto-populate from TMI object (applicable when type is &#x27;metadata_key&#x27;) | [optional] 
**numberMin** | **Number** | Minimum allowed value (applicable when type is &#x27;number&#x27;) | [optional] 
**numberMax** | **Number** | Maximum allowed value (applicable when type is &#x27;number&#x27;) | [optional] 
**stringMaxLength** | **Number** | Maximum string length (applicable when type is &#x27;string&#x27;) | [optional] 
**stringValidationRegex** | **String** | Regular expression for string validation (applicable when type is &#x27;string&#x27;) | [optional] 

<a name="TypeEnum"></a>
## Enum: TypeEnum

* `_enum` (value: `"enum"`)
* `_boolean` (value: `"boolean"`)
* `_string` (value: `"string"`)
* `_number` (value: `"number"`)
* `metadataKey` (value: `"metadata_key"`)

