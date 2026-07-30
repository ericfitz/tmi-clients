# ListSurveyResponsesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SurveyResponses** | [**[]SurveyResponseListItem**](SurveyResponseListItem.md) |  | 
**Total** | **int32** | Total number of responses matching criteria | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 

## Methods

### NewListSurveyResponsesResponse

`func NewListSurveyResponsesResponse(surveyResponses []SurveyResponseListItem, total int32, limit int32, offset int32, ) *ListSurveyResponsesResponse`

NewListSurveyResponsesResponse instantiates a new ListSurveyResponsesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListSurveyResponsesResponseWithDefaults

`func NewListSurveyResponsesResponseWithDefaults() *ListSurveyResponsesResponse`

NewListSurveyResponsesResponseWithDefaults instantiates a new ListSurveyResponsesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSurveyResponses

`func (o *ListSurveyResponsesResponse) GetSurveyResponses() []SurveyResponseListItem`

GetSurveyResponses returns the SurveyResponses field if non-nil, zero value otherwise.

### GetSurveyResponsesOk

`func (o *ListSurveyResponsesResponse) GetSurveyResponsesOk() (*[]SurveyResponseListItem, bool)`

GetSurveyResponsesOk returns a tuple with the SurveyResponses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurveyResponses

`func (o *ListSurveyResponsesResponse) SetSurveyResponses(v []SurveyResponseListItem)`

SetSurveyResponses sets SurveyResponses field to given value.


### GetTotal

`func (o *ListSurveyResponsesResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListSurveyResponsesResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListSurveyResponsesResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListSurveyResponsesResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListSurveyResponsesResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListSurveyResponsesResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListSurveyResponsesResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListSurveyResponsesResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListSurveyResponsesResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


