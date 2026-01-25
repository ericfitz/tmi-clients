# TmiJsClient.CellData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**[Metadata]**](Metadata.md) | Reserved namespace for structured business metadata | [optional] 
**securityBoundary** | **Boolean** | Indicates whether this cell represents a security boundary in the threat model | [optional] [default to false]
**dataAssets** | **[String]** | References to Asset IDs associated with this cell. Each UUID must reference an existing Asset in the same threat model. | [optional] 
