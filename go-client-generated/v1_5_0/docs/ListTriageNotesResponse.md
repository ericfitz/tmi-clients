# ListTriageNotesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TriageNotes** | [**[]TriageNoteListItem**](TriageNoteListItem.md) |  | 
**Total** | **int32** | Total number of triage notes | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 

## Methods

### NewListTriageNotesResponse

`func NewListTriageNotesResponse(triageNotes []TriageNoteListItem, total int32, limit int32, offset int32, ) *ListTriageNotesResponse`

NewListTriageNotesResponse instantiates a new ListTriageNotesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListTriageNotesResponseWithDefaults

`func NewListTriageNotesResponseWithDefaults() *ListTriageNotesResponse`

NewListTriageNotesResponseWithDefaults instantiates a new ListTriageNotesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTriageNotes

`func (o *ListTriageNotesResponse) GetTriageNotes() []TriageNoteListItem`

GetTriageNotes returns the TriageNotes field if non-nil, zero value otherwise.

### GetTriageNotesOk

`func (o *ListTriageNotesResponse) GetTriageNotesOk() (*[]TriageNoteListItem, bool)`

GetTriageNotesOk returns a tuple with the TriageNotes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTriageNotes

`func (o *ListTriageNotesResponse) SetTriageNotes(v []TriageNoteListItem)`

SetTriageNotes sets TriageNotes field to given value.


### GetTotal

`func (o *ListTriageNotesResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListTriageNotesResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListTriageNotesResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListTriageNotesResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListTriageNotesResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListTriageNotesResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListTriageNotesResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListTriageNotesResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListTriageNotesResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


