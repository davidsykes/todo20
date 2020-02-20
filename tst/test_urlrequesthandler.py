import unittest
import sys
sys.path.append('../src')
sys.path.append('../../temperatures/Library/src')
from unittest.mock import MagicMock
from urlrequesthandler import UrlRequestHandler
from factory import Factory


class TestUrlRequestHandler(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_data()
        self.set_up_object_under_test()
        self.set_up_expectations()

    def test_handle_request_passes_url_to_url_validator(self):
        self.handler.handle_request(self.url, self.http_request)
        self.mock_url_validator.validate_url.assert_called_once_with(self.url)

    def test_handle_request_passes_url_to_url_disector(self):
        self.handler.handle_request(self.url, self.http_request)
        self.mock_pagegroup_extractor.extract_pagegroup.assert_called_once_with(self.url)

    def test_handle_request_passes_disector_response_and_request_to_router(self):
        self.handler.handle_request(self.url, self.http_request)
        self.mock_url_router.route_request.assert_called_once_with(self.extracted_pagegroup, self.http_request)

    # Support code

    def set_up_mocks(self):
        self.factory = Factory()
        self.mock_url_validator = MagicMock()
        self.factory.register('UrlValidator', self.mock_url_validator)
        self.mock_pagegroup_extractor = MagicMock()
        self.factory.register('UrlPagegroupExtractor', self.mock_pagegroup_extractor)
        self.mock_url_router = MagicMock()
        self.factory.register('UrlRouter', self.mock_url_router)

    def set_up_data(self):
        self.url = 'test url'
        self.http_request = 'http request'
        self.extracted_pagegroup = 'extracted page group'

    def set_up_object_under_test(self):
        self.handler = UrlRequestHandler(self.factory)

    def set_up_expectations(self):
        self.mock_pagegroup_extractor.extract_pagegroup.side_effect = self.extract_pagegroup

    def extract_pagegroup(self, url):
        if url == self.url:
            return self.extracted_pagegroup
        else:
            return None