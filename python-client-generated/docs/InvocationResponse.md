# InvocationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Invocation identifier | 
**addon_id** | **str** | Add-on that was invoked | 
**threat_model_id** | **str** | Threat model context | 
**object_type** | **str** | Object type (if specified) | [optional] 
**object_id** | **str** | Object ID (if specified) | [optional] 
**invoked_by** | **AllOfInvocationResponseInvokedBy** | User who triggered the invocation | 
**payload** | **str** | JSON-encoded payload | [optional] 
**status** | **str** | Current status | 
**status_percent** | **int** | Progress percentage (0-100) | 
**status_message** | **str** | Optional status description | [optional] 
**created_at** | **datetime** | Creation timestamp | 
**status_updated_at** | **datetime** | Last status update timestamp | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

