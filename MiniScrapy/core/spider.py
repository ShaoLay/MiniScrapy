from MiniScrapy.item import Item
from MiniScrapy.https.request import Request


class Spider(object):
    start_url = 'http://www.baidu.com'

    def start_requests(self):
        return Request(self.start_url)

    def parse(self, response):
        return Item(response.body)
