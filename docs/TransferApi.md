# swagger_client.TransferApi

All URIs are relative to *https://localhost/ahoi/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_authorization**](TransferApi.md#post_authorization) | **POST** /accesses/{accessId}/accounts/{accountId}/transfers/{taskId}/authorize | Create a transfer authorization
[**post_transfer**](TransferApi.md#post_transfer) | **POST** /accesses/{accessId}/accounts/{accountId}/transfers | Create a new transfer


# **post_authorization**
> TransferTask post_authorization(access_id, account_id, task_id, transfer_challenge_response)

Create a transfer authorization

**Please note:** Exception from the norm. This POST request will not return  the two header fields X-Id and Location. The returned JSON document  represents the transfer.

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
api_instance = swagger_client.TransferApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for the triggered authorization
account_id = 'account_id_example' # str | The **account** for the triggered authorization
task_id = 'task_id_example' # str | The **taskId** given in the TransferChallenge
transfer_challenge_response = swagger_client.TransferChallengeResponse() # TransferChallengeResponse | The *TransferChallengeResponse* object to authorize the transfer

try:
    # Create a transfer authorization
    api_response = api_instance.post_authorization(access_id, account_id, task_id, transfer_challenge_response)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferApi->post_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for the triggered authorization | 
 **account_id** | **str**| The **account** for the triggered authorization | 
 **task_id** | **str**| The **taskId** given in the TransferChallenge | 
 **transfer_challenge_response** | [**TransferChallengeResponse**](TransferChallengeResponse.md)| The *TransferChallengeResponse* object to authorize the transfer | 

### Return type

[**TransferTask**](TransferTask.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_transfer**
> TransferChallenge post_transfer(access_id, account_id, transfer)

Create a new transfer

The transfer represents a money  transfer from the account identified by its ID to another bank account.   **Please note:** Exception from the norm. This POST request will not return  the two header fields X-Id and Location. Also, the returned JSON document  does not represent the transfer entity but rather a temporary placeholder.

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
api_instance = swagger_client.TransferApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for the transfer
account_id = 'account_id_example' # str | The **accountId** for the transfer
transfer = swagger_client.Transfer() # Transfer | The *Transfer* object to initiate a transfer

try:
    # Create a new transfer
    api_response = api_instance.post_transfer(access_id, account_id, transfer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferApi->post_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for the transfer | 
 **account_id** | **str**| The **accountId** for the transfer | 
 **transfer** | [**Transfer**](Transfer.md)| The *Transfer* object to initiate a transfer | 

### Return type

[**TransferChallenge**](TransferChallenge.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

