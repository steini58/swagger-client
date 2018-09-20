# swagger_client.AccessApi

All URIs are relative to *https://localhost/ahoi/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_access**](AccessApi.md#delete_access) | **DELETE** /accesses/{accessId} | Delete access
[**get_access**](AccessApi.md#get_access) | **GET** /accesses/{accessId} | Get access
[**get_accesses**](AccessApi.md#get_accesses) | **GET** /accesses | List accesses
[**get_asset**](AccessApi.md#get_asset) | **GET** /accesses/{accessId}/accounts/{accountId}/assets/{assetId} | Get transaction.
[**list_assets**](AccessApi.md#list_assets) | **GET** /accesses/{accessId}/accounts/{accountId}/assets | Returns a list of assets for the related account represented by path  parameter accountId.
[**post_access**](AccessApi.md#post_access) | **POST** /accesses | Create a new access
[**put_access**](AccessApi.md#put_access) | **PUT** /accesses/{accessId} | Update access


# **delete_access**
> delete_access(access_id)

Delete access

Delete access with **accessId** and all related accounts. This also deletes related notifications. If this is a user's last remaining access, all notification targets will also be deleted.

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
api_instance = swagger_client.AccessApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **id** for the access to delete

try:
    # Delete access
    api_instance.delete_access(access_id)
except ApiException as e:
    print("Exception when calling AccessApi->delete_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **id** for the access to delete | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access**
> Access get_access(access_id)

Get access

Retrieve the access with **accessId**. The retrieved object does not contain sensitive information such as the PIN.

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
api_instance = swagger_client.AccessApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **id** for the access to retrieve.

try:
    # Get access
    api_response = api_instance.get_access(access_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->get_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **id** for the access to retrieve. | 

### Return type

[**Access**](Access.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accesses**
> list[Access] get_accesses()

List accesses

Returns all registered accesses for the authenticated user. Confidential information like the PIN will not be returned.

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
api_instance = swagger_client.AccessApi(swagger_client.ApiClient(configuration))

try:
    # List accesses
    api_response = api_instance.get_accesses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->get_accesses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Access]**](Access.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> Asset get_asset(access_id, account_id, asset_id)

Get transaction.

Returns the asset identified by **assetId** in relationship with  **accountId**.

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
api_instance = swagger_client.AccessApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | 
account_id = 'account_id_example' # str | The **id** for the account.
asset_id = 'asset_id_example' # str | The **assetId** for the asset to retrieve

try:
    # Get transaction.
    api_response = api_instance.get_asset(access_id, account_id, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->get_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**|  | 
 **account_id** | **str**| The **id** for the account. | 
 **asset_id** | **str**| The **assetId** for the asset to retrieve | 

### Return type

[**Asset**](Asset.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets**
> list[Asset] list_assets(access_id, account_id, max_age=max_age)

Returns a list of assets for the related account represented by path  parameter accountId.

The return list can be filtered by the query  parameters \"max-age\".

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
api_instance = swagger_client.AccessApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | 
account_id = 'account_id_example' # str | The **id** for the account.
max_age = 789 # int | optional - in seconds - indicates the maximum acceptable         timeframe since the last refresh of the given account (optional)

try:
    # Returns a list of assets for the related account represented by path  parameter accountId.
    api_response = api_instance.list_assets(access_id, account_id, max_age=max_age)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->list_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**|  | 
 **account_id** | **str**| The **id** for the account. | 
 **max_age** | **int**| optional - in seconds - indicates the maximum acceptable         timeframe since the last refresh of the given account | [optional] 

### Return type

[**list[Asset]**](Asset.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_access**
> Access post_access(access_dto)

Create a new access

Create a new access and setup all associated accounts and transactions. This will also trigger the creation of monthly transaction summaries, the analysis of all accounts for recurring transactions, and the calculation of the balance forecast.   If the credentials were invalid, the validation state is set accordingly.    It is possible to have multiple accesses for one user.

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
api_instance = swagger_client.AccessApi(swagger_client.ApiClient(configuration))
access_dto = swagger_client.Access() # Access | A valid BankAccess object containing the required             **accessFields** as indicated by the provider object and the             **providerId**.

try:
    # Create a new access
    api_response = api_instance.post_access(access_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->post_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_dto** | [**Access**](Access.md)| A valid BankAccess object containing the required             **accessFields** as indicated by the provider object and the             **providerId**. | 

### Return type

[**Access**](Access.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_access**
> Access put_access(access_id, access_dto)

Update access

Update the access credentials in **accessFields**. If the access does not exist, the **accessId** does not match the **id** in **accessDto** or the **providerId** is not the same, the status code 404 is returned. If another access with the same login  data already exists, the status code 409 is returned.  The updated access is validated by setting up an account. The status code 200 does not imply that the credentials are correct. To check this the client should obtain access.

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
api_instance = swagger_client.AccessApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **id** for the access to update.
access_dto = swagger_client.Access() # Access | The Access object that contains the changed credentials in             **accessFields**. Other fields cannot be edited.

try:
    # Update access
    api_response = api_instance.put_access(access_id, access_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->put_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **id** for the access to update. | 
 **access_dto** | [**Access**](Access.md)| The Access object that contains the changed credentials in             **accessFields**. Other fields cannot be edited. | 

### Return type

[**Access**](Access.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

