# coding: utf-8

"""
    SignRequest API

    API for SignRequest.com

    OpenAPI spec version: v1
    Contact: tech-support@signrequest.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from signrequest_client.api_client import ApiClient


class SignrequestQuickCreateApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def signrequest_quick_create_create(self, data, **kwargs):  # noqa: E501
        """Quick create a SignRequest  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.signrequest_quick_create_create(data, async=True)
        >>> result = thread.get()

        :param async bool
        :param SignRequestQuickCreate data: (required)
        :return: SignRequestQuickCreate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.signrequest_quick_create_create_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.signrequest_quick_create_create_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def signrequest_quick_create_create_with_http_info(self, data, **kwargs):  # noqa: E501
        """Quick create a SignRequest  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.signrequest_quick_create_create_with_http_info(data, async=True)
        >>> result = thread.get()

        :param async bool
        :param SignRequestQuickCreate data: (required)
        :return: SignRequestQuickCreate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method signrequest_quick_create_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `signrequest_quick_create_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/signrequest-quick-create/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SignRequestQuickCreate',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)