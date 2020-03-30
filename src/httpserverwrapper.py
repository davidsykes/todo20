import os
from todoexception import ToDoException

class HTTPServerWrapper(object):
    def __init__(self, http_server):
        self.http_server = http_server
        self.content_types = {
            '.css': 'text/css',
            '.html': 'text/html',
            '.js': 'text/javascript',
            '.png': 'text/png',
            '.ico': 'text/png',
            '.woff': 'text/png',
            '.tiff': 'text/png',
            '.jpg': 'text/jpg',
            }


    def server_response_json(self, json):
        self.http_server.send_code(200)
        self.http_server.send_header('Content-type','application/json')
        self.http_server.send_header('Access-Control-Allow-Origin', '*')
        self.http_server.end_headers()
        self.http_server.write_text(json)

    def server_response_text(self, code, response):
        self.http_server.send_code(code)
        self.send_header('Content-type','text/html')
        self.http_server.end_headers()
        self.http_server.write_text(response)
        return

    def write_file(self, path):
        if not os.path.isfile(path):
            raise ToDoException('Requested file path not found: %s' % (path))
        extension = os.path.splitext(path)[1]
        content_type = self.get_content_type(extension)
        f = open(path,"rb")
        self.http_server.send_code(200)
        self.http_server.send_header('Content-type', content_type)
        self.http_server.end_headers()
        self.http_server.wfile.write(f.read())
        f.close()
        return

    def get_content_type(self, ext):
        if ext in self.content_types:
            return self.content_types[ext]
        raise Exception('Unrecognised content type %s' % (ext))


