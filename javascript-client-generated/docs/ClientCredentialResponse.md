# TmiThreatModelingImprovedApi.ClientCredentialResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique identifier for the credential | 
**clientId** | **String** | OAuth 2.0 client ID (format: tmi_cc_*) | 
**clientSecret** | **String** | OAuth 2.0 client secret - ONLY returned at creation time, cannot be retrieved later | 
**name** | **String** | Human-readable name for the credential | 
**description** | **String** | Optional description of the credential&#x27;s purpose | [optional] 
**createdAt** | **Date** | Creation timestamp (ISO 8601) | 
**expiresAt** | **Date** | Optional expiration timestamp (ISO 8601) | [optional] 
