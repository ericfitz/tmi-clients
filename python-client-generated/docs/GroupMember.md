# GroupMember

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the membership record | 
**group_internal_uuid** | **str** | Internal UUID of the group | 
**user_internal_uuid** | **str** | Internal UUID of the user | [optional] 
**user_email** | **str** | Email address of the user | [optional] 
**user_name** | **str** | Display name of the user | [optional] 
**user_provider** | **str** | OAuth/SAML provider for the user | [optional] 
**user_provider_user_id** | **str** | Provider-specific user identifier | [optional] 
**added_by_internal_uuid** | **str** | Internal UUID of the administrator who added this member | [optional] 
**added_by_email** | **str** | Email of the administrator who added this member | [optional] 
**added_at** | **datetime** | Timestamp when the user was added to the group (RFC3339) | 
**notes** | **str** | Optional notes about this membership | [optional] 
**subject_type** | **str** | Type of member: user (direct user membership) or group (group-in-group membership) | [default to 'user']
**member_group_internal_uuid** | **str** | Internal UUID of the member group (when subject_type is group) | [optional] 
**member_group_name** | **str** | Display name of the member group (when subject_type is group) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

