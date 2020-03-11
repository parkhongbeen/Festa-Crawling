# -*- coding: utf-8 -*-
import os
import time
from pathlib import Path

import scrapy
from festalist.models import FestaList
from festcp.items import FestcpItem
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
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/google-chrome-unstable'
        options.add_argument('headless')
        options.add_argument('no-sandbox')
        options.add_argument('disable-gpu')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument('window-size=1200x600')
        try:
            self.driver = webdriver.Chrome(chrome_options=options)
        except:
            self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(5)

        html = self.driver.find_element_by_xpath('//*').get_attribute('outerHTML')
        selector = Selector(text=html)
        details = selector.xpath('//div[@style]/a[contains(@class, "Mobile")]/@href').extract()[:10]

        events = FestaList.objects.order_by('-pk')[:10]
        event_titles = [event.title for event in events]
        event_dates = [event.date for event in events]
        details.reverse()
        # 키워드 전체를 받아옴 (keywords = FestaListKeyword.objects.all())
        # keywords = [keyword.keyword for keyword in keywords]
        for detail in details:
            tickets = []

            self.driver.get('https://www.festa.io' + detail)
            time.sleep(5)

            detail_html = self.driver.find_element_by_xpath('//*').get_attribute('outerHTML')
            detail_selector = Selector(text=detail_html)

            title = detail_selector.xpath('//h1[contains(@class, "Heading")]/text()').extract()[0]
            date = detail_selector.xpath('//div[contains(@class, "TextBlock")]/text()').extract()[1]

            if title in event_titles and date in event_dates:
                if event_titles.index(title) == event_dates.index(date):
                    continue

            # 키워드를 받아와서 있는지 검사
            # if keyword in keywords:
            #    keyword 알아냈음
            # 키워드에 연결된 유저들 (key_users = keyword.user.all()) 에게 이메일 보냄
            # user_email = [user.useremail for user in key_users] <- to
            # title = f'{keyword}가 등록'

            image = detail_selector.xpath('//div[contains(@class, "MainImage")]/@src').extract()[0]
            try:
                host = detail_selector.xpath('//div[contains(@class, "HostText")]/text()').extract()[0]
            except:  # host가 빈 값인 경우가 있어서 대비하기 위함.
                host = ''
            content = detail_selector.xpath('//div[contains(@class, "UserContentArea")]').extract()[0]
            apply = detail_selector.xpath('//*[contains(@class, "ButtonNew")]/text()').extract()[0]
            tickets_wrap = detail_selector.xpath('//div[contains(@class, "TicketWrapper")]').extract()
            for i, ticket in enumerate(tickets_wrap):
                if i + 1 > len(tickets_wrap) / 2:
                    break

                ticket_selector = Selector(text=ticket)
                customer = ticket_selector.xpath('//span[contains(@class, "TicketName")]/text()').extract()[0]
                price = ticket_selector.xpath('//span[contains(@class, "PriceSpan")]/text()').extract()[0]
                ticket_tuple = (customer, price)
                tickets.append(ticket_tuple)

            tickets = ', '.join([
                f'({ticket[0]}, {ticket[1]})' for ticket in tickets
            ])

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

        self.driver.quit()
