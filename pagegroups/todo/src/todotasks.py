import sys
sys.path.append('../../../Library/src')
from staticfactory import StaticFactory



class ToDoTasks(object):
    @staticmethod
    def db_tasks_to_task_objects(db_tasks):
        task_converter = StaticFactory.fetch('TaskConverter')
        tasks = map(task_converter.db_task_to_task, db_tasks)
        return list(tasks)

    @staticmethod
    def task_objects_to_dictionaries(tasks):
        task_converter = StaticFactory.fetch('TaskConverter')
        dictonaries = map(task_converter.task_to_dictionary, tasks)
        return list(dictonaries)
