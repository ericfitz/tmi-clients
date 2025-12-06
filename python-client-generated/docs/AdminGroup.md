# AdminGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_uuid** | **str** | Internal system UUID for the group | 
**provider** | **str** | OAuth/SAML provider identifier, or \&quot;*\&quot; for provider-independent groups | 
**group_name** | **str** | Provider-assigned group name | 
**name** | **str** | Human-readable group name | [optional] 
**description** | **str** | Group description | [optional] 
**first_used** | **datetime** | First time this group was referenced | 
**last_used** | **datetime** | Last time this group was referenced | 
**usage_count** | **int** | Number of times this group has been referenced | 
**used_in_authorizations** | **bool** | Whether this group is used in any authorizations (enriched) | [optional] 
**used_in_admin_grants** | **bool** | Whether this group is used in any admin grants (enriched) | [optional] 
**member_count** | **int** | Number of members in the group from IdP (enriched, if available) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

