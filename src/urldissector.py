import re

class UrlDissector(object):
    def __init__(self):
        self.url_regex = re.compile('^/([a-z]+)/(.*)')

    def dissect(self, url):
        m = self.url_regex.match(url)
        return [m.group(1), m.group(2)] if m else None
