# TmiThreatModelingImprovedApi.UpdateInvocationStatusRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **String** | New status (cannot transition back to pending) | 
**statusPercent** | **Number** | Progress percentage | [optional] 
**statusMessage** | **String** | Optional status description | [optional] 

<a name="StatusEnum"></a>
## Enum: StatusEnum

* `inProgress` (value: `"in_progress"`)
* `completed` (value: `"completed"`)
* `failed` (value: `"failed"`)

