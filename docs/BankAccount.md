# BankAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Account number (national) | 
**bank_code_number** | **str** | Bank code number (BLZ, national, 8 digits) | 
**bic** | **str** | Business Identifier Code (BIC; ISO 9362) | 
**iban** | **str** | International Bank Account Number (IBAN; ISO 13616-1) | 
**currency** | **str** | Account currency (ISO 4217) (e.g., \&quot;EUR\&quot;) | 
**balance** | [**Balance**](Balance.md) | Current balance. This value is set whenever the account is refreshed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


