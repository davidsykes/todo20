import unittest
import sys
sys.path.append('../src')
from unittest.mock import MagicMock
from urlvalidator import UrlValidator


class TestUrlValidator(unittest.TestCase):
    def setUp(self):
        self.set_up_object_under_test()

    def test_a_simple_url_passes(self):
        try:
            self.validator.validate_url('/url')
        except Exception:
            self.fail("myFunc() raised ExceptionType unexpectedly!")

    def test_alphanumerics_pass(self):
        try:
            self.validator.validate_url('/urlURL1234')
        except Exception:
            self.fail("myFunc() raised ExceptionType unexpectedly!")

    def test_double_slashes_fail(self):
        with self.assertRaises(Exception) as ctx:
            self.validator.validate_url('//todo/tasks')
        self.assertEqual('Invalid URL: //todo/tasks', str(ctx.exception))

    def test_leading_dots_fail(self):
        with self.assertRaises(Exception) as ctx:
            self.validator.validate_url('../todo/./tasks')
        self.assertEqual('Invalid URL: ../todo/./tasks', str(ctx.exception))

    def test_any_dots_fail(self):
        with self.assertRaises(Exception) as ctx:
            self.validator.validate_url('/todo/./tasks')
        self.assertEqual('Invalid URL: /todo/./tasks', str(ctx.exception))

    def test_non_alphanumeric_fails(self):
        with self.assertRaises(Exception) as ctx:
            self.validator.validate_url('/t!do/tasks')
        self.assertEqual('Invalid URL: /t!do/tasks', str(ctx.exception))

    # Support code

    def set_up_object_under_test(self):
        self.validator = UrlValidator()
