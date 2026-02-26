# TmiJsClient.SurveyBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Name of the survey | 
**description** | **String** | Description of the survey and its purpose | [optional] 
**version** | **String** | Custom version string (e.g., &#x27;2024-Q1&#x27;, &#x27;v2-pilot&#x27;) | 
**status** | **String** | Survey status: active surveys appear in intake, inactive are hidden but editable, archived are read-only and preserved for historical reference | [optional] 
**settings** | [**SurveySettings**](SurveySettings.md) |  | [optional] 
**surveyJson** | **{String: Object}** | Complete SurveyJS JSON definition. Opaque to the server; validated only for top-level structure (must contain a pages array). | 
