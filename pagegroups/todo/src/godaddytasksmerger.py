

class GoDaddyTasksMerger(object):
    def __init__(self, factory):
        self.godaddy_task_merger = factory.fetch('GoDaddyTaskMerger')

    def merge_godaddy_tasks(self, tasks):
        for t in tasks:
            self.godaddy_task_merger.merge_godaddy_task(t)
