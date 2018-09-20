# TransactionPattern

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal ID of this transactionPattern (generated value) | [optional] 
**state** | **str** | State of this pattern  can be &#x60;ACTIVE&#x60; (default) or &#x60;INACTIVE&#x60; (user has disabled it) | 
**cycle** | **str** | Frequency of occurrence for this pattern | 
**origin** | **str** | Origin of creation can be &#x60;FINDER&#x60; (automatically found) or &#x60;MANUAL&#x60; (created by user). Cannot be set with creation or update. | [optional] 
**day** | **int** | Day in the cycle this pattern occurs | 
**related_account_owner** | **str** | Name of owner of related account (debtor or creditor) | 
**amount** | [**Amount**](Amount.md) | Amount value | 
**account_number** | **str** | Account number or IBAN of related account (debtor or creditor) | 
**bank_code** | **str** | Bank code number or BIC of related account (debtor or creditor) | 
**kind** | **str** | Kind of transaction (e.g., \&quot;Lastschrift\&quot; or \&quot;Dauerauftrag\&quot;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


