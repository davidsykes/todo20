import unittest
import sys
sys.path.append('../src')
#sys.path.append('../../temperatures/Library/src')
from unittest.mock import MagicMock
from filepathhandler import FilePathHandler


class TestFilePathHandler(unittest.TestCase):
    def setUp(self):
#        self.set_up_mocks()
#        self.set_up_data()
        self.set_up_object_under_test()
#        self.set_up_expectations()

    def test_simple_file_name_is_appended_to_base_path(self):
        path = self.handler.generate_path('simple.path')
        self.assertEqual('base path/simple.path', path)

    def test_simple_file_path_is_appended_to_base_path(self):
        path = self.handler.generate_path('folder/simple.path')
        self.assertEqual('base path/folder/simple.path', path)

    def test_leading_dots_are_rejected(self):
        with self.assertRaises(Exception) as ctx:
            self.handler.generate_path('../simple.path')
        self.assertEqual('Not Found: ../simple.path', str(ctx.exception))

    def test_middle_dots_are_rejected(self):
        with self.assertRaises(Exception) as ctx:
            self.handler.generate_path('f/../simple.path')
        self.assertEqual('Not Found: f/../simple.path', str(ctx.exception))

    def test_anything_with_leading_slashes_is_rejected(self):
        with self.assertRaises(Exception) as ctx:
            self.handler.generate_path('/folder/simple.path')
        self.assertEqual('Not Found: /folder/simple.path', str(ctx.exception))

    def test_only_simple_characters_are_accepted(self):
        with self.assertRaises(Exception) as ctx:
            self.handler.generate_path('~/folder/simple.path')
        self.assertEqual('Not Found: ~/folder/simple.path', str(ctx.exception))

    # Support code

    # def set_up_mocks(self):
    #     self.factory = Factory()
    #     self.mock_url_dissector = MagicMock()
    #     self.mock_url_dissector.dissect_url = MagicMock()
    #     self.factory.register('UrlDissector', self.mock_url_dissector)
    #     self.mock_url_router = MagicMock()
    #     self.factory.register('UrlRouter', self.mock_url_router)

    # def set_up_data(self):
    #     self.url = 'test url'
    #     self.http_request = 'http request'
    #     self.dissected_url = 'dissected url'

    def set_up_object_under_test(self):
        self.handler = FilePathHandler('base path')

    # def set_up_expectations(self):
    #     self.mock_url_dissector.dissect_url.side_effect = self.dissect_url

    # def dissect_url(self, url):
    #     if url == self.url:
    #         return self.dissected_url
    #     else:
    #         return 'something else'