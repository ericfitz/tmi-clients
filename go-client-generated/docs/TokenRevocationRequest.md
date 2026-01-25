# TokenRevocationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Token** | **string** | The token to be revoked (access token or refresh token) | [default to null]
**TokenTypeHint** | **string** | A hint about the type of the token. If omitted, the server will attempt to determine the token type. | [optional] [default to null]
**ClientId** | **string** | Client identifier for client credentials authentication (alternative to Bearer token) | [optional] [default to null]
**ClientSecret** | **string** | Client secret (required if client_id is provided) | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

