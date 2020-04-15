import datetime
from todotask import ToDoTask

class GoDaddyTaskMerger(object):
    def __init__(self, factory):
        self.task_data_access = factory.fetch('TaskDataAccess')
        self.logger = factory.fetch('Logger')

    def merge_godaddy_task(self, task):
        existing_task = self.task_data_access.retrieve_godaddy_task(int(task['Id']))

        if self.task_does_not_exist(existing_task):
            self.create_new_task(task)
        else:
            self.logger.log("Existing task %s: %s" % (task['Title'], task['Detail']))

    def task_does_not_exist(self, existing_task):
        return existing_task is None or len(existing_task) == 0

    def create_new_task(self, task):
        new_task = ToDoTask.create_todotask_from_godaddytask(task, self)
        self.task_data_access.create_task(new_task)
        self.logger.log("Created new task %s: %s" % (task['Title'], task['Detail']))

    def convert_godaddy_datetime(self, godaddy_datetime):
        datepart = godaddy_datetime.split(' ')[0]
        return datetime.datetime.strptime(datepart, "%m/%d/%Y") if len(datepart) > 0 else None
