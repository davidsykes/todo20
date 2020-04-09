import unittest
import sys
import datetime
sys.path.append('../src')
sys.path.append('../../../../temperatures/Library/src')
from unittest.mock import MagicMock
from taskdataaccess import TaskDataAccess
from factory import Factory
from todotask import ToDoTask


class TestTaskDataAccess(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_data()
        self.set_up_object_under_test()
        self.set_up_expectations()

    # create_task

    def test_create_task_creates_new_task(self):
        self.task_data_access.create_task(self.task)

        self.mock_sqlite_database.execute_with_commit.assert_called_with(self.create_task_sql)

    # Retrieve go daddy task

    def test_retrieve_godaddy_task_retrieves_godaddy_task(self):
        self.task_data_access.retrieve_godaddy_task(123)

        query = 'SELECT ' + self.task_fields + 'FROM Tasks WHERE GoDaddyId=123'

        self.mock_sqlite_database.query.assert_called_with(query)

    # Support code

    def set_up_mocks(self):
        self.factory = Factory()
        self.mock_sqlite_database = MagicMock()
        self.factory.register('Database', self.mock_sqlite_database)

    def set_up_data(self):
        self.task_fields = 'Title, Detail, Done, Due, Contexts, Position, GoDaddyId'
        self.task = ToDoTask.create_task('Task Title', 'Task Detail')
        self.task.position = 1.23
        self.task.godaddy_id = 42
        self.task.contexts = '101'
        self.task.due = datetime.datetime(2020, 3, 15, 12, 34, 56)
        self.create_task_sql = "INSERT INTO Tasks (" + self.task_fields + ") VALUES ('Task Title','Task Detail',0,2020-03-15 12:34:56,'101',1.230000,42)"

    def set_up_object_under_test(self):
        self.task_data_access = TaskDataAccess(self.factory)

    def set_up_expectations(self):
        pass


