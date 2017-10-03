# -*- coding: utf-8 -*-
import scrapy


class ScrapySpiderSpider(scrapy.Spider):
    name = 'scrapy_spider'
    allowed_domains = ['scrapy.org']
    start_urls = ['http://scrapy.org/']

    def parse(self, response):
        pass
