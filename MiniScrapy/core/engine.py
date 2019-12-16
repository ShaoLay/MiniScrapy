from MiniScrapy.core.spider import Spider
from MiniScrapy.core.scheduler import Scheduler
from MiniScrapy.core.pipeline import Pipeline
from MiniScrapy.core.downloader import Downloader
from https.request import Request
from MiniScrapy.middlewares.downloader_middlewares import DownloaderMiddleware
from MiniScrapy.middlewares.spider_middlewares import SpiderMiddleware


class Engine():
    def __init__(self):
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()

        self.spider_mids = SpiderMiddleware()
        self.downloader_mids = DownloaderMiddleware()

    def start(self):
        self._start_engine()

    def _start_engine(self):
        start_request = self.spider.start_requests()
        start_request = self.spider_mids.process_response(start_request)
        self.scheduler.add_request(start_request)
        request = self.scheduler.get_request()
        response = self.downloader.get_response(request)
        response = self.spider_mids.process_response(response)
        result = self.spider.parse(response)
        if isinstance(result, Request):
            result = self.spider_mids.process_request(result)
            self.scheduler.add_request(result)
        else:
            self.pipeline.process_item(result)