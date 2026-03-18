# TmiJsClient.ApiInfoStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Status code indicating system health: OK (all components healthy), DEGRADED (server up but database or Redis unhealthy), ERROR (critical failure) | 
**time** | **Date** | Current server time in UTC, formatted as RFC 3339 | 

<a name="CodeEnum"></a>
## Enum: CodeEnum

* `OK` (value: `"OK"`)
* `DEGRADED` (value: `"DEGRADED"`)
* `ERROR` (value: `"ERROR"`)

