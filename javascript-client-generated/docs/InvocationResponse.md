# TmiJsClient.InvocationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Invocation identifier | 
**addonId** | **String** | Add-on that was invoked | 
**threatModelId** | **String** | Threat model context | 
**objectType** | **String** | Object type (if specified) | [optional] 
**objectId** | **String** | Object ID (if specified) | [optional] 
**invokedBy** | **AllOfInvocationResponseInvokedBy** | User who triggered the invocation | 
**payload** | **String** | JSON-encoded payload | [optional] 
**status** | **String** | Current status | 
**statusPercent** | **Number** | Progress percentage (0-100) | 
**statusMessage** | **String** | Optional status description | [optional] 
**createdAt** | **Date** | Creation timestamp | 
**statusUpdatedAt** | **Date** | Last status update timestamp | 

<a name="StatusEnum"></a>
## Enum: StatusEnum

* `pending` (value: `"pending"`)
* `inProgress` (value: `"in_progress"`)
* `completed` (value: `"completed"`)
* `failed` (value: `"failed"`)

