import unittest
import sys
sys.path.append('../src')
from unittest.mock import MagicMock
from filepathhandler import FilePathHandler


class TestFilePathHandler(unittest.TestCase):
    def setUp(self):
        self.set_up_object_under_test()

    def test_file_name_is_appended_to_base_path(self):
        path = self.handler.generate_path('file.name')
        self.assertEqual('base path/file.name', path)

    def test_simple_file_path_is_appended_to_base_path(self):
        path = self.handler.generate_path('folder/simple.path')
        self.assertEqual('base path/folder/simple.path', path)

    def test_path_handler_does_no_path_validation(self):
        path = self.handler.generate_path('/../!!!.path')
        self.assertEqual('base path/../!!!.path', path)

    def test_missing_paths_become_index(self):
        path = self.handler.generate_path('')
        self.assertEqual('base path/index.html', path)

    def test_root_paths_become_index(self):
        path = self.handler.generate_path('/')
        self.assertEqual('base path/index.html', path)

    # Support code

    def set_up_object_under_test(self):
        self.handler = FilePathHandler('base path')

