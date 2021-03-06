# coding: utf-8

"""
    

    [AHOI cookbook](/ahoi/docs/cookbook/index.html)  [Data Privacy](/sandboxmanager/#/privacy)  [Terms of Service](/sandboxmanager/#/terms)  [Imprint](https://sparkassen-hub.com/impressum/)  &copy; 2016&dash;2017 Starfinanz - Ein Unternehmen der Finanz Informatik  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TransactionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_transaction(self, access_id, account_id, transaction_id, **kwargs):  # noqa: E501
        """Get transaction  # noqa: E501

        Returns the transaction identified by **transactionId** in relationship with **accountId**.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_transaction(access_id, account_id, transaction_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str access_id: The **accessId** for the transaction to retrieve (required)
        :param str account_id: The **accountId** for the transaction to retrieve (required)
        :param str transaction_id: The **transactionId** for the pattern to retrieve (required)
        :return: Transaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_transaction_with_http_info(access_id, account_id, transaction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_transaction_with_http_info(access_id, account_id, transaction_id, **kwargs)  # noqa: E501
            return data

    def get_transaction_with_http_info(self, access_id, account_id, transaction_id, **kwargs):  # noqa: E501
        """Get transaction  # noqa: E501

        Returns the transaction identified by **transactionId** in relationship with **accountId**.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_transaction_with_http_info(access_id, account_id, transaction_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str access_id: The **accessId** for the transaction to retrieve (required)
        :param str account_id: The **accountId** for the transaction to retrieve (required)
        :param str transaction_id: The **transactionId** for the pattern to retrieve (required)
        :return: Transaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_id', 'account_id', 'transaction_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_id' is set
        if ('access_id' not in params or
                params['access_id'] is None):
            raise ValueError("Missing the required parameter `access_id` when calling `get_transaction`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_transaction`")  # noqa: E501
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params or
                params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `get_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'access_id' in params:
            path_params['accessId'] = params['access_id']  # noqa: E501
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501
        if 'transaction_id' in params:
            path_params['transactionId'] = params['transaction_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/accesses/{accessId}/accounts/{accountId}/transactions/{transactionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Transaction',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_transactions(self, access_id, account_id, **kwargs):  # noqa: E501
        """List transactions for account  # noqa: E501

        Retrieve all transactions for **accountId**.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_transactions(access_id, account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str access_id: The **accessId** for which to retrieve transactions. (required)
        :param str account_id: The **accountId** for which to retrieve transactions. (required)
        :param int max_age: Optional — indicates the maximum acceptable timeframe (in seconds) since the last refresh of the given account.
        :param int limit: Optional — limit the number of returned transactions
        :param int offset: Optional — skip the first **offset** transactions in result
        :param str _from: Optional — only return transactions with booking date later than **from**; an ISO8601 Month(2014-11), Date (2014-11-17) or DateTime         (2014-11-17T12:00:00Z)
        :param str to: Optional — only return transactions with booking date prior or equal to **to**; an ISO8601 Date, Month or DateTime
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_transactions_with_http_info(access_id, account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_transactions_with_http_info(access_id, account_id, **kwargs)  # noqa: E501
            return data

    def list_transactions_with_http_info(self, access_id, account_id, **kwargs):  # noqa: E501
        """List transactions for account  # noqa: E501

        Retrieve all transactions for **accountId**.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_transactions_with_http_info(access_id, account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str access_id: The **accessId** for which to retrieve transactions. (required)
        :param str account_id: The **accountId** for which to retrieve transactions. (required)
        :param int max_age: Optional — indicates the maximum acceptable timeframe (in seconds) since the last refresh of the given account.
        :param int limit: Optional — limit the number of returned transactions
        :param int offset: Optional — skip the first **offset** transactions in result
        :param str _from: Optional — only return transactions with booking date later than **from**; an ISO8601 Month(2014-11), Date (2014-11-17) or DateTime         (2014-11-17T12:00:00Z)
        :param str to: Optional — only return transactions with booking date prior or equal to **to**; an ISO8601 Date, Month or DateTime
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_id', 'account_id', 'max_age', 'limit', 'offset', '_from', 'to']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_id' is set
        if ('access_id' not in params or
                params['access_id'] is None):
            raise ValueError("Missing the required parameter `access_id` when calling `list_transactions`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'access_id' in params:
            path_params['accessId'] = params['access_id']  # noqa: E501
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []
        if 'max_age' in params:
            query_params.append(('max-age', params['max_age']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/accesses/{accessId}/accounts/{accountId}/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Transaction]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_transactions_for_pattern(self, access_id, account_id, pattern_id, **kwargs):  # noqa: E501
        """List transactions for pattern  # noqa: E501

        Retrieve all transactions for **patternId**.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_transactions_for_pattern(access_id, account_id, pattern_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str access_id: The **accessId** for which to retrieve transactions (required)
        :param str account_id: The **accountId** for which to retrieve transactions (required)
        :param str pattern_id: The **patternId** for which to retrieve transactions (required)
        :param int max_age: Optional — indicates the maximum acceptable timeframe (in seconds) since the last refresh of the given account
        :param int limit: Optional — limit the number of returned transactions
        :param int offset: Optional — skip the first **offset** transactions in result
        :param str _from: Optional — only return transactions with a booking date later than **from**; an ISO8601 Month(2014-11), Date (2014-11-17) or DateTime         (2014-11-17T12:00:00Z)
        :param str to: Optional — only return transactions with a booking date prior or equal to **to**; an ISO8601 Date, Month or DateTime
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_transactions_for_pattern_with_http_info(access_id, account_id, pattern_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_transactions_for_pattern_with_http_info(access_id, account_id, pattern_id, **kwargs)  # noqa: E501
            return data

    def list_transactions_for_pattern_with_http_info(self, access_id, account_id, pattern_id, **kwargs):  # noqa: E501
        """List transactions for pattern  # noqa: E501

        Retrieve all transactions for **patternId**.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_transactions_for_pattern_with_http_info(access_id, account_id, pattern_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str access_id: The **accessId** for which to retrieve transactions (required)
        :param str account_id: The **accountId** for which to retrieve transactions (required)
        :param str pattern_id: The **patternId** for which to retrieve transactions (required)
        :param int max_age: Optional — indicates the maximum acceptable timeframe (in seconds) since the last refresh of the given account
        :param int limit: Optional — limit the number of returned transactions
        :param int offset: Optional — skip the first **offset** transactions in result
        :param str _from: Optional — only return transactions with a booking date later than **from**; an ISO8601 Month(2014-11), Date (2014-11-17) or DateTime         (2014-11-17T12:00:00Z)
        :param str to: Optional — only return transactions with a booking date prior or equal to **to**; an ISO8601 Date, Month or DateTime
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_id', 'account_id', 'pattern_id', 'max_age', 'limit', 'offset', '_from', 'to']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_transactions_for_pattern" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_id' is set
        if ('access_id' not in params or
                params['access_id'] is None):
            raise ValueError("Missing the required parameter `access_id` when calling `list_transactions_for_pattern`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_transactions_for_pattern`")  # noqa: E501
        # verify the required parameter 'pattern_id' is set
        if ('pattern_id' not in params or
                params['pattern_id'] is None):
            raise ValueError("Missing the required parameter `pattern_id` when calling `list_transactions_for_pattern`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'access_id' in params:
            path_params['accessId'] = params['access_id']  # noqa: E501
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501
        if 'pattern_id' in params:
            path_params['patternId'] = params['pattern_id']  # noqa: E501

        query_params = []
        if 'max_age' in params:
            query_params.append(('max-age', params['max_age']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/accesses/{accessId}/accounts/{accountId}/transactionpatterns/{patternId}/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Transaction]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
