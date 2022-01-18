"""
    Apis

    IGT Cloud entities  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import igtcloud.client.services.entities
from igtcloud.client.services.entities.model.annotation_series import AnnotationSeries
from igtcloud.client.services.entities.model.core_labs_series import CoreLabsSeries
from igtcloud.client.services.entities.model.echo_nav_series import EchoNavSeries
from igtcloud.client.services.entities.model.igt_cloud_series import IgtCloudSeries
from igtcloud.client.services.entities.model.marvel_series import MarvelSeries
from igtcloud.client.services.entities.model.we_trust_series import WeTrustSeries
globals()['AnnotationSeries'] = AnnotationSeries
globals()['CoreLabsSeries'] = CoreLabsSeries
globals()['EchoNavSeries'] = EchoNavSeries
globals()['IgtCloudSeries'] = IgtCloudSeries
globals()['MarvelSeries'] = MarvelSeries
globals()['WeTrustSeries'] = WeTrustSeries
from igtcloud.client.services.entities.model.series import Series


class TestSeries(unittest.TestCase):
    """Series unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSeries(self):
        """Test Series"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Series()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()