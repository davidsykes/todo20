import os
import re

INDEX = 'index.html'

class FilePathHandler(object):
    def __init__(self, base_path):
        self.base_path = base_path
        self.regex = re.compile('[^a-zA-Z/]')

    def generate_path(self, path):
        path = path.strip("/")
        if self.path_is_invalid(path):
            raise Exception('Path not found: %s' % (path))
        print('sfsdfds', path, self.path_is_empty(path))
        if self.path_is_empty(path):
            path = INDEX
        return os.path.join(self.base_path, path.strip("/"))

    def path_is_invalid(self, path):
        (filepath, ext) = os.path.splitext(path)
        return self.regex.search(filepath) is not None

    def path_is_empty(self, path):
        return path == ''
