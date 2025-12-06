# ClientCredentialResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the credential | 
**client_id** | **str** | OAuth 2.0 client ID (format: tmi_cc_*) | 
**client_secret** | **str** | OAuth 2.0 client secret - ONLY returned at creation time, cannot be retrieved later | 
**name** | **str** | Human-readable name for the credential | 
**description** | **str** | Optional description of the credential&#x27;s purpose | [optional] 
**created_at** | **datetime** | Creation timestamp (ISO 8601) | 
**expires_at** | **datetime** | Optional expiration timestamp (ISO 8601) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

