# EdgeRouter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Router algorithm name | 
**Args** | Pointer to [**EdgeRouterOneOfArgs**](EdgeRouterOneOfArgs.md) |  | [optional] 

## Methods

### NewEdgeRouter

`func NewEdgeRouter(name string, ) *EdgeRouter`

NewEdgeRouter instantiates a new EdgeRouter object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEdgeRouterWithDefaults

`func NewEdgeRouterWithDefaults() *EdgeRouter`

NewEdgeRouterWithDefaults instantiates a new EdgeRouter object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *EdgeRouter) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *EdgeRouter) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *EdgeRouter) SetName(v string)`

SetName sets Name field to given value.


### GetArgs

`func (o *EdgeRouter) GetArgs() EdgeRouterOneOfArgs`

GetArgs returns the Args field if non-nil, zero value otherwise.

### GetArgsOk

`func (o *EdgeRouter) GetArgsOk() (*EdgeRouterOneOfArgs, bool)`

GetArgsOk returns a tuple with the Args field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArgs

`func (o *EdgeRouter) SetArgs(v EdgeRouterOneOfArgs)`

SetArgs sets Args field to given value.

### HasArgs

`func (o *EdgeRouter) HasArgs() bool`

HasArgs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


