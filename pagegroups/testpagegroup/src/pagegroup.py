import sys
import traceback
sys.path.append('../../../src')
sys.path.append('../../../../temperatures/Library/src')

from urlparser import UrlParser
from filepathhandler import FilePathHandler
from factory import Factory
from logchainer import LogChainer
from daily_file_logger import DailyFileLogger
from datetime_wrapper import DateTimeWrapper
from fs_wrapper import FsWrapper
from console_logger import ConsoleLogger

DAILY_LOG_NAME = 'testpageslog'
DAILY_LOG_EXT = 'log'
WEB_PATH = '~/Documents/todo20/pagegroups/testpagegroup/pages'

class TestPageGroup(object):
    def __init__(self):
        self.factory = Factory()
        self.factory.register('DateTimeWrapper', DateTimeWrapper())
        self.factory.register('FsWrapper', FsWrapper())
        self.urlparser = UrlParser()
        self.filepathhandler = FilePathHandler(WEB_PATH)
        self.logger = LogChainer(DailyFileLogger(self.factory, DAILY_LOG_NAME, DAILY_LOG_EXT))
        self.logger.chain(ConsoleLogger(True))

    def process_request(self, request):
        try:
            rest = self.urlparser.parse_url(request.url)
            if (rest):
                pass
                return

            path = self.filepathhandler.generate_path(request.url)
            request.server.write_file(path)

        except Exception as e:
            self.logger.log('Exception: %s' % (str(e)))
            self.logger.log('Path: %s' % (request.url))
            self.logger.log('Stack: %s' % (traceback.format_exc(10)))

            request.server.write_text_response(500, 'exception')