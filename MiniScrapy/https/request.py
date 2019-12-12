class Request(object):
    def __init__(self, url, method='GET',
                 headers=None, data=None):
        self.url = url
        self.method = method
        self.headers = headers
        self.data = data