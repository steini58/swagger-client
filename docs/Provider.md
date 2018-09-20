# Provider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID of this provider. A constant to identify provider even when  e.g. their bank code changes (provided type is BankProvider) | 
**name** | **str** | Name of this provider e.g. \&quot;Hamburger Bank\&quot; | 
**location** | **str** | Location of this provider e.g. \&quot;Hamburg\&quot; | 
**access_description** | [**AccessDescription**](AccessDescription.md) | Description of the access for the account-setup e.g. UI-input-fields | [optional] 
**supported** | **bool** | Whether this bank is supported by AHOI-API, i.e. whether you can use a connection of this provider. | 
**type** | **str** | Discriminator for subtypes. At the moment only &#x60;BankProvider&#x60; is supported. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


