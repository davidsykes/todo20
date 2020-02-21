import sys
import traceback
sys.path.append('../../../src')
sys.path.append('../../../../temperatures/Library/src')

from filepathhandler import FilePathHandler
from factory import Factory
from logger import Logger
from logchainer import LogChainer
from dailyfilewriter import DailyFileWriter
from datetime_wrapper import DateTimeWrapper
from fs_wrapper import FsWrapper
from console_logger import ConsoleLogger

DAILY_LOG_NAME = 'tttpageslog'
DAILY_LOG_EXT = 'log'
DAILY_ERR_EXT = 'err'

class TickTackToePagegroup(object):
    def __init__(self, www_path):
        self.factory = Factory()
        self.factory.register('DateTimeWrapper', DateTimeWrapper())
        self.factory.register('FsWrapper', FsWrapper())
        self.filepathhandler = FilePathHandler(www_path)

        daily_log_writer = DailyFileWriter(self.factory, DAILY_LOG_NAME, DAILY_LOG_EXT)
        daily_err_writer = DailyFileWriter(self.factory, DAILY_LOG_NAME, DAILY_ERR_EXT)
        daily_logger = Logger(self.factory, daily_log_writer, daily_err_writer)
        self.logger = LogChainer(daily_logger)
        self.logger.chain(ConsoleLogger(True))

    def process_request(self, pagegroup_url, request):
        try:
            path = self.filepathhandler.generate_path(pagegroup_url)
            request.server.write_file(path)

        except Exception as e:
            self.logger.log('Exception: %s' % (str(e)))
            self.logger.log('Path: %s' % (request.url))
            self.logger.log('Stack: %s' % (traceback.format_exc(10)))

            request.server.server_response_text(500, 'exception')
