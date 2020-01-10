

class DefaultDestination(object):
    def process_request(self, request):
        http_server = request.server
        http_server.send_code(404)
        http_server.send_text_header()
        http_server.write("Not found: '%s'" % (request.url))
