# AddonParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Parameter name (used as key in invocation data payload) | [default to null]
**Type_** | **string** | Parameter type determining client UI control | [default to null]
**Description** | **string** | Human-readable description for UI display | [optional] [default to null]
**Required** | **bool** | Whether the parameter must be provided on invocation | [optional] [default to false]
**EnumValues** | **[]string** | Allowed values (applicable when type is &#x27;enum&#x27;) | [optional] [default to null]
**DefaultValue** | **string** | Default value if not provided by user | [optional] [default to null]
**MetadataKey** | **string** | Metadata key name to auto-populate from TMI object (applicable when type is &#x27;metadata_key&#x27;) | [optional] [default to null]
**NumberMin** | **float64** | Minimum allowed value (applicable when type is &#x27;number&#x27;) | [optional] [default to null]
**NumberMax** | **float64** | Maximum allowed value (applicable when type is &#x27;number&#x27;) | [optional] [default to null]
**StringMaxLength** | **int32** | Maximum string length (applicable when type is &#x27;string&#x27;) | [optional] [default to null]
**StringValidationRegex** | **string** | Regular expression for string validation (applicable when type is &#x27;string&#x27;) | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

