# swagger_client.AccountApi

All URIs are relative to *https://localhost/ahoi/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_account**](AccountApi.md#delete_account) | **DELETE** /accesses/{accessId}/accounts/{accountId} | Delete account
[**get_account**](AccountApi.md#get_account) | **GET** /accesses/{accessId}/accounts/{accountId} | Get account
[**get_accounts**](AccountApi.md#get_accounts) | **GET** /accesses/{accessId}/accounts | List accounts
[**update_account**](AccountApi.md#update_account) | **PUT** /accesses/{accessId}/accounts/{accountId}/userdefinedname/{name} | Update account name


# **delete_account**
> delete_account(access_id, account_id)

Delete account

Delete the account identified by **accountId**. 

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for the account to delete
account_id = 'account_id_example' # str | The **id** for the account to delete

try:
    # Delete account
    api_instance.delete_account(access_id, account_id)
except ApiException as e:
    print("Exception when calling AccountApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for the account to delete | 
 **account_id** | **str**| The **id** for the account to delete | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> Account get_account(access_id, account_id)

Get account

Returns the account identified by **accountId**.

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for the account to retrieve
account_id = 'account_id_example' # str | The **id** for the account to retrieve

try:
    # Get account
    api_response = api_instance.get_account(access_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for the account to retrieve | 
 **account_id** | **str**| The **id** for the account to retrieve | 

### Return type

[**Account**](Account.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> list[Account] get_accounts(access_id)

List accounts

Retrieve all accounts for the current user under the **accessId**.

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **id** for the access for which to retrieve all accounts

try:
    # List accounts
    api_response = api_instance.get_accounts(access_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **id** for the access for which to retrieve all accounts | 

### Return type

[**list[Account]**](Account.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> Account update_account(access_id, account_id, name)

Update account name

Update the account name used in AHOI. Name must be URL encoded.

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for which the user-defined account name should be altered
account_id = 'account_id_example' # str | The **id** for which the user-defined account name should be altered
name = 'name_example' # str | The new URL-encoded name

try:
    # Update account name
    api_response = api_instance.update_account(access_id, account_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for which the user-defined account name should be altered | 
 **account_id** | **str**| The **id** for which the user-defined account name should be altered | 
 **name** | **str**| The new URL-encoded name | 

### Return type

[**Account**](Account.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

