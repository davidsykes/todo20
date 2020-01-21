

class UrlHandler(object):
    def __init__(self, factory):
        self.url_dissector = factory.fetch('UrlDissector')
        self.url_router = factory.fetch('UrlRouter')
        self.logger = factory.fetch('Logger')

    def handle_request(self, url, request):
        dissected = self.url_dissector.dissect_url(url)
        if not dissected:
            self.logger.log('Invalid URL: %s' % (url))
        self.url_router.route_request(dissected, request)

