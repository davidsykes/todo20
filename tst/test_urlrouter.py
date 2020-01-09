import unittest
import sys
sys.path.append('../src')
sys.path.append('../../temperatures/Library/src')
from unittest.mock import MagicMock
from urlrouter import UrlRouter


class TestUrlRouter(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_data()
        self.set_up_object_under_test()

    def test_blank_requests_are_send_to_default_destination(self):
        self.router.route_request(None, self.request)
        self.mock_default_destination.process_request.assert_called_once_with(self.request)

    # Support code

    def set_up_mocks(self):
        self.mock_default_destination = MagicMock()

    def set_up_data(self):
        self.request = 'http request'

    def set_up_object_under_test(self):
        self.router = UrlRouter(self.mock_default_destination)
