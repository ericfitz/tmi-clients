# ApiInfoStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** | Status code indicating system health: OK (all components healthy), DEGRADED (server up but database or Redis unhealthy), ERROR (critical failure) | [default to null]
**Time** | [**time.Time**](time.Time.md) | Current server time in UTC, formatted as RFC 3339 | [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

