# SurveyBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the survey | 
**description** | **str** | Description of the survey and its purpose | [optional] 
**version** | **str** | Custom version string (e.g., &#x27;2024-Q1&#x27;, &#x27;v2-pilot&#x27;) | 
**status** | **str** | Survey status: active surveys appear in intake, inactive are hidden but editable, archived are read-only and preserved for historical reference | [optional] 
**settings** | [**SurveySettings**](SurveySettings.md) |  | [optional] 
**survey_json** | **dict(str, object)** | Complete SurveyJS JSON definition. Opaque to the server; validated only for top-level structure (must contain a pages array). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

