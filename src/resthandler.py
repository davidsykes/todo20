

class RestHandler(object):
    def __init__(self, factory):
        self.url_validator = factory.fetch('UrlValidator')
        self.url_dissector = factory.fetch('UrlDissector')
        self.url_router = factory.fetch('UrlRouter')

    def handle_request(self, url, request):
        self.url_validator.validate_url(url)
        dissected = self.url_dissector.dissect_url(url)
        self.url_router.route_request(dissected, request)

