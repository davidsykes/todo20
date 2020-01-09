import unittest
import sys
sys.path.append('../src')
from unittest.mock import MagicMock
#from factory import Factory
from urlsanitiser import UrlSanitiser


class TestUrlSanitiser(unittest.TestCase):
    def setUp(self):
        self.set_up_object_under_test()

    def test_lowercase_characters_are_allowed(self):
        url = 'abcdefghijklmnopqrstuvwxyz'
        self.assertTrue(self.sanitiser.CheckUrl(url))

    def set_up_object_under_test(self):
        self.sanitiser = UrlSanitiser()

