import unittest
import sys
sys.path.append('../src')
from unittest.mock import MagicMock
from urlpagegroupextractor import UrlPagegroupExtractor


class TestUrlPagegroupExtractor(unittest.TestCase):
    def setUp(self):
        self.set_up_object_under_test()

    def test_a_simple_pagegroup_is_extracted(self):
        result = self.pagegroup_extractor.extract_pagegroup('/todo')
        self.assertEqual(['todo', ''], result)

    def test_sub_folders_are_extracted(self):
        result = self.pagegroup_extractor.extract_pagegroup('/todo/tasks')
        self.assertEqual(['todo', 'tasks'], result)

    def test_url_with_no_leading_slash_is_accepted(self):
        result = self.pagegroup_extractor.extract_pagegroup('todo/tasks')
        self.assertEqual(['todo', 'tasks'], result)

    def test_sub_sub_folders_are_not_extracted_yet(self):
        result = self.pagegroup_extractor.extract_pagegroup('/todo/tasks/watev')
        self.assertEqual(['todo', 'tasks/watev'], result)

    # Support code

    def set_up_object_under_test(self):
        self.pagegroup_extractor = UrlPagegroupExtractor()
