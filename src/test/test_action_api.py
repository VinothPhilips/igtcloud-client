"""
    IGT Cloud Action

    IGT Cloud action  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import igtcloud.client.services.action
from igtcloud.client.services.action.api.action_api import ActionApi  # noqa: E501


class TestActionApi(unittest.TestCase):
    """ActionApi unit test stubs"""

    def setUp(self):
        self.api = ActionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_preprocess_file(self):
        """Test case for post_preprocess_file

        """
        pass

    def test_post_update_database(self):
        """Test case for post_update_database

        """
        pass


if __name__ == '__main__':
    unittest.main()