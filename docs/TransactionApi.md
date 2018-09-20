# swagger_client.TransactionApi

All URIs are relative to *https://localhost/ahoi/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction**](TransactionApi.md#get_transaction) | **GET** /accesses/{accessId}/accounts/{accountId}/transactions/{transactionId} | Get transaction
[**list_transactions**](TransactionApi.md#list_transactions) | **GET** /accesses/{accessId}/accounts/{accountId}/transactions | List transactions for account
[**list_transactions_for_pattern**](TransactionApi.md#list_transactions_for_pattern) | **GET** /accesses/{accessId}/accounts/{accountId}/transactionpatterns/{patternId}/transactions | List transactions for pattern


# **get_transaction**
> Transaction get_transaction(access_id, account_id, transaction_id)

Get transaction

Returns the transaction identified by **transactionId** in relationship with **accountId**.

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
api_instance = swagger_client.TransactionApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for the transaction to retrieve
account_id = 'account_id_example' # str | The **accountId** for the transaction to retrieve
transaction_id = 'transaction_id_example' # str | The **transactionId** for the pattern to retrieve

try:
    # Get transaction
    api_response = api_instance.get_transaction(access_id, account_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for the transaction to retrieve | 
 **account_id** | **str**| The **accountId** for the transaction to retrieve | 
 **transaction_id** | **str**| The **transactionId** for the pattern to retrieve | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> list[Transaction] list_transactions(access_id, account_id, max_age=max_age, limit=limit, offset=offset, _from=_from, to=to)

List transactions for account

Retrieve all transactions for **accountId**.

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
api_instance = swagger_client.TransactionApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for which to retrieve transactions.
account_id = 'account_id_example' # str | The **accountId** for which to retrieve transactions.
max_age = 789 # int | Optional — indicates the maximum acceptable timeframe (in seconds) since the last refresh of the given account. (optional)
limit = 56 # int | Optional — limit the number of returned transactions (optional)
offset = 56 # int | Optional — skip the first **offset** transactions in result (optional)
_from = '_from_example' # str | Optional — only return transactions with booking date later than **from**; an ISO8601 Month(2014-11), Date (2014-11-17) or DateTime         (2014-11-17T12:00:00Z) (optional)
to = 'to_example' # str | Optional — only return transactions with booking date prior or equal to **to**; an ISO8601 Date, Month or DateTime (optional)

try:
    # List transactions for account
    api_response = api_instance.list_transactions(access_id, account_id, max_age=max_age, limit=limit, offset=offset, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->list_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for which to retrieve transactions. | 
 **account_id** | **str**| The **accountId** for which to retrieve transactions. | 
 **max_age** | **int**| Optional — indicates the maximum acceptable timeframe (in seconds) since the last refresh of the given account. | [optional] 
 **limit** | **int**| Optional — limit the number of returned transactions | [optional] 
 **offset** | **int**| Optional — skip the first **offset** transactions in result | [optional] 
 **_from** | **str**| Optional — only return transactions with booking date later than **from**; an ISO8601 Month(2014-11), Date (2014-11-17) or DateTime         (2014-11-17T12:00:00Z) | [optional] 
 **to** | **str**| Optional — only return transactions with booking date prior or equal to **to**; an ISO8601 Date, Month or DateTime | [optional] 

### Return type

[**list[Transaction]**](Transaction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions_for_pattern**
> list[Transaction] list_transactions_for_pattern(access_id, account_id, pattern_id, max_age=max_age, limit=limit, offset=offset, _from=_from, to=to)

List transactions for pattern

Retrieve all transactions for **patternId**.

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
api_instance = swagger_client.TransactionApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for which to retrieve transactions
account_id = 'account_id_example' # str | The **accountId** for which to retrieve transactions
pattern_id = 'pattern_id_example' # str | The **patternId** for which to retrieve transactions
max_age = 789 # int | Optional — indicates the maximum acceptable timeframe (in seconds) since the last refresh of the given account (optional)
limit = 56 # int | Optional — limit the number of returned transactions (optional)
offset = 56 # int | Optional — skip the first **offset** transactions in result (optional)
_from = '_from_example' # str | Optional — only return transactions with a booking date later than **from**; an ISO8601 Month(2014-11), Date (2014-11-17) or DateTime         (2014-11-17T12:00:00Z) (optional)
to = 'to_example' # str | Optional — only return transactions with a booking date prior or equal to **to**; an ISO8601 Date, Month or DateTime (optional)

try:
    # List transactions for pattern
    api_response = api_instance.list_transactions_for_pattern(access_id, account_id, pattern_id, max_age=max_age, limit=limit, offset=offset, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->list_transactions_for_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for which to retrieve transactions | 
 **account_id** | **str**| The **accountId** for which to retrieve transactions | 
 **pattern_id** | **str**| The **patternId** for which to retrieve transactions | 
 **max_age** | **int**| Optional — indicates the maximum acceptable timeframe (in seconds) since the last refresh of the given account | [optional] 
 **limit** | **int**| Optional — limit the number of returned transactions | [optional] 
 **offset** | **int**| Optional — skip the first **offset** transactions in result | [optional] 
 **_from** | **str**| Optional — only return transactions with a booking date later than **from**; an ISO8601 Month(2014-11), Date (2014-11-17) or DateTime         (2014-11-17T12:00:00Z) | [optional] 
 **to** | **str**| Optional — only return transactions with a booking date prior or equal to **to**; an ISO8601 Date, Month or DateTime | [optional] 

### Return type

[**list[Transaction]**](Transaction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

