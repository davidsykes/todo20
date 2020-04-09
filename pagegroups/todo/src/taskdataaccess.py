



class TaskDataAccess(object):
    def __init__(self, factory):
        self.database = factory.fetch('Database')
        self.task_fields = 'Title, Detail, Done, Due, Contexts, Position, GoDaddyId'

    def create_task(self, task):
        sql = "INSERT INTO Tasks (" + self.task_fields + ") VALUES ('%s','%s',%d,%s,'%s',%f,%d)" \
            % (task.title, task.detail, task.done, task.due, task.contexts, task.position, task.godaddy_id)

        self.database.execute_with_commit(sql)

    def retrieve_godaddy_task(self, godaddy_id):
        query = 'SELECT ' + self.task_fields + ("FROM Tasks WHERE GoDaddyId=%d" % (godaddy_id))
        return self.database.query(query)
