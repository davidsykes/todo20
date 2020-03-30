from enum import Enum

class RequestObjectType(Enum):
    get = 1
    put = 2
    post = 3


class RequestObject(object):
    def __init__(self, type, url, server):
        self.type = type
        self.url = url
        self.server = server

    @staticmethod
    def create_get_request(url, server):
        return RequestObject(RequestObjectType.get, url, server)

    @staticmethod
    def create_post_request(url, server):
        return RequestObject(RequestObjectType.post, url, server)

