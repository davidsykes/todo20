import os
import re

INDEX = 'index.html'

class FilePathHandler(object):
    def __init__(self, base_path):
        self.base_path = base_path

    def generate_path(self, path):
        path = path.strip("/")
        if self.path_is_empty(path):
            path = INDEX
        return os.path.join(self.base_path, path.strip("/"))

    def path_is_empty(self, path):
        return path == ''
