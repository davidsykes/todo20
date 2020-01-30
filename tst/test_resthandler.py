import unittest
import sys
sys.path.append('../src')
sys.path.append('../../temperatures/Library/src')
from unittest.mock import MagicMock
from resthandler import RestHandler
from factory import Factory


class TestRestHandler(unittest.TestCase):
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
        self.mock_url_dissector.dissect_url.assert_called_once_with(self.url)

    def test_handle_request_passes_disector_response_and_request_to_router(self):
        self.handler.handle_request(self.url, self.http_request)
        self.mock_url_router.route_request.assert_called_once_with(self.dissected_url, self.http_request)

    # Support code

    def set_up_mocks(self):
        self.factory = Factory()
        self.mock_url_validator = MagicMock()
        #self.mock_url_validator.validate_url = MagicMock()
        self.factory.register('UrlValidator', self.mock_url_validator)
        self.mock_url_dissector = MagicMock()
        #self.mock_url_dissector.dissect_url = MagicMock()
        self.factory.register('UrlDissector', self.mock_url_dissector)
        self.mock_url_router = MagicMock()
        self.factory.register('UrlRouter', self.mock_url_router)

    def set_up_data(self):
        self.url = 'test url'
        self.http_request = 'http request'
        self.dissected_url = 'dissected url'

    def set_up_object_under_test(self):
        self.handler = RestHandler(self.factory)

    def set_up_expectations(self):
        self.mock_url_dissector.dissect_url.side_effect = self.dissect_url

    def dissect_url(self, url):
        if url == self.url:
            return self.dissected_url
        else:
            return None