import unittest
import sys
sys.path.append('../src')
sys.path.append('../../temperatures/Library/src')
from unittest.mock import MagicMock
from urlhandler import UrlHandler
from factory import Factory


class TestUrlRouter(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_data()
        self.set_up_object_under_test()
        self.set_up_expectations()

    def test_get_passes_url_to_url_disector(self):
        self.handler.handle_request(self.url, self.http_request)
        self.mock_url_dissector.dissect_url.assert_called_once_with(self.url)

    def test_get_passes_disector_response_and_request_to_router(self):
        self.handler.handle_request(self.url, self.http_request)
        self.mock_url_router.route_request.assert_called_once_with(self.dissected_url, self.http_request)

    def test_failed_dissections_are_passed_to_the_logger(self):
        self.handler.handle_request('invalid url', self.http_request)
        self.mock_logger.log.assert_called_once_with('Invalid URL: invalid url')

    # Support code

    def set_up_mocks(self):
        self.factory = Factory()
        self.mock_url_dissector = MagicMock()
        self.mock_url_dissector.dissect_url = MagicMock()
        self.factory.register('UrlDissector', self.mock_url_dissector)
        self.mock_url_router = MagicMock()
        self.factory.register('UrlRouter', self.mock_url_router)
        self.mock_logger = MagicMock()
        self.mock_logger.log = MagicMock()
        self.factory.register('Logger', self.mock_logger)

    def set_up_data(self):
        self.url = 'test url'
        self.http_request = 'http request'
        self.dissected_url = 'dissected url'

    def set_up_object_under_test(self):
        self.handler = UrlHandler(self.factory)

    def set_up_expectations(self):
        self.mock_url_dissector.dissect_url.side_effect = self.dissect_url

    def dissect_url(self, url):
        if url == self.url:
            return self.dissected_url
        else:
            return None