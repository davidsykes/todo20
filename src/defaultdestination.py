
from filepathhandler import FilePathHandler


class DefaultDestination(object):
    def __init__(self, factory, www_path):
        self.filepathhandler = FilePathHandler(www_path)
        self.logger = factory.fetch('Logger')

    def process_request(self, pagegroup_url, request):
        path = self.filepathhandler.generate_path(pagegroup_url)
        request.server.write_file(path)
