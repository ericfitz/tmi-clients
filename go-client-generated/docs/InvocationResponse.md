# InvocationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Invocation identifier | [default to null]
**AddonId** | **string** | Add-on that was invoked | [default to null]
**ThreatModelId** | **string** | Threat model context | [default to null]
**ObjectType** | **string** | Object type (if specified) | [optional] [default to null]
**ObjectId** | **string** | Object ID (if specified) | [optional] [default to null]
**InvokedBy** | [***AllOfInvocationResponseInvokedBy**](AllOfInvocationResponseInvokedBy.md) | User who triggered the invocation | [default to null]
**Payload** | **string** | JSON-encoded payload | [optional] [default to null]
**Status** | **string** | Current status | [default to null]
**StatusPercent** | **int32** | Progress percentage (0-100) | [default to null]
**StatusMessage** | **string** | Optional status description | [optional] [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Creation timestamp | [default to null]
**StatusUpdatedAt** | [**time.Time**](time.Time.md) | Last status update timestamp | [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

