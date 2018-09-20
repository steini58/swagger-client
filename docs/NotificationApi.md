# swagger_client.NotificationApi

All URIs are relative to *https://localhost/ahoi/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_notification**](NotificationApi.md#delete_notification) | **DELETE** /notificationtargets/{targetId}/notifications/{notificationId} | Delete notification
[**get_notification**](NotificationApi.md#get_notification) | **GET** /notificationtargets/{targetId}/notifications/{notificationId} | Get notification 
[**get_notifications**](NotificationApi.md#get_notifications) | **GET** /notificationtargets/{targetId}/notifications | List notifications
[**post_balance_change_notification**](NotificationApi.md#post_balance_change_notification) | **POST** /notificationtargets/{targetId}/notifications/balancechangenotification | Create a balance change notification
[**post_budget_notification**](NotificationApi.md#post_budget_notification) | **POST** /notificationtargets/{targetId}/notifications/budgetnotification | Create a budget change notification
[**post_daily_summary_notification**](NotificationApi.md#post_daily_summary_notification) | **POST** /notificationtargets/{targetId}/notifications/dailysummarynotification | Create a daily summary notification
[**post_new_transaction_notification**](NotificationApi.md#post_new_transaction_notification) | **POST** /notificationtargets/{targetId}/notifications/newtransactionnotification | Create a new transaction notification
[**put_notification**](NotificationApi.md#put_notification) | **PUT** /notificationtargets/{targetId}/notifications/{notificationId} | Update notification


# **delete_notification**
> delete_notification(target_id, notification_id)

Delete notification

Delete notification identified by **notificationId**.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
target_id = 'target_id_example' # str | The **targetId** for which to delete the notification
notification_id = 'notification_id_example' # str | The **notificationId** to delete

try:
    # Delete notification
    api_instance.delete_notification(target_id, notification_id)
except ApiException as e:
    print("Exception when calling NotificationApi->delete_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| The **targetId** for which to delete the notification | 
 **notification_id** | **str**| The **notificationId** to delete | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification**
> Notification get_notification(target_id, notification_id)

Get notification 

Retrieve notification identified by **notificationId**.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
target_id = 'target_id_example' # str | The **targetId** for which to retrieve the notification
notification_id = 'notification_id_example' # str | The *notificationId* to retrieve

try:
    # Get notification 
    api_response = api_instance.get_notification(target_id, notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->get_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| The **targetId** for which to retrieve the notification | 
 **notification_id** | **str**| The *notificationId* to retrieve | 

### Return type

[**Notification**](Notification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications**
> list[Notification] get_notifications(target_id)

List notifications

Retrieve all notifications associated with **targetId**.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
target_id = 'target_id_example' # str | The **targetId** for which to retrieve notifications

try:
    # List notifications
    api_response = api_instance.get_notifications(target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->get_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| The **targetId** for which to retrieve notifications | 

### Return type

[**list[Notification]**](Notification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_balance_change_notification**
> BalanceChangeNotification post_balance_change_notification(target_id, notification_dto)

Create a balance change notification

Only one notification per target and account can be created.   Receive notifications when the balance crosses the configured threshold; only one of **lowerThreshold** and **upperThreshold** may be set.    This example sends a notification when the balance is less than 0 &euro;    ```json {   \"type\": \"BalanceChangeNotification\",   \"accountId\": 0,   \"upperThreshold\": {     \"value\": 0,     \"currency\": \"EUR\"   } } ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
target_id = 'target_id_example' # str | The **targetId** for which to create the notification
notification_dto = swagger_client.BalanceChangeNotification() # BalanceChangeNotification | The balance change notification to create

try:
    # Create a balance change notification
    api_response = api_instance.post_balance_change_notification(target_id, notification_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->post_balance_change_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| The **targetId** for which to create the notification | 
 **notification_dto** | [**BalanceChangeNotification**](BalanceChangeNotification.md)| The balance change notification to create | 

### Return type

[**BalanceChangeNotification**](BalanceChangeNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_budget_notification**
> BudgetNotification post_budget_notification(target_id, notification_dto)

Create a budget change notification

Receive notifications when the calculated budget for the current month crosses the configured threshold; only one of **lowerThreshold** and **upperThreshold** may be set.    This example send a notification when the budget crosses 100 &euro;    ```json {   \"type\": \"BudgetNotification\",   \"accountId\": 0,   \"lowerThreshold\": {     \"value\": 10000,     \"currency\": \"EUR\"   } } ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
target_id = 'target_id_example' # str | The **targetId** for which to create the notification
notification_dto = swagger_client.BudgetNotification() # BudgetNotification | The budget change notification to create

try:
    # Create a budget change notification
    api_response = api_instance.post_budget_notification(target_id, notification_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->post_budget_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| The **targetId** for which to create the notification | 
 **notification_dto** | [**BudgetNotification**](BudgetNotification.md)| The budget change notification to create | 

### Return type

[**BudgetNotification**](BudgetNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_daily_summary_notification**
> DailySummaryNotification post_daily_summary_notification(target_id, notification_dto)

Create a daily summary notification

Receive a notification for your account status on the configured days and at the configured time. Please make sure to pass your timezone or adjust for UTC.    This example notifies you every day at 12:03 UTC    ```json {   \"type\": \"DailySummaryNotification\",   \"accountId\": 0,   \"daysOfWeek\": [     'MONDAY', 'TUESDAY', 'WEDNESDAY',      'THURSDAY', 'FRIDAY', 'SATURDAY',      'SUNDAY'   ],   \"timeOfDay\": \"12:03Z\" } ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
target_id = 'target_id_example' # str | The **targetId** for which to create the notification
notification_dto = swagger_client.DailySummaryNotification() # DailySummaryNotification | The daily summary notification to create

try:
    # Create a daily summary notification
    api_response = api_instance.post_daily_summary_notification(target_id, notification_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->post_daily_summary_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| The **targetId** for which to create the notification | 
 **notification_dto** | [**DailySummaryNotification**](DailySummaryNotification.md)| The daily summary notification to create | 

### Return type

[**DailySummaryNotification**](DailySummaryNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_new_transaction_notification**
> NewTransactionNotification post_new_transaction_notification(target_id, notification_dto)

Create a new transaction notification

Receive a notification for every new transaction, for transactions within a given threshold or that match a **searchKeyword**. To receive all transactions, simply leave the optional fields blank.     This example notifies you of every transaction that contains the keyword \"food\" between 20 &euro; and 60 &euro;:    ```json {   \"type\": \"NewTransactionNotification\",   \"accountId\": 0,   \"lowerThreshold\": {     \"value\": 2000,     \"currency\": \"EUR\"   },   \"upperThreshold\": {     \"value\": 6000,     \"currency\": \"EUR\"   },   \"searchKeyword\": \"Rent\" } ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
target_id = 'target_id_example' # str | The **targetId** for which to create the notification
notification_dto = swagger_client.NewTransactionNotification() # NewTransactionNotification | The new transaction notification to create

try:
    # Create a new transaction notification
    api_response = api_instance.post_new_transaction_notification(target_id, notification_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->post_new_transaction_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| The **targetId** for which to create the notification | 
 **notification_dto** | [**NewTransactionNotification**](NewTransactionNotification.md)| The new transaction notification to create | 

### Return type

[**NewTransactionNotification**](NewTransactionNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_notification**
> Notification put_notification(target_id, notification_id, notification_dto)

Update notification

Update the notification identified by **notificationId**. The **notificationId** must match the **id** in **notificationDto**. Please note that type depending restrictions from creating a notification also apply here.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
target_id = 'target_id_example' # str | The **targetId** for which to create the notification
notification_id = 'notification_id_example' # str | The **notificationId** to update
notification_dto = swagger_client.Notification() # Notification | The notification data to update

try:
    # Update notification
    api_response = api_instance.put_notification(target_id, notification_id, notification_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->put_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| The **targetId** for which to create the notification | 
 **notification_id** | **str**| The **notificationId** to update | 
 **notification_dto** | [**Notification**](Notification.md)| The notification data to update | 

### Return type

[**Notification**](Notification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

