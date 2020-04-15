
import datetime


class ToDoTask(object):
    @staticmethod
    def create_task(title, detail):
        task = ToDoTask()
        task.title = title
        task.detail = detail
        task.id = None
        task.done = False
        task.position = None
        task.godaddy_id = None
        task.contexts = None
        task.due = None
        return task

    @staticmethod
    def create_todotask_from_godaddytask(godaddytask, godaddy_datetime_converter):
        todotask = ToDoTask.create_task(godaddytask['Title'], godaddytask['Detail'])
        todotask.done = godaddytask['Done'] == '1'
        todotask.position = float(godaddytask['Position'])
        todotask.godaddy_id = int(godaddytask['Id'])
        todotask.contexts = ToDoTask.get_contexts(godaddytask['Contexts'])
        todotask.due = godaddy_datetime_converter.convert_godaddy_datetime(godaddytask['Due'])
        return todotask

    @staticmethod
    def get_contexts(contexts):
        return contexts if len(contexts) > 0 else None
