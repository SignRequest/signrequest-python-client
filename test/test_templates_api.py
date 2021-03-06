# coding: utf-8

"""
    SignRequest API

    API for SignRequest.com

    OpenAPI spec version: v1
    Contact: tech-support@signrequest.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import signrequest_python_client
from signrequest_python_client.api.templates_api import TemplatesApi  # noqa: E501
from signrequest_python_client.rest import ApiException


class TestTemplatesApi(unittest.TestCase):
    """TemplatesApi unit test stubs"""

    def setUp(self):
        self.api = signrequest_python_client.api.templates_api.TemplatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_templates_list(self):
        """Test case for templates_list

        Retrieve a list of Templates  # noqa: E501
        """
        pass

    def test_templates_read(self):
        """Test case for templates_read

        Retrieve a Template  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
