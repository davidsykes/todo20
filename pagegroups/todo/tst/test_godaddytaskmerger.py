import unittest
import sys
import datetime
sys.path.append('../src')
sys.path.append('../../../../temperatures/Library/src')
from unittest.mock import MagicMock
from godaddytaskmerger import GoDaddyTaskMerger
from factory import Factory
from todotask import ToDoTask

class TestGoDaddyTaskMerger(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_data()
        self.set_up_object_under_test()
        self.set_up_expectations()

    def test_merge_checks_if_godaddy_id_already_exists(self):
        self.merger.merge_godaddy_task(self.godaddy_task)

        self.mock_task_access.retrieve_godaddy_task.assert_called_once_with(42)

    # Task does not exist

    def test_if_task_does_not_exist_it_is_created(self):
        self.set_up_task_as_new()
        self.merger.merge_godaddy_task(self.godaddy_task)
        self.assertEqual('Task Title', self.created_task.title)

    def test_if_task_is_created_the_creation_is_logged(self):
        self.set_up_task_as_new()
        self.merger.merge_godaddy_task(self.godaddy_task)
        self.mock_logger.log.assert_called_once_with('Created new task Task Title: Task Detail')

    # Task does exist

    def test_if_task_does_exist_it_is_not_created(self):
        self.set_up_existing_task(self.existing_task)

        self.merger.merge_godaddy_task(self.godaddy_task)

        self.mock_task_access.create_task.assert_not_called()

    #   convert_godaddy_datetime

    def test_convert_godaddy_datetime_converts_datetime_from_godaddy_data_using_mdy(self):
        dt = self.merger.convert_godaddy_datetime('3/15/2020 12:34:56 PM')
        self.assertEqual(datetime.datetime(2020, 3, 15), dt)

    def test_convert_godaddy_datetime_converts_empty_datetime_to_none(self):
        dt = self.merger.convert_godaddy_datetime('')
        self.assertIsNone(dt)

    # Support code

    def set_up_mocks(self):
        self.factory = Factory()
        self.mock_task_access = MagicMock()
        self.factory.register('TaskDataAccess', self.mock_task_access)
        self.mock_logger = MagicMock()
        self.factory.register('Logger', self.mock_logger)

    def set_up_data(self):
        self.godaddy_task = {'Done': '0', 'Title': 'Task Title', 'Position': '1.23', 'Id': '42', 'Contexts': '101', 'Detail': 'Task Detail', 'Due': '3/15/2020 12:34:56 PM', 'Ordered': '0'}
        self.existing_task = {}

    def set_up_object_under_test(self):
        self.merger = GoDaddyTaskMerger(self.factory)

    def set_up_expectations(self):
        self.mock_task_access.create_task = MagicMock(side_effect = self.create_task)

    def set_up_task_as_new(self):
        self.mock_task_access.retrieve_godaddy_task = MagicMock(return_value = [])
    
    def set_up_existing_task(self, task):
        self.mock_task_access.retrieve_godaddy_task = MagicMock(return_value = [task])

    def create_task(self, task):
        self.created_task = task

