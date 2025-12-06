# AdminUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_uuid** | **str** | Internal system UUID for the user | 
**provider** | **str** | OAuth/SAML provider identifier | 
**provider_user_id** | **str** | Provider-assigned user identifier | 
**email** | **str** | User email address | 
**name** | **str** | User display name | 
**email_verified** | **bool** | Whether the email has been verified | 
**created_at** | **datetime** | Account creation timestamp | 
**modified_at** | **datetime** | Last modification timestamp | 
**last_login** | **datetime** | Last login timestamp | [optional] 
**is_admin** | **bool** | Whether the user has administrator privileges (enriched) | [optional] 
**groups** | **list[str]** | List of group names the user belongs to (enriched) | [optional] 
**active_threat_models** | **int** | Number of active threat models owned by user (enriched) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

