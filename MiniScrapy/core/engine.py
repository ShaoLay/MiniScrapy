from MiniScrapy.core.spider import Spider
from MiniScrapy.core.scheduler import Scheduler
from MiniScrapy.core.pipeline import Pipeline
from MiniScrapy.core.downloader import Downloader
from https.request import Request


class Engine():
    def __init__(self):
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()

    def start(self):
        self._start_engine()

    def _start_engine(self):
        start_request = self.spider.start_requests()
        self.scheduler.add_request(start_request)
        request = self.scheduler.get_request()
        response = self.downloader.get_response(request)
        result = self.spider.parse(response)
        if isinstance(result, Request):
            self.scheduler.add_request(result)
        else:
            self.pipeline.process_item(result)