# swagger_client.RegistrationApi

All URIs are relative to *https://localhost/ahoi/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_registration**](RegistrationApi.md#delete_registration) | **DELETE** /registration | Delete the user context for the current token.
[**get_json_web_key**](RegistrationApi.md#get_json_web_key) | **GET** /registration/jwk | Request API jwk public key
[**get_registration_public_key**](RegistrationApi.md#get_registration_public_key) | **GET** /registration/keys | Request API public key
[**register**](RegistrationApi.md#register) | **POST** /registration | User registration


# **delete_registration**
> delete_registration()

Delete the user context for the current token.

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
api_instance = swagger_client.RegistrationApi(swagger_client.ApiClient(configuration))

try:
    # Delete the user context for the current token.
    api_instance.delete_registration()
except ApiException as e:
    print("Exception when calling RegistrationApi->delete_registration: %s\n" % e)
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

# **get_json_web_key**
> JwkJwkPublicKey get_json_web_key()

Request API jwk public key

A valid API public key will be returned in JWK format to be used to encrypt registration data

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
api_instance = swagger_client.RegistrationApi(swagger_client.ApiClient(configuration))

try:
    # Request API jwk public key
    api_response = api_instance.get_json_web_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->get_json_web_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JwkJwkPublicKey**](JwkJwkPublicKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_public_key**
> RegistrationPublicKey get_registration_public_key()

Request API public key

A valid API public key will be returned to be used to encrypt registration data

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
api_instance = swagger_client.RegistrationApi(swagger_client.ApiClient(configuration))

try:
    # Request API public key
    api_response = api_instance.get_registration_public_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->get_registration_public_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RegistrationPublicKey**](RegistrationPublicKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> RegistrationResponse register()

User registration

Registers a user with AHOI

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
api_instance = swagger_client.RegistrationApi(swagger_client.ApiClient(configuration))

try:
    # User registration
    api_response = api_instance.register()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->register: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RegistrationResponse**](RegistrationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

