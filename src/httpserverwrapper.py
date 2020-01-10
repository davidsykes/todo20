

class HTTPServerWrapper(object):
    def __init__(self, http_server):
        self.http_server = http_server

    def send_code(self, response):
        self.http_server.send_code(response)

    def send_text_header(self):
        self.http_server.send_text_header()

    def write(self, data):
        self.http_server.write(data)
