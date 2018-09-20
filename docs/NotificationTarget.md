# NotificationTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID of this notificationTarget (generated value) | [optional] 
**app_token** | **str** | Installation specific application token to send push notifications to. (e.g. device token on iOS devices) | 
**product_id** | **str** | Id of the application. Has to be set up in AHOI. Use \&quot;sandbox-product\&quot; in sandbox environment. | 
**operating_system** | **str** | Operating system of the application | 
**state** | **str** | State of the application | [optional] 
**locale** | **str** | Locale used to determine notification titles and texts for this target.   Defaults to &#39;de_DE&#39;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


