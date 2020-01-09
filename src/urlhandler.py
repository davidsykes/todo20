

class UrlHandler(object):
    def __init__(self, factory):
        self.url_dissector = factory.fetch('UrlDissector')
        self.url_router = factory.fetch('UrlRouter')

    def get(self, url, server):
        dissected = self.url_dissector.dissect_url(url)
        self.url_router.get(dissected, server)
