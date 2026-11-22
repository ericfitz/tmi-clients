# EdgeRouterOneOfArgs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Padding** | Pointer to **float32** | Padding around obstacles for routing | [optional] 
**Step** | Pointer to **float32** | Grid step size for orthogonal routing | [optional] 
**Directions** | Pointer to **[]string** | Allowed routing directions | [optional] 

## Methods

### NewEdgeRouterOneOfArgs

`func NewEdgeRouterOneOfArgs() *EdgeRouterOneOfArgs`

NewEdgeRouterOneOfArgs instantiates a new EdgeRouterOneOfArgs object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEdgeRouterOneOfArgsWithDefaults

`func NewEdgeRouterOneOfArgsWithDefaults() *EdgeRouterOneOfArgs`

NewEdgeRouterOneOfArgsWithDefaults instantiates a new EdgeRouterOneOfArgs object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPadding

`func (o *EdgeRouterOneOfArgs) GetPadding() float32`

GetPadding returns the Padding field if non-nil, zero value otherwise.

### GetPaddingOk

`func (o *EdgeRouterOneOfArgs) GetPaddingOk() (*float32, bool)`

GetPaddingOk returns a tuple with the Padding field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPadding

`func (o *EdgeRouterOneOfArgs) SetPadding(v float32)`

SetPadding sets Padding field to given value.

### HasPadding

`func (o *EdgeRouterOneOfArgs) HasPadding() bool`

HasPadding returns a boolean if a field has been set.

### GetStep

`func (o *EdgeRouterOneOfArgs) GetStep() float32`

GetStep returns the Step field if non-nil, zero value otherwise.

### GetStepOk

`func (o *EdgeRouterOneOfArgs) GetStepOk() (*float32, bool)`

GetStepOk returns a tuple with the Step field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStep

`func (o *EdgeRouterOneOfArgs) SetStep(v float32)`

SetStep sets Step field to given value.

### HasStep

`func (o *EdgeRouterOneOfArgs) HasStep() bool`

HasStep returns a boolean if a field has been set.

### GetDirections

`func (o *EdgeRouterOneOfArgs) GetDirections() []string`

GetDirections returns the Directions field if non-nil, zero value otherwise.

### GetDirectionsOk

`func (o *EdgeRouterOneOfArgs) GetDirectionsOk() (*[]string, bool)`

GetDirectionsOk returns a tuple with the Directions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDirections

`func (o *EdgeRouterOneOfArgs) SetDirections(v []string)`

SetDirections sets Directions field to given value.

### HasDirections

`func (o *EdgeRouterOneOfArgs) HasDirections() bool`

HasDirections returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


