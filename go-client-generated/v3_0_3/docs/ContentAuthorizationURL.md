# ContentAuthorizationURL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthorizationUrl** | **string** | Provider authorization URL to which the client must navigate the user. | 
**ExpiresAt** | **time.Time** | Timestamp after which the associated server-side state nonce is no longer valid (ISO 8601). | 

## Methods

### NewContentAuthorizationURL

`func NewContentAuthorizationURL(authorizationUrl string, expiresAt time.Time, ) *ContentAuthorizationURL`

NewContentAuthorizationURL instantiates a new ContentAuthorizationURL object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewContentAuthorizationURLWithDefaults

`func NewContentAuthorizationURLWithDefaults() *ContentAuthorizationURL`

NewContentAuthorizationURLWithDefaults instantiates a new ContentAuthorizationURL object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthorizationUrl

`func (o *ContentAuthorizationURL) GetAuthorizationUrl() string`

GetAuthorizationUrl returns the AuthorizationUrl field if non-nil, zero value otherwise.

### GetAuthorizationUrlOk

`func (o *ContentAuthorizationURL) GetAuthorizationUrlOk() (*string, bool)`

GetAuthorizationUrlOk returns a tuple with the AuthorizationUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationUrl

`func (o *ContentAuthorizationURL) SetAuthorizationUrl(v string)`

SetAuthorizationUrl sets AuthorizationUrl field to given value.


### GetExpiresAt

`func (o *ContentAuthorizationURL) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *ContentAuthorizationURL) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *ContentAuthorizationURL) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


