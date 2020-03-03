# -*- coding: utf-8 -*-
import os
import time
from pathlib import Path

import scrapy
from scrapy import Selector
from selenium import webdriver

HOME = str(Path.home())
CHROME_DRIVER = os.path.join(HOME, 'projects', 'wps12th', 'Festa-Crawling', 'app', 'festcp', 'festcp',
                             'chromedriver')


class QuotesSpider(scrapy.Spider):
    name = "festa-spider"
    start_urls = [
        'https://www.festa.io/events/',
    ]

    def __init__(self):
        scrapy.Spider.__init__(self)
        try:
            self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
        except:
            self.driver = webdriver.Chrome()

    def parse(self, response):
        data = []

        self.driver.get(response.url)
        time.sleep(5)
        html = self.driver.find_element_by_xpath('//*').get_attribute('outerHTML')
        selector = Selector(text=html)

        details = selector.xpath('//div[@style]/a[contains(@class, "Mobile")]/@href').extract()

        for detail in details:
            tickets = []

            self.driver.get('https://www.festa.io' + detail)
            time.sleep(5)

            detail_html = self.driver.find_element_by_xpath('//*').get_attribute('outerHTML')
            detail_selector = Selector(text=detail_html)

            title = detail_selector.xpath('//h1[contains(@class, "Heading")]/text()').extract()[0]
            image = detail_selector.xpath('//div[contains(@class, "MainImage")]/@src').extract()[0]
            try:
                host = detail_selector.xpath('//div[contains(@class, "HostText")]/text()').extract()[0]
            except:  # host가 빈 값인 경우가 있어서 대비하기 위함.
                host = ''
            date = detail_selector.xpath('//div[contains(@class, "TextBlock")]/text()').extract()[1]
            content = detail_selector.xpath('//div[contains(@class, "UserContentArea")]').extract()[0]
            apply = detail_selector.xpath('//*[contains(@class, "ButtonNew")]/text()').extract()[0]
            tickets_wrap = selector.xpath('//div[contains(@class, "TicketWrapper")]').extract()
            for i, ticket in enumerate(tickets_wrap):
                if i + 1 > len(tickets_wrap) / 2:
                    break

                ticket_selector = Selector(text=ticket)
                customer = ticket_selector.xpath('//p[contains(@class, "TicketDesc")]/text()').extract()[0]
                price = ticket_selector.xpath('//span[contains(@class, "PriceSpan")]/text()').extract()[0]
                tickets.append((customer, price))

            item = {
                'title': title,
                'image': image,
                'host': host,
                'date': date,
                'content': content,
                'apply': apply,
                # 'link': link,
                'tickets': tickets,
            }

            data.append(item)

        yield {
            'data': data
        }
        self.driver.close()
