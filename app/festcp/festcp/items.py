# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem


class FestcpItem(DjangoItem):
    title = scrapy.Field()
    image = scrapy.Field()
    host = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    apply = scrapy.Field()
    tickets = scrapy.Field()
