import unittest
import sys
sys.path.append('../src')
from unittest.mock import MagicMock
from urldissector import UrlDissector


class TestUrlDissector(unittest.TestCase):
    def setUp(self):
        self.set_up_object_under_test()

    def test_a_simple_request_is_dissected(self):
        result = self.dissector.dissect('/todo/tasks')
        self.assertEqual(['todo', 'tasks'], result)

    def test_double_slashes_fail(self):
        result = self.dissector.dissect('//todo/tasks')
        self.assertIsNone(result)

    def test_non_lowercase_fails(self):
        result = self.dissector.dissect('/tOdo/tasks')
        self.assertIsNone(result)

    # Support code

    def set_up_object_under_test(self):
        self.dissector = UrlDissector()
