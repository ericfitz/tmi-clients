# TokenRevocationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The token to be revoked (access token or refresh token) | 
**token_type_hint** | **str** | A hint about the type of the token. If omitted, the server will attempt to determine the token type. | [optional] 
**client_id** | **str** | Client identifier for client credentials authentication (alternative to Bearer token) | [optional] 
**client_secret** | **str** | Client secret (required if client_id is provided) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

