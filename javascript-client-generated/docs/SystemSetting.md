# TmiJsClient.SystemSetting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | Unique setting identifier using dot notation (e.g., rate_limit.requests_per_minute) | 
**value** | **String** | Setting value as a string (interpreted based on type) | 
**type** | **String** | Data type of the setting value | 
**description** | **String** | Human-readable description of the setting | [optional] 
**modifiedAt** | **Date** | When the setting was last modified | [optional] 
**modifiedBy** | **String** | UUID of the user who last modified the setting | [optional] 

<a name="TypeEnum"></a>
## Enum: TypeEnum

* `_string` (value: `"string"`)
* `_int` (value: `"int"`)
* `bool` (value: `"bool"`)
* `json` (value: `"json"`)

