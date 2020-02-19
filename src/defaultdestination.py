
from filepathhandler import FilePathHandler


class DefaultDestination(object):
    def __init__(self, factory, www_path):
        self.filepathhandler = FilePathHandler(www_path)
        self.logger = factory.fetch('Logger')

    def process_request(self, pagegroup_url, request):
        #try:
            path = self.filepathhandler.generate_path(pagegroup_url)
            request.server.write_file(path)
        #except Exception as e:
        #    self.logger.error('Exception: %s' % (str(e)))
        #    self.logger.error('Path: %s' % (path))
        #    self.logger.error('Stack: %s' % (traceback.format_exc(10)))

        #    http_server = request.server
        #    http_server.send_code(404)
        #    http_server.send_text_header()
        #    http_server.write_text("Not found: '%s'" % (request.url))
