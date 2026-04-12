# DeletionChallenge

Challenge response for user account deletion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_text** | **str** | The exact challenge string that must be provided to confirm deletion | 
**expires_at** | **datetime** | When the challenge expires (3 minutes from issuance) | 

## Example

```python
from tmi_client.models.deletion_challenge import DeletionChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of DeletionChallenge from a JSON string
deletion_challenge_instance = DeletionChallenge.from_json(json)
# print the JSON string representation of the object
print(DeletionChallenge.to_json())

# convert the object into a dict
deletion_challenge_dict = deletion_challenge_instance.to_dict()
# create an instance of DeletionChallenge from a dict
deletion_challenge_from_dict = DeletionChallenge.from_dict(deletion_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


