import requests
import json


#payload = {'username': 'bob', 'email': 'bob@bob.com'}
#r = requests.put("http://localhost:8080/value?sensor=23232&time=32234&value=432.234", data=payload)
#r = requests.get("http://localhost:8080/Pendpoint", data=payload)


class GoDaddyTaskRetriever(object):
    def __init__(self):
        self.url = "http://www.sykestest.info/todo/JsonTasks.aspx"

    def retrieve_godaddy_tasks(self):
        cookies = {'Login': 'L3tM31n'}
        r = requests.get(self.url, cookies=cookies)
        end_of_json = r.text.rfind(']')
        tasks_json = r.text[0:end_of_json+1]
        tasks = json.loads(tasks_json)
        return tasks


r = GoDaddyTaskRetriever()
tasks = r.retrieve_godaddy_tasks()
for t in tasks:
    print t