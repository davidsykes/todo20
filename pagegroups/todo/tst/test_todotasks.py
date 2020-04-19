import unittest
import sys
sys.path.append('../src')
sys.path.append('../../../Library/src')
from unittest.mock import MagicMock
from todotasks import ToDoTasks
from staticfactory import StaticFactory


class TestToDoTasks(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_expectations()

    def test_db_tasks_to_task_objectss_creates_from_db_tasks(self):
        db_tasks = ['db task 1', 'db task 2']

        tasks = ToDoTasks.db_tasks_to_task_objects(db_tasks)

        self.assertEqual(['db task 1 as task', 'db task 2 as task'], tasks)

    #   tasks_to_dict

    def test_task_objects_to_dictionaries_converts_tasks_to_dictionaries(self):
        tasks = ['Task 1', 'Task 2']

        dictionaries = ToDoTasks.task_objects_to_dictionaries(tasks)

        self.assertEqual(['Task 1 as dictionary', 'Task 2 as dictionary'], dictionaries)

    # Support code

    def set_up_mocks(self):
        self.mock_taskconverter = MagicMock()
        factory = StaticFactory.initialise_factory()
        factory.register('TaskConverter', self.mock_taskconverter)

    def set_up_expectations(self):
        self.mock_taskconverter.db_task_to_task.side_effect = self.db_task_to_task
        self.mock_taskconverter.task_to_dictionary.side_effect = self.task_to_dictionary

    def db_task_to_task(self, db_task):
        return db_task + ' as task'

    def task_to_dictionary(self, task):
        return task + ' as dictionary'


