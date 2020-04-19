import unittest
import sys
import datetime
sys.path.append('../src')
sys.path.append('../../../Library/src')
from unittest.mock import MagicMock
from taskdataaccess import TaskDataAccess
from staticfactory import StaticFactory
from todotask import ToDoTask
from todotasks import ToDoTasks
from taskconverter import TaskConverter


class TestTaskDataAccess(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_data()
        self.set_up_object_under_test()
        self.set_up_expectations()

    # create_task

    def test_create_task_creates_new_task(self):
        task = TaskConverter.db_task_to_task((None,'Task Title','Task Detail',0,datetime.datetime(2020,3,15,12,34,56),'101',1.23,42))
        self.task_data_access.create_task(task)

        self.assertEqual(self.sql_to_create_task, self.sqlite_database_execute_with_commit_query)
        expected_params = ('Task Title','Task Detail',0,datetime.datetime(2020,3,15,12,34,56),'101',1.23,42)
        self.assertEqual(expected_params, self.sqlite_database_execute_with_commit_params)

    # Retrieve go daddy task

    def test_retrieve_godaddy_task_retrieves_godaddy_task(self):
        self.task_data_access.retrieve_godaddy_task(123)

        query = 'SELECT ' + self.retrieve_task_fields + ' FROM Tasks WHERE GoDaddyId=123'

        self.mock_sqlite_database.query.assert_called_with(query)

    # Retrieve current tasks

    def test_retrieve_current_tasks_retrieves_tasks_due_before_today(self):
        self.task_data_access.retrieve_current_tasks()

        query = 'SELECT ' + self.retrieve_task_fields + " FROM Tasks WHERE Done=0 AND (Due IS NULL OR Due < Date('now'))"

        self.mock_sqlite_database.query.assert_called_with(query)

    def test_retrieve_current_tasks_converts_db_tasks_into_tasks(self):
        self.mock_sqlite_database.query = MagicMock(return_value = 'db tasks')
        self.mock_todotasks.db_tasks_to_task_objects = MagicMock(side_effect = self.db_tasks_to_task_objects)
        
        tasks = self.task_data_access.retrieve_current_tasks()

        self.assertEqual('tasks as objects', tasks)

    def db_tasks_to_task_objects(self, db_tasks):
        return 'tasks as objects' if db_tasks == 'db tasks' else None

    # Support code

    def set_up_mocks(self):
        self.factory = StaticFactory.initialise_factory()
        self.mock_sqlite_database = MagicMock()
        self.factory.register('Database', self.mock_sqlite_database)
        self.mock_todotasks = MagicMock()
        self.factory.register('ToDoTasks', self.mock_todotasks)

    def set_up_data(self):
        self.create_task_fields = 'Title, Detail, Done, Due, Contexts, Position, GoDaddyId'
        self.sql_to_create_task = 'INSERT INTO Tasks (' + self.create_task_fields + ') VALUES (?,?,?,?,?,?,?)'
        self.retrieve_task_fields = 'TaskId, Title, Detail, Done, Due, Contexts, Position, GoDaddyId'

    def set_up_object_under_test(self):
        self.task_data_access = TaskDataAccess(self.factory)

    def set_up_expectations(self):
        self.mock_sqlite_database.execute_with_commit = MagicMock(side_effect = self.sqlite_database_execute_with_commit)
    
    def sqlite_database_execute_with_commit(self, sql, params):
        self.sqlite_database_execute_with_commit_query = sql
        self.sqlite_database_execute_with_commit_params = params        

    def task_converter_db_to_dictionary(self, task):
        self.task_converter_db_to_dictionary_converted_tasks.append(task)        

