# TmiThreatModelingImprovedApi.WebhookSubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique identifier | 
**ownerId** | **String** | Owner user ID | 
**threatModelId** | **String** | Optional threat model filter (null means all threat models) | [optional] 
**name** | **String** | Descriptive name | 
**url** | **String** | Webhook endpoint URL (must be HTTPS) | 
**events** | [**[WebhookEventType]**](WebhookEventType.md) | List of event types to subscribe to. See WebhookEventType for available events. | 
**secret** | **String** | HMAC secret for signing payloads (not returned in GET responses) | [optional] 
**status** | **String** | Subscription status | 
**challengesSent** | **Number** | Number of verification challenges sent | [optional] 
**createdAt** | **Date** | Creation timestamp | 
**modifiedAt** | **Date** | Last modification timestamp | 
**lastSuccessfulUse** | **Date** | Last successful delivery timestamp | [optional] 
**publicationFailures** | **Number** | Count of consecutive failed deliveries | [optional] 

<a name="StatusEnum"></a>
## Enum: StatusEnum

* `pendingVerification` (value: `"pending_verification"`)
* `active` (value: `"active"`)
* `pendingDelete` (value: `"pending_delete"`)

