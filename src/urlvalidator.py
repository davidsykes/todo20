import re

class UrlValidator(object):
    def __init__(self):
        self.url_regex = re.compile('^/?[a-zA-Z0-9]+[a-zA-Z0-9_/]*$')

    def validate_url(self, url):
        if self.url_regex.fullmatch(url) is None:
            raise Exception('Invalid URL: %s' % (url))
