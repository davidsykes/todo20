import unittest
import sys
sys.path.append('../src')
from unittest.mock import MagicMock
from urlvalidator import UrlValidator


class TestUrlSanitiser(unittest.TestCase):
    def setUp(self):
        self.set_up_object_under_test()

    def test_lowercase_characters_are_allowed(self):
        url = 'abcdefghijklmnopqrstuvwxyz'
        self.assertTrue(self.validator.CheckUrl(url))

    def set_up_object_under_test(self):
        self.validator = UrlValidator()

