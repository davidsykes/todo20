

class UrlRouter(object):
    def __init__(self, default_destination):
        self.default_destination = default_destination
        self.destinations = {}

    def register_destination(self, command, destination):
        self.destinations[command] = destination

    def route_request(self, extracted_pagegroup, request):
        destination, parameters = self.get_destination(extracted_pagegroup)
        destination.process_request(parameters, request)

    def get_destination(self, url):
        if url is None:
            return self.default_destination, None
        
        if url[0] in self.destinations:
            return self.destinations[url[0]], url[1]

        return self.default_destination, url[1]