import sys
import traceback
import sqlite3
import json
sys.path.append('../../../src')
sys.path.append('../../../Library/src')

from filepathhandler import FilePathHandler
from staticfactory import StaticFactory
from logger import Logger
from logchainer import LogChainer
from dailyfilewriter import DailyFileWriter
from datetime_wrapper import DateTimeWrapper
from fs_wrapper import FsWrapper
from console_logger import ConsoleLogger
from restcommandparser import RestCommandParser
from taskreloader import TaskReloader
from godaddytaskretriever import GoDaddyTaskRetriever
from godaddytaskmerger import GoDaddyTaskMerger
from godaddytasksmerger import GoDaddyTasksMerger
from todotasks import ToDoTasks
from taskdataaccess import TaskDataAccess
from sqlite_database import SQLiteDatabase
from migration_runner import MigrationRunner
from taskconverter import TaskConverter

DAILY_LOG_NAME = 'todopageslog'
DAILY_LOG_EXT = 'log'
DAILY_ERR_EXT = 'err'

class ToDoPagegroup(object):
    def __init__(self, configurations):
        www_path = configurations['WWWPath']
        self.factory = StaticFactory.initialise_factory()

        self.factory.register('DateTimeWrapper', DateTimeWrapper())
        self.factory.register('FsWrapper', FsWrapper())
        self.set_up_database(configurations['DatabasePath'], configurations['MigrationsPath'])
        self.factory.register('ToDoTasks', ToDoTasks())
        self.taskdataaccess = TaskDataAccess(self.factory)
        self.factory.register('TaskDataAccess', self.taskdataaccess)
        self.factory.register('GoDaddyTaskRetriever', GoDaddyTaskRetriever())
        self.restcommandparser = RestCommandParser()
        self.filepathhandler = FilePathHandler(www_path)

        daily_log_writer = DailyFileWriter(self.factory, DAILY_LOG_NAME, DAILY_LOG_EXT)
        daily_err_writer = DailyFileWriter(self.factory, DAILY_LOG_NAME, DAILY_ERR_EXT)
        daily_logger = Logger(self.factory, daily_log_writer, daily_err_writer)
        self.logger = LogChainer(daily_logger)
        self.logger.chain(ConsoleLogger(True))
        self.factory.register('Logger', self.logger)

        self.factory.register('TaskConverter', TaskConverter())
        self.factory.register('GoDaddyTaskMerger', GoDaddyTaskMerger(self.factory))
        self.factory.register('GoDaddyTasksMerger', GoDaddyTasksMerger(self.factory))
        self.tesk_reloader = TaskReloader(self.factory)

    def set_up_database(self, database_path, migrations_folder_path):
        try:
            database = SQLiteDatabase(sqlite3.connect(database_path, check_same_thread = False))
            self.factory.register('Database', database)
            migration_runner = MigrationRunner(self.factory, migrations_folder_path)
            migration_runner.run_migrations()
        except Exception as e:
            print("Exception setting up database '%s'" % (database_path))
            raise

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
            self.tesk_reloader.reload_tasks()
            request.server.server_response_json(self.fetch_current_tasks_as_json())
        else:
            request.server.server_response_json(self.fetch_current_tasks_as_json())

    def fetch_current_tasks_as_json(self):
        tasks = self.taskdataaccess.retrieve_current_tasks()
        tasks_dictionary = ToDoTasks.task_objects_to_dictionaries(tasks)
        return json.dumps(tasks_dictionary)
