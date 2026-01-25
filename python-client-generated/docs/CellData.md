# CellData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**list[Metadata]**](Metadata.md) | Reserved namespace for structured business metadata | [optional] 
**security_boundary** | **bool** | Indicates whether this cell represents a security boundary in the threat model | [optional] [default to False]
**data_assets** | **list[str]** | References to Asset IDs associated with this cell. Each UUID must reference an existing Asset in the same threat model. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

