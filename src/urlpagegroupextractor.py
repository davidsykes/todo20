import re

class UrlPagegroupExtractor(object):
    def __init__(self):
        self.url_regex = re.compile('^/?([^/]+)/?(.*)$')

    def extract_pagegroup(self, url):
        m = self.url_regex.match(url)
        return [m.group(1), m.group(2)] if m else None
