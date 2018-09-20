# swagger_client.ForecastApi

All URIs are relative to *https://localhost/ahoi/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_forecast**](ForecastApi.md#get_forecast) | **GET** /accesses/{accessId}/accounts/{accountId}/forecast | Get balance forecast
[**get_forecast_transactions**](ForecastApi.md#get_forecast_transactions) | **GET** /accesses/{accessId}/accounts/{accountId}/forecast/transactions | Retrieve balance forecast for the end of the current month.


# **get_forecast**
> Forecast get_forecast(access_id, account_id)

Get balance forecast

The current month is determined by the latest refresh.

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
api_instance = swagger_client.ForecastApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for which to retrieve forecasts
account_id = 'account_id_example' # str | The **accountId** for which to retrieve forecasts

try:
    # Get balance forecast
    api_response = api_instance.get_forecast(access_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForecastApi->get_forecast: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for which to retrieve forecasts | 
 **account_id** | **str**| The **accountId** for which to retrieve forecasts | 

### Return type

[**Forecast**](Forecast.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forecast_transactions**
> ForecastTransaction get_forecast_transactions(access_id, account_id)

Retrieve balance forecast for the end of the current month.

The current  month is determined by latest refresh of transactions. The request  also retrieves the transactions expected to be applied until the  end of the current month.

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
api_instance = swagger_client.ForecastApi(swagger_client.ApiClient(configuration))
access_id = 'access_id_example' # str | The **accessId** for the forecast.
account_id = 'account_id_example' # str | The **id** for the account.

try:
    # Retrieve balance forecast for the end of the current month.
    api_response = api_instance.get_forecast_transactions(access_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForecastApi->get_forecast_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_id** | **str**| The **accessId** for the forecast. | 
 **account_id** | **str**| The **id** for the account. | 

### Return type

[**ForecastTransaction**](ForecastTransaction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

