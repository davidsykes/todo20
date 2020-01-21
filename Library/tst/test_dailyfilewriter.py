import unittest
import sys
import datetime
sys.path.append('../src')
sys.path.append('../../../temperatures/Library/src')
from unittest.mock import MagicMock
from factory import Factory
from dailyfilewriter import DailyFileWriter


class TestDailyFileWriter(unittest.TestCase):

    def setUp(self):
        self.set_up_mocks()
        self.set_up_expectations()
        self.set_up_object_under_test()

    # First Write

    def test_first_write_requests_current_date(self):
        self.writer.write('text')
        self.mock_datetime.now.assert_called_once()

    def test_first_write_opens_logfile_with_dated_name(self):
        self.writer.write('text')
        self.mock_fs_wrapper.open.assert_called_once_with('name_20190315.ext', 'a')

    def test_first_write_writes_log_data_to_original_opened_file(self):
        self.writer.write('text')
        self.mock_file_20190315.write.assert_called_once_with("text")

    # Second write with no date change

    def test_second_write_with_no_date_change_requests_current_date(self):
        self.writer.write('text1')
        self.writer.write('text2')
        self.assertEqual(self.mock_datetime.now.call_count, 2)

    def test_second_write_with_no_date_change_uses_original_logfile(self):
        self.writer.write('text1')
        self.writer.write('text2')
        self.assertEqual(self.mock_fs_wrapper.open.call_count, 1)
        self.mock_fs_wrapper.open.assert_called_once_with('name_20190315.ext', 'a')

    def test_second_write_with_no_date_change_writes_log_data_to_original_opened_file(self):
        self.writer.write('text1')
        self.mock_file_20190315.write.reset_mock()
        self.writer.write('text2')
        self.mock_file_20190315.write.assert_called_once_with("text2")

    # Second write with date change

    def test_second_write_with_date_change_requests_current_date(self):
        self.writer.write('text1')
        self.mock_datetime.now = MagicMock(return_value=datetime.datetime(2019,3,17,0,0,1))
        self.writer.write('text2')
        self.mock_datetime.now.assert_called_once()

    def test_second_write_with_date_opens_second_logfile(self):
        self.writer.write('text1')
        self.mock_datetime.now = MagicMock(return_value=datetime.datetime(2019,3,17,0,0,1))
        self.mock_fs_wrapper.open.reset_mock()
        self.writer.write('text2')
        self.mock_fs_wrapper.open.assert_called_once_with('name_20190317.ext', 'a')

    def test_second_write_with_date_change_writes_log_data_to_second_opened_file(self):
        self.writer.write('text1')
        self.mock_datetime.now = MagicMock(return_value=datetime.datetime(2019,3,17,0,0,1))
        self.writer.write('text2')
        self.mock_file_20190317.write.assert_called_once_with("text2")

    def second_write_with_date_change_closes_original_file(self):
        self.writer.write('text1')
        self.mock_datetime.now = MagicMock(return_value=datetime.datetime(2019,3,17,0,0,1))
        self.writer.write('text2')

        self.mock_file_20190315.close.assert_called_once()

    # Support code

    def set_up_mocks(self):
        self.factory = Factory()
        self.mock_datetime = MagicMock()
        self.factory.register('DateTimeWrapper', self.mock_datetime)
        self.mock_fs_wrapper = MagicMock()
        self.factory.register('FsWrapper', self.mock_fs_wrapper)
        self.mock_file_20190315 = MagicMock()
        self.mock_file_20190317 = MagicMock()
        #self.mock_logger_console = MagicMock()
        #self.factory.register('LoggerConsole', self.mock_logger_console)

    def set_up_object_under_test(self):
        self.writer = DailyFileWriter(self.factory, 'name', 'ext')

    def set_up_expectations(self):
        self.mock_datetime.now = MagicMock(return_value=datetime.datetime(2019,3,15,21,43,54))
        self.mock_fs_wrapper.open = MagicMock()
        self.mock_fs_wrapper.open.side_effect = self.file_open

    def file_open(self, filename, mode):
        if filename == 'name_20190315.ext' and mode == 'a':
            return self.mock_file_20190315
        elif filename == 'name_20190317.ext' and mode == 'a':
            return self.mock_file_20190317
        else:
            raise Exception('Unexpected log file name: ' + filename)
