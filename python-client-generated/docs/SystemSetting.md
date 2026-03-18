# SystemSetting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Unique setting identifier using dot notation (e.g., rate_limit.requests_per_minute) | 
**value** | **str** | Setting value as a string (interpreted based on type) | 
**type** | **str** | Data type of the setting value | 
**description** | **str** | Human-readable description of the setting | [optional] 
**modified_at** | **datetime** | When the setting was last modified | [optional] 
**modified_by** | **str** | UUID of the user who last modified the setting | [optional] 
**source** | **str** | Where the effective value of this setting comes from. Server-managed, not writable. | [optional] 
**read_only** | **bool** | Whether this setting can be modified via the API. True when source is not database. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

