import re

class UrlValidator(object):
    def __init__(self):
        self.url_regex = re.compile('[^a-z]+')

    def CheckUrl(self, url):
        m = self.url_regex.match(url)
        return m is None
