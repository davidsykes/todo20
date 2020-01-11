

class FilePathHandler(object):
    def __init__(self, base_path):
        self.base_path = base_path

    def generate_path(self, path):
        return self.base_path