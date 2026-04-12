# ListThreatsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Threats** | [**[]Threat**](Threat.md) |  | 
**Total** | **int32** | Total number of threats matching criteria | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 

## Methods

### NewListThreatsResponse

`func NewListThreatsResponse(threats []Threat, total int32, limit int32, offset int32, ) *ListThreatsResponse`

NewListThreatsResponse instantiates a new ListThreatsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListThreatsResponseWithDefaults

`func NewListThreatsResponseWithDefaults() *ListThreatsResponse`

NewListThreatsResponseWithDefaults instantiates a new ListThreatsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetThreats

`func (o *ListThreatsResponse) GetThreats() []Threat`

GetThreats returns the Threats field if non-nil, zero value otherwise.

### GetThreatsOk

`func (o *ListThreatsResponse) GetThreatsOk() (*[]Threat, bool)`

GetThreatsOk returns a tuple with the Threats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreats

`func (o *ListThreatsResponse) SetThreats(v []Threat)`

SetThreats sets Threats field to given value.


### GetTotal

`func (o *ListThreatsResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListThreatsResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListThreatsResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListThreatsResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListThreatsResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListThreatsResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListThreatsResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListThreatsResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListThreatsResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


