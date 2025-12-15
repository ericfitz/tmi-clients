# TmiThreatModelingImprovedApi.WebhookSubscriptionInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threatModelId** | **String** | Optional threat model filter | [optional] 
**name** | **String** | Descriptive name for the subscription | 
**url** | **String** | Webhook endpoint URL (must be HTTPS) | 
**events** | **[String]** | List of event types to subscribe to | 
**secret** | **String** | Optional HMAC secret for signing payloads (auto-generated if not provided) | [optional] 
