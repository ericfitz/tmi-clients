# ProjectBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Project name | 
**description** | **str** | Project description | [optional] 
**team_id** | **str** | UUID of the team this project belongs to | 
**responsible_parties** | [**list[ResponsibleParty]**](ResponsibleParty.md) | Responsible parties for this project | [optional] 
**related_projects** | [**list[RelatedProject]**](RelatedProject.md) | Relationships to other projects | [optional] 
**uri** | **str** | URL or reference to internal project page | [optional] 
**status** | **AllOfProjectBaseStatus** | Project lifecycle status. Defaults to &#x27;active&#x27; if not provided or set to null. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

