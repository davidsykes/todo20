import unittest
import sys
sys.path.append('../src')
from unittest.mock import MagicMock
from urldissector import UrlDissector


class TestUrlDissector(unittest.TestCase):
    def setUp(self):
        self.set_up_object_under_test()

    def test_a_simple_request_is_dissected(self):
        result = self.dissector.dissect_url('/todo')
        self.assertEqual(['todo', ''], result)

    def test_sub_folders_are_dissected(self):
        result = self.dissector.dissect_url('/todo/tasks')
        self.assertEqual(['todo', 'tasks'], result)

    def test_url_with_no_leading_slash_is_accepted(self):
        result = self.dissector.dissect_url('todo/tasks')
        self.assertEqual(['todo', 'tasks'], result)

    def test_sub_sub_folders_are_not_dissected_yet(self):
        result = self.dissector.dissect_url('/todo/tasks/watev')
        self.assertEqual(['todo', 'tasks/watev'], result)

    # Support code

    def set_up_object_under_test(self):
        self.dissector = UrlDissector()
