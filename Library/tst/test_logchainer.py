import unittest
import sys
sys.path.append('../src')
from unittest.mock import MagicMock
from logchainer import LogChainer


class TestLogChainer(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_object_under_test()

    def test_log_message_is_passed_to_all_chained_loggers(self):
        self.chainer.log('message')
        self.logger1.log.assert_called_once_with('message')
        self.logger2.log.assert_called_once_with('message')

    def test_error_message_is_passed_to_all_chained_loggers(self):
        self.chainer.error('message')
        self.logger1.error.assert_called_once_with('message')
        self.logger2.error.assert_called_once_with('message')

    # Support code

    def set_up_mocks(self):
        self.logger1 = MagicMock()
        self.logger2 = MagicMock()

    def set_up_object_under_test(self):
        self.chainer = LogChainer(self.logger1)
        self.chainer.chain(self.logger2)

