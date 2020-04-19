import unittest
import sys
sys.path.append('../src')
from unittest.mock import MagicMock
from todotask import ToDoTask
from taskconverter import TaskConverter


class TestTaskConverter(unittest.TestCase):
    def test_db_to_dictionary_maps_db_format_to_dictionary(self):
        task = TaskConverter.db_to_dictionary('Id', 'Title', 'Detail', 'Done', 'Due', 'Contexts', 'Position', 'GoDaddyId')
        self.assertEqual('Id', task['Id'])
        self.assertEqual('Title', task['Title'])
        self.assertEqual('Detail', task['Detail'])
        self.assertEqual('Done', task['Done'])
        self.assertEqual('Due', task['Due'])
        self.assertEqual('Contexts', task['Contexts'])
        self.assertEqual('Position', task['Position'])
        self.assertEqual('GoDaddyId', task['GoDaddyId'])

    #   db_task_to_task
    def test_db_task_to_task_converts_db_format_to_task(self):
        db_task = ('Id', 'Title', 'Detail', 'Done', 'Due', 'Contexts', 'Position', 'GoDaddyId')
        task = TaskConverter.db_task_to_task(db_task)
        self.assertEqual('Id', task.id)
        self.assertEqual('Title', task.title)
        self.assertEqual('Detail', task.detail)
        self.assertEqual('Done', task.done)
        self.assertEqual('Due', task.due)
        self.assertEqual('Contexts', task.contexts)
        self.assertEqual('Position', task.position)
        self.assertEqual('GoDaddyId', task.godaddy_id)

    #   task_to_dictionary
    def test_task_to_dictionary_converts_task_to_dictionary(self):
        task = ToDoTask()
        task.id = 'Id'
        task.title = 'Title'
        task.detail = 'Detail'
        task.id = 'Id'
        task.done = 'Done'
        task.position = 'Position'
        task.godaddy_id = 'GoDaddyId'
        task.contexts = 'Contexts'
        task.due = 'Due'
        dict_task = TaskConverter.task_to_dictionary(task)
        self.assertEqual('Id', dict_task['Id'])
        self.assertEqual('Title', dict_task['Title'])
        self.assertEqual('Detail', dict_task['Detail'])
        self.assertEqual('Done', dict_task['Done'])
        self.assertEqual('Due', dict_task['Due'])
        self.assertEqual('Contexts', dict_task['Contexts'])
        self.assertEqual('Position', dict_task['Position'])
        self.assertEqual('GoDaddyId', dict_task['GoDaddyId'])
