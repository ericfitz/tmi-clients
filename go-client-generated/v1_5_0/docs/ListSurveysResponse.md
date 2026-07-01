# ListSurveysResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Total** | **int32** | Total number of surveys matching criteria | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 
**Surveys** | [**[]SurveyListItem**](SurveyListItem.md) |  | 

## Methods

### NewListSurveysResponse

`func NewListSurveysResponse(total int32, limit int32, offset int32, surveys []SurveyListItem, ) *ListSurveysResponse`

NewListSurveysResponse instantiates a new ListSurveysResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListSurveysResponseWithDefaults

`func NewListSurveysResponseWithDefaults() *ListSurveysResponse`

NewListSurveysResponseWithDefaults instantiates a new ListSurveysResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTotal

`func (o *ListSurveysResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListSurveysResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListSurveysResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListSurveysResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListSurveysResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListSurveysResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListSurveysResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListSurveysResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListSurveysResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.


### GetSurveys

`func (o *ListSurveysResponse) GetSurveys() []SurveyListItem`

GetSurveys returns the Surveys field if non-nil, zero value otherwise.

### GetSurveysOk

`func (o *ListSurveysResponse) GetSurveysOk() (*[]SurveyListItem, bool)`

GetSurveysOk returns a tuple with the Surveys field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurveys

`func (o *ListSurveysResponse) SetSurveys(v []SurveyListItem)`

SetSurveys sets Surveys field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


