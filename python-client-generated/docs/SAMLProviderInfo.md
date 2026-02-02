# SAMLProviderInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Provider identifier | 
**name** | **str** | Display name of the provider | 
**icon** | **str** | Icon identifier for the provider (Font Awesome class, URL, or path) | 
**auth_url** | **str** | TMI SAML login endpoint URL | 
**metadata_url** | **str** | SAML service provider metadata URL | 
**entity_id** | **str** | Service Provider entity ID | 
**acs_url** | **str** | Assertion Consumer Service URL | 
**slo_url** | **str** | Single Logout URL | [optional] 
**initialized** | **bool** | Whether the SAML provider was successfully initialized and is available for authentication | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

