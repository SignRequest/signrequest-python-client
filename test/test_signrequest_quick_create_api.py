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
from signrequest_python_client.api.signrequest_quick_create_api import SignrequestQuickCreateApi  # noqa: E501
from signrequest_python_client.rest import ApiException


class TestSignrequestQuickCreateApi(unittest.TestCase):
    """SignrequestQuickCreateApi unit test stubs"""

    def setUp(self):
        self.api = signrequest_python_client.api.signrequest_quick_create_api.SignrequestQuickCreateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_signrequest_quick_create_create(self):
        """Test case for signrequest_quick_create_create

        Quick create a SignRequest  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()