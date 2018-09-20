# NewTransactionNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Identifier of the account to which this notification belongs | 
**lower_threshold** | [**Amount**](Amount.md) | Optional limitation; lower threshold of the amount (negative values allowed) above which notifications will be sent | [optional] 
**upper_threshold** | [**Amount**](Amount.md) | Optional limitation; upper threshold of the amount (negative values allowed) below which notifications will be sent | [optional] 
**search_keyword** | **str** | Optional limitation on transactions for given keywords (e.g., owner \&quot;Hans Muster\&quot; or purpose \&quot;Salary\&quot;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


