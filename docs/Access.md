# Access

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal ID of this access (generated value) | [optional] 
**provider_id** | **str** | Identifier of the provider to which this access belongs | 
**access_fields** | [**AccessFieldsMap**](AccessFieldsMap.md) | Authentication data for the given provider as map of InputFieldId to String (e.g., &#x60;{\&quot;USERNAME\&quot;, \&quot;yourName\&quot;}&#x60;)  The fields necessary for the access are determined by the   InputField descriptions of the related provider. | 
**validation_state** | **str** | The state reflects the validity of the access credentials. The state can change after communicating with the provider.  It can be OK (access credentials are valid); &#x60;ACCESS_LOCKED&#x60; (access is locked: This can happen when, for example, someone tried to login to your account by  using an incorrect PIN too many times or if your account was used for illegal purposes — automatic refresh will be disabled); or &#x60;ACCESS_WRONG&#x60; (access wrong: Saved  credentials are incorrect and no communication with the provider is possible — automatic refresh will be disabled) | [optional] 
**type** | **str** | Discriminator for subtypes. At the moment only &#x60;BankAccess&#x60; is supported. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


