# DeletionChallenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ChallengeText** | **string** | The exact challenge string that must be provided to confirm deletion | 
**ExpiresAt** | **time.Time** | When the challenge expires (3 minutes from issuance) | 

## Methods

### NewDeletionChallenge

`func NewDeletionChallenge(challengeText string, expiresAt time.Time, ) *DeletionChallenge`

NewDeletionChallenge instantiates a new DeletionChallenge object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDeletionChallengeWithDefaults

`func NewDeletionChallengeWithDefaults() *DeletionChallenge`

NewDeletionChallengeWithDefaults instantiates a new DeletionChallenge object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetChallengeText

`func (o *DeletionChallenge) GetChallengeText() string`

GetChallengeText returns the ChallengeText field if non-nil, zero value otherwise.

### GetChallengeTextOk

`func (o *DeletionChallenge) GetChallengeTextOk() (*string, bool)`

GetChallengeTextOk returns a tuple with the ChallengeText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChallengeText

`func (o *DeletionChallenge) SetChallengeText(v string)`

SetChallengeText sets ChallengeText field to given value.


### GetExpiresAt

`func (o *DeletionChallenge) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *DeletionChallenge) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *DeletionChallenge) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


