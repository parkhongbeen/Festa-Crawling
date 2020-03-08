#!/usr/bin/env python

import os
import django
import sys

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,PROJECT)

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
django.setup()

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from festcp.spiders.festspider import QuotesSpider

process = CrawlerProcess(get_project_settings())
process.crawl(QuotesSpider)
process.start()
