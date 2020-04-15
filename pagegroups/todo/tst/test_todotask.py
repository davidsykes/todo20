import unittest
import sys
sys.path.append('../src')
sys.path.append('../../temperatures/Library/src')
from unittest.mock import MagicMock
from todotask import ToDoTask


class TestToDoTask(unittest.TestCase):
    def setUp(self):
        self.set_up_mocks()
        self.set_up_expectations()

    def test_create_task_creates_a_task(self):
        task = ToDoTask.create_task('Title', 'Detail')
        self.assertEqual('Title', task.title)
        self.assertEqual('Detail', task.detail)
        self.assertIsNone(task.id)
        self.assertFalse(task.done)
        self.assertIsNone(task.position)
        self.assertIsNone(task.godaddy_id)
        self.assertIsNone(task.contexts)
        self.assertIsNone(task.due)

    #   create_todotask_from_godaddytask

    def test_create_todotask_from_godaddytask(self):
        godaddy_task = {'Done': '1', 'Title': 'Task Title', 'Position': '1.23', 'Id': '42', 'Contexts': '101', 'Detail': 'Task Detail', 'Due': 'due date', 'Ordered': '0'}
        task = ToDoTask.create_todotask_from_godaddytask(godaddy_task, self.mock_godaddy_datetime_converter)
        self.assertEqual('Task Title', task.title)
        self.assertEqual('Task Detail', task.detail)
        self.assertIsNone(task.id)
        self.assertTrue(task.done)
        self.assertEqual(1.23, task.position)
        self.assertEqual(42, task.godaddy_id)
        self.assertEqual('101', task.contexts)
        self.assertEqual('converted datetime', task.due)

    def test_done_is_false_for_values_other_than_1(self):
        godaddy_task = {'Done': 'any', 'Title': 'Task Title', 'Position': '1.23', 'Id': '42', 'Contexts': '101', 'Detail': 'Task Detail', 'Due': '15/3/2020 12:34:56 PM', 'Ordered': '0'}
        task = ToDoTask.create_todotask_from_godaddytask(godaddy_task, self.mock_godaddy_datetime_converter)
        self.assertFalse(task.done)

    def test_context_can_be_empty(self):
        godaddy_task = {'Done': 'any', 'Title': 'Task Title', 'Position': '1.23', 'Id': '42', 'Contexts': '', 'Detail': 'Task Detail', 'Due': '15/3/2020 12:34:56 PM', 'Ordered': '0'}
        task = ToDoTask.create_todotask_from_godaddytask(godaddy_task, self.mock_godaddy_datetime_converter)
        self.assertIsNone(task.contexts)

    # Support code

    def set_up_mocks(self):
        self.mock_godaddy_datetime_converter = MagicMock()

    def set_up_expectations(self):
        self.mock_godaddy_datetime_converter.convert_godaddy_datetime.side_effect = self.convert_godaddy_datetime

    def convert_godaddy_datetime(self, dt):
        return 'converted datetime' if dt == 'due date' else 'invalid datetime'


