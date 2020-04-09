

class GoDaddyTaskMerger(object):
    def __init__(self, factory):
        self.task_data_access = factory.fetch('TaskDataAccess')

    def merge_godaddy_task(self, task):
        existing_task = self.task_data_access.retrieve_godaddy_task(int(task['Id']))

        if existing_task is None:
            self.create_new_task(task)

    def create_new_task(self, task):
        new_task = { \
            'Done': task['Done'], \
                'Title': task['Title'], \
                    'Position': task['Position'], \
                        'GoDaddyId': task['Id'], 'Contexts': task['Contexts'], 'Detail': task['Detail'], \
                            'Due': task['Due'], 'Ordered': task['Ordered']}
        self.task_data_access.create_task(new_task)


