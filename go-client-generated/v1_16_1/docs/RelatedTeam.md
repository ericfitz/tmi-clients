# RelatedTeam

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RelatedTeamId** | **string** | UUID of the related team | 
**Relationship** | [**RelationshipType**](RelationshipType.md) |  | 
**CustomRelationship** | Pointer to **string** | Custom relationship description when relationship is &#39;other&#39; | [optional] 

## Methods

### NewRelatedTeam

`func NewRelatedTeam(relatedTeamId string, relationship RelationshipType, ) *RelatedTeam`

NewRelatedTeam instantiates a new RelatedTeam object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRelatedTeamWithDefaults

`func NewRelatedTeamWithDefaults() *RelatedTeam`

NewRelatedTeamWithDefaults instantiates a new RelatedTeam object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRelatedTeamId

`func (o *RelatedTeam) GetRelatedTeamId() string`

GetRelatedTeamId returns the RelatedTeamId field if non-nil, zero value otherwise.

### GetRelatedTeamIdOk

`func (o *RelatedTeam) GetRelatedTeamIdOk() (*string, bool)`

GetRelatedTeamIdOk returns a tuple with the RelatedTeamId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelatedTeamId

`func (o *RelatedTeam) SetRelatedTeamId(v string)`

SetRelatedTeamId sets RelatedTeamId field to given value.


### GetRelationship

`func (o *RelatedTeam) GetRelationship() RelationshipType`

GetRelationship returns the Relationship field if non-nil, zero value otherwise.

### GetRelationshipOk

`func (o *RelatedTeam) GetRelationshipOk() (*RelationshipType, bool)`

GetRelationshipOk returns a tuple with the Relationship field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelationship

`func (o *RelatedTeam) SetRelationship(v RelationshipType)`

SetRelationship sets Relationship field to given value.


### GetCustomRelationship

`func (o *RelatedTeam) GetCustomRelationship() string`

GetCustomRelationship returns the CustomRelationship field if non-nil, zero value otherwise.

### GetCustomRelationshipOk

`func (o *RelatedTeam) GetCustomRelationshipOk() (*string, bool)`

GetCustomRelationshipOk returns a tuple with the CustomRelationship field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomRelationship

`func (o *RelatedTeam) SetCustomRelationship(v string)`

SetCustomRelationship sets CustomRelationship field to given value.

### HasCustomRelationship

`func (o *RelatedTeam) HasCustomRelationship() bool`

HasCustomRelationship returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


