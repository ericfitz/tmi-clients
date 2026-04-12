# MigrateSystemSettings200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Migrated** | **int32** | Number of settings migrated (created or updated) | 
**Skipped** | **int32** | Number of settings skipped (already exist and overwrite&#x3D;false) | 
**Settings** | [**[]SystemSetting**](SystemSetting.md) | List of settings that were migrated | 

## Methods

### NewMigrateSystemSettings200Response

`func NewMigrateSystemSettings200Response(migrated int32, skipped int32, settings []SystemSetting, ) *MigrateSystemSettings200Response`

NewMigrateSystemSettings200Response instantiates a new MigrateSystemSettings200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMigrateSystemSettings200ResponseWithDefaults

`func NewMigrateSystemSettings200ResponseWithDefaults() *MigrateSystemSettings200Response`

NewMigrateSystemSettings200ResponseWithDefaults instantiates a new MigrateSystemSettings200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMigrated

`func (o *MigrateSystemSettings200Response) GetMigrated() int32`

GetMigrated returns the Migrated field if non-nil, zero value otherwise.

### GetMigratedOk

`func (o *MigrateSystemSettings200Response) GetMigratedOk() (*int32, bool)`

GetMigratedOk returns a tuple with the Migrated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMigrated

`func (o *MigrateSystemSettings200Response) SetMigrated(v int32)`

SetMigrated sets Migrated field to given value.


### GetSkipped

`func (o *MigrateSystemSettings200Response) GetSkipped() int32`

GetSkipped returns the Skipped field if non-nil, zero value otherwise.

### GetSkippedOk

`func (o *MigrateSystemSettings200Response) GetSkippedOk() (*int32, bool)`

GetSkippedOk returns a tuple with the Skipped field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSkipped

`func (o *MigrateSystemSettings200Response) SetSkipped(v int32)`

SetSkipped sets Skipped field to given value.


### GetSettings

`func (o *MigrateSystemSettings200Response) GetSettings() []SystemSetting`

GetSettings returns the Settings field if non-nil, zero value otherwise.

### GetSettingsOk

`func (o *MigrateSystemSettings200Response) GetSettingsOk() (*[]SystemSetting, bool)`

GetSettingsOk returns a tuple with the Settings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSettings

`func (o *MigrateSystemSettings200Response) SetSettings(v []SystemSetting)`

SetSettings sets Settings field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


