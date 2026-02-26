# SurveyBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the survey | [default to null]
**Description** | **string** | Description of the survey and its purpose | [optional] [default to null]
**Version** | **string** | Custom version string (e.g., &#x27;2024-Q1&#x27;, &#x27;v2-pilot&#x27;) | [default to null]
**Status** | **string** | Survey status: active surveys appear in intake, inactive are hidden but editable, archived are read-only and preserved for historical reference | [optional] [default to null]
**Settings** | [***SurveySettings**](SurveySettings.md) |  | [optional] [default to null]
**SurveyJson** | [**ModelMap**](interface{}.md) | Complete SurveyJS JSON definition. Opaque to the server; validated only for top-level structure (must contain a pages array). | [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

