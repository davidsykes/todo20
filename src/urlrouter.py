

class UrlRouter(object):
    def __init__(self, default_destination):
        self.default_destination = default_destination
        self.destinations = {}

    def register_destination(self, command, destination):
        self.destinations[command] = destination

    def route_request(self, dissected_url, request):
        destination = self.get_destination(dissected_url)
        destination.process_request(request)

    def get_destination(self, url):
        if url is None:
            return self.default_destination
        
        if url[0] in self.destinations:
            return self.destinations[url[0]]

        return self.default_destination