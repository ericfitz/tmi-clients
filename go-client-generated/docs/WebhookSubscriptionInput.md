# WebhookSubscriptionInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ThreatModelId** | **string** | Optional threat model filter | [optional] [default to null]
**Name** | **string** | Descriptive name for the subscription | [default to null]
**Url** | **string** | Webhook endpoint URL (must be HTTPS) | [default to null]
**Events** | **[]string** | List of event types to subscribe to | [default to null]
**Secret** | **string** | Optional HMAC secret for signing payloads (auto-generated if not provided) | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

