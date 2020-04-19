from todotask import ToDoTask


class TaskConverter(object):
    @staticmethod
    def db_to_dictionary(Id, Title, Detail, Done, Due, Contexts, Position, GoDaddyId):
        task = {}
        task['Id'] = Id
        task['Title'] = Title
        task['Detail'] = Detail
        task['Done'] = Done
        task['Due'] = Due
        task['Contexts'] = Contexts
        task['Position'] = Position
        task['GoDaddyId'] = GoDaddyId
        return task

    @staticmethod
    def db_task_to_task(db_task):
        # Id, Title, Detail, Done, Due, Contexts, Position, GoDaddyId
        task = ToDoTask.create_task(db_task[1], db_task[2])
        task.id = db_task[0]
        task.done = db_task[3]
        task.due = db_task[4]
        task.contexts = db_task[5]
        task.position = db_task[6]
        task.godaddy_id = db_task[7]
        return task

    @staticmethod
    def task_to_dictionary(task):
        task_dict = {}
        task_dict['Id'] = task.id
        task_dict['Title'] = task.title
        task_dict['Detail'] = task.detail
        task_dict['Done'] = task.done
        task_dict['Due'] = task.due
        task_dict['Contexts'] = task.contexts
        task_dict['Position'] = task.position
        task_dict['GoDaddyId'] = task.godaddy_id
        return task_dict
