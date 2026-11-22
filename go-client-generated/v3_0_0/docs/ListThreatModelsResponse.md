# ListThreatModelsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ThreatModels** | [**[]TMListItem**](TMListItem.md) |  | 
**Total** | **int32** | Total number of threat models matching criteria | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 

## Methods

### NewListThreatModelsResponse

`func NewListThreatModelsResponse(threatModels []TMListItem, total int32, limit int32, offset int32, ) *ListThreatModelsResponse`

NewListThreatModelsResponse instantiates a new ListThreatModelsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListThreatModelsResponseWithDefaults

`func NewListThreatModelsResponseWithDefaults() *ListThreatModelsResponse`

NewListThreatModelsResponseWithDefaults instantiates a new ListThreatModelsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetThreatModels

`func (o *ListThreatModelsResponse) GetThreatModels() []TMListItem`

GetThreatModels returns the ThreatModels field if non-nil, zero value otherwise.

### GetThreatModelsOk

`func (o *ListThreatModelsResponse) GetThreatModelsOk() (*[]TMListItem, bool)`

GetThreatModelsOk returns a tuple with the ThreatModels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModels

`func (o *ListThreatModelsResponse) SetThreatModels(v []TMListItem)`

SetThreatModels sets ThreatModels field to given value.


### GetTotal

`func (o *ListThreatModelsResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListThreatModelsResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListThreatModelsResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListThreatModelsResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListThreatModelsResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListThreatModelsResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListThreatModelsResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListThreatModelsResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListThreatModelsResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


