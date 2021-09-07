# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ynab
from ynab.models.save_category_response import SaveCategoryResponse  # noqa: E501
from ynab.rest import ApiException


class TestSaveCategoryResponse(unittest.TestCase):
    """SaveCategoryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSaveCategoryResponse(self):
        """Test SaveCategoryResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ynab.models.save_category_response.SaveCategoryResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
