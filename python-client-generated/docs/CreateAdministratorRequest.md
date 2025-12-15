# CreateAdministratorRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email to grant admin privileges (mutually exclusive with provider_user_id and group_name) | [optional] 
**provider_user_id** | **str** | Provider&#x27;s user ID to grant admin privileges (mutually exclusive with email and group_name) | [optional] 
**group_name** | **str** | Group name to grant admin privileges (mutually exclusive with email and provider_user_id) | [optional] 
**provider** | **str** | OAuth/SAML provider | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

