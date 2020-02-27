import scrapy
from selenium import webdriver


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://festa.io',
    ]

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self):
        test = response.css('h3.cpLyAa::text').getall()
