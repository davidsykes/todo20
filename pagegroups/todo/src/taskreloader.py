



class TaskReloader(object):
    def __init__(self, factory):
        self.godaddy_task_retriever = factory.fetch('GoDaddyTaskRetriever')
        self.godaddy_tasks_merger = factory.fetch('GoDaddyTasksMerger')

    def reload_tasks(self):
        tasks = self.godaddy_task_retriever.retrieve_godaddy_tasks()
        self.godaddy_tasks_merger.merge_godaddy_tasks(tasks)