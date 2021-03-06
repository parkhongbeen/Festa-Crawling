# -*- coding: utf-8 -*-
import json
import os
import time
from pathlib import Path

import scrapy
from festcp.items import FestcpItem
from scrapy import Selector
from selenium import webdriver

from festalist.models import FestaList

HOME = str(Path.home())
CHROME_DRIVER = os.path.join(HOME, 'projects', 'wps12th', 'Festa-Crawling', 'app', 'festcp', 'festcp',
                             'chromedriver')


class QuotesSpider(scrapy.Spider):
    name = "festa-first-spider"
    start_urls = [
        'https://www.festa.io/events/',
    ]

    def __init__(self):
        scrapy.Spider.__init__(self)
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('no-sandbox')
        options.add_argument('disable-gpu')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument('window-size=1200x600')
        try:
            self.driver = webdriver.Chrome('chromedriver', chrome_options=options)
        except:
            options.binary_location = '/usr/bin/google-chrome-unstable'
            self.driver = webdriver.Chrome(chrome_options=options)

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(5)

        # ------------------------------- 무한스크롤 -------------------------------

        SCROLL_PAUSE_TIME = 3

        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(SCROLL_PAUSE_TIME)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
            time.sleep(SCROLL_PAUSE_TIME)

            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

        # ------------------------------- 무한스크롤 -------------------------------
        database = FestaList.objects.all()
        db_titles = []
        db_date = []

        for data in database:
            db_titles.append(data.title)
            db_date.append(data.date)

        html = self.driver.find_element_by_xpath('//*').get_attribute('outerHTML')
        selector = Selector(text=html)
        details = selector.xpath('//div[@style]/a[contains(@class, "Mobile")]/@href').extract()

        details.reverse()
        for detail in details:
            try:
                tickets = []

                self.driver.get('https://www.festa.io' + detail)
                time.sleep(5)

                detail_html = self.driver.find_element_by_xpath('//*').get_attribute('outerHTML')
                detail_selector = Selector(text=detail_html)

                title = detail_selector.xpath('//h1[contains(@class, "Heading")]/text()').extract()[0]
                date = detail_selector.xpath('//div[contains(@class, "TextBlock")]/text()').extract()[1]

                if title in db_titles:
                    if date in db_date:
                        continue

                image = detail_selector.xpath('//div[contains(@class, "MainImage")]/@src').extract()[0]
                try:
                    host = detail_selector.xpath('//div[contains(@class, "HostText")]/text()').extract()[0]
                except:  # host가 빈 값인 경우가 있어서 대비하기 위함.
                    host = ''
                content = detail_selector.xpath('//div[contains(@class, "UserContentArea")]').extract()[0]
                apply = detail_selector.xpath('//*[contains(@class, "ButtonNew")]/text()').extract()[0]
                tickets_wrap = detail_selector.xpath('//div[contains(@class, "TicketWrapper")]').extract()
                if tickets_wrap:
                    for i, ticket in enumerate(tickets_wrap):
                        if i + 1 > len(tickets_wrap) / 2:
                            break

                        ticket_selector = Selector(text=ticket)
                        customer = ticket_selector.xpath('//span[contains(@class, "TicketName")]/text()').extract()[0]
                        price = ticket_selector.xpath('//span[contains(@class, "PriceSpan")]/text()').extract()[0]
                        ticket_dict = {
                            'name': customer,
                            'price': price
                        }
                        ticket_str = json.dumps(ticket_dict, ensure_ascii=False)
                        tickets.append(ticket_str)

                tickets = ', '.join([
                    f'{ticket}' for ticket in tickets
                ])

                tickets = f'[{tickets}]'

                if apply == '이벤트 신청(외부등록)':
                    button = self.driver.find_element_by_css_selector('button')
                    self.driver.execute_script("arguments[0].click();", button)
                    self.driver.switch_to_window(self.driver.window_handles[1])
                    time.sleep(3)
                    self.driver.switch_to_window(self.driver.window_handles[0])
                    time.sleep(3)
                    self.driver.switch_to_window(self.driver.window_handles[1])  # alert 처리
                    link = self.driver.current_url

                    self.driver.close()
                    self.driver.switch_to_window(self.driver.window_handles[0])

                else:
                    link = ''

                # 데이터베이스에 넣기
                item = FestcpItem()
                item['title'] = title
                item['image'] = image
                item['host'] = host
                item['date'] = date
                item['content'] = content
                item['apply'] = apply
                item['tickets'] = tickets
                item['link'] = link
                yield item
            except:
                continue

        self.driver.quit()
