



class TaskDataAccess(object):
    def __init__(self, factory):
        self.database = factory.fetch('Database')
        self.todo_tasks = factory.fetch('ToDoTasks')
        self.create_task_fields = 'Title, Detail, Done, Due, Contexts, Position, GoDaddyId'
        self.retrieve_task_fields = 'TaskId, Title, Detail, Done, Due, Contexts, Position, GoDaddyId'

    def create_task(self, task):
        sql = "INSERT INTO Tasks (" + self.create_task_fields + ") VALUES (?,?,?,?,?,?,?)"
        params = (task.title, task.detail, task.done, task.due, task.contexts, task.position, task.godaddy_id)

        self.database.execute_with_commit(sql, params)

    def retrieve_godaddy_task(self, godaddy_id):
        query = 'SELECT ' + self.retrieve_task_fields + (" FROM Tasks WHERE GoDaddyId=%d" % (godaddy_id))
        return self.database.query(query)

    def retrieve_current_tasks(self):
        query = 'SELECT ' + self.retrieve_task_fields + " FROM Tasks WHERE Done=0 AND (Due IS NULL OR Due < Date('now'))"
        db_tasks = self.database.query(query)
        tasks = self.todo_tasks.db_tasks_to_task_objects(db_tasks)
        return tasks
