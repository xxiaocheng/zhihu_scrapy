# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response


class PeopleSpider(scrapy.Spider):
    name = 'people'
    allowed_domains = ['www.zhihu.com/people/kaifulee/activities']
    start_urls = ['http://www.zhihu.com/people/kaifulee/activities/']

    def parse(self, response):
        if "1059807" in str(response.body):
            self.logger.info("Success!")
            inspect_response(response, self)
        else:
            self.logger.warning('失败')
            inspect_response(response, self)
            return
