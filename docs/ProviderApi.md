# swagger_client.ProviderApi

All URIs are relative to *https://localhost/ahoi/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_provider**](ProviderApi.md#get_provider) | **GET** /providers/{providerId} | Get provider
[**get_providers**](ProviderApi.md#get_providers) | **GET** /providers | List bank providers


# **get_provider**
> Provider get_provider(provider_id)

Get provider

Retrieve a single provider identified by **providerId**.

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
api_instance = swagger_client.ProviderApi(swagger_client.ApiClient(configuration))
provider_id = 'provider_id_example' # str | The **providerId** to retrieve

try:
    # Get provider
    api_response = api_instance.get_provider(provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->get_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| The **providerId** to retrieve | 

### Return type

[**Provider**](Provider.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers**
> list[Provider] get_providers(bank_code=bank_code, supported=supported, query=query)

List bank providers

Retrieve a list of bank providers. A provider-**id** is necessary to create an _access_. To retrieve the necessary access fields, you need to query the specific `provider/{providerId}`. For performance reasons they are kept separate. 

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
api_instance = swagger_client.ProviderApi(swagger_client.ApiClient(configuration))
bank_code = 'bank_code_example' # str | Optional — if length = 8, the response will also contain data describing             the fields required for account setup (optional)
supported = true # bool | Optional — response should only contain providers supported for account             setup via this API (optional)
query = 'query_example' # str | Optional — search parameters for BankCode, BIC, Location, Name. Will be ignored             if the bankCode query parameter is set. (optional)

try:
    # List bank providers
    api_response = api_instance.get_providers(bank_code=bank_code, supported=supported, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->get_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_code** | **str**| Optional — if length &#x3D; 8, the response will also contain data describing             the fields required for account setup | [optional] 
 **supported** | **bool**| Optional — response should only contain providers supported for account             setup via this API | [optional] 
 **query** | **str**| Optional — search parameters for BankCode, BIC, Location, Name. Will be ignored             if the bankCode query parameter is set. | [optional] 

### Return type

[**list[Provider]**](Provider.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

