
class RequestObjectType(Enum):
    get = 1
    put = 2


class RequestObject(object):
    def __init__(self, type, url, server):
        self.type = type
        self.url = url
        self.server = server

    @staticmethod
    def create_get_request(url, server):
        return RequestObject(RequestObjectType.get, url, server)
