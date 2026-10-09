# ListProjectNotesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Notes** | [**[]ProjectNoteListItem**](ProjectNoteListItem.md) |  | 
**Total** | **int32** | Total number of project notes matching criteria | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 

## Methods

### NewListProjectNotesResponse

`func NewListProjectNotesResponse(notes []ProjectNoteListItem, total int32, limit int32, offset int32, ) *ListProjectNotesResponse`

NewListProjectNotesResponse instantiates a new ListProjectNotesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListProjectNotesResponseWithDefaults

`func NewListProjectNotesResponseWithDefaults() *ListProjectNotesResponse`

NewListProjectNotesResponseWithDefaults instantiates a new ListProjectNotesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetNotes

`func (o *ListProjectNotesResponse) GetNotes() []ProjectNoteListItem`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *ListProjectNotesResponse) GetNotesOk() (*[]ProjectNoteListItem, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *ListProjectNotesResponse) SetNotes(v []ProjectNoteListItem)`

SetNotes sets Notes field to given value.


### GetTotal

`func (o *ListProjectNotesResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListProjectNotesResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListProjectNotesResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListProjectNotesResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListProjectNotesResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListProjectNotesResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListProjectNotesResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListProjectNotesResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListProjectNotesResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


