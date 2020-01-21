
from filepathhandler import FilePathHandler


class DefaultDestination(object):
    def __init__(self, www_path):
        self.filepathhandler = FilePathHandler(www_path)

    def process_request(self, page_group_url, request):
        try:
            path = self.filepathhandler.generate_path(page_group_url)
            request.server.write_file(path)
        except Exception as e:
            http_server = request.server
            http_server.send_code(404)
            http_server.send_text_header()
            http_server.write_text("Not found: '%s'" % (request.url))
