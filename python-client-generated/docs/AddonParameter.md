# AddonParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Parameter name (used as key in invocation data payload) | 
**type** | **str** | Parameter type determining client UI control | 
**description** | **str** | Human-readable description for UI display | [optional] 
**required** | **bool** | Whether the parameter must be provided on invocation | [optional] [default to False]
**enum_values** | **list[str]** | Allowed values (applicable when type is &#x27;enum&#x27;) | [optional] 
**default_value** | **str** | Default value if not provided by user | [optional] 
**metadata_key** | **str** | Metadata key name to auto-populate from TMI object (applicable when type is &#x27;metadata_key&#x27;) | [optional] 
**number_min** | **float** | Minimum allowed value (applicable when type is &#x27;number&#x27;) | [optional] 
**number_max** | **float** | Maximum allowed value (applicable when type is &#x27;number&#x27;) | [optional] 
**string_max_length** | **int** | Maximum string length (applicable when type is &#x27;string&#x27;) | [optional] 
**string_validation_regex** | **str** | Regular expression for string validation (applicable when type is &#x27;string&#x27;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

