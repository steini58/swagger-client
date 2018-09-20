# swagger_client.TransactionPatternApi

All URIs are relative to *https://localhost/ahoi/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_transaction_pattern**](TransactionPatternApi.md#activate_transaction_pattern) | **PUT** /accesses/{accessId}/accounts/{accountId}/transactionpatterns/{patternId}/active/{activated} | Enable a transaction pattern
[**delete_transaction_pattern**](TransactionPatternApi.md#delete_transaction_pattern) | **DELETE** /accesses/{accessId}/accounts/{accountId}/transactionpatterns/{patternId} | Delete transaction pattern
[**get_transaction_pattern**](TransactionPatternApi.md#get_transaction_pattern) | **GET** /accesses/{accessId}/accounts/{accountId}/transactionpatterns/{patternId} | Get transaction pattern
[**list_transaction_patterns**](TransactionPatternApi.md#list_transaction_patterns) | **GET** /accesses/{accessId}/accounts/{accountId}/transactionpatterns | List transaction patterns for account
[**post_transaction_pattern**](TransactionPatternApi.md#post_transaction_pattern) | **POST** /accesses/{accessId}/accounts/{accountId}/transactionpatterns | Create a new pattern


# **activate_transaction_pattern**
> TransactionPattern activate_transaction_pattern(access_id, account_id, pattern_id, activated)

Enable a transaction pattern

Disabling the transaction pattern results in ignoring the pattern in the forecast. The transaction still exists and relations with transactions are not modified.

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
api_instance = swagger_client.TransactionPatternApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for which to activate the pattern
account_id = 'account_id_example' # str | The **accountId** for which to activate the pattern
pattern_id = 'pattern_id_example' # str | The **patternId** to (de)activate
activated = true # bool | If `true`, the pattern will be used for forecast calculations;         `false` will be ignored

try:
    # Enable a transaction pattern
    api_response = api_instance.activate_transaction_pattern(access_id, account_id, pattern_id, activated)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPatternApi->activate_transaction_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for which to activate the pattern | 
 **account_id** | **str**| The **accountId** for which to activate the pattern | 
 **pattern_id** | **str**| The **patternId** to (de)activate | 
 **activated** | **bool**| If &#x60;true&#x60;, the pattern will be used for forecast calculations;         &#x60;false&#x60; will be ignored | 

### Return type

[**TransactionPattern**](TransactionPattern.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_pattern**
> delete_transaction_pattern(access_id, account_id, pattern_id)

Delete transaction pattern

Delete the transaction pattern identified by the **patternId**. All associated transactions will be updated to {{patternId = null}}.

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
api_instance = swagger_client.TransactionPatternApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for the transaction pattern to delete
account_id = 'account_id_example' # str | The **accountId** for the transaction pattern to delete
pattern_id = 'pattern_id_example' # str | The **patternId** to delete

try:
    # Delete transaction pattern
    api_instance.delete_transaction_pattern(access_id, account_id, pattern_id)
except ApiException as e:
    print("Exception when calling TransactionPatternApi->delete_transaction_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for the transaction pattern to delete | 
 **account_id** | **str**| The **accountId** for the transaction pattern to delete | 
 **pattern_id** | **str**| The **patternId** to delete | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_pattern**
> TransactionPattern get_transaction_pattern(access_id, account_id, pattern_id)

Get transaction pattern

Returns the transaction pattern identified by **patternId** in relationship with  **accountId**.

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
api_instance = swagger_client.TransactionPatternApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for the pattern to retrieve
account_id = 'account_id_example' # str | The **accoundId** for the pattern to retrieve
pattern_id = 'pattern_id_example' # str | The **patternId** for the pattern to retrieve

try:
    # Get transaction pattern
    api_response = api_instance.get_transaction_pattern(access_id, account_id, pattern_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPatternApi->get_transaction_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for the pattern to retrieve | 
 **account_id** | **str**| The **accoundId** for the pattern to retrieve | 
 **pattern_id** | **str**| The **patternId** for the pattern to retrieve | 

### Return type

[**TransactionPattern**](TransactionPattern.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_patterns**
> list[TransactionPattern] list_transaction_patterns(access_id, account_id)

List transaction patterns for account

Returns all transaction pattern for **accountId**. Transaction patterns are recurring transactions automatically identified by the server or manually created via [create transaction pattern](#!/Transaction_pattern/postTransactionPattern).

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
api_instance = swagger_client.TransactionPatternApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for which to retrieve transaction patterns
account_id = 'account_id_example' # str | The **accountId** for which to retrieve transaction patterns

try:
    # List transaction patterns for account
    api_response = api_instance.list_transaction_patterns(access_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPatternApi->list_transaction_patterns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for which to retrieve transaction patterns | 
 **account_id** | **str**| The **accountId** for which to retrieve transaction patterns | 

### Return type

[**list[TransactionPattern]**](TransactionPattern.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_transaction_pattern**
> TransactionPattern post_transaction_pattern(access_id, account_id, transaction_pattern_dto)

Create a new pattern

Create a new pattern for an **accountId**. The **cycle** can be one of `MONTHLY`, `QUARTERLY`, `SEMI_ANNUALLY` or `ANNUALLY`. The **day** can be between `1` and `366`, depending on **cycle**:  | cycle | day range | example | | --- | --- | --- | | `MONTHLY` | `1`-`31`  | every 29th of the month => `29` | | `QUARTERLY` | `1`-`92`  | 23rd of February (23rd of May, etc.) => `54` (31 [complete first month] + 23 [days in second month]) | | `SEMI_ANNUALLY` | `1`-`184` | 1st of May and 1st of November => `121` (for first half of year: 31 + 28 + 31 + 30 + 1) | | `ANNUALLY` | `1`-`366` | 24th of December => `358` |  If a similar pattern already exists, you will receive an HTTP status code 409.

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
api_instance = swagger_client.TransactionPatternApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** to which the new created pattern is associated with
account_id = 'account_id_example' # str | The **accountId** to which the new created pattern is associated with
transaction_pattern_dto = swagger_client.TransactionPattern() # TransactionPattern | The transaction pattern to create

try:
    # Create a new pattern
    api_response = api_instance.post_transaction_pattern(access_id, account_id, transaction_pattern_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPatternApi->post_transaction_pattern: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** to which the new created pattern is associated with | 
 **account_id** | **str**| The **accountId** to which the new created pattern is associated with | 
 **transaction_pattern_dto** | [**TransactionPattern**](TransactionPattern.md)| The transaction pattern to create | 

### Return type

[**TransactionPattern**](TransactionPattern.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

