# AddGroupMemberRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_internal_uuid** | **str** | Internal UUID of the user to add to the group | [optional] 
**notes** | **str** | Optional notes about this membership | [optional] 
**subject_type** | **str** | Type of member to add: user or group | [optional] [default to 'user']
**member_group_internal_uuid** | **str** | Internal UUID of the group to add as a member (required when subject_type is group) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

