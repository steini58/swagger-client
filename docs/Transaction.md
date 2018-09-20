# Transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal ID of this transaction (generated value) | 
**transaction_pattern_id** | **str** | Identifier of the transactionPattern to which this transaction belongs | [optional] 
**additional_information** | [**list[AdditionalInformation]**](AdditionalInformation.md) |  | [optional] 
**type** | **str** | Discriminator for subtypes. At the moment only &#x60;GiroTransaction&#x60; is supported. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


