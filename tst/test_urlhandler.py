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
        self.handler.get(self.url, self.mock_http_server)
        self.mock_url_dissector.dissect_url.assert_called_once_with(self.url)

    def test_get_passes_disector_response_and_server_to_router(self):
        self.handler.get(self.url, self.mock_http_server)
        self.mock_url_router.get.assert_called_once_with(self.dissected_url, self.mock_http_server)

    # Support code

    def set_up_mocks(self):
        self.factory = Factory()
        self.mock_http_server = MagicMock()
        self.mock_url_dissector = MagicMock()
        self.mock_url_dissector.dissect_url = MagicMock()
        self.factory.register('UrlDissector', self.mock_url_dissector)
        self.mock_url_router = MagicMock()
        self.factory.register('UrlRouter', self.mock_url_router)

    def set_up_data(self):
        self.url = 'test url'
        self.dissected_url = 'dissected url'

    def set_up_object_under_test(self):
        self.handler = UrlHandler(self.factory)

    def set_up_expectations(self):
        self.mock_url_dissector.dissect_url.side_effect = self.dissect_url

    def dissect_url(self, url):
        if url == self.url:
            return self.dissected_url
        else:
            return 'something else'