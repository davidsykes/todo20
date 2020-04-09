import unittest
import sys
sys.path.append('../src')
sys.path.append('../../../../temperatures/Library/src')
from unittest.mock import MagicMock
from godaddytaskmerger import GoDaddyTaskMerger
from factory import Factory

class TestGoDaddyTaskMerger(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_data()
        self.set_up_object_under_test()
        self.set_up_expectations()

    def test_merge_checks_if_godaddy_id_already_exists(self):
        self.merger.merge_godaddy_task(self.godaddy_task)

        self.mock_task_access.retrieve_godaddy_task.assert_called_once_with(42)

    def test_if_task_does_not_exist_it_is_created(self):
        self.set_up_task_as_new()

        self.merger.merge_godaddy_task(self.godaddy_task)

        self.assertEqual(self.expected_created_task, self.created_task)

    def test_if_task_does_exist_it_is_created(self):
        self.set_up_existing_task(self.existing_task)

        self.merger.merge_godaddy_task(self.godaddy_task)

        self.mock_task_access.create_task.assert_not_called()

    # Support code

    def set_up_mocks(self):
        self.factory = Factory()
        self.mock_task_access = MagicMock()
        self.factory.register('TaskDataAccess', self.mock_task_access)

    def set_up_data(self):
        self.godaddy_task = {'Done': '0', 'Title': 'Task Title', 'Position': '1.23', 'Id': '42', 'Contexts': '101', 'Detail': 'Task Detail', 'Due': '15/3/2020 12:34:56 PM', 'Ordered': '0'}
        self.expected_created_task = {'Done': '0', 'Title': 'Task Title', 'Position': '1.23', 'GoDaddyId': '42', 'Contexts': '101', 'Detail': 'Task Detail', 'Due': '15/3/2020 12:34:56 PM', 'Ordered': '0'}
        self.existing_task = {}

    def set_up_object_under_test(self):
        self.merger = GoDaddyTaskMerger(self.factory)

    def set_up_expectations(self):
        self.mock_task_access.create_task = MagicMock(side_effect = self.create_task)

    def set_up_task_as_new(self):
        self.mock_task_access.retrieve_godaddy_task = MagicMock(return_value = None)
    
    def set_up_existing_task(self, task):
        self.mock_task_access.retrieve_godaddy_task = MagicMock(return_value = task)

    def create_task(self, task):
        self.created_task = task

