# MonthlySummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | MonthlySummary id in UUID form | 
**month** | **str** | The month this entry belongs to (year-month in the ISO-8601: \&quot;yyyy-MM\&quot;) | 
**account_id** | **str** | Id of account this entry belongs to | 
**income** | [**Amount**](Amount.md) | Sum of all incoming transactions for this month | 
**outgoings** | [**Amount**](Amount.md) | Sum of all outgoing transactions for this month | 
**balance** | [**Amount**](Amount.md) | Balance at end of month | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


