

class RestHandler(object):
    def __init__(self, factory):
        self.url_validator = factory.fetch('UrlValidator')
        self.url_pagegroup_extractor = factory.fetch('UrlPagegroupExtractor')
        self.url_router = factory.fetch('UrlRouter')

    def handle_request(self, url, request):
        self.url_validator.validate_url(url)
        extracted_pagegroup = self.url_pagegroup_extractor.extract_pagegroup(url)
        self.url_router.route_request(extracted_pagegroup, request)

