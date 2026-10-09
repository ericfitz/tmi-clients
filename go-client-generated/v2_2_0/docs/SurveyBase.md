# SurveyBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the survey | 
**Description** | Pointer to **NullableString** | Description of the survey and its purpose | [optional] 
**Version** | **string** | Custom version string (e.g., &#39;2024-Q1&#39;, &#39;v2-pilot&#39;) | 
**Status** | Pointer to **NullableString** | Survey status: active surveys appear in intake, inactive are hidden but editable, archived are read-only and preserved for historical reference | [optional] 
**Settings** | Pointer to [**SurveySettings**](SurveySettings.md) |  | [optional] 
**SurveyJson** | **map[string]interface{}** | Complete SurveyJS JSON definition. Opaque to the server; validated only for top-level structure (must contain a pages array). | 

## Methods

### NewSurveyBase

`func NewSurveyBase(name string, version string, surveyJson map[string]interface{}, ) *SurveyBase`

NewSurveyBase instantiates a new SurveyBase object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSurveyBaseWithDefaults

`func NewSurveyBaseWithDefaults() *SurveyBase`

NewSurveyBaseWithDefaults instantiates a new SurveyBase object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *SurveyBase) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SurveyBase) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SurveyBase) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *SurveyBase) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SurveyBase) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SurveyBase) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *SurveyBase) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *SurveyBase) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *SurveyBase) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetVersion

`func (o *SurveyBase) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *SurveyBase) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *SurveyBase) SetVersion(v string)`

SetVersion sets Version field to given value.


### GetStatus

`func (o *SurveyBase) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SurveyBase) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SurveyBase) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *SurveyBase) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatusNil

`func (o *SurveyBase) SetStatusNil(b bool)`

 SetStatusNil sets the value for Status to be an explicit nil

### UnsetStatus
`func (o *SurveyBase) UnsetStatus()`

UnsetStatus ensures that no value is present for Status, not even an explicit nil
### GetSettings

`func (o *SurveyBase) GetSettings() SurveySettings`

GetSettings returns the Settings field if non-nil, zero value otherwise.

### GetSettingsOk

`func (o *SurveyBase) GetSettingsOk() (*SurveySettings, bool)`

GetSettingsOk returns a tuple with the Settings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSettings

`func (o *SurveyBase) SetSettings(v SurveySettings)`

SetSettings sets Settings field to given value.

### HasSettings

`func (o *SurveyBase) HasSettings() bool`

HasSettings returns a boolean if a field has been set.

### GetSurveyJson

`func (o *SurveyBase) GetSurveyJson() map[string]interface{}`

GetSurveyJson returns the SurveyJson field if non-nil, zero value otherwise.

### GetSurveyJsonOk

`func (o *SurveyBase) GetSurveyJsonOk() (*map[string]interface{}, bool)`

GetSurveyJsonOk returns a tuple with the SurveyJson field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurveyJson

`func (o *SurveyBase) SetSurveyJson(v map[string]interface{})`

SetSurveyJson sets SurveyJson field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


