import sys
import traceback
sys.path.append('../../../src')
sys.path.append('../../../../temperatures/Library/src')

from urlparser import UrlParser
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

class TickTackToePageGroup(object):
    def __init__(self, www_path):
        self.factory = Factory()
        self.factory.register('DateTimeWrapper', DateTimeWrapper())
        self.factory.register('FsWrapper', FsWrapper())
        self.urlparser = UrlParser()
        self.filepathhandler = FilePathHandler(www_path)

        daily_log_writer = DailyFileWriter(self.factory, DAILY_LOG_NAME, DAILY_LOG_EXT)
        daily_err_writer = DailyFileWriter(self.factory, DAILY_LOG_NAME, DAILY_ERR_EXT)
        daily_logger = Logger(self.factory, daily_log_writer, daily_err_writer)
        self.logger = LogChainer(daily_logger)
        self.logger.chain(ConsoleLogger(True))

    def process_request(self, page_group_url, request):
        try:
            print('ttt request', page_group_url, '||||', request)
            rest = self.urlparser.parse_url(request.url)
            if (rest):
                pass
                return

            path = self.filepathhandler.generate_path(page_group_url)
            request.server.write_file(path)

        except Exception as e:
            self.logger.log('Exception: %s' % (str(e)))
            self.logger.log('Path: %s' % (request.url))
            self.logger.log('Stack: %s' % (traceback.format_exc(10)))

            request.server.write_text_response(500, 'exception')
