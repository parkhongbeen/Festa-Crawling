import os
import time
from pathlib import Path

import scrapy
from scrapy import Selector
from selenium import webdriver

HOME = str(Path.home())
CHROME_DRIVER = os.path.join(HOME, 'projects', 'wps12th', 'Festa-Crawling', 'app', 'festascraper', 'festascraper',
                             'chromedriver')


class QuotesSpider(scrapy.Spider):
    name = "festa-spider"
    start_urls = [
        'https://www.festa.io',
    ]

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER)

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(5)
        html = self.driver.find_element_by_xpath('//*').get_attribute('outerHTML')
        selector = Selector(text=html)


        title = selector.xpath('//h3[contains(@class,"Mobile")]/text()').extract()

        yield {
            'title': title
        }
        self.driver.close()
