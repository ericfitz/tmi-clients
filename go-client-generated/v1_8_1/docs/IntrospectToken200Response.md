# IntrospectToken200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Active** | **bool** | Whether the token is active/valid | 
**Sub** | Pointer to **string** | Subject (user identifier) | [optional] 
**Email** | Pointer to **string** | User email address | [optional] 
**Name** | Pointer to **string** | User&#39;s full name | [optional] 
**Exp** | Pointer to **int32** | Token expiration time (Unix timestamp) | [optional] 
**Iat** | Pointer to **int32** | Token issued at time (Unix timestamp) | [optional] 
**Iss** | Pointer to **string** | Token issuer | [optional] 
**TokenType** | Pointer to **string** | Type of the token (RFC 7662) | [optional] 
**Scope** | Pointer to **string** | Space-separated list of scopes (RFC 7662) | [optional] 

## Methods

### NewIntrospectToken200Response

`func NewIntrospectToken200Response(active bool, ) *IntrospectToken200Response`

NewIntrospectToken200Response instantiates a new IntrospectToken200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIntrospectToken200ResponseWithDefaults

`func NewIntrospectToken200ResponseWithDefaults() *IntrospectToken200Response`

NewIntrospectToken200ResponseWithDefaults instantiates a new IntrospectToken200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActive

`func (o *IntrospectToken200Response) GetActive() bool`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *IntrospectToken200Response) GetActiveOk() (*bool, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *IntrospectToken200Response) SetActive(v bool)`

SetActive sets Active field to given value.


### GetSub

`func (o *IntrospectToken200Response) GetSub() string`

GetSub returns the Sub field if non-nil, zero value otherwise.

### GetSubOk

`func (o *IntrospectToken200Response) GetSubOk() (*string, bool)`

GetSubOk returns a tuple with the Sub field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSub

`func (o *IntrospectToken200Response) SetSub(v string)`

SetSub sets Sub field to given value.

### HasSub

`func (o *IntrospectToken200Response) HasSub() bool`

HasSub returns a boolean if a field has been set.

### GetEmail

`func (o *IntrospectToken200Response) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *IntrospectToken200Response) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *IntrospectToken200Response) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *IntrospectToken200Response) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### GetName

`func (o *IntrospectToken200Response) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *IntrospectToken200Response) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *IntrospectToken200Response) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *IntrospectToken200Response) HasName() bool`

HasName returns a boolean if a field has been set.

### GetExp

`func (o *IntrospectToken200Response) GetExp() int32`

GetExp returns the Exp field if non-nil, zero value otherwise.

### GetExpOk

`func (o *IntrospectToken200Response) GetExpOk() (*int32, bool)`

GetExpOk returns a tuple with the Exp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExp

`func (o *IntrospectToken200Response) SetExp(v int32)`

SetExp sets Exp field to given value.

### HasExp

`func (o *IntrospectToken200Response) HasExp() bool`

HasExp returns a boolean if a field has been set.

### GetIat

`func (o *IntrospectToken200Response) GetIat() int32`

GetIat returns the Iat field if non-nil, zero value otherwise.

### GetIatOk

`func (o *IntrospectToken200Response) GetIatOk() (*int32, bool)`

GetIatOk returns a tuple with the Iat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIat

`func (o *IntrospectToken200Response) SetIat(v int32)`

SetIat sets Iat field to given value.

### HasIat

`func (o *IntrospectToken200Response) HasIat() bool`

HasIat returns a boolean if a field has been set.

### GetIss

`func (o *IntrospectToken200Response) GetIss() string`

GetIss returns the Iss field if non-nil, zero value otherwise.

### GetIssOk

`func (o *IntrospectToken200Response) GetIssOk() (*string, bool)`

GetIssOk returns a tuple with the Iss field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIss

`func (o *IntrospectToken200Response) SetIss(v string)`

SetIss sets Iss field to given value.

### HasIss

`func (o *IntrospectToken200Response) HasIss() bool`

HasIss returns a boolean if a field has been set.

### GetTokenType

`func (o *IntrospectToken200Response) GetTokenType() string`

GetTokenType returns the TokenType field if non-nil, zero value otherwise.

### GetTokenTypeOk

`func (o *IntrospectToken200Response) GetTokenTypeOk() (*string, bool)`

GetTokenTypeOk returns a tuple with the TokenType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokenType

`func (o *IntrospectToken200Response) SetTokenType(v string)`

SetTokenType sets TokenType field to given value.

### HasTokenType

`func (o *IntrospectToken200Response) HasTokenType() bool`

HasTokenType returns a boolean if a field has been set.

### GetScope

`func (o *IntrospectToken200Response) GetScope() string`

GetScope returns the Scope field if non-nil, zero value otherwise.

### GetScopeOk

`func (o *IntrospectToken200Response) GetScopeOk() (*string, bool)`

GetScopeOk returns a tuple with the Scope field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScope

`func (o *IntrospectToken200Response) SetScope(v string)`

SetScope sets Scope field to given value.

### HasScope

`func (o *IntrospectToken200Response) HasScope() bool`

HasScope returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


