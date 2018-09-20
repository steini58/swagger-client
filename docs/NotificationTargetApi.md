# swagger_client.NotificationTargetApi

All URIs are relative to *https://localhost/ahoi/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_notification_target**](NotificationTargetApi.md#delete_notification_target) | **DELETE** /notificationtargets/{targetId} | Delete notification target
[**get_notification_target**](NotificationTargetApi.md#get_notification_target) | **GET** /notificationtargets/{targetId} | Get notification target
[**get_notification_targets**](NotificationTargetApi.md#get_notification_targets) | **GET** /notificationtargets | List notification targets
[**post_notification_target**](NotificationTargetApi.md#post_notification_target) | **POST** /notificationtargets | Create a new notification target
[**put_notification_target**](NotificationTargetApi.md#put_notification_target) | **PUT** /notificationtargets/{targetId} | Update notification target


# **delete_notification_target**
> delete_notification_target(target_id)

Delete notification target

Delete a notification target identified by **targetId**. Also deletes associated notifications.

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
api_instance = swagger_client.NotificationTargetApi(swagger_client.ApiClient(configuration))
target_id = 'target_id_example' # str | The **targetId** to delete

try:
    # Delete notification target
    api_instance.delete_notification_target(target_id)
except ApiException as e:
    print("Exception when calling NotificationTargetApi->delete_notification_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| The **targetId** to delete | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_target**
> NotificationTarget get_notification_target(target_id)

Get notification target

Retrieve notification target identified by **targetId**.

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
api_instance = swagger_client.NotificationTargetApi(swagger_client.ApiClient(configuration))
target_id = 'target_id_example' # str | The **targetId** to retrieve

try:
    # Get notification target
    api_response = api_instance.get_notification_target(target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationTargetApi->get_notification_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| The **targetId** to retrieve | 

### Return type

[**NotificationTarget**](NotificationTarget.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_targets**
> list[NotificationTarget] get_notification_targets()

List notification targets

Retrieve all notification targets for the authenticated client.

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
api_instance = swagger_client.NotificationTargetApi(swagger_client.ApiClient(configuration))

try:
    # List notification targets
    api_response = api_instance.get_notification_targets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationTargetApi->get_notification_targets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NotificationTarget]**](NotificationTarget.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_notification_target**
> NotificationTarget post_notification_target(notification_target_dto)

Create a new notification target

Create a new notification target to receive configured notifications.  The two current supported systems are the Apple Push Notification service (APNs) for `IOS` devices and Google Cloud Messaging (GCM) for `ANDROID`, which must be supplied in **state**. The **appToken** must contain the unique identifier you receive after registering your device with the messaging services. The **locale** must comply to ISO 3166 language code. Currently only `de_DE` is supported. 

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
api_instance = swagger_client.NotificationTargetApi(swagger_client.ApiClient(configuration))
notification_target_dto = swagger_client.NotificationTarget() # NotificationTarget | The notification target to create

try:
    # Create a new notification target
    api_response = api_instance.post_notification_target(notification_target_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationTargetApi->post_notification_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_target_dto** | [**NotificationTarget**](NotificationTarget.md)| The notification target to create | 

### Return type

[**NotificationTarget**](NotificationTarget.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_notification_target**
> NotificationTarget put_notification_target(target_id, notification_target_dto)

Update notification target

Update a notification target. Usually used to change the **appToken** since the messaging services alter those periodically. The **id** in **notificationDto** must match the **targetId**.

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
api_instance = swagger_client.NotificationTargetApi(swagger_client.ApiClient(configuration))
target_id = 'target_id_example' # str | The **targetId** to update
notification_target_dto = swagger_client.NotificationTarget() # NotificationTarget | The notification target with updated token

try:
    # Update notification target
    api_response = api_instance.put_notification_target(target_id, notification_target_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationTargetApi->put_notification_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| The **targetId** to update | 
 **notification_target_dto** | [**NotificationTarget**](NotificationTarget.md)| The notification target with updated token | 

### Return type

[**NotificationTarget**](NotificationTarget.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

