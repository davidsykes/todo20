import os
import re

class FilePathHandler(object):
    def __init__(self, base_path):
        self.base_path = base_path
        self.regex = re.compile('[^a-zA-Z/]')

    def generate_path(self, path):
        if self.path_is_invalid(path):
            raise Exception('Not Found: %s' % (path))
        return os.path.join(self.base_path, path)

    def path_is_invalid(self, path):
        (filepath, ext) = os.path.splitext(path)
        return self.regex.search(filepath) is not None or filepath[0] == '/'
