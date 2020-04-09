



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
