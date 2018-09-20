# GiroTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) | Amount value | 
**booking_date** | **datetime** | Booking date (ISO 8601: \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssX\&quot;) | 
**value_date** | **datetime** | Value Date (ISO 8601: \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssX\&quot;) | 
**creditor** | **str** | Creditor&#39;s name | 
**creditor_bank_code** | **str** | Creditor&#39;s bank code or BIC | [optional] 
**creditor_account_number** | **str** | Creditor&#39;s account number or IBAN | [optional] 
**debtor** | **str** | Debtor&#39;s name | 
**debtor_bank_code** | **str** | Debtor&#39;s bank code or BIC | [optional] 
**debtor_account_number** | **str** | Debtor&#39;s account number or IBAN | [optional] 
**purpose** | **str** | Purpose (as given by the provider) | 
**clean_purpose** | **str** | Cleaned purpose. Some SEPA information is filtered out (e.g., \&quot;KREF+-1434947533-2...\&quot;) | [optional] 
**prebooked** | **bool** | Flag to identify if the transaction is marked as pre-booked | 
**booking_key** | **str** | Booking key for transaction | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


