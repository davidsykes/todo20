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
from restcommandparser import RestCommandParser
from taskreloader import TaskReloader

DAILY_LOG_NAME = 'todopageslog'
DAILY_LOG_EXT = 'log'
DAILY_ERR_EXT = 'err'

class ToDoPagegroup(object):
    def __init__(self, www_path):
        self.factory = Factory()
        self.factory.register('DateTimeWrapper', DateTimeWrapper())
        self.factory.register('FsWrapper', FsWrapper())
        self.restcommandparser = RestCommandParser()
        self.filepathhandler = FilePathHandler(www_path)
        self.tesk_reloader = TaskReloader()

        daily_log_writer = DailyFileWriter(self.factory, DAILY_LOG_NAME, DAILY_LOG_EXT)
        daily_err_writer = DailyFileWriter(self.factory, DAILY_LOG_NAME, DAILY_ERR_EXT)
        daily_logger = Logger(self.factory, daily_log_writer, daily_err_writer)
        self.logger = LogChainer(daily_logger)
        self.logger.chain(ConsoleLogger(True))

    def process_request(self, pagegroup_url, request):
        self.logger.log('ToDo request: %s' % pagegroup_url)
        command = self.restcommandparser.parse_rest_command(pagegroup_url)
        if command is not None:
            self.handle_command(request, command)
        else:
            path = self.filepathhandler.generate_path(pagegroup_url)
            request.server.write_file(path)

    def handle_command(self, request, command):
        if command.Command == 'reloadtasks':
            self.tesk_reloader.reload_tasks
        else:
            request.server.server_response_json('[{"task":"do"},{"task":"something"}]')
