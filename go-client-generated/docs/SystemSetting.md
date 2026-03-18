# SystemSetting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Key** | **string** | Unique setting identifier using dot notation (e.g., rate_limit.requests_per_minute) | [default to null]
**Value** | **string** | Setting value as a string (interpreted based on type) | [default to null]
**Type_** | **string** | Data type of the setting value | [default to null]
**Description** | **string** | Human-readable description of the setting | [optional] [default to null]
**ModifiedAt** | [**time.Time**](time.Time.md) | When the setting was last modified | [optional] [default to null]
**ModifiedBy** | **string** | UUID of the user who last modified the setting | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

