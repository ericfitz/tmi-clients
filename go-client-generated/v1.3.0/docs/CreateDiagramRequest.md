# CreateDiagramRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the diagram | 
**Type** | **string** | Type of diagram with version | 

## Methods

### NewCreateDiagramRequest

`func NewCreateDiagramRequest(name string, type_ string, ) *CreateDiagramRequest`

NewCreateDiagramRequest instantiates a new CreateDiagramRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateDiagramRequestWithDefaults

`func NewCreateDiagramRequestWithDefaults() *CreateDiagramRequest`

NewCreateDiagramRequestWithDefaults instantiates a new CreateDiagramRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateDiagramRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateDiagramRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateDiagramRequest) SetName(v string)`

SetName sets Name field to given value.


### GetType

`func (o *CreateDiagramRequest) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *CreateDiagramRequest) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *CreateDiagramRequest) SetType(v string)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


