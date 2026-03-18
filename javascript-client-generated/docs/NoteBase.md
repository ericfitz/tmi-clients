# TmiJsClient.NoteBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Note name | 
**content** | **String** | Note content in markdown format. Safe inline HTML (tables, SVG, formatting) is allowed and sanitized server-side; dangerous elements (script, iframe, event handlers) are stripped. | 
**description** | **String** | Description of note purpose or context | [optional] 
**includeInReport** | **Boolean** | Whether this item should be included in generated reports | [optional] [default to true]
