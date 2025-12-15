# ClientCredentialResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the credential | [default to null]
**ClientId** | **string** | OAuth 2.0 client ID (format: tmi_cc_*) | [default to null]
**ClientSecret** | **string** | OAuth 2.0 client secret - ONLY returned at creation time, cannot be retrieved later | [default to null]
**Name** | **string** | Human-readable name for the credential | [default to null]
**Description** | **string** | Optional description of the credential&#x27;s purpose | [optional] [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Creation timestamp (ISO 8601) | [default to null]
**ExpiresAt** | [**time.Time**](time.Time.md) | Optional expiration timestamp (ISO 8601) | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

