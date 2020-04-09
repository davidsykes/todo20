import unittest
import sys
sys.path.append('../src')
sys.path.append('../../temperatures/Library/src')
from unittest.mock import MagicMock
from todotask import ToDoTask


class TestToDoTask(unittest.TestCase):
    def setUp(self):
        #self.set_up_mocks()
        #self.set_up_data()
        self.set_up_object_under_test()
        #self.set_up_expectations()

    def test_create_task_creates_a_task(self):
        task = self.task
        self.assertEqual('Title', task.title)
        self.assertEqual('Detail', task.detail)
        self.assertIsNone(task.id)
        self.assertFalse(task.done)
        self.assertFalse(task.position)
        self.assertIsNone(task.godaddy_id)
        self.assertIsNone(task.contexts)
        self.assertIsNone(task.due)

    # Support code

    #def set_up_mocks(self):
    #    self.mock_1 = MagicMock()

    #def set_up_data(self):
    #    self.date = 'data'

    def set_up_object_under_test(self):
        self.task = ToDoTask.create_task('Title', 'Detail')

    #def set_up_expectations(self):
    #    pass


