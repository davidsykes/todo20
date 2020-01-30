import re
from todoexception import ToDoException

class UrlValidator(object):
    def __init__(self):
        self.re_split_path = re.compile('^(.*/)([^/]*)$')
        self.re_prefix_valid = re.compile('^/?([a-zA-Z0-9]+[a-zA-Z0-9_/]*)?$')
        self.re_suffix_valid = re.compile('^[a-zA-Z0-9_/.]*$')

    def validate_url(self, url):
        split = self.re_split_path.match(url)
        self.check_prefix_valid(url, split.group(1))
        self.check_suffix_valid(url, split.group(2))

    def check_prefix_valid(self, url, prefix):
        if self.re_prefix_valid.fullmatch(prefix) is None:
            raise ToDoException('Invalid URL: %s' % (url))

    def check_suffix_valid(self, url, suffix):
        if suffix == None or suffix == '':
            raise ToDoException('Invalid URL: %s' % (url))
        if self.re_suffix_valid.fullmatch(suffix) is None:
            raise ToDoException('Invalid URL: %s' % (url))

