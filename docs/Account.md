# Account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal ID of this account (generated value) | 
**name** | **str** | Account name returned by bank provider (e.g., \&quot;Giro Account\&quot;) | 
**user_defined_name** | **str** | Account userDefinedName. This value can be set to define a custom name used in AHOI (e.g., \&quot;My Giro Account\&quot;).  Can be changed by using the account resource. | [optional] 
**owner** | **str** | Account owner returned by bank provider (e.g., \&quot;Max Mustermann\&quot;) | 
**provider_id** | **str** | Identifier of the provider to which this account belongs | 
**kind** | **str** | An account kind is a classification of its structure and its possibilities.   This is typically defined by the bank provider. | 
**automatic_refresh_interval** | **int** | Interval that indicates the freguency of which the account is updated.   This interval is read-only and is determined by the server depending on created notifications and last use of the API. The range is between every hour, daily and monthly. | 
**type** | **str** | Discriminator for subtypes. At the moment only &#x60;BankAccount&#x60; is supported. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


