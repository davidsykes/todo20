import unittest
import sys
import datetime
sys.path.append('../src')
from unittest.mock import MagicMock
from logger import Logger
from factory import Factory


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_expectations()
        self.set_up_object_under_test()

    def test_log_message_is_passed_to_first_writer(self):
        self.logger.log('message')
        self.assertEqual(1, self.mock_writer1.write.call_count)

    def test_log_message_prefixes_date_and_time_and_appends_lf(self):
        self.logger.log('message')
        self.mock_writer1.write.assert_called_with("2019-03-15 21:43:54: message\n")

    def test_error_message_is_passed_to_second_writer(self):
        self.logger.error('message')
        self.assertEqual(1, self.mock_writer2.write.call_count)

    def test_error_message_prefixes_date_and_time_and_appends_lf(self):
        self.logger.error('message')
        self.mock_writer2.write.assert_called_with("2019-03-15 21:43:54: message\n")

    # Support code

    def set_up_mocks(self):
        self.mock_writer1 = MagicMock()
        self.mock_writer2 = MagicMock()
        self.factory = Factory()
        self.mock_datetime = MagicMock()
        self.factory.register('DateTimeWrapper', self.mock_datetime)

    def set_up_expectations(self):
        self.mock_datetime.now = MagicMock(return_value=datetime.datetime(2019,3,15,21,43,54))

    def set_up_object_under_test(self):
        self.logger = Logger(self.factory, self.mock_writer1, self.mock_writer2)

