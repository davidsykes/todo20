import unittest
import sys
sys.path.append('../src')
sys.path.append('../../../../temperatures/Library/src')
from unittest.mock import MagicMock
from factory import Factory
from taskreloader import TaskReloader


class TestClassToTest(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_data()
        self.set_up_object_under_test()
        self.set_up_expectations()

    def test_reload_tasks_passes_godaddy_tasks_to_godaddy_tasks_merger(self):
        self.task_reloader.reload_tasks()
        self.mock_godaddy_tasks_merger.merge_godaddy_tasks.assert_called_once_with(self.godaddy_tasks)

    def test_reload_tasks_logs_action(self):
        self.task_reloader.reload_tasks()
        self.mock_logger.log.assert_called_once_with('Reload GoDaddy Tasks')

    # Support code

    def set_up_mocks(self):
        self.factory = Factory()
        self.mock_godaddy_task_retriever = MagicMock()
        self.factory.register('GoDaddyTaskRetriever', self.mock_godaddy_task_retriever)
        self.mock_godaddy_tasks_merger = MagicMock()
        self.factory.register('GoDaddyTasksMerger', self.mock_godaddy_tasks_merger)
        self.mock_logger = MagicMock()
        self.factory.register('Logger', self.mock_logger)

    def set_up_data(self):
        self.godaddy_tasks = 'godaddy tasks'

    def set_up_object_under_test(self):
        self.task_reloader = TaskReloader(self.factory)

    def set_up_expectations(self):
        self.mock_godaddy_task_retriever.retrieve_godaddy_tasks = MagicMock(return_value=self.godaddy_tasks)

