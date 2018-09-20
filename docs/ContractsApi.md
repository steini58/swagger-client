# swagger_client.ContractsApi

All URIs are relative to *https://localhost/ahoi/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contract_list**](ContractsApi.md#get_contract_list) | **GET** /contract/list | Retrieves the contract list for a given user


# **get_contract_list**
> get_contract_list()

Retrieves the contract list for a given user

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
api_instance = swagger_client.ContractsApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves the contract list for a given user
    api_instance.get_contract_list()
except ApiException as e:
    print("Exception when calling ContractsApi->get_contract_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

