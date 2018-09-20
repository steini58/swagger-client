# swagger_client.TANSchemesApi

All URIs are relative to *https://localhost/ahoi/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_tan_media**](TANSchemesApi.md#get_current_tan_media) | **GET** /accesses/{accessId}/currenttanmedia | Get current TAN media.
[**get_current_tan_scheme**](TANSchemesApi.md#get_current_tan_scheme) | **GET** /accesses/{accessId}/currenttanscheme | Get current TAN scheme.
[**get_tan_schemes**](TANSchemesApi.md#get_tan_schemes) | **GET** /accesses/{accessId}/tanschemes | List TAN schemes for access
[**put_current_tan_media**](TANSchemesApi.md#put_current_tan_media) | **PUT** /accesses/{accessId}/currenttanmedia/{tanMediaId} | Update current TAN media.
[**put_current_tan_scheme**](TANSchemesApi.md#put_current_tan_scheme) | **PUT** /accesses/{accessId}/currenttanscheme/{tanSchemeId} | Update current TAN scheme.


# **get_current_tan_media**
> TanMedia get_current_tan_media(access_id)

Get current TAN media.

Returns the currently selected TAN media for the access.

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
api_instance = swagger_client.TANSchemesApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for which to retrieve the current TAN media.

try:
    # Get current TAN media.
    api_response = api_instance.get_current_tan_media(access_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TANSchemesApi->get_current_tan_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for which to retrieve the current TAN media. | 

### Return type

[**TanMedia**](TanMedia.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_tan_scheme**
> TanScheme get_current_tan_scheme(access_id)

Get current TAN scheme.

Returns the currently selected TAN scheme for the access.

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
api_instance = swagger_client.TANSchemesApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for which to retrieve the current TAN scheme.

try:
    # Get current TAN scheme.
    api_response = api_instance.get_current_tan_scheme(access_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TANSchemesApi->get_current_tan_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for which to retrieve the current TAN scheme. | 

### Return type

[**TanScheme**](TanScheme.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tan_schemes**
> list[TanScheme] get_tan_schemes(access_id, max_age=max_age)

List TAN schemes for access

Retrieves all available TAN schemes for access.

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
api_instance = swagger_client.TANSchemesApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **id** for the access for which to retrieve the TAN list
max_age = 789 # int | Optional - in seconds - indicates the maximum acceptable         timeframe since the last refresh of the tan scheme list. (optional)

try:
    # List TAN schemes for access
    api_response = api_instance.get_tan_schemes(access_id, max_age=max_age)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TANSchemesApi->get_tan_schemes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **id** for the access for which to retrieve the TAN list | 
 **max_age** | **int**| Optional - in seconds - indicates the maximum acceptable         timeframe since the last refresh of the tan scheme list. | [optional] 

### Return type

[**list[TanScheme]**](TanScheme.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_current_tan_media**
> Access put_current_tan_media(access_id, tan_media_id)

Update current TAN media.

Update the access with a new currentTanMedia.

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
api_instance = swagger_client.TANSchemesApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for which to set the current TAN media.
tan_media_id = 'tan_media_id_example' # str | The **id** for the TAN media that should be set as the new currentTanMedia.

try:
    # Update current TAN media.
    api_response = api_instance.put_current_tan_media(access_id, tan_media_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TANSchemesApi->put_current_tan_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for which to set the current TAN media. | 
 **tan_media_id** | **str**| The **id** for the TAN media that should be set as the new currentTanMedia. | 

### Return type

[**Access**](Access.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_current_tan_scheme**
> Access put_current_tan_scheme(access_id, tan_scheme_id)

Update current TAN scheme.

Update the access with a new currentTanScheme.

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
api_instance = swagger_client.TANSchemesApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for which to set the current TAN scheme.
tan_scheme_id = 'tan_scheme_id_example' # str | The **id** for the TAN scheme that should be set as the new currentTanScheme.

try:
    # Update current TAN scheme.
    api_response = api_instance.put_current_tan_scheme(access_id, tan_scheme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TANSchemesApi->put_current_tan_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for which to set the current TAN scheme. | 
 **tan_scheme_id** | **str**| The **id** for the TAN scheme that should be set as the new currentTanScheme. | 

### Return type

[**Access**](Access.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

