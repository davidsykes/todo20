import unittest
import sys
sys.path.append('../src')
sys.path.append('../../../../temperatures/Library/src')
from unittest.mock import MagicMock
from godaddytasksmerger import GoDaddyTasksMerger
from factory import Factory

class TestGoDaddyTasksMerger(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_data()
        self.set_up_object_under_test()
        self.set_up_expectations()

    def test_tasksmergerpassesalltaskstotaskmerger(self):
        self.tasks_merger.merge_godaddy_tasks(self.tasks)
        self.assertEqual(self.merged_tasks, self.tasks)

    # Support code

    def set_up_mocks(self):
        self.factory = Factory()
        self.mock_task_merger = MagicMock()
        self.mock_task_merger.merge_godaddy_task = MagicMock(side_effect = self.add_task)
        self.factory.register('GoDaddyTaskMerger', self.mock_task_merger)

    def set_up_data(self):
        self.tasks = ['task1', 'task2', 'task3']
        self.merged_tasks = []

    def set_up_object_under_test(self):
        self.tasks_merger = GoDaddyTasksMerger(self.factory)

    def set_up_expectations(self):
        pass

    def add_task(self, task):
        self.merged_tasks.append(task)

