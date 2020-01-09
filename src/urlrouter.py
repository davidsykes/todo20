

class UrlRouter(object):
    def __init__(self, default_destination):
        self.default_destination = default_destination

    def route_request(self, dissected_url, request):
        self.default_destination.process_request(request)
