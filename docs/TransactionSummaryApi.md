# swagger_client.TransactionSummaryApi

All URIs are relative to *https://localhost/ahoi/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_summary**](TransactionSummaryApi.md#list_summary) | **GET** /accesses/{accessId}/accounts/{accountId}/transactionsummaries | List account summaries


# **list_summary**
> list[MonthlySummary] list_summary(access_id, account_id, limit=limit, offset=offset, _from=_from, to=to)

List account summaries

Retrieve account summaries and provide a sum for incoming and outgoing transactions.

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
api_instance = swagger_client.TransactionSummaryApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for which to list the summaries
account_id = 'account_id_example' # str | The **accountId** for which to list the summaries
limit = 56 # int | Optional — limit the number of returned summary entries (optional)
offset = 56 # int | Optional — skip the first **offset** summary entries in the result (optional)
_from = '_from_example' # str | Optional — only return summary entries later than **from**; an         ISO8601 Date (2014-11-17) (optional)
to = 'to_example' # str | Optional — only return summary entries prior or equal to         **to**; an ISO8601 Date (optional)

try:
    # List account summaries
    api_response = api_instance.list_summary(access_id, account_id, limit=limit, offset=offset, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionSummaryApi->list_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for which to list the summaries | 
 **account_id** | **str**| The **accountId** for which to list the summaries | 
 **limit** | **int**| Optional — limit the number of returned summary entries | [optional] 
 **offset** | **int**| Optional — skip the first **offset** summary entries in the result | [optional] 
 **_from** | **str**| Optional — only return summary entries later than **from**; an         ISO8601 Date (2014-11-17) | [optional] 
 **to** | **str**| Optional — only return summary entries prior or equal to         **to**; an ISO8601 Date | [optional] 

### Return type

[**list[MonthlySummary]**](MonthlySummary.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

