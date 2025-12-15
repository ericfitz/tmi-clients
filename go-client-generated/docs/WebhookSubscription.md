# WebhookSubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier | [default to null]
**OwnerId** | **string** | Owner user ID | [default to null]
**ThreatModelId** | **string** | Optional threat model filter (null means all threat models) | [optional] [default to null]
**Name** | **string** | Descriptive name | [default to null]
**Url** | **string** | Webhook endpoint URL (must be HTTPS) | [default to null]
**Events** | [**[]WebhookEventType**](WebhookEventType.md) | List of event types to subscribe to. See WebhookEventType for available events. | [default to null]
**Secret** | **string** | HMAC secret for signing payloads (not returned in GET responses) | [optional] [default to null]
**Status** | **string** | Subscription status | [default to null]
**ChallengesSent** | **int32** | Number of verification challenges sent | [optional] [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Creation timestamp | [default to null]
**ModifiedAt** | [**time.Time**](time.Time.md) | Last modification timestamp | [default to null]
**LastSuccessfulUse** | [**time.Time**](time.Time.md) | Last successful delivery timestamp | [optional] [default to null]
**PublicationFailures** | **int32** | Count of consecutive failed deliveries | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

