# RelatedProject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RelatedProjectId** | **string** | UUID of the related project | 
**Relationship** | [**RelationshipType**](RelationshipType.md) |  | 
**CustomRelationship** | Pointer to **string** | Custom relationship description when relationship is &#39;other&#39; | [optional] 

## Methods

### NewRelatedProject

`func NewRelatedProject(relatedProjectId string, relationship RelationshipType, ) *RelatedProject`

NewRelatedProject instantiates a new RelatedProject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRelatedProjectWithDefaults

`func NewRelatedProjectWithDefaults() *RelatedProject`

NewRelatedProjectWithDefaults instantiates a new RelatedProject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRelatedProjectId

`func (o *RelatedProject) GetRelatedProjectId() string`

GetRelatedProjectId returns the RelatedProjectId field if non-nil, zero value otherwise.

### GetRelatedProjectIdOk

`func (o *RelatedProject) GetRelatedProjectIdOk() (*string, bool)`

GetRelatedProjectIdOk returns a tuple with the RelatedProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelatedProjectId

`func (o *RelatedProject) SetRelatedProjectId(v string)`

SetRelatedProjectId sets RelatedProjectId field to given value.


### GetRelationship

`func (o *RelatedProject) GetRelationship() RelationshipType`

GetRelationship returns the Relationship field if non-nil, zero value otherwise.

### GetRelationshipOk

`func (o *RelatedProject) GetRelationshipOk() (*RelationshipType, bool)`

GetRelationshipOk returns a tuple with the Relationship field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelationship

`func (o *RelatedProject) SetRelationship(v RelationshipType)`

SetRelationship sets Relationship field to given value.


### GetCustomRelationship

`func (o *RelatedProject) GetCustomRelationship() string`

GetCustomRelationship returns the CustomRelationship field if non-nil, zero value otherwise.

### GetCustomRelationshipOk

`func (o *RelatedProject) GetCustomRelationshipOk() (*string, bool)`

GetCustomRelationshipOk returns a tuple with the CustomRelationship field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomRelationship

`func (o *RelatedProject) SetCustomRelationship(v string)`

SetCustomRelationship sets CustomRelationship field to given value.

### HasCustomRelationship

`func (o *RelatedProject) HasCustomRelationship() bool`

HasCustomRelationship returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


