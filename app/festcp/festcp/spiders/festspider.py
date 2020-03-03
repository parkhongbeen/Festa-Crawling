# -*- coding: utf-8 -*-
import os
import time
from pathlib import Path

import scrapy
from scrapy import Selector
from selenium import webdriver

from festcp.items import FestcpItem

HOME = str(Path.home())
CHROME_DRIVER = os.path.join(HOME, 'projects', 'wps12th', 'Festa-Crawling', 'app', 'festcp', 'festcp',
                             'chromedriver')

class FestspiderSpider(scrapy.Spider):
    name = 'festspider'
    allowed_domains = ['festspider']
    start_urls = ['https://www.festa.io']

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER)

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(5)
        html = self.driver.find_element_by_xpath('//*').get_attribute('outerHTML')
        selector = Selector(text=html)
        title = selector.xpath('//h3[contains(@class,"Mobile")]/text()').extract()

        for t in title:
            item = FestcpItem()
            item['title'] = t
            yield item

        self.driver.close()
